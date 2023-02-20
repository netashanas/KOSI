from selenium import webdriver
from selenium.webdriver.common.by import By
from time import  sleep

def scrape_current_song():
    '''
    Get the current song form their webstie

    :return:
    '''
    with open('kosi.csv', 'w', newline = '\n') as file:
        writer = csv.writer(file)
        writer.writerow(['Artist', 'Title'])
        while
            #for i in range(10):
            driver = webdriver.Chrome()
            # Make a request to the website
            url = 'https://kosi101.com'
            driver.get(url)

            artist = driver.find_element(By.ID,"artist")
            title = driver.find_element(By.ID,"title")



            # Print the text content of the element
            print(artist.text,',',title.text)
            driver.quit()












scrape_current_song()


