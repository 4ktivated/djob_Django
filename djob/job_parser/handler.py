
from bs4 import BeautifulSoup
from selenium import webdriver
import lxml
import requests
import time

class VacHandler():
    vac_base = []

    def __init__(self, lang: str) -> None:
        self.lang = lang.lower()
        self.func_list = list(filter(lambda x: x[0] == 'j',dir(self)))
        #фильтрация методов объекта по первой букве что бы в списке были только те что парсят вакансии


    def get_base(self):
        if not self.vac_base:
            for func in self.func_list:
                func(self.lang)
        return self.vac_base
        


    def jobs_geekjob(self):
        url = "https://geekjob.ru/vacancies?qs=" + self.lang
        browser = webdriver.Chrome()
    

        browser.get(url)
        time.sleep(2)
        html = browser.page_source
        soup = BeautifulSoup(html, 'lxml')

    
        for vacaincie in soup.find_all('li', class_ = 'collection-item avatar'):
            name = vacaincie.find('p', class_ = 'truncate company-name').text.strip()
            title = vacaincie.find('p', class_ = 'truncate vacancy-name').text.strip()
            info = str(vacaincie.find('div', class_ = 'info')).replace('<br/>', ' ')[18:-7]
            #при использованнии text тег br стирает пробел между городом и потенциаяльной зарплатой
            if not info:
                info = 'Не указанно'
            link = 'https://geekjob.ru' + vacaincie.a['href']
            
        
            self.vac_base.append({'lang': self.lang, 'Title': title, 'Company': name, 'URL': link, 'Salary': 'из-за источника все даныне в инфо', 'Info': info})


    def jobs_habr(self):
        habr_url = 'https://career.habr.com/vacancies?q='+ self.lang +'&qid=3&type=all'
        
        response = requests.get(habr_url, timeout=10)

        soup = BeautifulSoup(response.text, "lxml")

        if response.status_code == 200:
            for box in soup.find_all('div', class_ = 'vacancy-card__info'):
                name = box.div.div.text
                title = box.find('div', class_ = 'vacancy-card__title').text
                stack = box.find('div', class_ = 'vacancy-card__skills').text
                link = 'https://career.habr.com' + box.a['href']

                if box.find('div', class_ = 'vacancy-card__salary').text:
                    salary = box.find('div', class_ = 'vacancy-card__salary').text
                else:
                    salary = 'Не указанна'
                self.vac_base.append({'lang': self.lang, 'Title': title, 'Company': name, 'URL': link, 'Salary': salary, 'Info': stack})


    def jobs_hh(self):
        url = "https://api.hh.ru/vacancies"
        params = {
            "text": self.lang,
            "area": [72, 2, 1, 3],  # Specify the desired area ID (72:Perm, 2:SPB, 1:MSC, 3:EKB)
            # "per_page": 100,  # Number of vacancies per page
        }

        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()
            vacancies = data.get("items", [])
            for vacancy in vacancies:
                
                vacancy_title = vacancy.get("name")
                vacancy_url = vacancy.get("alternate_url")
                company_name = vacancy.get("employer", {}).get("name")
                experience = vacancy.get('experience', {}).get('name')
                
                #Костыль с зарплатой из-за неправильного форматирования
                if vacancy.get('salary', {}) and vacancy.get('salary', {}).get("from") and vacancy.get('salary', {}).get('to'):
                    salary_from = vacancy.get('salary', {}).get("from")
                    salary_to = vacancy.get('salary', {}).get('to')
                    salary = f'{salary_from} - {salary_to}'
                elif vacancy.get('salary', {}) and not vacancy.get('salary', {}).get("from"):
                    salary = vacancy.get('salary', {}).get('to')
                elif vacancy.get('salary', {}) and not vacancy.get('salary', {}).get("to"):
                    salary = vacancy.get('salary', {}).get('from')
                else:
                    salary = 'Не указанна'
                    
                self.vac_base.append({'lang': self.lang, 'Title': vacancy_title, 'Company': company_name, 'URL': vacancy_url, 'Salary': salary, 'Info': experience})
                
        # else:
        #     print(f"Request failed with status code: {response.status_code}")
    
