from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from os import system
import time
import os.path
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import traceback
from random import randint
import undetected_chromedriver as uc 
import pickle
import os
import yaml

class Scraper:
    
    wait_time = 5
    
    options = uc.ChromeOptions() 
    options.add_experimental_option(
    "prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False})
    #options.add_argument('headless')
    driver = uc.Chrome(options=options)
    driver.maximize_window()
    login_link = "https://chat.openai.com/auth/login"
    emailxpath = "/html/body/div/main/section/div/div/div/div[1]/div/form/div[1]/div/div/div/input"
    passwordxpath = "/html/body/div[1]/main/section/div/div/div/form/div[2]/div/div[2]/div/input"
    continuexpath = "/html/body/div/main/section/div/div/div/div[1]/div/form/div[2]/button"
    continuexpath2 = "/html/body/div[1]/main/section/div/div/div/form/div[3]/button"
    mainpage = "https://chat.openai.com/"
    askid = "prompt-textarea"
    has_asked_question = False
    chatgptanswer = "/html/body/div[1]/div[1]/div/main/div[1]/div[1]/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]"
    question_nb = 3
    btn_there = "/html/body/div[1]/div[1]/div/main/div[1]/div[1]/div/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div"
    dodo  = "/html/body/div[1]/div[1]/div/main/div[1]/div[1]/div/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/button[1]/svg"
    d = "icon-md"
    #time.sleep(20)

def save_coockie(selenium_session):
    pickle.dump(selenium_session.driver.get_cookies(), open(f"cookies.pkl", "wb"))

def maker():
  S =  Scraper()
  with open("configuration.yml", "r",encoding="utf-8") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

  email_info = data["account_email"]
  password_info = data["account_password"]
  try:
    save_chatgpt_account(S,email_info,password_info)
  except:
     time.sleep(15)
     save_chatgpt_account(S,email_info,password_info)
  time.sleep(1)
  print("To stop the code just write stop or do Ctrl-C")
  while_loop(S)


def while_loop(S):
  stop = True
  while stop:
    query = input("Ask anything to ScrapGPT: ")
    if query.lower() == "stop":
      stop = False
    if S.has_asked_question == False:
      a = scrapping(S,query,"new",S.question_nb)
    else:
      a = scrapping(S,query,"",S.question_nb)
    S.question_nb += 2
    print("ScrapGPT answer: \n" , a)
    S.has_asked_question = True

def save_chatgpt_account(S,email_,password_):
  print("Starting Login")
  S.driver.get(S.login_link)
  time.sleep(2)
  element = WebDriverWait(S.driver, 15).until(
  EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="login-button"]')))
  login_button = S.driver.find_element(By.CSS_SELECTOR,'[data-testid="login-button"]')
  login_button.click()
  element = WebDriverWait(S.driver, 15).until(
  EC.presence_of_element_located((By.XPATH, S.emailxpath)))

  email = S.driver.find_element(By.XPATH,S.emailxpath)
  email.send_keys(email_) 

  element = WebDriverWait(S.driver, 15).until(
  EC.presence_of_element_located((By.XPATH, S.continuexpath)))

  continuebtn = S.driver.find_element(By.XPATH,S.continuexpath)
  
  continuebtn.click()
  element = WebDriverWait(S.driver, 15).until(
  EC.presence_of_element_located((By.XPATH, S.passwordxpath)))
  password = S.driver.find_element(By.XPATH,S.passwordxpath)
  password.send_keys(password_) 

  element = WebDriverWait(S.driver, 15).until(
  EC.presence_of_element_located((By.XPATH, S.continuexpath2)))
  
  continuebtn = S.driver.find_element(By.XPATH,S.continuexpath2)
  
  continuebtn.click()

  time.sleep(2)
  
  try:
    element = WebDriverWait(S.driver, 15).until(
    EC.presence_of_element_located((By.XPATH, S.passwordxpath)))
    password = S.driver.find_element(By.XPATH,S.passwordxpath)
    password.send_keys(password_) 

  except:
    pass
  
  print("Login went well")

def scrapping(S, query,mode,nb):
    if mode == "new":
      S.driver.get(S.mainpage)
      
    time.sleep(1)
    S.driver.refresh()
    element = WebDriverWait(S.driver, 10).until(
        EC.presence_of_element_located((By.ID, S.askid)))
    
    ask = S.driver.find_element(By.ID, S.askid)
    time.sleep(0.5)

    S.driver.execute_script("arguments[0].scrollIntoView();", ask)
    time.sleep(0.5)
    ask.click()
    time.sleep(0.5)
    ask.send_keys(query) 
    ask.send_keys(Keys.RETURN)
    time.sleep(5)
    
    for i in range(7):
      try:
          element = WebDriverWait(S.driver, 3).until(
          EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="send-button"]')))
      except:
        time.sleep(10)

    try:
      element = WebDriverWait(S.driver, 9).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, f'[data-testid="conversation-turn-{nb}"]')))
      answer = S.driver.find_element(By.CSS_SELECTOR,f'[data-testid="conversation-turn-{nb}"]')
    except Exception as e:
      if "element = WebDriverWait(S.driver, 9).until(" in str(e):
        time.sleep(15)
        scrapping(S,query,mode,nb)
      else:
        print("An error happend closing the program")
    answer = answer.text
    return (answer.replace("ChatGPT",""))