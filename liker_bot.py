from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep

driver_path = "~/chromedriver"
# Our account initialization
username = ""
password = ""

# Initialize drivers required for selenium to work
driver = webdriver.Chrome(executable_path=driver_path)
action = ActionChains(driver)

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

# Provide a link to the whoever you want to invade
victim_link = "https://www.instagram.com/"
driver.get(victim_link)
sleep(3)

# Get the <a> tag that contains a link to the standalone post for all posts
posts = driver.find_elements(
    By.CSS_SELECTOR, 'article div div div div a')

def like_posts():
    # For each link, go to the page and press the like button
    for link in post_links:
        driver.get(link)
        sleep(3)
        like_btn = driver.find_element(
            By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button')
        like_btn.click()
        sleep(0.5)

# Seperate the link from the <a> tag for all posts
post_links = [post.get_attribute("href") for post in posts]
like_posts()
