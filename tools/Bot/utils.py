import json,requests

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
            'image_url':"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaO-KtMrTzRRPDbYRZu8dIs5Gl6cfYCEZ4kA&usqp=CAU",
            "payload": json.dumps({
                'query_hosp': 'Rechercher',
            })
        },
        {
            'content_type': 'text',
            'title': 'Ajouter',
            'image_url':"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbGS3cjMKA1uTKKimJ-MgAU_WvqGWbNS_nNw&usqp=CAU",
            "payload": json.dumps({
                'query_hosp': 'Aider',
            })
        },
        {
            'content_type': 'text',
            'title': 'Menu principal',
            'image_url':"https://assets.stickpng.com/images/588a64cdd06f6719692a2d0d.png",
            "payload": json.dumps({
                'query_hosp': 'main_menuh',
            })
        }
        ]
menu_PH = [
        {
            'content_type': 'text',
            'title': 'Rechercher',
            'image_url':"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaO-KtMrTzRRPDbYRZu8dIs5Gl6cfYCEZ4kA&usqp=CAU",
            "payload": json.dumps({
                'query_ph': 'Rechercher',
            })
        },
        {
            'content_type': 'text',
            'title': 'Ajouter',
            'image_url':"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbGS3cjMKA1uTKKimJ-MgAU_WvqGWbNS_nNw&usqp=CAU",
            "payload": json.dumps({
                'query_ph': 'Aider',
            })
        },
        {
            'content_type': 'text',
            'title': 'Menu principal',
            'image_url':"https://assets.stickpng.com/images/588a64cdd06f6719692a2d0d.png",
            "payload": json.dumps({
                'query_ph': 'main_menuph',
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
resultat_info=["Malaria (paludisme)","Fièvre prolongée d’origine inconnue chez l’enfant","Fièvre au retour d’un voyage","Maladies causées par des parasites en dehors de l’intestin","Thalassémie","Prévention des infections en voyage","Déficit auditif et tests auditifs","Croissance normale et croissance anormale chez l’enfant"]
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
