import tkinter as tk
from tkinter import simpledialog
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
global point
point = 0

def add_account():
    username = simpledialog.askstring("Username", "Enter username:")
    password = simpledialog.askstring("Password", "Enter password:")
    if username is not None or password is not None:
        with open("accounts.txt", "a") as f:
            f.write(f"{username} {password}\n")

def show_accounts():
    with open("accounts.txt", "r") as f:
        accounts = f.readlines()
        accounts = [account.strip() for account in accounts]
        account_text.config(state=tk.NORMAL)
        account_text.delete(1.0, tk.END)
        for account in accounts:
            account_text.insert(tk.END, account + "\n")
        account_text.config(state=tk.DISABLED)

def add_tag():
    tag = simpledialog.askstring("Tag", "Enter tag:")
    if tag is not None:
        with open("tags.txt", "a") as f:
            f.write(tag + "\n")

def show_tags():
    with open("tags.txt", "r") as f:
        tags = f.readlines()
        tags = [tag.strip() for tag in tags]
        tag_text.config(state=tk.NORMAL)
        tag_text.delete(1.0, tk.END)
        for tag in tags:
            tag_text.insert(tk.END, tag + "\n")
        tag_text.config(state=tk.DISABLED)

def start_action():
    def login(username,password,driver):
        driver.get("https://www.instagram.com/")
        time.sleep(8)
        # Find the username and password fields and fill them in
        username_input = driver.find_element(By.NAME,"username")
        password_input = driver.find_element(By.NAME,"password")
        username_input.send_keys(username)
        password_input.send_keys(password)
        time.sleep(random.randint(3,6))
        # Submit the login form
        login_button = driver.find_element(By.XPATH,"//button[@type='submit']")
        login_button.click()

        # Wait for the page to load
        time.sleep(random.randint(10,15))

    def unfollow(driver):
        time.sleep(random.randint(2,6))
        findunfollow=driver.find_elements(By.XPATH,'//button[@tabindex="0"]')
        time.sleep(1)
        findunfollow[1].click()
    def click_on_close(driver):
        time.sleep(random.randint(6,12))
        close=driver.find_element(By.XPATH,'//*[@aria-label="Close"]')
        close.click()
    # search something
    def search(driver,name):
        time.sleep(random.randint(3,7))
        search_field = driver.find_element(By.XPATH,'//*[@aria-label="Search"]')
        search_field.click()

        # Wait for the search field to load
        time.sleep(2)
        searchinput=driver.find_element(By.XPATH,'//input[@aria-label="Search input"]')
        # Type in a search query
        search_query = name
        searchinput.send_keys(search_query)
        # searchinput.send_keys(Keys.RETURN)
        time.sleep(3)
        # try:
        # except:

        driver.implicitly_wait(3)

    def click_on_search_query(driver):
        time.sleep(random.randint(3,7))
        try:
            image=driver.find_elements(By.XPATH,'//*[@aria-label="Keyword"]')
            global ke
            ke=len(image)
        except:
            ke=0
        if ke == 0:
            search_link_click = driver.find_elements(By.XPATH, '//a[@role="link"]')
            search_link_click[10].click()
            time.sleep(random.randint(3,7))
        elif ke  !=0:
            search_link_click = driver.find_elements(By.XPATH, '//a[@role="link"]')
            search_link_click[11].click()
            time.sleep(random.randint(3,7))
    def click_on_following(driver,name):
        click_on_followings=driver.get(f'https://www.instagram.com/{name}/following/')
        time.sleep(random.randint(4,7))
        
    def check_is_following(driver,wait):
        time.sleep(random.randint(2,4))
        
    def click_on_follow_button(driver,wait):
        time.sleep(random.randint(3,7))
        
        button=wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[contains(text(),"Follow")]')))
        global point
        
        print(point)
        for i in button:
            time.sleep(random.randint(2,5))
            k=0
            try:
                i.click()
                try:
                    buttons=wait.until(EC.presence_of_all_elements_located((By.XPATH,'//button[@tabindex="0"]')))
                    point= len(buttons)
                
                except:
                    point = 1
                if point != 2:
                    # print(len(button))
                    pass
                elif point ==2:
                    time.sleep(2)
                    buttons=driver.find_elements(By.XPATH,'//button[@tabindex="0"]')
                    time.sleep(random.randint(0.8,1.5))
                    buttons[3].click()
                time.sleep(1)
                print(point,len(button))
            except:
                pass
            if k==22:
                break
            k=k+1
            
            
        
        
    
    def click_on_profile(driver,name):
        time.sleep(random.randint(3,5))
        my_following=driver.get(f'https://www.instagram.com/{name}/')
        

    def my_following(driver,name):
        time.sleep(random.randint(4,6))
        mf=driver.find_elements(By.XPATH,'//a[@role="link"]')
        mf[10].click
        print("Clicked on myfollowing")
        time.sleep(1000)
        
        
    def my_following_button(driver):
        time.sleep(random.randint(2,6))
        # try:
            
        my_followingbuttons=driver.find_elements(By.XPATH,'//*[contains(text(),"Following")]')
        j=0
        for k in my_followingbuttons:
            time.sleep(random.randint(2,3))
            k.click()
            unfollow(driver)
            if j==random.randint(5,8):
                break
            j=j+1
                #641900
        # except:
        #     pass

    def logout(driver):
        time.sleep(random.randint(4,8))
        sb=driver.find_element(By.XPATH,'//*[@aria-label="Settings"]')
        time.sleep(1.5)
        sb.click()
        time.sleep(0.7)
        lgu=driver.find_element(By.XPATH,'//span[contains(text(), "Log out")]')
        time.sleep(0.5)
        lgu.click()
        

    def pre_start_action():
        try:
            usernames = []
            passwords = []
            tags = []

            # Read usernames and passwords from the accounts file
            with open("accounts.txt", "r") as f:
                accounts = f.readlines()
                print(accounts)
                for account in accounts:
                    username, password = account.strip().split()
                    usernames.append(username)
                    passwords.append(password)
                print(usernames,passwords)
            # Read tag names from the tags file
            with open("tags.txt", "r") as jl:
                tags = [tag.strip() for tag in jl.readlines()]
            print(tags)
            return tags, usernames, passwords
        except:
            return None, None, None





    #chrome options
    def mainloop():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--incognito')

        # user name and password 
        tags, username, password = pre_start_action()
        if tags is None or username is None or password is None:
            print("Threre Is problem in file opening. Please check file path and try again")
        else:
            i=0
            while i<len(username):
                
                
                driver = webdriver.Chrome(options=chrome_options)
                driver.implicitly_wait(5)
                wait = WebDriverWait(driver, 5)
                time.sleep(2)
                login(username[i],password[i],driver)
                #for tag in tags:
                    #https://www.instagram.com/luxdynasties/following/
                    # search(driver,tag)
                    
                    # click_on_search_query(driver)
                    # click_on_following(driver,tag)
                    # click_on_follow_button(driver,wait)
                    # if point !=2:
                        
                    #     click_on_close(driver)
                click_on_profile(driver,username[i])
                my_following(driver,username[i])

                my_following_button(driver)

                # try:
                    
                #     click_on_close(driver)
                # except:
                #     pass
                # try:
                #     logout(driver)
                # except:
                #     pass
                i=i+1
                
            

            driver.close()
    mainloop()

root = tk.Tk()
root.title("Account and Tag Manager")

add_account_button = tk.Button(root, text="Add Account", command=add_account)
add_account_button.pack()

show_accounts_button = tk.Button(root, text="Show Accounts", command=show_accounts)
show_accounts_button.pack()

account_text = tk.Text(root, height=10, width=30)
account_text.pack()

add_tag_button = tk.Button(root, text="Add Tag", command=add_tag)
add_tag_button.pack()

show_tags_button = tk.Button(root, text="Show Tags", command=show_tags)
show_tags_button.pack()

tag_text = tk.Text(root, height=10, width=30)
tag_text.pack()

start_button = tk.Button(root, text="Start", command=start_action)
start_button.pack()

root.mainloop()
