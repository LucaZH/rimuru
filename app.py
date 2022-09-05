from flask import Flask, request
from tools.Bot.messenger import Messenger
from tools import api
import json,os
from tools.Bot.utils import *

app = Flask(__name__)
Rimuru = Messenger(os.environ.get("ACCESS_TOKEN"))

@app.route("/", methods=['GET'])
def handle_verification():
        if (request.args.get('hub.verify_token', '') == os.environ.get("VERIFY_TOKEN")):
            print("Verified")
            return request.args.get('hub.challenge', '')
        else:
            print("Wrong token")
            return "Error, wrong validation token"
    
@app.route('/', methods=['POST'])
def main():
    data = request.get_json()
    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                recipient_id = messaging_event["sender"]["id"]
                api.verifyuser(recipient_id)
                Rimuru.send_action(recipient_id,"mark_seen")
                user_state = api.getuserinfo(recipient_id,"state")
                if messaging_event.get("message"):
                    if 'text' in messaging_event['message'] and 'quick_reply' not in messaging_event['message']:
                        query = messaging_event["message"]["text"]
                        if user_state == 'START':
                            Rimuru.send_menu(recipient_id,main_menu,f"{message_menu[0]}")
                            Rimuru.send_action(recipient_id,"typing_off")
                        else:
                            if user_state == 'CM_SC':
                                api.updateinfo(recipient_id,'START',query=query)
                                getinfo('cm',query,recipient_id)
                                Rimuru.send_menu(recipient_id,main_menu,f"{message_menu[0]}")
                            if user_state == 'CM_HE':
                                api.updateinfo(recipient_id,'START',query=query)
                                api.insertinfo('cm',query,recipient_id)
                                Rimuru.send_text(recipient_id,f"Envoie du demande d'ajout => {query} aux admins")
                                Rimuru.send_menu(recipient_id,main_menu,f"{message_menu[0]}")
                            if user_state == 'PH_SC':
                                api.updateinfo(recipient_id,'START',query=query)
                                getinfo('pharmacie',query,recipient_id)
                                Rimuru.send_menu(recipient_id,main_menu,f"{message_menu[0]}")
                            if user_state == 'PH_HE':
                                api.updateinfo(recipient_id,'START',query=query)
                                api.insertinfo('pharmacie',query,recipient_id)
                                Rimuru.send_text(recipient_id,f"Envoie du demande d'ajout => {query} aux admins")
                                Rimuru.send_menu(recipient_id,main_menu,f"{message_menu[0]}")
                            # if user_state == 'CONSEIL':
                            #     Rimuru.send_text(recipient_id,api.getrandomconseil())
                            #     Rimuru.send_action(recipient_id,'typing_off')
                            #     Rimuru.send_menu(recipient_id,retry_co,'cliquer sur ces bouton')
                            if user_state =='INFO':
                                api.updateinfo(recipient_id,'START',query=query)
                                Rimuru.send_text(recipient_id,"Envoie du resultat de recherche en cour ...")
                                Rimuru.send_res_info(recipient_id,query)
                                Rimuru.send_menu(recipient_id,main_menu,f"{message_menu[0]}")
                    if 'quick_reply' in messaging_event['message']:
                        Rimuru.send_action(recipient_id,"mark_seen")
                        payload = messaging_event['message']['quick_reply']['payload']
                        if is_json(payload):
                            payload = json.loads(payload)
                            if 'menu' in payload:
                                if payload['menu'] == 'CM':
                                    Rimuru.send_text(recipient_id,"Bienvenu dans l'option Centre medical, ici vous pouvez soit rechercher un information concernant une Centre Medical soit en ajouter un\n L'ajout devra d'abord être verifier par l'admin ")
                                   
                                    Rimuru.send_menu(recipient_id,menu_CM,"Que choisisez-vous?")
                                elif payload['menu'] =='pharmacie':
                                    Rimuru.send_text(recipient_id,"Bienvenu dans l'option Pharmacie , ici vous pouvez soit rechercher un information concernant un pharmacie soit en ajouter un\n L'ajout devra d'abord être verifier par l'admin")
                                    Rimuru.send_menu(recipient_id,menu_PH,"Que choisisez-vous?")
                                elif payload['menu'] =='Actualités':
                                    # Rimuru.send_action(recipient_id,"typing_off")
                                    # Rimuru.send_info_fact(recipient_id)
                                    # Rimuru.send_menu(recipient_id,main_menu,f"{message_menu[0]}'")
                                    Rimuru.send_text(recipient_id,"Bienvenu dans la rubrique info santé , ici vous pouvez n'importe quelle information concernant la santé")
                                    Rimuru.send_text(recipient_id,"Entrer votre recherche")
                                    api.updateinfo(recipient_id,'INFO')
                                    
                                elif payload['menu'] =='Conseil_du_jour':
                                    Rimuru.send_action(recipient_id,'typing_off')
                                    Rimuru.send_text(recipient_id,api.getrandomconseil())
                                    Rimuru.send_menu(recipient_id,retry_co,"Qu'est ce que vous voullez faire?")
                                elif payload['menu'] =='Apropos':
                                    Rimuru.send_text(recipient_id,'Devollopé par RANDRIAMANANTENA Luca Zo Haingo')
                            elif 'actualite_covid19' in payload:
                                    Rimuru.send_text(recipient_id,'Actualité covid : Developpement du projet en cours')
                                    print("asdf")
                            elif 'conseil_covid19' in payload:
                                Rimuru.send_text(recipient_id, 'CONSEIL : Developpement du projet en cours')
                            elif 'query_hosp' in payload:
                                if payload['query_hosp']=='Rechercher':
                                    Rimuru.send_text(recipient_id,"Entrer votre localisation")
                                    api.updateinfo(recipient_id,'CM_SC')
                                elif payload['query_hosp']=='Aider':
                                    Rimuru.send_text(recipient_id,"Entrer le centre medical ou hopital que vous voulez ajouter en separant le nom , la localisation et le contact par une virgule (,) \n exemple : Hopital Fy , Vatofotsy , 034456655")
                                    api.updateinfo(recipient_id,'CM_HE')
                                elif payload['query_hosp']=='main_menu':
                                    api.updateinfo(recipient_id,'START')
                            elif 'query_ph' in payload:
                                if payload['query_ph']=='Rechercher':
                                    Rimuru.send_text(recipient_id,"Entrer votre localisation")
                                    api.updateinfo(recipient_id,'PH_SC')
                                elif payload['query_ph']=='Aider':
                                    Rimuru.send_text(recipient_id,"Entrer la pharmacie que vous voulez ajouter en separant le nom , la localisation et le contact par une virgule (,) \n exemple : Pharmacie Fy , Vatofotsy , 034456655")
                                    api.updateinfo(recipient_id,'PH_HE')
                            elif 'option_co' in payload:
                                if payload['option_co'] == 'retry_co':
                                    Rimuru.send_text(recipient_id,api.getrandomconseil())
                                    Rimuru.send_menu(recipient_id,retry_co,"Qu'est ce que vous voullez faire?")
                                if payload['option_co'] == 'main_menu':
                                    api.updateinfo(recipient_id,'START')
                                    Rimuru.send_menu(recipient_id,main_menu,f"{message_menu[0]}")
                elif 'postback' in messaging_event:
                    if 'payload' in messaging_event['postback']:
                        pload = messaging_event['postback']['payload']
                        if 'get_started' == pload:
                            Rimuru.send_menu(recipient_id,main_menu,"Bonjour je suis Rimuru,Qu'est ce que je peux faire pour vous?")
                        if pload=="Voir":
                            Rimuru.send_info_fact(recipient_id)
                        if is_json(pload):
                            pload_json = json.loads(pload)
                            print(pload_json)
                            if 'read' in pload_json:
                                text_info = pload_json['read']
                                print("arrived")
                                Rimuru.send_text(recipient_id,text_info)
                            


    return 'ok'
    
Rimuru.get_stared()

def getinfo(option,query,recipient_id):
    r= api.getinfobyzone(option,api.getzonejson(query))
    if r!=[]:
        for i in range(len(r)):
            if r[i]["contact"]!="":
                print(f'{r[i]["nom"]} {r[i]["localisation"]},contact: {r[i]["contact"]}')
                Rimuru.send_text(recipient_id,f'{r[i]["nom"]} {r[i]["localisation"]},contact: {r[i]["contact"]}')
            else:
                print(f'{r[i]["nom"]} {r[i]["localisation"]}')
                Rimuru.send_text(recipient_id,f'{r[i]["nom"]} {r[i]["localisation"]}')
    else:
        print("No found")
        Rimuru.send_text(recipient_id,"Introuvable")
        
def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True
