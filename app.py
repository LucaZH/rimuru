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
                            Rimuru.send_menu(sender_id,main_menu,f"'{message_menu[0]}'")
                            Rimuru.send_action(sender_id,"typing_off")
                        else:
                            if user_state == 'HOSPITAL':
                                api.updateinfo(sender_id,'HOSPITAL',query=query)
                                Rimuru.send_menu(sender_id,menu_hopital,"choix")
                            if user_state == 'CONSEIL':
                                Rimuru.send_text(sender_id,api.getrandomconseil())
                                Rimuru.send_action(sender_id,'typing_off')
                                Rimuru.send_menu(sender_id,retry_co,'cliquer sur ces bouton')

                                




                    if 'quick_reply' in messaging_event['message']:
                        Rimuru.send_action(sender_id,"mark_seen")
                        payload = messaging_event['message']['quick_reply']['payload']
                        if is_json(payload):
                            payload = json.loads(payload)
                            if 'menu' in payload:
                                if payload['menu'] == 'hopital':
                                    Rimuru.send_text(sender_id,'Bienvenu dans la fonctionnalité hospital . \n entrer votre localisation (ex: vatofotsy) ou enter le nom et la localisation de l hopital que vous voulez ajouter pour nous aider à completer la liste des hospital ')
                                    api.updateinfo(sender_id,'HOSPITAL')
                                    
                                elif payload['menu'] =='COVID19':
                                    Rimuru.send_action(sender_id,"typing_off")
                                    Rimuru.send_text(sender_id,'Covid-19 : Developpement du projet en cours')
                                    
                                elif payload['menu'] =='pharmacie':
                                    Rimuru.send_text(sender_id,'pharmacie : Developpement du projet en cours')

                                elif payload['menu'] =='Conseil_du_jour':
                                    api.updateinfo(sender_id,'CONSEIL')
                                    Rimuru.send_action(sender_id,'typing_off')
                                    Rimuru.send_text(sender_id,api.getrandomconseil())
                                    Rimuru.send_menu(sender_id,retry_co,'cliquer sur ces bouton')
                                elif payload['menu'] =='Apropos':
                                    Rimuru.send_text(sender_id,'Devollopé par RANDRIAMANANTENA Luca Zo Haingo')
                            elif 'actualite_covid19' in payload:
                                    Rimuru.send_text(sender_id,'Actualité covid : Developpement du projet en cours')
                                    print("asdf")
                            elif 'conseil_covid19' in payload:
                                Rimuru.send_text(sender_id, 'CONSEIL : Developpement du projet en cours')
                            elif 'query_hosp' in payload:
                                print('tonga ========')
                                if payload['query_hosp']=='Rechercher':
                                    query_hosp= api.getuserinfo(sender_id,'query')
                                    res= query_hosp + '  == >Resultats rechercher'
                                    Rimuru.send_text(sender_id,res)
                                    print(res)
                                    api.updateinfo(sender_id,'START')
                                elif payload['query_hosp']=='Aider':
                                    query_hosp= api.getuserinfo(sender_id,'query')
                                    res= query_hosp + '  == >Resultats Ajouter , merci pour votre contribution \n l admin verifiera votre ajout'
                                    Rimuru.send_text(sender_id,res)
                                    print(res)
                                    api.updateinfo(sender_id,'START')
                                elif payload['query_hosp']=='main_menu':
                                    api.updateinfo(sender_id,'START')
                            elif 'option_co' in payload:
                                if payload['option_co'] == 'retry_co':
                                    Rimuru.send_text(sender_id,api.getrandomconseil())
                                    Rimuru.send_action(sender_id,'typing_off')
                                    Rimuru.send_menu(sender_id,retry_co,'')
                                if payload['option_co'] == 'main_menu':
                                    api.updateinfo(sender_id,'START')
                                    Rimuru.send_menu(sender_id,main_menu,f"'{message_menu[0]}'")
                elif 'postback' in messaging_event:
                    if 'payload' in messaging_event['postback']:
                        pload = messaging_event['postback']['payload']
                    if 'get_started' == pload:
                        Rimuru.send_text(sender_id, "Bonjour je suis Rimuru")  
                        Rimuru.main_menu(sender_id)  
                    if is_json(pload):
                        pload_json = json.loads(pload)
                        print(pload_json)
                        


    return 'ok'
    
Rimuru.get_stared()

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True
