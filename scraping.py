from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


#you can change driver path to your location driver
driver = webdriver.Chrome(r"C:\Users\youssof okiel\Downloads\chromedriver.exe")


titles =[] 
companies =[]
locations = []
dates =[]

Experience_Needed = []
Career_Level = []
Job_Type = []
Salary = []
Vacancies = []

driver.get('https://wuzzuf.net/a/Engineering-Construction-Civil-Architecture-Jobs-in-Egypt?ref=browse-jobs')

content = driver.page_source
soup = BeautifulSoup(content)


for a in soup.findAll('a',href=True, attrs={'class':'mobile-job-link'}):

    link = a['href']
    driver.get(link)

    content2 = driver.page_source
    soup2 = BeautifulSoup(content2)
    
    for b , c in zip(soup2.findAll('div', {'class':'job-main-card content-card'}) , soup2.findAll('div', {'class':'about-job content-card'})):
                    
        title = b.find('h1', {'class':'job-title'})
        com_name =b.find('span', {'class':'company-name-and-status'})
        com_loc =b.find('span', {'class':'job-company-location'})
        job_post_date =b.find('time', {'itemprop':'datePosted'})


        titles.append((title.text).strip())
        companies.append((com_name.text).strip())
        locations.append((com_loc.text).strip())
        dates.append((job_post_date.text).strip())

        summary_table = c.find("table", attrs={"class": "table"})

        dd_text = []

        for dd in summary_table.find_all('dd'):
            dd_text.append((dd.text).strip().replace("\n                        " ," ").replace("                         ", " ") )

        Experience_Needed.append(dd_text[0])
        Career_Level.append(dd_text[1])
        Job_Type.append(dd_text[2])
        Salary.append(dd_text[3])
        Vacancies.append(dd_text[4])


    driver.execute_script("window.history.go(-1)")
    # number of iterate
    if len(titles) == 20:
        break

print(titles, companies, locations, dates )
df = pd.DataFrame({'Jop title':titles,'Companies names':companies,'job location':locations,'posted dates':dates,
                   'Experience Needed':Experience_Needed,'Career Level':Career_Level,'Job Type':Job_Type
                   ,'Salary':Salary,'Vacancies':Vacancies}) 

df.to_csv('IT-Software-Development-Jobs.csv', index=False, encoding='utf-8-sig')

==================================================================================================
                                                Data 
==================================================================================================
print(len(titles),len(companies),len(locations),len(dates),len(Experience_Needed),
      len(Career_Level),len(Job_Type),len(Salary),len(Vacancies))
print(titles)
print(companies)
print(locations)
print(dates)

print(Experience_Needed)
print(Career_Level)
print(Job_Type)
print(Salary)
print(Vacancies)