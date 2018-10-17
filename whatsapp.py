from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(r'C:\Users\Rishabh-Pc\Downloads\chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

with open(r'D:\Web Development and Programming\CS50\Final Project\Test\contact.txt') as f:
    for line in f:
        try:
            name = (line.rstrip('\n'))
            for i in range(5):
                text = """Hello {}, My name is RishBot...
                    """.format(name)
                inp_xpath_search = "//input[@title='Search or start new chat']"
                input_box_search = wait.until(EC.presence_of_element_located((
                    By.XPATH, inp_xpath_search)))
                input_box_search.send_keys(name + Keys.ENTER)
                x_arg_contact = '//div[@class="_1Plpp"]'
                input_box_contact = wait.until(EC.presence_of_element_located((
                    By.XPATH, x_arg_contact)))
                inp_xpath = "//div[@contenteditable='true']"
                input_box = wait.until(EC.presence_of_element_located((
                    By.XPATH, inp_xpath)))
                input_box.send_keys(text + Keys.ENTER)
                time.sleep(2)
                print("send")
        except:
            print("error")
