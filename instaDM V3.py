import webbrowser
from selenium import webdriver 
import time
import pyautogui 
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




current_path = os.path.dirname(os.path.abspath(__file__))

names_file_name = "users.txt"
index_file_name = "index.txt"

# Den vollständigen Pfad für die Dateien erstellen
names_file_path = os.path.join(current_path, names_file_name)
index_file_path = os.path.join(current_path, index_file_name)

index_file_path = os.path.join(current_path, "index.txt")



from selenium.webdriver.common.by import By 
browser=webdriver.Chrome('chromedriver.exe')
browser.get('https://instagram.com/')
time.sleep(5)

#browser.minimize_window()

current_index = 0
names_count = 0

def get_next_name():
    global names_count
    global current_index
    
    names = None

    with open(names_file_path, "r", encoding="utf-8") as names_file:
        names = names_file.read().strip().split("\n")
        names_count = len(names)

    with open(index_file_path, "r+") as index_file:
        current_index_str = index_file.read().strip()
        if not current_index_str:
            current_index_str = '-1'

        current_index = int(current_index_str) - 1
        index_file.seek(0)
        index_file.write(str((current_index + 1) % names_count))
        index_file.truncate()

    if names:
        return names[current_index % names_count]
    else:
        return None



def generate_text1():
    global generated_text1
    name = get_next_name()
    generated_text1 = f"Hey , {name}\n"
    
    
    return generated_text1

generated_text1 = generate_text1()
get_next_name = get_next_name



def genereate_text2():
    global generated_text2
    generated_text2 = f"Example Text\n"

    return generated_text2

generated_text2 = genereate_text2()


def genereate_text3():
    global generated_text3
    generated_text3 = f"Example Text!\n"

    return generated_text3

generated_text3 = genereate_text3()


def genereate_text4():
    global generated_text4
    generated_text4 = f"Best Wishes\n"

    return generated_text4

generated_text4 = genereate_text4()


def GlobalUsername():
    return 'Set Your Username'

def Globalpassword():
    return 'Your Password'
    

def login():
	username =browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
	username.send_keys(GlobalUsername())
	time.sleep(2)
	password=browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
	password.send_keys(Globalpassword())
	password.submit()
	time.sleep(7)
#Notifications
def notification():
	Notnow=browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
	Notnow.click()
	time.sleep(3)
	Noti=browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
	Noti.click()
	time.sleep(3)
        
        
#Message
def message():
    #url = "https://www.instagram.com/direct/inbox"
    #webbrowser.open(url)
	msgclick=browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/div/span/div/a/div/div[1]/div/div')
	msgclick.click()
	time.sleep(5)
    #msgclick=browser.find_element(By.CLASS_NAME, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[5]/div/div/div/span/div/a/div/div[1]/div/div/svg")
    #msgclick.click()
    #time.sleep(3)


#Final
def final():
    global names_count
    #chaticon=browser.find_element(By.CLASS_NAME, 'x1lliihq x1n2onr6')
    #chaticon.click()
    #time.sleep(5) 
    chaticon=browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[1]/div/div[1]/div/div')
    chaticon.click()
    time.sleep(5)
    botname=browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/form/div[1]/div[1]/div/label/input')
    botname.send_keys(GlobalUsername())
    botpass=browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/form/div[1]/div[2]/div/label/input')
    botpass.send_keys(Globalpassword())
    botpass.submit()
    time.sleep(5)
    iconchat=browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div')
    iconchat.click()
    time.sleep(3)
    typename=browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/input')
    typename.send_keys(get_next_name())
    time.sleep(5)
    name=browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[2]/div/div')
    name.click()
    #browser.maximize_window() 
    time.sleep(5)
    next=browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div')
    next.click()
    time.sleep(5)
    #browser.minimize_window()
    mbox=browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')
    mbox.send_keys(generated_text1, generated_text2, generated_text3, generated_text4)
    time.sleep(7)
    #send=browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/div')
    #send.click()
    #time.sleep(2)
    

    with open(index_file_path, "r+") as index_file:
        current_index_str = index_file.read().strip()
        if not current_index_str:
            current_index_str = '0'

        current_index = int(current_index_str)
        index_file.seek(0)
        index_file.write(str((current_index + 1) % names_count))
        index_file.truncate()
    time.sleep(10)


GlobalUsername()
Globalpassword()
login()
notification()
message()

for _ in range(20):
    name = get_next_name()
    generated_text1 = generate_text1()
    generated_text2 = genereate_text2()
    generated_text3 = genereate_text3()
    generated_text4 = genereate_text4()
    final()
    time.sleep(2)

    