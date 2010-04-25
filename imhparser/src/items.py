
# -*- coding: utf-8 -*-

import re

year_re = re.compile(ur".*?(\d+) год.*", re.UNICODE)
duration_re = re.compile(ur".*?(\d+) мин.*", re.UNICODE)

template = ur"""
h1
  title
div#HeadNavigation2 div span.nobr
  original_title
div.element_header div.mb10 div
  short_info
  year $".*?(\d+) год.*"
  duration $".*?(\d+) мин.*"
span#MainInfoSmallDescription
  description
a#rates_amount_1
  rates_count
"""

def item_from_page(page):
    item = {}
    # title
    title = page.cssselect("h1")
    if ( title != [] ):
        item["title"] = title[0].text_content()

    # original title
    original_title = page.cssselect("div#HeadNavigation2 div span.nobr")
    if ( original_title != [] ):
        item["original_title"] = original_title[0].text_content()

    # short info
    short_info = page.cssselect("div.element_header div.mb10 div")
    if ( short_info != []):
        item["short_info"] = short_info[0].text_content()        

        # extract year
        year_match = year_re.match(item["short_info"])        
        if ( year_match is not None ):
            item["year"] = year_match.group(1)            

        # extract duration
        duration_match = duration_re.match(item["short_info"])
        if ( duration_match is not None ):
            item["duration"] = duration_match.group(1)

    # description
    description = page.cssselect("span#MainInfoSmallDescription")
    if ( description != []):
        item["description"] = description[0].text_content()
        print item["description"]

    # rates count
    rates_count = page.cssselect("a#rates_amount_1")
    if ( rates_count != []):
        item["rates_count"] = rates_count[0].text_content()
        print item["rates_count"]


    
