from selenium import webdriver
from time import sleep 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
 
driver_service = Service(executable_path="/Applications/chromedriver.exe" )
driver = webdriver.Chrome(service=driver_service)

driver.get("https://www.english.com/gse/teacher-toolkit/user/vocabulary?page=1&sort=gse;asc&gseRange=10;90&audience=GL")
sleep(5)

rows = len(driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/section[2]/section/div[2]/div/vocabulary-table/table/tbody/tr/td[1]/div"))
print("The number of rows is: ", rows)
cols = len(driver.find_elements(By.XPATH, "/html/body/div[1]/div[1]/section[2]/section/div[2]/div/vocabulary-table/table/tbody/tr/td/div"))
print("The number of cols is: ", cols)

for r in range(2, rows+1):
    for p in range(1, cols+1):
        
        # obtaining the text from each column of the table
        value = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/section/div[2]/div/vocabulary-table/table/tbody/tr[str(r)]/td[str(p)]/div").text
        print(value, end='       ')
    print()
