from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from random import randint
import undetected_chromedriver as uc 
import os
import yaml

class Scraper:
    
    wait_time = 5
    options = uc.ChromeOptions() 
    options.add_experimental_option(
    "prefs", {"credentials_enable_service": False, "profile.password_manager_enabled": False})
    options.add_argument('headless')
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    options.add_argument(f'--user-agent={ua}') 
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
    with open("configuration.yml", "r") as file:
      data = yaml.load(file, Loader=yaml.FullLoader)
    
    user_google_mail = data["account_email"]
    user_google_password = data["account_password"]
    

def maker(questions):
  S =  Scraper()

  try:
    save_chatgpt_account(S,"","")
  except:
    time.sleep(15)
    save_chatgpt_account(S,"","")
  ans_list = []

  for i in range(len(questions)):
    time.sleep(1)
    ans = while_loop(S,questions[i])
    ans_list.append(ans)
  S.driver.close()
  return ans_list


def while_loop(S,q):
  q = q.replace("\n" , " ")
  query = q
  answer = scrapping(S,query,"new",S.question_nb)
  return answer
  
def save_chatgpt_account(S,email_,password_):
  try:
    S.driver.implicitly_wait(15)
    print("Starting Login")
    S.driver.get(S.login_link)
    time.sleep(2)
    ggl = "/html/body/div/main/section/div/div/div/div[4]/form[2]/button/span[2]"

    element = WebDriverWait(S.driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="login-button"]')))
    login_button = S.driver.find_element(By.CSS_SELECTOR,'[data-testid="login-button"]')
    login_button.click()
    time.sleep(3)
    S.driver.get(S.driver.current_url)
    
    ggl2 = "/html/body/div/div/main/section/div[2]/div[3]/button[1]"
    try:
      element = WebDriverWait(S.driver, 15).until(
      EC.presence_of_element_located((By.XPATH, ggl)))
    
    except:
      element = WebDriverWait(S.driver, 15).until(
      EC.presence_of_element_located((By.XPATH, ggl2)))
    

    element.click()
    time.sleep(5)

    email_ = "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
    email_2 = "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
    password_ = "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"
    password_2 = "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"
    btn_ = "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button"
    btn_2 = "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span"
    em = S.user_google_mail
    ps = S.user_google_password
    version_one_of_google_login_page = False
    try:
      element = WebDriverWait(S.driver, 10).until(EC.presence_of_element_located((By.XPATH, email_)))
      email = S.driver.find_element(By.XPATH, email_)
      email.send_keys(em)
    except:
      version_one_of_google_login_page = True
      element = WebDriverWait(S.driver, 10).until(EC.presence_of_element_located((By.XPATH, email_2)))
      email = S.driver.find_element(By.XPATH, email_2)
      email.send_keys(em)
    
    try:
      if version_one_of_google_login_page == True:
        a = 10/0
      element = WebDriverWait(S.driver, 10).until(EC.presence_of_element_located((By.XPATH,btn_)))
      btn = S.driver.find_element(By.XPATH,btn_)
      btn.click()
    except:
      element = WebDriverWait(S.driver, 10).until(EC.presence_of_element_located((By.XPATH,btn_2)))
      btn = S.driver.find_element(By.XPATH,btn_2)
      btn.click()
      
    time.sleep(5)

    try:
      if version_one_of_google_login_page == True:
        a = 10/0
      element = WebDriverWait(S.driver, 10).until(EC.presence_of_element_located((By.XPATH, password_)))
      password = S.driver.find_element(By.XPATH, password_)
      password.send_keys(ps)
    except:
      element = WebDriverWait(S.driver, 10).until(EC.presence_of_element_located((By.XPATH, password_2)))
      password = S.driver.find_element(By.XPATH, password_2)
      password.send_keys(ps)
    
    try:
      if version_one_of_google_login_page == True:
        a = 10/0
      element = WebDriverWait(S.driver, 10).until(EC.presence_of_element_located((By.XPATH,btn_)))
      btn = S.driver.find_element(By.XPATH,btn_)
      btn.click()
    except:
      element = WebDriverWait(S.driver, 10).until(EC.presence_of_element_located((By.XPATH,btn_2)))
      btn = S.driver.find_element(By.XPATH,btn_2)
      btn.click()
    
    time.sleep(3)
    print("Login went well")
    time.sleep(5)
    try:
       element = WebDriverWait(S.driver, 10).until(
      EC.presence_of_element_located((By.ID, S.askid)))
    except:
      S.driver.close()

    
  except:
    pass



def scrapping(S, query,mode,nb,stop=0):
    S.driver.implicitly_wait(15)
    if stop >= 10:
      print("Too many errors happend closing ScrapGPT")
      quit()
    if mode == "new":
      S.driver.get(S.mainpage)
      
    time.sleep(1)
    S.driver.refresh()
    time.sleep(2.5)
    time.sleep(0.5)
    actions = ActionChains(S.driver)
    actions.send_keys(query).perform()
    actions.send_keys(Keys.RETURN).perform()
    time.sleep(10)
    
    for i in range(15):
      get_url = S.driver.current_url
      if "https://chat.openai.com/auth/login" in get_url:
        print("Wrong email or password change it on configuration.yml file")
        exit()
      try:
        element = S.driver.find_element(By.CSS_SELECTOR, '[data-testid="send-button"]')
      except Exception as e:
        time.sleep(10)
    print("Answering gpt")
    try:
      element = WebDriverWait(S.driver, 9).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, f'[data-testid="conversation-turn-{nb}"]')))
      answer = S.driver.find_element(By.CSS_SELECTOR,f'[data-testid="conversation-turn-{nb}"]')
      answer = answer.text
      return (answer.replace("ChatGPT",""))
    except Exception as e:
      if "Message: unknown error: net::ERR_INTERNET_DISCONNECTED" in str(e):
        print("No connection sleeping for 5 minutes")
        scrapping(S,query,mode,nb,stop)
        time.sleep(300)
      elif "element = WebDriverWait(S.driver, 9).until(" in str(e):
        time.sleep(15)
        stop+=1
        scrapping(S,query,mode,nb,stop)
      else:
        print("An error happend try again")
        S.driver.close()
      S.driver.close()
