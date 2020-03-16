from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv


# load your driver
driver = webdriver.Chrome('/Users/hannahrarick/Documents/Web Apps/python/scraping/chromedriver')

# get the web page
driver.get('https://safesport.i-sight.com/published');

time.sleep(3)

# find the button to open the menu using XPath
# and click it
driver.find_element_by_xpath('//*[@id="published-grid"]/div/div[1]/div[2]/div[1]/div/div/ul/li[4]/div/div[2]/button').click()
time.sleep(2)

# find the sport on the menu using the text inside <a> tags
# and click it
driver.find_element_by_link_text('USA Gymnastics').click()
time.sleep(2)

# capture the page
#page = driver.page_source
#soup = BeautifulSoup(page, "html.parser")


csvfile = open('gymnastics.csv', 'w', newline='', encoding='utf-8')

c = csv.writer(csvfile)

c.writerow( ['Name', 'City', 'State', 'Sport Affiliation(s)', 'Adjudicating Body', 'Decision Date', 'Misconduct', 'Action Taken'])


 # This part of the code scrapes one table on one page and puts each row into a list. Add code to make this write to a CSV.
# write all the cells from the table into a list
def get_convicted(soup):
    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')
    for row in rows:
        td_list = row.find_all('td')
        one_convicted = []
        for td in td_list:
            try:
                one_convicted.append(td.text)
            except:
                one_convicted.append('blank')

        c.writerow(one_convicted)
        #print(one_convicted)

for i in range(0, 24):
    page = driver.page_source
    soup = BeautifulSoup(page, "html.parser")
    get_convicted(soup)
    next_page = driver.find_element_by_class_name('glyphicon-chevron-right').click()
    time.sleep(2)


# close the Selenium driver
csvfile.close()
driver.quit()
