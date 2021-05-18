import os
from subprocess import run
import pyautogui
from selenium import webdriver
import time

song_location = os.path.abspath(os.getcwd()+'\\Songs')  #create  a song folder in spotify folder before executing

os.chdir(song_location)

song_link = 'spotdl ' + pyautogui.prompt(text="Paste the link",title='Spotify Song Downloader') 

print("Song is downloading till the spotdl exe disappears")

data = run(song_link,capture_output=True)

song_name = ((data.stdout)[33:len(data.stdout)-2]).decode('utf-8')

#Code for sending song to your or someone else mobile

name = input("Name whom you want to send: ")

options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches',['enable-logging'])

options.add_argument(r"user-data-dir={x}".format(x=os.getcwd()+'\\'+'user'))      

driver  = webdriver.Chrome(options=options, executable_path=r'C:\Program Files (x86)\chromedriver.exe')

driver.get("https://web.whatsapp.com/")

time.sleep(10)

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

attachments = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[1]/div[2]/div/div/span")
attachments.click()

image = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/span")
image.click()

time.sleep(2)

pyautogui.typewrite(os.getcwd()+'\\'+song_name+'.mp3')
pyautogui.press('enter')

time.sleep(2)

send = driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/span/div/div")
send.click()
