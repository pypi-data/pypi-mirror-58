#include "Webview.h"
#include "WebViewImpl.h"

Webview::Webview()
	: m_webviewImpl(new WebViewImpl())
{

}

Webview::~Webview()
{
	delete m_webviewImpl;
	m_webviewImpl = nullptr;
}

void Webview::CreateWebView()
{
	m_webviewImpl->CreateWebView();
}

void Webview::RemoveWebView()
{
	m_webviewImpl->RemoveWebView();
}

void Webview::LoadURL(const char* url, bool cleanCache)
{
	m_webviewImpl->LoadURL(url, cleanCache);
}

void Webview::SetVisible(bool visible)
{
	m_webviewImpl->SetVisible(visible);
}

void Webview::SetRect(int left, int top, int maxWidth, int maxHeight)
{
    m_webviewImpl->SetRect(left, top, maxWidth, maxHeight);
}
