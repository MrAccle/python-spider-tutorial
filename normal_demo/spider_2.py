from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# using edge browser without window
options = webdriver.EdgeOptions()
options.add_argument("headless")
browser = webdriver.Edge(options=options)
browser.get('https://101.qq.com/#/hero')
# wait the hero list render finish
# using xpath to check the render finish or not
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[3]/div/div[2]/ul'))
)
# close the browser
body = browser.page_source
browser.close()

# paser the html body and find the hero detail
soup = BeautifulSoup(body, "html.parser")
heroes = soup.find_all("div", class_="hero-item")
print("=" * 20 + "采集到以下英雄" + "=" * 20)
for heroSoup in heroes:
    hero = {
        'name': heroSoup.find('p', class_="hero-name").text,
        'pic': heroSoup.find('img').get('src'),
    }
    print(hero)
print("=" * 20 + "采集结束,总共:" + str(len(heroes)) + "个英雄" + "=" * 20)
