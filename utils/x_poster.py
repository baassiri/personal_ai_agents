from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

def post_to_x(tweet_text):
    print("🧪 Starting browser to post on X...")

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)

    driver.get("https://x.com/login")
    sleep(5)

    # 💡 Fill in your login credentials here
    EMAIL = os.getenv("X_USERNAME")  # Add to .env
    PASSWORD = os.getenv("X_PASSWORD")  # Add to .env

    # Login flow
    driver.find_element(By.NAME, "text").send_keys(EMAIL)
    driver.find_element(By.NAME, "text").send_keys(Keys.RETURN)
    sleep(3)

    try:
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)
    except:
        pass

    sleep(5)

    # Click the "Post" input box
    tweet_box = driver.find_element(By.CSS_SELECTOR, "div.public-DraftStyleDefault-block")
    tweet_box.click()
    tweet_box.send_keys(tweet_text)

    sleep(2)

    # Find and click the "Post" button
    buttons = driver.find_elements(By.XPATH, "//div[@data-testid='tweetButtonInline']")
    if buttons:
        buttons[0].click()
        print("✅ Tweet posted!")
    else:
        print("❌ Couldn't find post button.")

    sleep(3)
    driver.quit()
