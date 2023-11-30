from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://dev.to")
 
driver.find_element_by_id("nav-search").send_keys("Selenium")