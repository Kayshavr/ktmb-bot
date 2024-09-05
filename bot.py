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

def dateSelector(driver, date, month, sleep=True):
    #Add Human Response Time
    sleeptime = 0
    if sleep:
        sleeptime=1

    print("Selecting Date...")
    #Select Date
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "OnwardDate"))
    )
    departure_box = driver.find_element(By.ID, "OnwardDate")
    departure_box.click()
    time.sleep(sleeptime)

    #Month
    for x in range(0,month):
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "lightpick__next-action"))
        )
        month_arrow = driver.find_element(By.CLASS_NAME, "lightpick__next-action")
        month_arrow.click()
    time.sleep(sleeptime)

    #Date
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//*[text()='"+date+"' and contains(@class,'lightpick__day') and not(contains(@class, 'is-previous-month'))]"))
    )
    date_number = driver.find_element(By.XPATH, "//*[text()='"+date+"' and contains(@class,'lightpick__day') and not(contains(@class, 'is-previous-month'))]")
    date_number.click()
    time.sleep(sleeptime)

    #Search Ticket
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "btnSubmit"))
    )
    search_button = driver.find_element(By.ID, "btnSubmit")
    search_button.click()
    time.sleep(sleeptime)

def ticketSelector(driver, ticket_time, sleep=True):
    #Add Human Response Time
    sleeptime = 0
    if sleep:
        sleeptime=1

    print("Selecting Ticket...")
    #Go through Table Rows
    # Make Python sleep for some time 
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, 
        "/html/body/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/table"))
    )
    
    # Obtain the number of rows in body 
    rows = 1+len(driver.find_elements(By.XPATH, 
        "/html/body/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/table/tbody/tr")) 
    
    # Obtain the number of columns in table 
    cols = len(driver.find_elements(By.XPATH, 
        "/html/body/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/table/tbody/tr[1]/td")) 
    
    # Printing the table headers 
    # print("Locators           "+"             Description") 
    
    # # Printing the data of the table 
    # for r in range(1, rows): 
    #     for p in range(1, cols+1): 
    #         # obtaining the text from each column of the table 
    #         value = driver.find_element(By.XPATH, 
    #             "/html/body/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text 
    #         print(value, end='       ') 
    #     print() 
    time.sleep(sleeptime)
    
    #Select Ticket
    for r in range(1, rows): 
        p = 2
        value = driver.find_element(By.XPATH, 
            "/html/body/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/table/tbody/tr["+str(r)+"]/td["+str(p)+"]").text
        print("Row:" + str(r) + " Value: " + str(value))
        #Find ticket time
        if value==ticket_time:
            #Select Ticket
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/table/tbody/tr["+str(r)+"]/td[7]/a"))
            )
            select_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div[1]/div[3]/div/table/tbody/tr["+str(r)+"]/td[7]/a")
            select_button.click()
    time.sleep(sleeptime)

    # WebDriverWait(driver, 30).until(
    #     EC.presence_of_element_located((By.XPATH, "//tr[contains(@data-hourminute='1630')]/td[contains(@class='text-left')]//a[contains(@class='class='btn select-btn btn-seat-layout')]"))
    # )
    # date_number = driver.find_element(By.XPATH, "//tr[contains(@data-hourminute='1630')]/td[contains(@class='text-left')]//a[contains(@class='class='btn select-btn btn-seat-layout')]")
    # date_number.click()


def main():
    service = Service(executable_path="/opt/homebrew/bin/chromedriver")
    driver = webdriver.Chrome(service=service)

    driver.get("https://shuttleonline.ktmb.com.my/Home/Shuttle")

    # loginAccount(driver=driver, username=username, password=password, sleep=False)

    #Select Date
    dateSelector(driver=driver, date=ticket_date, month=month, sleep=False)

    #Select Ticket
    ticketSelector(driver=driver, ticket_time=ticket_time, sleep=False)
    print("---Done Executing---")
    time.sleep(10)

    driver.quit()
    print("---Exit---")

if __name__ == "__main__":
    main()