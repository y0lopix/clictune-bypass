from requests import get
from urllib.parse import unquote
from lxml import html
from lxml import etree
from sys import argv

if len(argv)>1:
    for i in argv[1:]:
        tree = html.fromstring(get(i).text)
        redir_link = tree.xpath("//*[@id='compteur']/noscript/a")
        encoded_url=redir_link[0].attrib['href'].split("url=")[1].split("&")[0]
        print(unquote(encoded_url))
else:
    print("No arguments provided.")
