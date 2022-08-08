import json

main_menu  = [
        {
            'content_type': 'text',
            'title': 'Conseil du jour',
            'image_url':"https://cdn-icons-png.flaticon.com/512/3938/3938718.png",
            "payload": json.dumps({
                'menu': 'Conseil_du_jour',
                
            })
        },
        {
            'content_type': 'text',
            'title': 'Centre Medical',
            'image_url':'https://www.shareicon.net/data/512x512/2016/08/04/806609_medical_512x512.png',
            "payload": json.dumps({
                'menu': 'CM',
                
            })
        },
        {
            'content_type': 'text',
            'title': 'Pharmacie',
            'image_url':"https://cdn3.iconfinder.com/data/icons/maps-and-navigation-flat-icons-vol-2/256/77-512.png",
            "payload": json.dumps({
                'menu': 'pharmacie',
            })
        },
        {
            'content_type': 'text',
            'title': 'Info santé',
            'image_url':"https://cdn-icons-png.flaticon.com/512/2764/2764545.png",
            "payload": json.dumps({
                'menu': 'Actualités',
            })
        },
        {
            'content_type': 'text',
            'title': 'A propos',
            'image_url': "https://icon-library.com/images/about-us-icon/about-us-icon-8.jpg",
            "payload": json.dumps({
                'menu': 'Apropos',
            })
        }
        ]
menu_CM = [
        {
            'content_type': 'text',
            'title': 'Rechercher',
            "payload": json.dumps({
                'query_hosp': 'Rechercher',
            })
        },
        {
            'content_type': 'text',
            'title': 'Aider',
            "payload": json.dumps({
                'query_hosp': 'Aider',
            })
        },
        {
            'content_type': 'text',
            'title': 'Retour au menu principal',
            "payload": json.dumps({
                'query_hosp': 'main_menu',
            })
        }
        ]
retry_co = [
    {
            'content_type': 'text',
            'title': 'Réesayer',
            'image_url':"https://w7.pngwing.com/pngs/202/842/png-transparent-computer-icons-retry-cdr-trademark-logo.png",
            "payload": json.dumps({
                'option_co': 'retry_co',
            })
        },
        {
            'content_type': 'text',
            'title': 'Menu principal',
            'image_url':'https://cdn-icons-png.flaticon.com/512/56/56763.png',
            "payload": json.dumps({
                'option_co': 'main_menu',
            })
        },
]
message_menu=["Qu'est ce que je peux faire pour vous?","Cliquer sur Rechercher pour voir l'hopital la plus proche de vous ou Aider pour enregister l'hopital "]
# print(main_menu[0])
# # print(main_menu[0:len(main_menu)%2])
# # print(main_menu[len(main_menu)%2:len(main_menu)])
# print(f"'{message_menu[0]}'")

def get_news():
    listnews = []
    list_result= []
    for news in list_result:
        listnews.append({
            'title': news['title'],
            'url': news['link'],
            'thumbnail': news['thumbnails'][0]['url'],
            'publishedTime':news['publishedTime'],
            })
    return listnews

def info():
    listeinfo=[]
    for i in range(6):
        listeinfo.append({
        "titre":tittreinfo[i],
        "text": linfo[i],
    })
    return listeinfo


