import urllib.request as urllib2

response = urllib2.urlopen('http://python.org/')
f = open("html_doc.txt", "w")
f.write(str(response.read()))
f.close()
