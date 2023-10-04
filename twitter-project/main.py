from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "C://Users/eduardo.cafiero/Downloads/Python_udemy_course/chromedriver.exe"
PROMISED_DOWN = 70
PROMISED_UP = 15
TWITTER_EMAIL = "skyflye@inwind.it"
TWITTER_PASSWORD = "xxxxx"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)



class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(executable_path=CHROME_DRIVER_PATH), options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        self.driver.find_element(By.ID, value="onetrust-accept-btn-handler").click()
        self.driver.find_element(By.CLASS_NAME, value="start-text").click()
        time.sleep(60)
        speeds = self.driver.find_elements(By.CLASS_NAME, value="result-data-large")
        self.down = float(speeds[0].text)
        self.up = float(speeds[1].text)


    def tweet_at_provider(self):
        self.driver.get("https://www.twitter.com/")
        time.sleep(7)
        username = self.driver.find_element(By.CSS_SELECTOR, value="input[type=text]")
        username.send_keys(TWITTER_EMAIL)
        username.send_keys(Keys.ENTER)
        time.sleep(7)
        try:
            username1 = self.driver.find_element(By.CSS_SELECTOR, value="input[type=text]")
            username1.send_keys("ProvaProva74449")
            username1.send_keys(Keys.ENTER)
        except:
            pass
        time.sleep(7)
        password = self.driver.find_element(By.CSS_SELECTOR, value="input[type=password]")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(10)
        #post_box = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        post_box = self.driver.find_element(By.CSS_SELECTOR, value="div.public-DraftStyleDefault-block")
        post_box.send_keys(f"Hey vodafone my internet connection is bad.\nDownload speed: {bot.down}\nUpload speed: {bot.up}")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

print(f"Download speed: {bot.down}")
print(f"Upload speed: {bot.up}")
bot.tweet_at_provider()
