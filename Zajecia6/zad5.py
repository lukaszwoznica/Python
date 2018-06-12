import urllib.request as urllib

from xml.dom import minidom

response = urllib.urlopen('https://www.yr.no/sted/Polen/Lublin/Lublin/forecast.xml')
document = minidom.parse(response)

elements = document.getElementsByTagName("sun")

print(elements[0].getAttribute("rise"))
