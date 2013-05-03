from HTMLParser import HTMLParser
from urlparse import urlparse
import sys

# from: http://stackoverflow.com/a/11659969/447661
#-------------------------------------------------------------------------------
def read_entirely( file ):
    with open( file, 'r' ) as handle:
        return handle.read()

images = []

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for name,value in attrs:
                if name == 'src':
                    o = urlparse(value)
                    images.append(o.scheme + "://" + o.netloc + o.path)

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
f = read_entirely(sys.argv[1])
parser.feed(f)

out = open('out.txt','w')
for item in images:
  out.write("%s\n" % item)
