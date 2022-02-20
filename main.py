from selenium import webdriver
import geckodriver_autoinstaller
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time 

def seleniumDefinition():
    options = Options()
    driver = webdriver.Firefox()
    return driver

def startAndRun(driver, speed):
    driver.find_element(By.CLASS_NAME,"prompt-button").click()
    time.sleep(10)
    test = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div").text
    print(test)
    time.sleep(15)
    for char in range(0,len(test)):
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input").send_keys(test[char])
        time.sleep(speed)
    
def runBot(driver, username, psw, speed):
    driver.get("https://play.typeracer.com/?universe=lang_it")
    time.sleep(4)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/table/tbody/tr/td[3]/div/div[2]/div[1]/div[2]/a[2]").click() 
    driver.find_element(By.NAME,"username").send_keys(username)
    driver.find_element(By.NAME,"password").send_keys(psw)
    driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[4]/td[2]/table/tbody/tr/td[1]/button").click()
    time.sleep(2)
    driver.get("https://play.typeracer.com/?universe=lang_it")
    time.sleep(1)
    startAndRun(driver, speed)

def main():
    geckodriver_autoinstaller.install()
    
    username = input("Insert your username: ")
    psw = input("Insert your password: ")
    print("NOTE: a value of 0,09 it's about 100 wpm")
    speed = float(input("Insert typing speed: "))
    
    driver = seleniumDefinition()


    runBot(driver, username, psw, speed)
    time.sleep(5)
    driver.close()

if __name__ == "__main__":
    main()
    




