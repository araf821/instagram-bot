from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep

driver_path = "~/chromedriver"
username = ""
password = ""

driver = webdriver.Chrome(executable_path=driver_path)
action = ActionChains(driver)

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
sleep(3)

posts = driver.find_elements(
    By.CSS_SELECTOR, '._aang > ._aabd > a')

print(posts)
for post in posts:
    post.click()
    print("Clicked on post")
    sleep(2)
    post_content = driver.find_element(
        By.XPATH, '//*[@id="mount_0_0_pd"]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
    action.double_click(post_content)
    sleep(0.5)
    action.send_keys(Keys.ESCAPE)
    sleep(0.5)