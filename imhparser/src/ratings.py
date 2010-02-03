import yaml
import re

#regex to extract JS data associated with the item
dataJsPattern = re.compile(r"""/\* <!\[CDATA\[ \*/var params = (\{.*\}).*""")

def ratings_from_page(page):
    for rating_html in page.cssselect("td.'vat pl10'"):
        rating = {}
        
        #parse author
        author_html = rating_html.cssselect("div span a")[0]    
        rating["authorLink"] = author_html.attrib["href"]
        rating["authorName"] = author_html.text_content()    

        #parse item name
        item_html = rating_html.cssselect("div div a")[0]
        rating["itemLink"] = item_html.attrib["href"]
        rating["itemName"] = item_html.text_content()

        #parse rating data from javascript
        for script_html in rating_html.cssselect("script"):        
            script = script_html.text_content()
            
            match = dataJsPattern.match(script)            
            if match is not None:
                # let's treat JS object initializer as YAML
                # put space after semicolon to make a valid YAML
                yamlData = match.group(1).replace(":", ": ")
                data = yaml.load(yamlData)
                #add all the data from JS
                rating.update(data)

        yield rating
