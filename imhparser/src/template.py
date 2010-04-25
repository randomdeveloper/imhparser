
# -*- coding: cp1251 -*-

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

def dict_from_page(page, template):
    # states
    top, element = range(2)
    state = top
    
    last_indent = 0
    for line in template.splitlines():
        s = line.lstrip()
        if s == "":
            continue
        
        indent = len(line) - len(s)
        if indent < last_indent:
            state = top  #must be element again
        last_indent = indent

        if state == top:
            selector = s
            state = element
            print "Css selector: ", selector
        elif state == element:
            print "smth else: ", s
        


dict_from_page(None, template)
