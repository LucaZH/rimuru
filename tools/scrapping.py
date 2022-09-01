import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class ScrapInfoSante():
    def __init__(self):
        self.path = "/home/luca/Documents/Code/Selenium/chromedriver"
        self.service = Service(self.path)
        self.chop = webdriver.ChromeOptions()
        self.chop.add_extension("tools/I-don-t-care-about-cookies.crx")
        self.driver = webdriver.Chrome(service=self.service,options=self.chop)
        
    def Get_result_search(self,query):
        TextSearchResult= []
        UrlSearchResult=[]
        ListResult = []
        self.driver.get(f"https://www.infosante.be/recherche?q={query}")
        listeInfo=self.driver.find_elements(By.CLASS_NAME, 'morphsearch-content')
        for itemInfo in listeInfo:
            TextInfo = itemInfo.find_element(By.XPATH,'//*[@id="morphsearch"]/div/div/div/ul').text
        TextSearchResult = TextInfo.split("\n")
        for i in range(1,len(TextSearchResult)+1):
            xpath=f'//*[@id="morphsearch"]/div/div/div/ul/li[{i}]/a'
            geturl = self.driver.find_element(By.XPATH,xpath).get_attribute('href')
            UrlSearchResult.append(geturl)
        self.driver.close()
        for j in range(len(TextSearchResult)):
            info = {
                'titre' : TextSearchResult[j],
                'url': UrlSearchResult[j]
            }
            ListResult.append(info)
        return ListResult

    def GetInfoSante(self,URLSANTE):
        self.driver.get(URLSANTE)
        Getp=self.driver.find_elements(By.XPATH, '//*[@id="main"]/div/div/div[1]/div[3]')
        OriginList=[]
        for getp in Getp :
            GetpText=getp.text
            OriginList.append(GetpText)
        self.driver.close()
        FirstSplit= OriginList[0].split("\n")
        question = ["De quoi s’agit-il ?","Quelle est sa fréquence ?","Comment le reconnaître ?","Comment le diagnostic est-il posé ?","Que pouvez-vous faire ?","Que peut faire votre médecin?","En savoir plus ?"]
        NewQuestion=[]
        for i in range(len(FirstSplit)-1):
            if FirstSplit[i] in question:
                NewQuestion.append(FirstSplit[i])
                FirstSplit[i]="[Titre]"
        Joined = "".join(FirstSplit)
        Splited = Joined.split("[Titre]")
        FinalResult=[]
        for x in range (len(Splited)-1):
            info = {
                NewQuestion[x]:Splited[x+1],
            }
            FinalResult.append(info)
        
        return FinalResult
Sc = ScrapInfoSante()
print(Sc.GetInfoSante("file:///home/luca/Documents/Code/Selenium/Malaria%20(paludisme)%20%C2%B7%20Info%20sant%C3%A9.html"))