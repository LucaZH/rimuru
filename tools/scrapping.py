import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# path="/home/luca/Documents/Code/Selenium/chromedriver"
# chop = webdriver.ChromeOptions()
# s = Service(path)
# chop.add_extension("/home/luca/Documents/Memoire - Licences/Memoire - Code/tools/I-don-t-care-about-cookies.crx")
# driver = webdriver.Chrome(service=s,options=chop)
# def get_result_search():
#     r= []
#     urlm=[]
#     result = []
#     driver.get("https://www.infosante.be/recherche?q=paludisme")
#     listeInfo=driver.find_elements(By.CLASS_NAME, 'morphsearch-content')
#     for itemInfo in listeInfo:
#         textInfo = itemInfo.find_element(By.XPATH,'//*[@id="morphsearch"]/div/div/div/ul').text
#     r = textInfo.split("\n")
#     for i in range(1,len(r)+1):
#         xpath=f'//*[@id="morphsearch"]/div/div/div/ul/li[{i}]/a'
#         geturl = driver.find_element(By.XPATH,xpath).get_attribute('href')
#         urlm.append(geturl)
#     driver.close()
#     for j in range(len(r)):
#         info = {
#             'titre' : r[j],
#             'url': urlm[j]
#         }
#         result.append(info)
#     return result
# # //*[@id="main"]/div/div/div[1]/div[3]/p[1]/strong
# # //*[@id="main"]/div/div/div[1]/div[3]/p[5]/strong
# # //*[@id="main"]/div/div/div[1]/div[3]/p
# def re():
#     driver.get("file:///home/luca/Documents/Code/Selenium/Malaria%20(paludisme)%20%C2%B7%20Info%20sant%C3%A9.html")
#     ggo=driver.find_elements(By.XPATH, '//*[@id="main"]/div/div/div[1]/div[3]')
#     question = ["De quoi s’agit-il ?","Quelle est sa fréquence ?","Comment le reconnaître ?","Comment le diagnostic est-il posé ?","Que pouvez-vous faire ?","Que peut faire votre médecin?","En savoir plus ?"]
#     resultat = []
#     for gi in ggo :
#         g=gi.text
#         for element in question:
#             if element != g :
#                 resultat.append(g)

#     print(resultat)

#     driver.close()
a = ["a","g","l","w"]
c = "ayyyyfsgseelbbbwpp"
def separateInfo(question,info)
    for elements in question :
        for g in info:
            if elements == g:
                info = info.replace(g,"[TITRE]")
    rs=c.split("[TITRE]")
    f= []
    for j in range(len(question)):
        info = {
                question[j] : rs[j+1],
            }
        f.append(info)
        
print(f)