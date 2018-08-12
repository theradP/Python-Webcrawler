from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__(self)
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

# when we call feed() this function is called when it gets an opening tag 'a'    
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for(attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links                 

    def error(self, message):
        pass    