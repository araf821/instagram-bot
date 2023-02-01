from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver_path = "~/chromedriver"
# Our account initialization
username = ""
password = ""

# Initialize drivers required for selenium to work
driver = webdriver.Chrome(executable_path=driver_path)

login_page = "https://www.instagram.com/"
driver.get(login_page)
sleep(2)

# Logging in to instagram
input_username = driver.find_element(By.NAME, "username")
input_password = driver.find_element(By.NAME, "password")

input_username.send_keys(username)
input_password.send_keys(password)
input_password.send_keys(Keys.ENTER)
sleep(3)

# Provide a link to the post you'd like to invade
post_link = "https://www.instagram.com/"
driver.get(post_link)
sleep(3)

num_of_comments = 20
comment_field = driver.get(By.XPATH, '')



sleep(30)