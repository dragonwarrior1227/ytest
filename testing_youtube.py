from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import random 
import socket 
from webdriver_manager.chrome import ChromeDriverManager
import os,sys, stat
import subprocess

hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr)
options = Options()



# chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
#                                       # and if it doesn't exist, download it automatically,
#                                       # then add chromedriver to path

# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument('--headless')
print(subprocess.Popen("npm install chromium-version@77",shell=True,stdout=subprocess.PIPE).communicate()[0])
chrome_path=r"{}/node_modules/chromium-version/lib/chromium/chrome-linux/chrome".format(os.getcwd())

os.environ['CHROME_PATH']=chrome_path
binary_path=os.environ.get('CHROME_PATH')
# out,err=subprocess.Popen("export NODE_CHROMIUM_CACHE_PATH=/opt/build/repo/chromer/ export NODE_CHROMIUM_REVISION=1039557 & export NODE_CHROMIUM_DOWNLOAD_HOST=https://npm.taobao.org/mirrors/chromium-browser-snapshots/ & npm install --save chromium",shell=True,stdout=subprocess.PIPE).communicate()
# print(out)

# p=subprocess.Popen("npm install --save  chromedriver selenium-webdriver" ,shell=True,stdout=subprocess.PIPE)

# out, err = p.communicate()
# print("abc",out)

# p2=subprocess.Popen("{} --version".format(chrome_path) ,shell=True,stdout=subprocess.PIPE)
# out, err = p2.communicate()
# print("abc",out)

# print(os.listdir(os.getcwd()+'/node_modules/chromium-version/lib/chromium/chrome-linux'))

# # print(os.listdir(os.getcwd()+'/chromer/'))
# print(os.getcwd())

# print(os.stat(path+'/chrome'))

# path=os.getcwd()+'/chrome/.org.chromium.Chromium.zLGDPO'
path=r'chrome/chromedriver'
os.chmod(path, 0o777)
options = Options()
options.binary_location =binary_path
options.add_argument('--headless')
options.add_argument('--no-sandbox')
# options.add_experimental_option("debuggerAddress", "127.0.0.1:8989")
try:
    driver = webdriver.Chrome(executable_path=path,chrome_options=options)
except Exception as e:
    print(e)
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

# driver.get('https://google.com')
# print(driver.title)

# search_bar = driver.find_element_by_name('q')
# search_bar.send_keys('test')


# options.add_argument('--disable-dev-shm-usage')
# service=Service(ChromeDriverManager(path = r"Drivers").install())
# path=os.getcwd()+'/Drivers/.wdm/drivers/chromedriver'
# print(os.stat(path))
# os.chmod(path, 0o777)
# os.chmod(path,stat.S_IRWXO)
# print(os.stat(path))
# path="chromedriver.exe"
# driver = webdriver.Chrome( options=options)
print(os.listdir(os.getcwd()))
url = 'https://www.youtube.com/watch?v=ku3HSNT0I-g'
# # path = 'scrape.png'

# # driver = webdriver.Firefox()

driver.get(url)
time.sleep(3)
driver.save_screenshot(path)
driver.quit()
# cookies=[{'domain': '.youtube.com', 'expiry': 1693776783, 'httpOnly': True, 'name': '__Secure-3PSIDCC', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AEf-XMQGTwepyjBYX6sYbodnnxwpSzoIOpIE6AK-n40ls8_KbwpTfkgM99q391xYqF6DqAVVhg'}, {'domain': '.youtube.com', 'expiry': 1693776783, 'httpOnly': True, 'name': '__Secure-1PSIDCC', 'path': '/', 'secure': True, 'value': 'AEf-XMTKzYGKwa95ycyzlraVG0n13BdCGq3W-izNxCf7-yIYyzVPz0sthK5Ix2BVsxmJzb4W'}, {'domain': '.youtube.com', 'expiry': 1696368755, 'httpOnly': True, 'name': '__Secure-YEC', 'path': '/', 'sameSite': 'Lax', 'secure': True, 'value': 'CgtyNm9xbndna0dtayiOkM-YBg%3D%3D'}, {'domain': '.youtube.com', 'expiry': 1696800781, 'httpOnly': True, 'name': 'LOGIN_INFO', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'AFmmF2swRAIgeTSsxUyWhTidfq_qLwbF9J9PjopO7kk3EgLSwG2jdy4CIByzmM0oOgZ13nf_Eun1OkPxaLn3lnMeH1XCaleRY1Td:QUQ3MjNmelQzMDlFSDhjb3REVnp1bGtIN2l2WU1oX2NRRDIxRmNTZmttcnM4TTZueTR3cWlZcG1wT3JJMlNscjZvX3FzT2hla0F2Y3RjWkN4RkFHcm8xTm1iNzMySE82UG5ZekVUNkxiUkZyQXAxdWdxTnVxYnJRc3FySFZ5NlhSNGZlS2VfZVh6MmtuWXVyWWEzRFl0eE9PVmotNmh3N29n'}, {'domain': '.youtube.com', 'expiry': 1696800780, 'httpOnly': False, 'name': '__Secure-3PAPISID', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'D0-PPVn4xbMsTJ-M/AzMLLnzWaFjh6JknU'}, {'domain': '.youtube.com', 'expiry': 1696800780, 'httpOnly': True, 'name': '__Secure-1PSID', 'path': '/', 'secure': True, 'value': 'OAjcTQfQ3DWWajAPttwUu1MOMR7-HNujx33PIBs9iZ9qdOftLUsSY20xgaKiR-K4QADX1w.'}, {'domain': '.youtube.com', 'expiry': 1696800780, 'httpOnly': False, 'name': 'SAPISID', 'path': '/', 'secure': True, 'value': 'D0-PPVn4xbMsTJ-M/AzMLLnzWaFjh6JknU'}, {'domain': '.youtube.com', 'expiry': 1696800780, 'httpOnly': True, 'name': '__Secure-3PSID', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'OAjcTQfQ3DWWajAPttwUu1MOMR7-HNujx33PIBs9iZ9qdOftybCVRCMMLOGlpyKpYKYi8g.'}, {'domain': '.youtube.com', 'expiry': 1696800780, 'httpOnly': False, 'name': 'APISID', 'path': '/', 'secure': False, 'value': 'qQ52g4iKIt1yw3Ah/AAg8Z2PHROAXWfxhc'}, {'domain': '.youtube.com', 'expiry': 1696800780, 'httpOnly': True, 'name': 'SSID', 'path': '/', 'secure': True, 'value': 'A9IY-7Y2ccQWGbw_W'}, {'domain': '.youtube.com', 'expiry': 1696800780, 'httpOnly': False, 'name': 'SID', 'path': '/', 'secure': False, 'value': 'OAjcTQfQ3DWWajAPttwUu1MOMR7-HNujx33PIBs9iZ9qdOftXUuYBT0cDAAOqzLBXpEa5A.'}, {'domain': '.youtube.com', 'expiry': 1693776783, 'httpOnly': False, 'name': 'SIDCC', 'path': '/', 'secure': False, 'value': 'AEf-XMQDt2IFP6wOOGs2EaRB2AMjITTRDJFjRzOaB434gfteuHwszvrw-rTX4dl9n6nnIzq2vw'}, {'domain': '.youtube.com', 'expiry': 1696800782, 'httpOnly': False, 'name': 'PREF', 'path': '/', 'secure': True, 'value': 'f4=4000000&tz=Europe.Berlin'}, {'domain': '.youtube.com', 'expiry': 1696800780, 'httpOnly': False, 'name': '__Secure-1PAPISID', 'path': '/', 'secure': True, 'value': 'D0-PPVn4xbMsTJ-M/AzMLLnzWaFjh6JknU'}, {'domain': '.youtube.com', 'expiry': 1696800756, 'httpOnly': False, 'name': 'CONSENT', 'path': '/', 'secure': True, 'value': 'PENDING+759'}, {'domain': '.youtube.com', 'expiry': 1696800780, 'httpOnly': True, 'name': 'HSID', 'path': '/', 'secure': False, 'value': 'ALKicwGR6CrqSgocV'}, {'domain': '.youtube.com', 'httpOnly': True, 'name': 'YSC', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'Mo74Hzmqjhg'}]
# for cookie in cookies:
#     driver.add_cookie({'name':cookie['name'],'value':cookie['value']})



# for i in range(300):

#     # time.sleep(15)
#     driver.get(url)

#     time.sleep(5)
#     actions = ActionChains(driver)
#     actions.send_keys(Keys.SPACE).perform()
#     # eles=driver.find_elements(By.TAG_NAME, 'tp-yt-paper-button"]')
#     # print(eles)
#     # for ele in eles:
#     #     t=ele.get_attribute("aria-label")
#     #     print(t)
#     # driver.find_element_by_tag_name('body')
#     a=random.randint(5,80)
#     print("sleeping for ",a, " seconds")
#     time.sleep(a)
#     # print(driver.get_cookies())
#     # driver.save_screenshot(path)
#     # el.screenshot(path)
#     driver.get("www.google.com")
#     b=random.randint(1500,4200)
#     print("sleeping for ",b, " seconds")
#     time.sleep(b)

# # driver.quit()