import requests,json,random,os

# url = os.environ.get('urlpy')
url="http://127.0.0.1:8000/"
headers = {"Content-Type": "application/json"}

def verifyuser(fb_id):
    r = requests.get(f'{url}api/user/', headers=headers)
    user = r.json()
    all_fb_id = []
    for i in user:
        for key,value in i.items():
            if key == "fb_id":
                all_fb_id.append(value)
    if fb_id not in all_fb_id:
        print(f"{fb_id} is not in database")
        insertuser(fb_id)

def getuserinfo(fb_id,info):
    if info not in ['all','fb_id', 'state', 'role','query']:
        return None
    r = requests.get(f'{url}api/user/{fb_id}/', headers=headers)
    user = r.json()
    if info == "all":
        return user
    else:
        for key,value in user.items():
            if key==info:
                return value

def updateinfo(fb_id,state,query=""):
    data = {
    "fb_id": fb_id,
    "state": state,
    "query": query,
    "role": "normaluser"
        }
    r = requests.put(f'{url}api/user/{fb_id}/', data= json.dumps(data),headers=headers)
    print(r.content)
    print(f"user {fb_id} updated") 
def insertuser(fb_id, state='START'):
    data = {
    "fb_id": fb_id,
    "state": state,
    "query": '',
    "role": "normaluser"
        }
    r = requests.post(f'{url}api/user/', data= json.dumps(data),headers=headers)
    print(r.content)
    print(f"user {fb_id} insered")

def getconseil(id):
    r = requests.get(f'{url}api/conseil/{id}',headers=headers)
    cons = r.json()
    for key,value in cons.items():
        if key=="text":
            return value
def getrandomconseil():
    r = requests.get(f'{url}api/conseil/',headers=headers)
    randn = random.randrange(1,len(r.json()))
    return getconseil(randn)

def gethopitalbyzone(option,searched):
    if option not in ['pharmacie','cm']:
        return None
    r = requests.get(f'{url}api/{option}/',headers=headers)
    cm = r.json()
    resultat=[]
    resultat_verified=[]
    for i in range(len(cm)):
        for key,value in cm[i].items():
            if key=="zone" and value==searched:
                resultat.append(cm[i])
    for i in range(len(resultat)):
        for key,value in resultat[i].items():
            if key=="verifier" and value==True:
                resultat_verified.append(resultat[i])
    return resultat_verified
def inserthopital(name,localisation,contact,published_id):
    print(os.environ.get('urlpy'))

import sqlite3
def getzone(query):
    try:
        db_path="../mada.db"
        conn = sqlite3.connect(db_path)
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    try:
        cur = conn.cursor()
        cur.execute(f"SELECT zone FROM fokontany where name='{query}'")
        zone = cur.fetchone()
        return zone[0]
    except:
        return None

r= gethopitalbyzone("pharmacie",getzone("Ambal"))
if r!=[]:
    for i in range(len(r)):
        if r[i]["contact"]!="":
            print(f'{r[i]["nom"]} {r[i]["localisation"]},contact: {r[i]["contact"]}')
        else:
            print(f'{r[i]["nom"]} {r[i]["localisation"]}')
else:
    print("No found")

# print(getrandomconseil())
# print(getconseil(5))
# print(getuserinfo("123","all"))
# updateinfo('123','HOPITAL','')
# insertuser("12345678")
# verifyuser("2342344")
# r = requests.get(f'{url}api/user/', headers=headers)
# print(r.json())
# conseil = {
#     "text": "Evite les choses trop sucree"
# }
# r = requests.post("https://rimuruadmin.herokuapp.com/api/conseil/",data=json.dumps(conseil),headers=headers)
# print(f"{r} {r.content}")
# print(gethopital())