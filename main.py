import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromedriver_autoinstaller.install()

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless")  # Railway GUI yo‘q!
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1280x720")

driver = webdriver.Chrome(options=options)
driver.get("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

print("Video ochildi! 60s kutilmoqda...")
time.sleep(60)
driver.quit()
