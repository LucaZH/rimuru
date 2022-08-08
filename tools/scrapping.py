# from bs4 import BeautifulSoup as bs
# import requests

# url = "https://www.infosante.be/recherche?q=paludisme"
# r = requests.get(
#     url,
#     headers = {
#         'User-Agent': 'Popular browser\'s user-agent',
#     }
# )
# print(r.content)
titreinfo=["De quoi s’agit-il ?","Quelle est sa fréquence ?","Comment le reconnaître ?","Comment le diagnostic est-il posé ?","Que pouvez-vous faire ?","Que peut faire votre médecin ?"]
info1="Le paludisme est une maladie infectieuse causée par le parasite Plasmodium. Ce parasite se transmet à l'homme par la piqûre d’un moustique bien spécifique : l’anophèle."
info2 ="Le paludisme est l’une des infections les plus répandues sur la planète. On compte chaque année plus de 200 millions de cas de paludisme et, selon les estimations, la maladie fait plus de 400 000 morts par an, essentiellement parmi les enfants d’Afrique."
info3= "La période d'incubation, c’est-à-dire l’intervalle entre la piqûre de moustique et l'apparition des premiers symptômes, varie de 10 jours à 1 mois. Il se peut donc que vous soyez rentré chez vous depuis un moment avant de tomber malade."
info4= "Toute personne ayant voyagé dans une région touchée par le paludisme et ayant de la fièvre est suspectée d’être infectée par le paludisme."
info5="La principale mesure à prendre est d’empêcher les moustiques de vous piquer. C’est après la tombée de la nuit qu’ils sévissent le plus. Portez des vêtements de couleur claire et recouvrant vos bras et vos jambes (manches longues, pantalons longs ou jupes longues)."
info6="Si vous vous rendez dans une région touchée par le paludisme, le médecin vous prescrira un médicament à titre préventif. Il évaluera le médicament qui vous convient le mieux. Il est donc tout à fait possible que vous ne preniez pas le même traitement que vos compagnons de voyage. À partir de 40 kg, la dose pour adultes doit être administrée. Pour un poids inférieur à 40 kg, la dose doit être calculée en fonction du poids."
linfo=[info1,info2,info3,info4,info5,info6]
listeinfo=[]
for i in range(6):
    listeinfo.append({
        "titre":titreinfo[i],
        "text": linfo[i],
    })

for infor in listeinfo:
    print(infor['titre'])