from lxml.html import fromstring
from lxml.html import tostring
import yaml
import re

def trace(obj):
    #soup version print unicode(obj).encode("cp1251")
    s = tostring(obj, encoding="cp1251")
    print s[:50]

class Author:
    pass

class Item:
    pass
 

html = open("../../books.html").read()

doc = fromstring(html)

#regex to extract JS data associated with the item
dataJsPattern = re.compile(r"""/\* <!\[CDATA\[ \*/var params = (\{.*\}).*""")

for row in  doc.cssselect("td.'vat pl10'"):    
    #parse author
    authorElement = row.cssselect("div span a")[0]

    author = Author()
    author.Link = authorElement.attrib["href"]
    author.Name = authorElement.text_content()
    print author.Name

    #parse item
    itemElement = row.cssselect("div div a")[0]
    item = Item()
    item.Link = itemElement.attrib["href"]
    item.Name = itemElement.text_content()
    print item.Name

    #parse script data
    for scriptElement in row.cssselect("script"):        
        scriptData = scriptElement.text_content()
        match = dataJsPattern.match(scriptData)
        if match:
            # not really yaml, but the fast way to get started...
            yamlData = match.group(1).replace(":", ": ") # YAML is strict...
            data = yaml.load(yamlData)
            print data["user_rate"]
