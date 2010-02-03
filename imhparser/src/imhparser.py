from lxml.html import fromstring
from lxml.html import tostring

from ratings import *

def trace(obj):
    s = tostring(obj, encoding="cp1251")
    print s[:50]

html = open("../../books.html").read()

doc = fromstring(html)

for rating in ratings_from_page(doc):
    print rating
    break
