import requests
from bs4 import BeautifulSoup
import pandas as pd

print('Choose the city')
city_ch=input('The city is ')
print('Choose the job')
job_ch=input('The job is ')


def extract(page):
    url=f'https://www.receptix.de/us/python?page={page}'

    rq=requests.get(url).text
    soup=BeautifulSoup(rq, 'lxml')
    return soup
   



def find_jobs (soup):
    jobs=soup.find_all('div', class_='job-dsply-div mt-0 jobs-add-div')
    for job in jobs:
        
        title=job.find('p',class_='secondary-font-style').text.strip()
        company=job.find('h4').text.strip()
        city=job.find('div', class_='d-flex align-items-center flex-wrap mb-2').text.strip()

        if city_ch in city and job_ch in title:
                job_match={'Title':title, 'Company':company, 'Location':city}
                list_jobs.append(job_match)
                 
       
    return    
        
list_jobs=[]
for i in range (1,4):
    e=extract(i)
    find_jobs(e)


df=pd.DataFrame(list_jobs)
df.to_csv('jobs_python_excercise.csv')
print(df)
