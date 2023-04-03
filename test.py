from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# Navigate to the URL
driver.get("https://dir.indiamart.com/impcat/tmt-bars.html")

# Wait for the page to load
driver.implicitly_wait(10)


body = driver.find_element(By.TAG_NAME, "body")
for i in range(10):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

# Get the HTML of the whole page
html = driver.page_source




file = open("./data.csv", "w")
writer = csv.writer(file)
writer.writerow(
    ["title", "price", "Brand", "Type", "Usage", "Grade", "Size", "PCT Elongation"]
)
doc = BeautifulSoup(html, "html.parser")

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
