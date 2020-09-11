import sys
import time
import datetime

user_id = ""
user_pw = ""

from modules.Chrome import Chrome

def open_chrome():

  # data binding
  url = "https://www.facebook.com"
  
  # create chrome object
  facebook = Chrome()

  # url setting
  facebook.set_url(url)

  # get chrome driver for input parameter
  driver = facebook.get_driver()

  return driver

def login(driver):
  driver.find_element_by_name('email').send_keys(user_id)
  driver.find_element_by_name('pass').send_keys(user_pw)
  driver.find_element_by_name('login').click()
  time.sleep(3)

def user_page(drive):
  driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[4]/div[1]/div[4]').click()

def scroll_down(driver, whileSeconds):
  start = datetime.datetime.now()
  end = start + datetime.timedelta(seconds=whileSeconds)
  while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)
    if datetime.datetime.now() > end:
        break

def get_data(driver):
  post = driver.find_elements_by_xpath("//div[@class='du4w35lb k4urcfbm l9j0dhe7 sjgh65i0']/div/div/div/div/div/div/div/div/div/div[2]/div/div[3]")
  for item in post:
    idx = post.index(item)
    print(idx)
    try:
      img = item.find_element_by_tag_name('img')
      img = img.get_attribute("src")
      print(img)
    except:
      continue

driver = open_chrome()
login(driver)
user_page(driver)

scroll_down(driver, 100)
get_data(driver)
