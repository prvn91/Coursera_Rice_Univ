import urllib.request as ur
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

url = input("ENter the Url: ")
url_handler = ur.urlopen(url)
data = url_handler.read()

tree = ET.fromstring(data)

total = 0
lst = tree.findall('comments/comment')
print (len(lst))
for item in lst:
    inte = int(item.find('count').text)
    total += inte
print(total)
