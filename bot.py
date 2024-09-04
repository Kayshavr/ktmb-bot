from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

def loginAccount(driver, username, password, sleep=True):
    #Add Human Response Time
    sleeptime = 0
    if sleep:
        sleeptime=1

    print("Logging In...")

    #Go to Login Page
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/Account/Login']"))
    )
    departure_box = driver.find_element(By.XPATH, "//a[@href='/Account/Login']")
    departure_box.click()
    time.sleep(sleeptime)

    #Fill up Username
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "Email"))
    )
    username_box = driver.find_element(By.ID, "Email")
    username_box.clear()
    username_box.send_keys(username)
    time.sleep(sleeptime)

    #Fill up Password
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "Password"))
    )
    password_box = driver.find_element(By.ID, "Password")
    password_box.clear()
    password_box.send_keys(password)
    time.sleep(sleeptime)

    #Login
    if username!="Test":
        print("Authenticating...")
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "LoginButton"))
        )
        login_button = driver.find_element(By.ID, "LoginButton")
        login_button.click()
    time.sleep(0.5)

    #Go to Shuttle Tebrau Page
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div[2]/button"))
    )
    ok_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div[2]/button")
    ok_button.click()
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/Home/Shuttle']"))
    )
    departure_box = driver.find_element(By.XPATH, "//a[@href='/Home/Shuttle']")
    departure_box.click()

def main():
    service = Service(executable_path="/opt/homebrew/bin/chromedriver")
    driver = webdriver.Chrome(service=service)

    driver.get("https://shuttleonline.ktmb.com.my/Home/Shuttle")

    # loginAccount(driver=driver, username=username, password=password, sleep=False)

    print("---Done Executing---")
    time.sleep(10)

    driver.quit()
    print("---Exit---")

if __name__ == "__main__":
    main()