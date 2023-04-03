from bs4 import BeautifulSoup
import requests
from datetime import time
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
import re
import csv
from util import trim_data
driver = webdriver.Firefox()
url = "https://dir.indiamart.com/impcat/tmt-bars.html"
driver.get(url)
elem = driver
no_of_pagedowns = 20
while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1
file = open("./data.csv", "w")
writer = csv.writer(file)
writer.writerow(
    ["title", "price", "Brand", "Type", "Usage", "Grade", "Size", "PCT Elongation"]
)


post_elems = driver.find_elements_by_class_name("post-item-title")

for post in post_elems:
    print(post.text)


# r = requests.get(url)

# doc = BeautifulSoup(r.content, "html.parser")

# content_div = doc.find("div", {"id": "content"})
# second_div = content_div.contents[3]
# right_div = second_div.contents[1]
# products_list = right_div.contents[2].contents[5].contents[9]

# for item in products_list.contents[1].contents[1]:
#     try:
#         product = item.find("div").contents[0].contents[1]
#         product_desc = product.find("div", {"class": "desc"})
#         print(
#             product_desc.text,
#         )

#         a_tag = product.find("a")
#         writer.writerow([product_desc.text])
#     except Exception as error:
#         # print(error)
#         pass
