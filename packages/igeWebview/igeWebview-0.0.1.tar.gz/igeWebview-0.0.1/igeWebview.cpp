#include "igeWebview.h"
#include "igeWebview_doc_en.h"

PyObject* webview_new(PyTypeObject* type, PyObject* args, PyObject* kw)
{
	webview_obj* self = NULL;

	self = (webview_obj*)type->tp_alloc(type, 0);
	self->webview = new Webview();

	return (PyObject*)self;
}

void webview_dealloc(webview_obj* self)
{
	delete self->webview;
	Py_TYPE(self)->tp_free(self);
}

PyObject* webview_str(webview_obj* self)
{
	char buf[64];
	snprintf(buf, 64, "webview object");
	return _PyUnicode_FromASCII(buf, strlen(buf));
}

PyObject* webview_create(webview_obj* self)
{
	self->webview->CreateWebView();

	Py_INCREF(Py_None);
    return Py_None;
}

PyObject* webview_remove(webview_obj* self)
{
	self->webview->RemoveWebView();

	Py_INCREF(Py_None);
	return Py_None;
}

PyObject* webview_loadURL(webview_obj* self, PyObject* args)
{
	char* url;
	int cleanCache = 1;
	if (!PyArg_ParseTuple(args, "s|i", &url, &cleanCache))
		return NULL;

	self->webview->LoadURL(url, cleanCache);

	Py_INCREF(Py_None);
	return Py_None;
}

PyObject* webview_visible(webview_obj* self, PyObject* args)
{
	int visible = 0;
	if (!PyArg_ParseTuple(args, "i", &visible))
		return NULL;

	self->webview->SetVisible(visible);

	Py_INCREF(Py_None);
	return Py_None;
}

PyObject* webview_rect(webview_obj* self, PyObject* args)
{
	int left = 0;
	int top = 0;
	int maxWidth = 0;
	int maxHeight = 0;
	if (!PyArg_ParseTuple(args, "iiii", &left, &top, &maxWidth, &maxHeight))
		return NULL;

	self->webview->SetRect(left, top, maxWidth, maxHeight);

	Py_INCREF(Py_None);
	return Py_None;
}

PyMethodDef webview_methods[] = {
	{ "create", (PyCFunction)webview_create, METH_NOARGS, webviewCreate_doc },
	{ "remove", (PyCFunction)webview_remove, METH_NOARGS, webviewRemove_doc },
	{ "loadURL", (PyCFunction)webview_loadURL, METH_VARARGS, webviewLoadURL_doc },
	{ "visible", (PyCFunction)webview_visible, METH_VARARGS, webviewVisible_doc },
	{ "rect", (PyCFunction)webview_rect, METH_VARARGS, webviewRect_doc },
	{ NULL,	NULL }
};

PyGetSetDef webview_getsets[] = {
	{ NULL, NULL }
};

PyTypeObject WebviewType = {
	PyVarObject_HEAD_INIT(NULL, 0)
	"igeWebview",						/* tp_name */
	sizeof(webview_obj),				/* tp_basicsize */
	0,                                  /* tp_itemsize */
	(destructor)webview_dealloc,		/* tp_dealloc */
	0,                                  /* tp_print */
	0,							        /* tp_getattr */
	0,                                  /* tp_setattr */
	0,                                  /* tp_reserved */
	0,                                  /* tp_repr */
	0,					                /* tp_as_number */
	0,                                  /* tp_as_sequence */
	0,                                  /* tp_as_mapping */
	0,                                  /* tp_hash */
	0,                                  /* tp_call */
	(reprfunc)webview_str,				/* tp_str */
	0,                                  /* tp_getattro */
	0,                                  /* tp_setattro */
	0,                                  /* tp_as_buffer */
	Py_TPFLAGS_DEFAULT,					/* tp_flags */
	0,									/* tp_doc */
	0,									/* tp_traverse */
	0,                                  /* tp_clear */
	0,                                  /* tp_richcompare */
	0,                                  /* tp_weaklistoffset */
	0,									/* tp_iter */
	0,									/* tp_iternext */
	webview_methods,					/* tp_methods */
	0,                                  /* tp_members */
	webview_getsets,					/* tp_getset */
	0,                                  /* tp_base */
	0,                                  /* tp_dict */
	0,                                  /* tp_descr_get */
	0,                                  /* tp_descr_set */
	0,                                  /* tp_dictoffset */
	0,                                  /* tp_init */
	0,                                  /* tp_alloc */
	webview_new,						/* tp_new */
	0,									/* tp_free */
};

static PyModuleDef webview_module = {
	PyModuleDef_HEAD_INIT,
	"igeWebview",						// Module name to use with Python import statements
	"Webview Module.",					// Module description
	0,
	webview_methods						// Structure that defines the methods of the module
};

PyMODINIT_FUNC PyInit_igeWebview() {
	PyObject* module = PyModule_Create(&webview_module);

	if (PyType_Ready(&WebviewType) < 0) return NULL;

	Py_INCREF(&WebviewType);
	PyModule_AddObject(module, "webview", (PyObject*)&WebviewType);

	return module;
}
