from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import keyboard
import time
from jklm_scipts import *


#options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)
#driver = webdriver.Chrome(options=options)

def check_game_mode():
    loop = True
    while loop ==True:
        try:
            test_code.switch_to.frame(0)
            loop = False
        except:
            pass
    while True:
        data = test_code.find_element(By.XPATH, "/html/head/link[4]").get_attribute("href")
        loop = True
        while loop == True:
            try:
                time.sleep(0.1)  
                language = test_code.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[1]/div/span[1]').text
                loop = False
            except:
                pass
        if data.find("bombparty") != -1:
            print(f"Game: BombParty {language}")
            game = "bombparty"
            return game
        elif data.find("popsauce") == 31:
            print(f"Game: PopSauce{language}")
            print("This game is not supported yet. Please use the BombParty game mode.")
            game = "popsauce"
            return game
        else:
            print("Game: Unknown")
            return "unknown"

while True:
    code = input("what is the code:")
    if len(code) == 4:
        url = f"https://jklm.fun/{code}"
        print("trying code")
        test_code = webdriver.Chrome()
        test_code.minimize_window()
        test_code.get(url)
        time.sleep(0.2)
        button_test = test_code.find_element(By.XPATH, "/html/body/div[2]/div[3]/form/div[2]/button")
        button_test.click()
        time.sleep(0.2)
        data_test = test_code.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]")
        if data_test.text[0:5] == "Sorry":
            print("invalid code")
            test_code.quit()
        else:
            print("valid code, checking game")
            game = check_game_mode()


            if game == "bombparty":
                test_code.quit()
                print("starting bot")
                while True:
                    try:
                        type_delay = float(input("what is the delay time between each letter:"))
                        break
                    except:
                        print("only numbers are allowed")
                while True:
                    account_name = input("what is the account name:")
                    if len(account_name) > 0 and len(account_name) < 21:
                        break
                    else:
                        print("account name cannot be empty or exceed 20 characters")
                while True:
                    auto_rejoin = input("do you want to auto rejoin if you get kicked? (y/n):")
                    auto_rejoin = auto_rejoin.lower()
                    if auto_rejoin == "y" or auto_rejoin == "n":
                        break
                    else:
                        print("invalid input")

                bombparty_game_start(code, type_delay, account_name, auto_rejoin)


                
            elif game == "popsauce":
                test_code.quit()
                
            elif game == "unknown":
                test_code.quit()
                
            else:
                print("error")
                test_code.quit()
            