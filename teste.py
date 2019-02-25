import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome() #set my browser
driver.get("https://www.youtube.com/?feature=youtu.be") # get the url
assert "YouTube" in driver.title
elem = driver.find_element_by_name("search_query")
print(elem)
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# driver.close()
