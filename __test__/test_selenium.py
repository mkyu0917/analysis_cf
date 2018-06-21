import time
from selenium import webdriver

wd=webdriver.Chrome('C:/Users/minkyu/Desktop/코딩프로그램/chromedriver.exe')
wd.get('http://www.google.com')

time.sleep(5) # 대기 5초
html=wd.page_source
print(html)



wd.quit()#끄기