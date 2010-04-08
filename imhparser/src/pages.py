
import logging
from urllib import urlopen

def ratingpages(user):    
    page = 1

    while(True):
        url = "http://%s.imhonet.ru/rates/all/?page=%d" % (user, page)
        logging.info("retrieving page %d from %s", page, url)
        
        html = urlopen(url).read()
        yield html

        page+=1       