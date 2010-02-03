from lxml.html import fromstring
from pymongo import Connection
import logging

from ratings import *

logging.basicConfig(level = logging.DEBUG)

connection = Connection()
db = connection["imhonet"]

html = open("../../books.html").read()

page = fromstring(html)

for rating in ratings_from_page(page):
    #update existing rating or insert a new one    
    db.ratings.update({"element_id": rating["element_id"]}, rating, True)
    
    logging.info("Item rating saved: %s", rating["item_name"])
