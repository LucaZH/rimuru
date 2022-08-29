from flask import Flask, request
from conf import *
from tools.Bot.messenger import Messenger
from tools import api
import json
from tools.Bot.utils import *

app = Flask(__name__)
Rimuru = Messenger(ACCESS_TOKEN)

@app.route("/", methods=['GET'])
def handle_verification():
        if (request.args.get('hub.verify_token', '') == VERIFY_TOKEN):
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
                sender_id = messaging_event["sender"]["id"]
                api.verifyuser(sender_id)
                Rimuru.send_action(sender_id,"mark_seen")
                user_state = api.getuserinfo(sender_id,"state")
                if messaging_event.get("message"):
                    if 'text' in messaging_event['message'] and 'quick_reply' not in messaging_event['message']:
                        query = messaging_event["message"]["text"]
                        if user_state == 'START':
                            Rimuru.send_menu(sender_id,main_menu,f"{message_menu[0]}")
                            Rimuru.send_action(sender_id,"typing_off")
                        else:
                            if user_state == 'CM_SC':
                                api.updateinfo(sender_id,'START',query=query)
                                Rimuru.send_text(sender_id,f"Le centre medical dans votre zone est la Clinique Ave Maria Antanambao \n Contact : 0204448998")
                                Rimuru.send_menu(sender_id,main_menu,f"{message_menu[0]}")
                            if user_state == 'CM_HE':
                                api.updateinfo(sender_id,'START',query=query)
                                Rimuru.send_text(sender_id,f"Envoie du demande d'ajout => {query} aux admin")
                                Rimuru.send_menu(sender_id,main_menu,f"{message_menu[0]}")
                            if user_state == 'CONSEIL':
                                Rimuru.send_text(sender_id,api.getrandomconseil())
                                Rimuru.send_action(sender_id,'typing_off')
                                Rimuru.send_menu(sender_id,retry_co,'cliquer sur ces bouton')
                            if user_state =='INFO':
                                Rimuru.send_res_info_fact(sender_id)
                    if 'quick_reply' in messaging_event['message']:
                        Rimuru.send_action(sender_id,"mark_seen")
                        payload = messaging_event['message']['quick_reply']['payload']
                        if is_json(payload):
                            payload = json.loads(payload)
                            if 'menu' in payload:
                                if payload['menu'] == 'CM':
                                    Rimuru.send_text(sender_id,'Bienvenu dans la fonctionnalité hospital ')
                                    # api.updateinfo(sender_id,'CENTREMEDICAL')
                                    Rimuru.send_menu(sender_id,menu_CM,"choix")
                                elif payload['menu'] =='Actualités':
                                    # Rimuru.send_action(sender_id,"typing_off")
                                    # Rimuru.send_info_fact(sender_id)
                                    # Rimuru.send_menu(sender_id,main_menu,f"{message_menu[0]}'")
                                    Rimuru.send_text(sender_id,"Bienvenu dans la rubrique info santé , ici vous pouvez n'importe quelle information concernant la santé")
                                    Rimuru.send_text(sender_id,"Entrer votre recherche")
                                    api.updateinfo(sender_id,'INFO')
                                    
                                elif payload['menu'] =='pharmacie':
                                    Rimuru.send_text(sender_id,'pharmacie : Developpement du projet en cours')

                                elif payload['menu'] =='Conseil_du_jour':
                                    api.updateinfo(sender_id,'CONSEIL')
                                    Rimuru.send_action(sender_id,'typing_off')
                                    Rimuru.send_text(sender_id,api.getrandomconseil())
                                    Rimuru.send_menu(sender_id,retry_co,"Qu'est ce que vous voullez faire?")
                                elif payload['menu'] =='Apropos':
                                    Rimuru.send_text(sender_id,'Devollopé par RANDRIAMANANTENA Luca Zo Haingo')
                            elif 'actualite_covid19' in payload:
                                    Rimuru.send_text(sender_id,'Actualité covid : Developpement du projet en cours')
                                    print("asdf")
                            elif 'conseil_covid19' in payload:
                                Rimuru.send_text(sender_id, 'CONSEIL : Developpement du projet en cours')
                            elif 'query_hosp' in payload:
                                if payload['query_hosp']=='Rechercher':
                                    # query_hosp= api.getuserinfo(sender_id,'query')
                                    # res= query_hosp + '  == >Resultats rechercher'
                                    # Rimuru.send_text(sender_id,res)
                                    Rimuru.send_text(sender_id,"Entrer votre localisation")
                                    api.updateinfo(sender_id,'CM_SC')
                                elif payload['query_hosp']=='Aider':
                                    # query_hosp= api.getuserinfo(sender_id,'query')
                                    # res= query_hosp + '  == >Resultats Ajouter , merci pour votre contribution \n l admin verifiera votre ajout'
                                    # Rimuru.send_text(sender_id,res)
                                    Rimuru.send_text(sender_id,"Entrer le centre medical ou hopital que vous voulez ajouter")
                                    api.updateinfo(sender_id,'CM_HE')
                                elif payload['query_hosp']=='main_menu':
                                    api.updateinfo(sender_id,'START')
                            elif 'option_co' in payload:
                                if payload['option_co'] == 'retry_co':
                                    Rimuru.send_text(sender_id,api.getrandomconseil())
                                    Rimuru.send_menu(sender_id,retry_co,"Qu'est ce que vous voullez faire?")
                                if payload['option_co'] == 'main_menu':
                                    api.updateinfo(sender_id,'START')
                                    Rimuru.send_menu(sender_id,main_menu,f"{message_menu[0]}")
                elif 'postback' in messaging_event:
                    if 'payload' in messaging_event['postback']:
                        pload = messaging_event['postback']['payload']
                        if 'get_started' == pload:
                            Rimuru.send_menu(sender_id,main_menu,"Bonjour je suis Rimuru,Qu'est ce que je peux faire pour vous?")
                        if pload=="Voir":
                            Rimuru.send_info_fact(sender_id)
                        if is_json(pload):
                            pload_json = json.loads(pload)
                            print(pload_json)
                            if 'read' in pload_json:
                                text_info = pload_json['read']
                                print("arrived")
                                Rimuru.send_text(sender_id,text_info)
                            


    return 'ok'
    
Rimuru.get_stared()

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True
