from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com")
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

# bypass captcha by clicking try different image...
try:
    captcha = driver.find_element(By.LINK_TEXT, "Try different image")
    captcha.click()
except:
    pass

price = driver.find_element(By.CLASS_NAME, "a-offscreen").get_attribute('innerHTML')
# num_price = price.strip("$")
print(price)

# driver.close()
driver.quit()