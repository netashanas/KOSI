from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import csv

def scrape_current_song(writer):
    '''
    Get the current song form their webstie
    :return:
    '''
    
    driver = webdriver.Chrome()
    # Make a request to the website
    url = 'https://kosi101.com/recently-played/?station=KOSIFM'
    driver.get(url)

    raw = driver.find_element(By.XPATH, "//*[@id='main_body']/div[5]/div[1]/div")
    raw_to_test= raw.text
    artist_and_title = raw_to_test.split("\n")
    print(artist_and_title)
    previous_song = None
    while True:
        current_song = artist_and_title
        if current_song != previous_song:
            writer.writerow(artist_and_title)
            previous_song = current_song




