import urllib, urllib2, cookielib, webbrowser

username = 'ram'
password = 'ram'
url = 'http://example.com'
webbrowser.open(url, new=1, autoraise=1)
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({'username' : username, 'j_password' : password})
opener.open('http://example.com', login_data)
resp = opener.open('http://example.com/afterlogin')
print (resp)
webbrowser.open(url, new=1, autoraise=1)
