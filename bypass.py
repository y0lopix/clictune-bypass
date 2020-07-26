from requests import get
from urllib.parse import unquote
from lxml import html
from lxml import etree
from sys import argv

if len(argv)==2:
    tree = html.fromstring(get(argv[1]).text)
    redir_link = tree.xpath("//*[@id='compteur']/noscript/a")
    encoded_url=redir_link[0].attrib['href'].split("url=")[1].split("&")[0]
    print(unquote(encoded_url))
else:
    print("Wrong number of arguments.")
