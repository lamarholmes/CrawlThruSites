import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
print(url)
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

Times = 7

def loopThruURL(url, times):
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	URL = tags[17].get('href', None)
	print(URL)
	global Times
	Times = Times - 1
	if Times == 0:
		return True
	return loopThruURL(URL,Times)

loopThruURL(url,Times)




