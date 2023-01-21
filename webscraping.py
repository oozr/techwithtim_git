from selenium import webdriver
from time import sleep 
from selenium.webdriver.chrome.service import Service

#Path = "/Applications/chromedriver.exe"

driver_service = Service(executable_path="/Applications/chromedriver.exe" )
driver = webdriver.Chrome(service=driver_service)

driver.get("https://www.english.com/gse/teacher-toolkit/user/lo")
sleep(10)