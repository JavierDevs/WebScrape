import sys
from urllib import request
from bs4 import BeautifulSoup

#css selector=>dev console=>press "ctrl+shift+c"=>hover over element and click=>right click=>copy=>copy selector
def findPrice(url,css_selector):
    request_page = request.urlopen(url)
    page = request_page.read()
    request_page.close()

    document = BeautifulSoup(page, "html.parser")
    price = document.select_one(css_selector)

    return(price.get_text())

if __name__ == "__main__":
    url = sys.argv[1]
    css_selector = sys.argv[2]
    print(findPrice(url,css_selector))