
# -*- coding: cp1251 -*-

import re
from lxml.html import fromstring

template = ur"""
h1
  title
div#HeadNavigation2 div span.nobr
  original_title
div.element_header div.mb10 div
  short_info
  year $.*?(\d+) год.*
  duration $.*?(\d+) мин.*
span#MainInfoSmallDescription
  description
a#rates_amount_1
  rates_count
"""

class Parser:
    def __init__(self):
        self.elements = []
    def extract(self, page):
        dict = {}
        for element in self.elements:
            elist = page.cssselect(element.selector)
            if elist != []:
                e = elist[0]
                for key, extractor in element.extractors:
                    s = extractor.extract(e)
                    if s:
                        dict[key] = s
            pass
        return dict

class Element:
    def __init__(self, selector):
        self.extractors = []
        self.selector = selector

class TextExtractor:
    def extract(self, element):
        return element.text_content()
            
class RegexExtractor:
    def __init__(self, regex):
        print regex
        self.re = re.compile(regex, re.UNICODE)        
    def extract(self, element):
        match = self.re.match(element.text_content())        
        if ( match ):
            return match.group(1)  

def make_parser(template):
    parser = Parser()

    # parse states
    top, element = range(2)
    state = top

    last_indent = 0
    current = None
    for line in template.splitlines():
        s = line.lstrip()
        if s == "":
            continue

        # unindent means new css selector block        
        indent = len(line) - len(s)
        if indent < last_indent:
            state = top  #must be element again
            parser.elements.append(current)
            current = None
        last_indent = indent

        if state == top:
            state = element
            current = Element(s)
        elif state == element:
            key, separator, tail = s.partition(" ")
            if separator == "":
                current.extractors.append([key, TextExtractor()])
            else:
                tail = tail.lstrip()
                if tail[0] == "$":
                    current.extractors.append([key, RegexExtractor(tail[1:])])
      
    if ( element != None ):
        parser.elements.append(current)

    return parser

f = open("..\\..\\item.html")
html = f.read()
page = fromstring(html)
parser = make_parser(template)
print parser.extract(page)
