from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://quotes.toscrape.com/')

love_tag = WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH,'/html/body/div/div[2]/div[2]/span[1]/a'))
)
love_tag.click()

assert 'It is better to be hated for what you are than to be loved for what you are not.' in driver.page_source

inspirational_tag = WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH,'//html/body/div/div[2]/div[2]/span[2]/a'))
)
inspirational_tag.click()

assert "I have not failed. I've just found 10,000 ways that won't work." in driver.page_source

life_tag = WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.XPATH,'/html/body/div/div[2]/div[2]/span[3]/a'))
)
life_tag.click()

assert "Good friends, good books, and a sleepy conscience: this is the ideal life." in driver.page_source

driver.close()