#include "WebViewImpl.h"
#include <cstdio>

void WebViewImpl::LoadURL(const char* url, bool cleanCache)
{
	char result[128];
	sprintf(result, "cmd /c start %s", url);

	system(result);
}