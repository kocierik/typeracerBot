from selenium import webdriver
import geckodriver_autoinstaller
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time 

def seleniumDefinition():
    options = Options()
    driver = webdriver.Firefox()
    return driver

def runBot(driver):
    driver.get("https://play.typeracer.com/?universe=lang_it")
    time.sleep(4)
    driver.find_element(By.CLASS_NAME,"prompt-button").click()
    time.sleep(10)
    test = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div").text
    print(test)
    time.sleep(15)
    for char in range(0,len(test)):
        driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[2]/td[3]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input").send_keys(test[char])
        #time.sleep(0.08)
#send_keys()
def main():
    geckodriver_autoinstaller.install()
    driver = seleniumDefinition()
    runBot(driver)
    time.sleep(10)
#    driver.close()

if __name__ == "__main__":
    main()
    





