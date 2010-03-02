
import logging
from urllib import urlopen

def ratingpages(user, type):    
    page = 1

    while(True):
        url = "http://%s.imhonet.ru/rates/all/?type=%s&page=%d" % (user, type, page)        
        logging.info("retrieving page %d from %s", page, url)
        
        html = urlopen(url).read()
        yield html

        page+=1       