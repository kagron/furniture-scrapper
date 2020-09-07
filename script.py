#! python3
import requests, bs4
from bs4 import Tag

URLS = (
    "https://www.ashleyfurniture.com/p/gavelston_coffee_table/T732-1.html#q=gavelston%2Bcoffee%2Btable&lang=default&start=2",
    "https://www.ashleyfurniture.com/p/gavelston_coffee_table_with_lift_top/T752-9.html#q=gavelston%2Bcoffee%2Btable&lang=default&start=1",
    "https://www.ashleyfurniture.com/p/parellen_counter_height_bar_stool/D291-124.html?cgid=bar-stools#start=1"
)

def filter_hidden_class(tag):
    if (tag.name == "button"):
        print(tag.attrs['class'])
        print(len(tag.attrs['class']))
        print("-------------")
    # return True
    return tag and tag.name == "button" and "visually-hidden" not in tag.attrs['class']

for url in URLS:
    res = requests.get(url)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('div.product-add-to-cart')
    if (len(elems) > 0):
        tags = elems[0].find_all(filter_hidden_class)
        print(tags)
            
        