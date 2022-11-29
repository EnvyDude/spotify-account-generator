import requests, string, random
import threading 
from colorama import Fore
from faker import Faker
fake = Faker()
import os
import json


with open('config.json') as config_file:config = json.load(config_file)

def intro():
    os.system('cls')
    print('Generating accounts!')

intro()
print('Enter number of threads')
threadCount = int(input(Fore.LIGHTMAGENTA_EX+"[>] "+Fore.RESET))
os.system('cls')

def stringg(length):
    pool=string.ascii_lowercase+string.digits
    return "".join(random.choice(pool) for i in range(length))

def text(length):
    return "".join(random.choice(string.ascii_lowercase) for i in range(length))

success = 0
errors = 0
intro()

def generate():
    global success
    global errors
    while True:
        nick =  fake.first_name()+ "1337"
        passw = config['password']
        email = nick+"@"+text(5)+".com"
        headers={"Accept-Encoding": "gzip",
             "Accept-Language": "en-US",
             "App-Platform": "Android",
             "Connection": "Keep-Alive",
             "Content-Type": "application/x-www-form-urlencoded",
             "Host": "spclient.wg.spotify.com",
             "User-Agent": "Spotify/8.6.72 Android/29 (SM-N976N)",
             "Spotify-App-Version": "8.6.72",
             "X-Client-Id": stringg(32)}
        payload = {"creation_point": "client_mobile",
            "gender": "male" if random.randint(0, 1) else "female",
            "birth_year": random.randint(1990, 2000),
            "displayname": nick,
            "iagree": "true",
            "birth_month": random.randint(1, 11),
            "password_repeat": passw,
            "password": passw,
            "key": "142b583129b2df829de3656f9eb484e6", 
            "platform": "Android-ARM",
            "email": email,
            "birth_day": random.randint(1, 20)}

        r = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account/', headers=headers, data=payload)
        
        if r.status_code==200:
            if r.json()['status']==1:
                print(r.text)
                print(Fore.BLUE + email+":"+passw+Fore.RESET)
                file = open('accounts.txt','a')
                file.write(email+':'+passw+'\n')
                file.close()
                success += 1
                os.system('title Spotify Gen - Success: '+str(success)+ ' Error: '+str(errors))
            else:
                print(Fore.LIGHTMAGENTA_EX + "Could not create the account, some errors occurred")
                errors +=1
                os.system('title Spotify Gen - Success: '+str(success)  + ' Error: '+str(errors))
    
threads = []
for i in range(threadCount):
     t = threading.Thread(target=generate)
     t.start()
     threads.append(t)
for i in range(threadCount):
    threads[i].join()




