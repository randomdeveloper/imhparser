from lxml.html import fromstring, tostring

def trace(obj):
  #soup version print unicode(obj).encode("cp1251")
  print tostring(obj)

class Author:
    pass

class Item:
    pass
 

html = open("../../books.html").read()


doc = fromstring(html)

for item in  doc.cssselect("td.'vat pl10'"):
    trace(item)

    #parse author
    authorElement = item.cssselect("span a")[0]
    trace(authorElement)

    author = Author()
    author.Link =authorElement.attrib["href"]
    author.Name =authorElement.text_content()
    print author.Name

    #parse item
    itemElement = item.cssselect("div a")[0]
    trace(itemElement)
    
    break



#from BeautifulSoup import BeautifulSoup
#soup =  BeautifulSoup(html)
#
#for item in soup.findAll("td", "vat pl10"):
#    element = item.contents[1]
#
#    trace(element)
#
#    # parse author
#    authorElement = element.span.a
#    author = Author()
#    author.Name = authorElement.string
#    author.Link = authorElement["href"]
#    trace(author.Name)
#
#    # parse Item
#    itemElement = element.div.a
#    item = Item()
#    item.Link = itemElement["href"]
#    item.Name = itemElement.string
#    trace(item.Name)