
import logging
from lxml.html import fromstring
from pymongo import Connection

from pages import *
from ratings import *
from items import *

logging.basicConfig(level = logging.DEBUG)

connection = Connection()
db = connection["imhonet"]

f = open("..\\..\\item.html")
html = f.read()
page = fromstring(html)
item_from_page(page)

f = open("..\\..\\item2.html")
html = f.read()
page = fromstring(html)
item_from_page(page)

exit(0)

# process rating pages until they are over
for html in ratingpages("qizz"):
    try:        
        # create lxml document
        page = fromstring(html)

        # check whether it's past the last page
        if ratings_ended(page):
            logging.info("ratings ended")
            break

        # process ratings
        for rating in ratings_from_page(page):
            try:
                #update existing rating or insert a new one
                db.ratings.update({"element_id": rating["element_id"]}, rating, True)

                logging.info("Item rating saved: %s", rating["item_name"])
            except:
                logging.exception("error during processing rating %d" % rating["element_id"])
    except:
        logging.exception("error during processing a rating page")
        exit()
