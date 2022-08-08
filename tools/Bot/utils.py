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
            'title': 'Centre Medical',
            'image_url':'https://www.shareicon.net/data/512x512/2016/08/04/806609_medical_512x512.png',
            "payload": json.dumps({
                'menu': 'CM',
                
            })
        },
        {
            'content_type': 'text',
            'title': 'Pharmacie',
            'image_url':"https://thumbs.dreamstime.com/b/pharmacy-location-blue-map-pin-icon-element-map-point-mobile-concept-web-apps-icon-website-design-109712535.jpg",
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
            "payload": json.dumps({
                'option_co': 'retry_co',
            })
        },
        {
            'content_type': 'text',
            'title': 'Menu principal',
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
tittreinfo=["De quoi s’agit-il ?","Quelle est sa fréquence ?","Comment le reconnaître ?","Comment le diagnostic est-il posé ?","Que pouvez-vous faire ?","Que peut faire votre médecin ?"]
info1="Le paludisme est une maladie infectieuse causée par le parasite Plasmodium. Ce parasite se transmet à l'homme par la piqûre d’un moustique bien spécifique : l’anophèle."
info2 ="Le paludisme est l’une des infections les plus répandues sur la planète. On compte chaque année plus de 200 millions de cas de paludisme et, selon les estimations, la maladie fait plus de 400 000 morts par an, essentiellement parmi les enfants d’Afrique."
info3= "La période d'incubation, c’est-à-dire l’intervalle entre la piqûre de moustique et l'apparition des premiers symptômes, varie de 10 jours à 1 mois. Il se peut donc que vous soyez rentré chez vous depuis un moment avant de tomber malade."
info4= "Toute personne ayant voyagé dans une région touchée par le paludisme et ayant de la fièvre est suspectée d’être infectée par le paludisme."
info5="La principale mesure à prendre est d’empêcher les moustiques de vous piquer. C’est après la tombée de la nuit qu’ils sévissent le plus. Portez des vêtements de couleur claire et recouvrant vos bras et vos jambes (manches longues, pantalons longs ou jupes longues)."
info6="Si vous vous rendez dans une région touchée par le paludisme, le médecin vous prescrira un médicament à titre préventif. Il évaluera le médicament qui vous convient le mieux. Il est donc tout à fait possible que vous ne preniez pas le même traitement que vos compagnons de voyage. À partir de 40 kg, la dose pour adultes doit être administrée. Pour un poids inférieur à 40 kg, la dose doit être calculée en fonction du poids."
linfo=[info1,info2,info3,info4,info5,info6]
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


