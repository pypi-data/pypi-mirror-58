//create
PyDoc_STRVAR(webviewCreate_doc,
	"create the webview \n"\
	"\n"\
	"webview.create()");

//remove
PyDoc_STRVAR(webviewRemove_doc,
	"remove the webview\n"\
	"\n"\
	"webview.remove()");

//load url
PyDoc_STRVAR(webviewLoadURL_doc,
	"load url.\n"\
	"\n"\
	"webview.loadURL(url, cleanCache)\n"\
	"\n"\
	"Parameters\n"\
	"----------\n"\
	"    url : string\n"\
	"        the url link to display on webview\n"\
	"    cleanCache : bool\n"\
	"        clean the caching or not. True by default");

//visible
PyDoc_STRVAR(webviewVisible_doc,
	"webview visibility.\n"\
	"\n"\
	"webview.visible(visible)\n"\
	"\n"\
	"Parameters\n"\
	"----------\n"\
	"    visible : bool\n"\
	"        visible or not");

//rect
PyDoc_STRVAR(webviewRect_doc,
	"webview rect\n"\
	"\n"\
	"webview.rect(left, top, maxWidth, maxHeight)\n"\
	"\n"\
	"Parameters\n"\
	"----------\n"\
	"    left : int\n"\
	"        the webview left position\n"\
	"    top : int\n"\
	"        the webview top position\n"\
	"    maxWidth : int\n"\
	"        the webview maxWidth\n"\
	"    maxHeight : int\n"\
	"        the webview maxHeight");
