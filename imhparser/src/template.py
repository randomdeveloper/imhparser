
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
    # parser states
    top, element = range(2)
    state = top


    last_indent = 0
    for line in template.splitlines():
        s = line.lstrip()
        if s == "":
            continue

        # unindent means new css selector block        
        indent = len(line) - len(s)
        if indent < last_indent:
            state = top  #must be element again
        last_indent = indent

        if state == top:
            selector = s
            state = element
            print "->css selector: ", selector
        elif state == element:
            t = s.partition(" ")
            key = t[0]
            print "key ", key
            if t[1] == "":                
                print "text content"
            else:
                tail = t[2].lstrip()
                if tail[0] == "$":
                    print "regexp ", tail
                else:
                    print "unknown"

dict_from_page(None, template)
