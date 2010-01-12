from lxml.html import fromstring
from lxml.html import tostring
import simplejson as json

def trace(obj):
    #soup version print unicode(obj).encode("cp1251")
    print tostring(obj, encoding="cp1251")

class Author:
    pass

class Item:
    pass
 

html = open("../../books.html").read()

doc = fromstring(html)

for row in  doc.cssselect("td.'vat pl10'"):
    trace(row)
    
    #parse author
    authorElement = row.cssselect("div span a")[0]
    trace(authorElement)

    author = Author()
    author.Link = authorElement.attrib["href"]
    author.Name = authorElement.text_content()
    print author.Name

    #parse item
    itemElement = row.cssselect("div div a")[0]
    trace(itemElement)
    item = Item()
    item.Link = itemElement.attrib["href"]
    item.Name = itemElement.text_content()
    print item.Name

    #parse script data
    scriptElement = row.cssselect("script")[3]
    trace(scriptElement)
    scriptData = scriptElement.text_content()
    print scriptData

    #get JSON data between braces {} - dirty way
    openingBrace = scriptData.find("{")
    closingBrace = scriptData.find("}")
    jsonString = scriptData[openingBrace:closingBrace+1]
    print jsonString    

    #test...
    #ratingData = json.loads('{user_rate:27}')
    #print ratingData["user_rate"]

    break