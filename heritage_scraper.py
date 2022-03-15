!pip install selenium
!apt-get update # to update ubuntu to correctly run apt install
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin

import time
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

class HeritageScraper:

    def __init__(self):
      
        # Firstly, set up the chrome option
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        # Initialize the webdriver & relevant parameters
        self.wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
        self.url = 'https://www.historicplaces.ca/en/results-resultats.aspx?m=2&Keyword='
        self.id = 'ContentPlaceHolderDefault_ContentPlaceHolderDefault_ContentPlaceHolderDefault_ContentPlaceHolderDefault_DBSearchResultsLeft_ddlResultsPerPage'
        self.item_per_page = '65535'
        self.province = ['prince edward island', 'newfoundland', 'nova scotia',  
                        'Saskatchewan', 'yukon', 'ontario', 
                        'nunavut', 'quebec', 'alberta',
                        'british columbia', 'manitoba', 'newfoundland', 
                        'northwest', 'nova scotia']
                                  
    def scrap(self, location:str):
        '''
        This code try to scrap historicalplaces by province
        e.g 
          h = HeritageScraper()
          df = h.scrap('quebec')
        '''

        # Firstly, get the url
        self.wd.get(self.url+location)
        time.sleep(10)
        select = Select(self.wd.find_element_by_id(self.id))
        select.select_by_value(self.item_per_page)
        time.sleep(10)

        # Secondly, parse the page source
        source = self.wd.page_source
        soup = BeautifulSoup(source, "xml")
        buildings = soup.find_all('div', class_="resulttext")
        soup = BeautifulSoup(source, "xml")
        buildings = soup.find_all('div', class_="resultbox clear")

        # Thirdly, construct the final dataset
        print('parsing name&address per building discovered...')
        l = [[i.text.replace('\n','').strip() for i in b.find_all('p')] for b in tqdm(buildings)]
        df = pd.DataFrame(l)[[0,1,2]]
        df.columns = ['name','address','description']

        print('parsing url addres per building discovered...')
        df['web'] = [b.find_all('a')[1]['href'] for b in tqdm(buildings)]
        df['location'] = location
        return df
    
    def scrap_all(self):
      dfs = []
      for p in self.province:
        print(p)
        dfs.append(self.scrap(p))
      return pd.concat(dfs)
