import logging
import re
import yaml

#regex to extract JS data associated with the item
dataJsPattern = re.compile(r"""/\* <!\[CDATA\[ \*/var params = (\{.*\}).*""")

def trace(obj):
    s = tostring(obj, encoding="cp1251")
    print s[:50]
    
def ratings_from_page(page):
    i = 1
    for rating_html in page.cssselect("td.'vat pl10'"):
        try:
            rating = {}
            
            #parse author
            author_html = rating_html.cssselect("div span a")[0]    
            rating["author_link"] = author_html.attrib["href"]
            rating["author_name"] = author_html.text_content()

            #parse item name
            item_html = rating_html.cssselect("div div a")[0]
            rating["item_link"] = item_html.attrib["href"]
            rating["item_name"] = item_html.text_content()
            
            #parse rating data from javascript
            for script_html in rating_html.cssselect("script"):
                script = script_html.text_content()
                
                match = dataJsPattern.match(script)            
                if match is not None:
                    # let's treat JS object initializer as YAML                
                    yamlData = match.group(1)
                    # put space after semicolon to make a valid YAML
                    yamlData = yamlData.replace(":", ": ")
                    data = yaml.load(yamlData)
                    #add all the data from JS
                    rating.update(data)

            yield rating
        except:
            logging.error("Exception while parsing rating from html")
            pass
