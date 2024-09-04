from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def main():
    service = Service(executable_path="/opt/homebrew/bin/chromedriver")
    driver = webdriver.Chrome(service=service)

    driver.get("https://shuttleonline.ktmb.com.my/Home/Shuttle")
    print("---Done Executing---")
    time.sleep(10)

    driver.quit()
    print("---Exit---")

if __name__ == "__main__":
    main()