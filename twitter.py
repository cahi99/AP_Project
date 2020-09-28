import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('/chromedriver')
base_url = u'https://twitter.com/search?q='
query= u'Andres%20Arauz%20until%3A2019-12-31&src=typed_query&f=live'
url=base_url+query

browser.get(url)
time.sleep(1)
body= browser.find_elemente_by_tag_name('body')

for _ in range(5):
  body.send_keys(Keys.PAGE_DOWN)
  time.sleep(0.2)

tweets = browser.find_elemente_by_class_name('tweet-text')

for tweet in tweets:
  print(tweet.text)