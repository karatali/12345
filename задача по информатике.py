class my_class(object):
    pass




import random
import string
import re

f = ["@mail.ru","@bk.com","@gmail.ru"]

All_file = []
Login=[]
Password=[]
mails=[]
Phone=[]

def mail_file(mail):

    
    result = re.findall(r'@', mail)
    if len(result)==1:
        
        mailq = re.findall("(@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", mail)
        bool = False
        for i in f:
            if("".join(mailq) == i):
                bool = True
                break
            else:
               bool = False
       
        mails.append(mail)
    else:
        wread_deff_mail = open(r'D:\Программы C#\Итоговая работа\Итоговая работа\deff_mail.txt','a')
        wread_deff_mail.write(mail+'\n')
        wread_deff_mail.close()
        #print("Mail is incorrect")
        mails.append("2")

def Gener_Log():
    Big = "QWERTYUIOPASDFGHJKLZXCVBNM"
    Low ="qwertyuiopasdfghjklzxcvbnm"
    Pass = ""
    
    for u in range(random.randint(7,15)):
        t = random.randint(1, 2)
        if t == 1:
            Pass += Big[random.randint(0,25)]
        else:
            Pass += Low[random.randint(0,25)]
    return Pass

def login_file(login):
    if(len(re.findall(r'[A-Z]{1}',login))==0):


        if(len(re.findall(r'[0-9]',login))>=1):

            wread_deff_login = open(r'D:\Программы C#\Итоговая работа\Итоговая работа\deff_login.txt','a')
            wread_deff_login.write(login+'\n')
            wread_deff_login.close()
            #print("Login is incorrect")
            Login.append(Gener_Log())

        else:

            wread_deff_login = open(r'D:\Программы C#\Итоговая работа\Итоговая работа\deff_login.txt','a')
            wread_deff_login.write(login+'\n')
            wread_deff_login.close()
            #print("Login is incorrect")
            Login.append(login[0].upper()+login[1:])
    else:

        
        wread_deff_login = open(r'D:\Программы C#\Итоговая работа\Итоговая работа\true_login.txt','a')
        wread_deff_login.write(login+'\n')
        wread_deff_login.close()
        #print("Login is correct")
        Login.append(login)

def Gener_Pass():

    Big = "QWERTYUIOPASDFGHJKLZXCVBNM"
    Low ="qwertyuiopasdfghjklzxcvbnm"
    Pass = ""
    
    for u in range(random.randint(7,15)):
        t = random.randint(1, 3)
        if t == 1:
            Pass+=str(random.randint(0,9))
        elif t == 2:
            Pass += Big[random.randint(0,25)]
        else:
            Pass += Low[random.randint(0,25)]
    return Pass

def Phone_file(phone):

    if re.match(r'[7-8]{1}[0-9]{9}', phone) and len(phone) == 10:
        
        Phone.append(phone)
    else:

        if(len(phone)<10):

            Phone.append(str(8)+phone)
        else:
       
            wread_deff_login = open(r'D:\Программы C#\Итоговая работа\Итоговая работа\deff_Phone.txt','a')
            wread_deff_login.write(phone+'\n')
            wread_deff_login.close()
            #print("Phone is incorrect")
            sl = slice(1)
        
            Phone.append(str(8+phone[sl]))




files = open(r'D:\Программы C#\Итоговая работа\Итоговая работа\all.txt')
for i in files:
    
    All_file.append(i.split('\t'))
files.close()
Login.append("Login:")
Password.append("Password:")
mails.append("Mail:")
Phone.append("Phone:")

koll = len(All_file)

for i in range(1,len(All_file)):
    text=""
    
    for j in range(len(All_file[i])):
       text +=str(All_file[i][j])+" "
    print(text)
    r = (re.findall(r'\S+',text))
    print(r)
    for n in r:
        if(len(re.findall(r'(@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)',n))==0):
            if(len(re.findall(r'[0-9]{9,10}',n))==0):

                login_file(n)

            else:
                Phone_file(n)
                
        else:
            
            mail_file(n)

    Password.append(Gener_Pass())

new_file=[]



new_file.append(Login)
new_file.append(Password)
new_file.append(mails)
new_file.append(Phone)

print(mails)

file = open(r'D:\Программы C#\Итоговая работа\Итоговая работа\new.txt','w')
for i in range(len(new_file)):
    for j in range(len(new_file[i])):
        file.write(new_file[i][j]+'\t')
    file.write(""+'\n')
file.close()