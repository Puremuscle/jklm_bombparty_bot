from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import keyboard
import time
import random

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)



def join_game(driver):
    start = time.time()
    loop = True
    while loop == True:
        try:
            driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[1]/div[1]/button").click()
            loop = False
        except:
            pass
        if (time.time() - start) > 0.5:
            return
def get_text(driver):
    loop = True
    while loop == True:
        try:
            letters_given = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div").text
            return letters_given
        except:
            pass
def whos_turn(driver):
    loop = True
    start = time.time()
    while loop == True:
        try:
            turn = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[1]/span[1]").get_attribute("innerHTML")
            return turn
        except:
            pass
            if (time.time() - start) > 1:
                return "end"
def find_word(letters_given, read_in_dictionary):
    if read_in_dictionary == True: 
        with open('capitalize.txt') as word_file:
            valid_words = set(word_file.read().split())
    count = 0 
    word_list_data = []
    for i in valid_words:
        if i.find(letters_given) != -1:
            count = count + 1
            word_list_data.append(i)
    return word_list_data

def type_words(word, type_delay, driver, used_words):
    type_area = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div[2]/form/input")
    random_word = word[random.randint(0, len(word) - 1)]
    while used_words == random_word:
        random_word = word[random.randint(0, len(word) - 1)]
    used_words.append(random_word)
    type_delay_random = random.uniform(0, type_delay)
    try:
        for i in random_word:
            time.sleep(type_delay_random)
            type_area.send_keys(str(i))
        type_area.send_keys(Keys.ENTER)
    except:
        return


        




def bombparty_game_start(code, type_delay, account_name, auto_rejoin):
    read_in_dictionary = True
    driver = webdriver.Chrome(options=options)
    bombparty_game_url = f"https://jklm.fun/{code}"
    driver.get(bombparty_game_url)
    loop = True
    start = time.time()
    while loop == True:
        try:
            time.sleep(0.1)
            driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/form/div[2]/input").send_keys(Keys.DELETE)
            time.sleep(0.1)
            driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/form/div[2]/input").send_keys(account_name)
            time.sleep(0.1)
            driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/form/div[2]/button").click()
            loop = False
        except:
            pass
    loop = True
    while loop == True:
        try:
            driver.switch_to.frame(0)
            loop = False
        except: 
            pass
    loop = True
    start = time.time()
    while loop == True:
        try:
            driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/form/div[1]/div[1]/label").click()
            loop = False
        except:
            if (time.time() - start) > 0.5:
                loop = False
    loop = True
    while loop == True:
        try:
            try:
                driver.switch_to.frame(driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/iframe"))
            except:
                pass
            driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[1]/div[1]/button").click()
            loop = False
        except:
            pass
    while True:
        letters_given = get_text(driver)
        if letters_given.isalpha() == True:
            turn = whos_turn(driver)
            while turn == account_name:
                turn = whos_turn(driver)
                letters_given = get_text(driver)
                word = find_word(letters_given, read_in_dictionary)
                type_words(word, type_delay, driver, used_words)
                if letters_given.isalpha() == False:
                    if auto_rejoin == "y":
                        try:
                            join_game(driver)
                            used_words = []
                        except:
                                pass
        if letters_given.isalpha() == False:
            if auto_rejoin == "y":
                try:
                    join_game(driver)
                    used_words = []
                except:
                    pass







bombparty_game_start("FKRT",0.2, "best player", "y")