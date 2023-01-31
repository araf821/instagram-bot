from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver_path = "~/chromedriver"
username = ""
password = ""

driver = webdriver.Chrome(executable_path=driver_path)

login_page = "https://www.instagram.com/"
driver.get(login_page)
sleep(2)

input_username = driver.find_element(By.NAME, "username")
input_password = driver.find_element(By.NAME, "password")

input_username.send_keys(username)
input_password.send_keys(password)
input_password.send_keys(Keys.ENTER)
sleep(3)

victim_link = "https://www.instagram.com/georgeson/"
driver.get(victim_link)
sleep(50)

victim_followers = driver.find_element(
    By.XPATH, '//*[@id="mount_0_0_qA"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div/span/span')

victim_followers.click()
sleep(1)

followers_div = driver.find_element(
    By.XPATH, '//*[@id="mount_0_0_qA"]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div')
followers = followers_div.find_elements(By.CSS_SELECTOR, "button")

for follower in followers:
    follower.click()
