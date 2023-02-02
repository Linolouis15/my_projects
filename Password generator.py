import string
import time
import secrets
print('''
  _____                                           _    _____              
 |  __ \                                         | |  / ____|             
 | |__) |__ _  ___  ___ __      __ ___   _ __  __| | | |  __   ___  _ __  
 |  ___// _` |/ __|/ __|\ \ /\ / // _ \ | '__|/ _` | | | |_ | / _ \| '_ \ 
 | |   | (_| |\__ \\__ \ \ V  V /| (_) || |  | (_| | | |__| ||  __/| | | |
 |_|    \__,_||___/|___/  \_/\_/  \___/ |_|   \__,_|  \_____| \___||_| |_|
                                                                          
                                                                          
 ''')
def passwordgen(length):
    password="".join([secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.punctuation) for i in range(length)])
    print(str(password))
    time.sleep(10)
password_length=input("enter your password length : ")
passwordgen(int(password_length))
