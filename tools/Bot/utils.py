import json

main_menu  = [
        {
            'content_type': 'text',
            'title': 'Conseil du jour',
            "payload": json.dumps({
                'menu': 'Conseil_du_jour',
                
            })
        },
        {
            'content_type': 'text',
            'title': 'Hopital',
            "payload": json.dumps({
                'menu': 'hopital',
                
            })
        },
        {
            'content_type': 'text',
            'title': 'Pharmacie',
            "payload": json.dumps({
                'menu': 'pharmacie',
            })
        },
        {
            'content_type': 'text',
            'title': 'COVID-19',
            "payload": json.dumps({
                'menu': 'COVID19',
            })
        },
        {
            'content_type': 'text',
            'title': 'A propos',
            "payload": json.dumps({
                'menu': 'Apropos',
            })
        }
        ]
menu_hopital = [
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
message_menu=["Qu'est ce que je peux faire pour vous?","Cliquer sur Rechercher pour voir l'hopital la plus proche de vous ou Aider pour enregister l'hopital "]
print(main_menu[0])
# print(main_menu[0:len(main_menu)%2])
# print(main_menu[len(main_menu)%2:len(main_menu)])
print(f"'{message_menu[0]}'")

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
