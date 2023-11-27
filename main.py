from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.common.by import By


#login to the instagram and wait
def main():
    
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
        findunfollow[1].click()
        
    # search something
    def search(driver,name):
        time.sleep(random.randint(6,10))
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
        time.sleep(random.randint(6,10))
        search_link_click = driver.find_elements(By.XPATH, '//a[@role="link"]')
        search_link_click[10].click()
        time.sleep(random.randint(6,10))
        
    def click_on_following(driver):
        time.sleep(random.randint(6,10))
        click_on_followings=driver.find_elements(By.XPATH,'//a[@role="link"] ')
        click_on_followings[11].click()

    def click_on_follow_button(driver):
        time.sleep(random.randint(6,10))
        button=driver.find_elements(By.XPATH,'//*[contains(text(),"Follow")]')
        k=0
        print(len(button))
        for i in button:
            time.sleep(random.randint(2,5))
            
            try:
                i.click()
                time.sleep(1)
            except:
                pass
            if k==17:
                break
            k=k+1
        
        
    def click_on_close(driver):
        time.sleep(random.randint(6,12))
        close=driver.find_element(By.XPATH,'//*[@aria-label="Close"]')
        close.click()
        
    def click_on_profile(driver):
        time.sleep(random.randint(6,12))
        profile=driver.find_elements(By.XPATH,'//a[@role="link"]')
        profile[8].click()
        time.sleep(2)

    def my_following(driver):
        time.sleep(random.randint(2,6))
        my_following=driver.find_elements(By.XPATH,'//a[@role="link"]')
        my_following[14].click()
        
    def my_following_button(driver):
        time.sleep(random.randint(2,6))
        try:
            
            my_followingbuttons=driver.find_elements(By.XPATH,'//*[contains(text(),"Following")]')
            j=0
            for k in my_followingbuttons:
                time.sleep(random.randint(2,3))
                k.click()
                unfollow(driver)
                if j==random.randint(5,8):
                    break
                j=j+1
                
        except:
            pass

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
                for account in accounts:
                    username, password = account.strip().split()
                    usernames.append(username)
                    passwords.append(password)

            # Read tag names from the tags file
            with open("tags.txt", "r") as f:
                tags = [tag.strip() for tag in f.readlines()]
            return tags, username, password
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
            for tag, user, passw in tags, username, password:
                
                driver = webdriver.Chrome(options=chrome_options)
                time.sleep(2)
                login(user,passw,driver)
                search(driver,tag)
                click_on_search_query(driver)
                click_on_following(driver)
                click_on_follow_button(driver)
                click_on_close(driver)
                click_on_profile(driver)
                my_following(driver)

                my_following_button(driver)

                try:
                    
                    click_on_close(driver)
                except:
                    pass
                try:
                    logout(driver)
                except:
                    pass
                time.sleep(1000)

                driver.close()
    mainloop()











# import csv
# import requests
# import re

# def extract_emails_from_text(text):
#     email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
#     emails = re.findall(email_pattern, text)
#     return emails

# def process_csv_file(input_file, output_file):
#     with open(input_file, 'r') as csv_input , open(output_file, 'w', newline='') as csv_output, open("error1.csv", 'w') as errors:
#         csv_reader = csv.reader(csv_input)
#         csv_writer = csv.writer(csv_output)
#         csv_errorwriter = csv.writer(errors)
#         k=0
#         m=0
#         for row in csv_reader:
#             if m >= 0:
#                 if len(row) != 0:
                    
#                     link = row[0]
#                 #print(link)
                
#                     # Assuming the link is in the first column and data to search is in the second column
#                     # data_to_search = row[1]
#                     try:
#                         response = requests.get(f"https://{link}/",timeout=3)
#                         if response.status_code == 200:
#                             emails = extract_emails_from_text(response.text)
#                             email_string = ', '.join(emails)
#                             new_row = [link, email_string]
#                             csv_writer.writerow(new_row)
#                             print(f"Processed: {link}")
#                         else:
#                             csv_writer.writerow(row)
#                             print(f"Error: {link}")
#                     except:
#                         k=k+1
#                         fail = f"Faild to connect {link}: {k}"
#                         print(fail)
#                         csv_errorwriter.writerow(row)
                    
#                 m=m+1    

# if __name__ == "__main__":
#     input_csv_file = input("Enter the input CSV file name: ")
#     output_csv_file = input("Enter the output CSV file name: ")
#     process_csv_file(input_csv_file, output_csv_file)





"""
import csv
import requests
import re
import threading
import signal
import sys
from queue import Queue

# Set up a thread-safe queue
data_queue = Queue()
exit_flag = False

def extract_emails_from_text(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    emails = re.findall(email_pattern, text)
    return emails

def process_row(row):
    global exit_flag
    link = row[0]
    #data_to_search = row[1]
    response = requests.get(f"https://{link}/")
    
    
    
    
    try:
        
        if response.status_code == 200:
            emails = extract_emails_from_text(response.text)
            email_string = ', '.join(emails)
            new_row = [link, email_string]
            data_queue.put(new_row)
            print(f"Processed: {link}")
        else:
            data_queue.put(row)
            print(f"Error: {link}")
    except:
        file=open("error1.csv","a",newline="")
        
        csver=csv.writer(file)
        csver.writerow(row)
        file.close()
        print(f"Error: {link}")
def process_csv_file(input_file):
    with open(input_file, 'r') as csv_input:
        csv_reader = csv.reader(csv_input)
        batch = []
        
        for row in csv_reader:
            batch.append(row)
            if len(batch) == 2000:
                process_batch(batch)
                batch = []
        
        if batch:
            process_batch(batch)

def process_batch(batch):
    threads = []
    
    for row in batch:
        thread = threading.Thread(target=process_row, args=(row,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def save_data_and_exit(signal, frame):
    global exit_flag
    
    if exit_flag:
        sys.exit(0)
    
    print("Saving data and exiting...")
    exit_flag = True
    process_batch(list(data_queue.queue))
    
    with open(output_csv_file, 'a', newline='') as csv_output:
        csv_writer = csv.writer(csv_output)
        while not data_queue.empty():
            csv_writer.writerow(data_queue.get())

    sys.exit(0)

if __name__ == "__main__":
    input_csv_file = input("Enter the input CSV file name: ")
    output_csv_file = input("Enter the output CSV file name: ")
    
    signal.signal(signal.SIGINT, save_data_and_exit)
    
    try:
        process_csv_file(input_csv_file)
        save_data_and_exit(None, None)
    except KeyboardInterrupt:
        save_data_and_exit(None, None)


"""