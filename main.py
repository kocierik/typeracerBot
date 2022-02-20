from selenium import webdriver
import geckodriver_autoinstaller
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time 

def seleniumDefinition():
    options = Options()
    driver = webdriver.Firefox()
    return driver

def startAndRun(driver):
    driver.find_element(By.CLASS_NAME,"prompt-button").click()
    time.sleep(10)
    test = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div").text
    print(test)
    time.sleep(15)
    for char in range(0,len(test)):
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input").send_keys(test[char])
        time.sleep(0.09)
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/a").click()
    time.sleep(15)
    test = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div").text
    print(test)
    time.sleep(15)
    for char in range(0,len(test)):
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input").send_keys(test[char])
        time.sleep(0.09)
    
def runBot(driver):
    driver.get("https://play.typeracer.com/?universe=lang_it")
    time.sleep(4)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/table/tbody/tr/td[3]/div/div[2]/div[1]/div[2]/a[2]").click() 
    driver.find_element(By.NAME,"username").send_keys("USERNAME")
    driver.find_element(By.NAME,"password").send_keys("PASSWORD")
    driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[3]/div/div[1]/div/table[1]/tbody/tr[2]/td/div/table/tbody/tr[4]/td[2]/table/tbody/tr/td[1]/button").click()
    time.sleep(2)
    driver.get("https://play.typeracer.com/?universe=lang_it")
    time.sleep(1)
    startAndRun(driver)

def main():
    geckodriver_autoinstaller.install()
    driver = seleniumDefinition()
    runBot(driver)
    time.sleep(10)
    driver.close()

if __name__ == "__main__":
    main()
    




