import requests,json,random,os,sqlite3

url = os.environ.get('urlpy')
# url="http://127.0.0.1:8000/"
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

def getinfobyzone(option,searched):
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



def insertinfo(option,info,publisher_id):
    if option not in ['pharmacie','cm']:
        return None
    resultsplit= info.split(',')
    if len(resultsplit)==3:
        data= {
            'nom':resultsplit[0],
            'localisation':resultsplit[1],
            'contact':resultsplit[2],
            'verifier': False,
            'publier_par':publisher_id,
            'zone':0
        }
    elif len(resultsplit)==2:
        data= {
            'nom':resultsplit[0],
            'localisation':resultsplit[1],
            'contact':'',
            'verifier': False,
            'publier_par':publisher_id,
            'zone':0
        }

    r = requests.post(f'{url}api/{option}/',data= json.dumps(data),headers=headers)
    print(r.content)

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

def getzonejson(searched):
    with open("tools/fokontany.json","r") as fokontany :
        data= json.load(fokontany)
    resultat=[]
    for i in range(len(data)):
        for key,value in data[i].items():
            if value==searched:
                resultat.append(data[i])
    if len(resultat)!= 0:
        for key , value in resultat[0].items():
            if key=="zone":
                return value
    else :
        return None
# print(getzonejson("Bemololo"))
userid = '8546564265369512'
ACCESS_TOKEN='EAAGfZAFN8lA4BAL3EHkJF7Fep3sSH7pwTCLuADvYrg64lTBRzjIEyC3XOExu5PvGAtnGrwhzLfvjdxDLdan7BKI8XcxypsoSJcEiuB4TVIstTC8NyuQUQjZBdGZBjMjQU6dSvybqcnPUPgxsZAxVjpAgK0k9ZCj7UDbsSY7oCwyyMlDQdxYAyM4dA3CDYoMsZD'
url = 'https://graph.facebook.com/v13.0/me/messages?access_token='+ACCESS_TOKEN
# "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCDL2AaXe1Jc7dqPmYZp_oXzXk_nyhrz38lw&usqp=CAU"
# scrap = scrapping.ScrapInfoSante()
# def send_res_info(dest_id):
#     listinfofact=scrap.Get_result_search("Ventre")[:10]
#     # listinfofact=[]
#     # print(listinfofact)
#     data = {
#         "recipient": {
#             "id": f'{dest_id}'
#         },
#         "messaging_type": "response",
#         "message":{
#         "attachment":{
#         "type":"template",
#         "payload":{
#                 "template_type":"generic",
#                 "elements":[
#                     {
#                         "title":f"{res_info['titre']}",
#                         "image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCDL2AaXe1Jc7dqPmYZp_oXzXk_nyhrz38lw&usqp=CAU",
#                         "subtitle":f"{res_info['url']}",
#                         "buttons":[
#                             {
#                                 "type":"postback",
#                                 "title":"Voir",
#                                 "payload":"DEVELOPER_DEFINED_PAYLOAD"
#                             }              
#                         ]      
#                     }for res_info in listinfofact
#                 ]
#             }
#     }
#   }
#     }
#     headers = {"Content-Type": "application/json"}
#     r = requests.post(url, data=json.dumps(data), headers=headers)
#     print(r.content)
# # send_res_info(userid)
# # listinfofact=scrap.Get_result_search("Maux de tête")
#     # print(res)