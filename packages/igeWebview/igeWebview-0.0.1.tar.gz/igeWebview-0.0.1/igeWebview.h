#include <Python.h>
#include "Webview.h"

typedef struct {
	PyObject_HEAD
		Webview* webview;
} webview_obj;


extern PyTypeObject WebviewType;
