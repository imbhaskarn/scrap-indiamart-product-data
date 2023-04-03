from bs4 import BeautifulSoup
import requests

import csv
url = "https://dir.indiamart.com/impcat/tmt-bars.html"

file = open("./product_data.csv", "w")
writer = csv.writer(file)
writer.writerow(
    ["title", "price", "Brand", "Type", "Usage", "Grade", "Size", "PCT Elongation"]
)




r = requests.get(url)

doc = BeautifulSoup(r.content, "html.parser")

content_div = doc.find("div", {"id": "content"})
second_div = content_div.contents[3]
right_div = second_div.contents[1]
products_list = right_div.contents[2].contents[5].contents[9]

for item in products_list.contents[1].contents[1]:
    try:
        product = item.find("div").contents[0].contents[1]
        product_desc = product.find("div", {"class": "desc"})
        print(
            product_desc.text,
        )

        a_tag = product.find("a")
        writer.writerow([product_desc.text])
    except Exception as error:
        # print(error)
        pass
