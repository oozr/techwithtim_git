from webscraping import webdriver

Path = "/Applications/chromedriver.exe"
driver = webdriver.Chrome(Path)

driver.get("https://www.english.com/gse/teacher-toolkit/user/lo")