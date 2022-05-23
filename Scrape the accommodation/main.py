from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

d = webdriver.Chrome(ChromeDriverManager().install())
d.get("https://www.ddproperty.com/%E0%B8%82%E0%B8%B2%E0%B8%A2%E0%B8%97%E0%B8%B5%E0%B9%88%E0%B8%94%E0%B8%B4%E0%B8%99")
d.find_element(By.CLASS_NAME, "btn-group").click()
d.find_element(By.ID, "more-filter-modal-residential-content").click()
d.find_element(By.XPATH, "//*[@id='price-content-for-sale']/ul/ul[1]/li[2]/input").send_keys(1000000)
d.find_element(By.XPATH, "//*[@id='price-content-for-sale']/ul/ul[2]/li[2]/input").send_keys(6000000)
d.find_element(By.XPATH, "//*[@id='more-filter-modal']/div/div/div[3]/button[2]").click()
page = d.find_elements(By.TAG_NAME, "div")