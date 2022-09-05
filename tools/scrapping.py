from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os


class ScrapInfoSante():
    def __init__(self):
        self.path = os.environ.get("CHROMEDRIVER_PATH")
        self.service = Service(self.path)
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_extension("tools/I-don-t-care-about-cookies.crx")
        self.chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        # self.chrome_options.add_argument('--headless')
        self.chrome_options.headless = True
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('--no-sandbox')
        
        self.driver = webdriver.Chrome(service=self.service,options=self.chrome_options)
        
    def Get_result_search(self,query):
        print("send result info")
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
        print("get result")
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
