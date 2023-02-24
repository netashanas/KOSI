from datetime import datetime, timedelta
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime as dt


def run_scraping(time_frame_in_minutes:int):
    '''
    runs the scraping loop until gets to time_frame_in_hours
    :param time_frame_in_minutes:
    :return:
    '''
    time_zero = datetime.now()
    time_end =  time_zero + timedelta(hours= time_frame_in_minutes)
    with open('kosi.csv', 'w', newline = '\n') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Artist", "Time"])
        previous_song = None
        while True:
            if datetime.now() > time_end:
                break
            else:
                driver = webdriver.Chrome()
                # Make a request to the website
                url = 'https://kosi101.com/recently-played/?station=KOSIFM'
                driver.get(url)
                raw = driver.find_element(By.XPATH, "//*[@id='main_body']/div[5]/div[1]/div")
                raw_to_test = raw.text
                artist_and_title = raw_to_test.split("\n")
                current_song = artist_and_title
                if current_song != previous_song:
                    print(current_song)
                    now = dt.datetime.now()
                    new_row = [artist_and_title[0],artist_and_title[1],now.strftime('%Y-%m-%d %H:%M:%S')]
                    writer.writerow(new_row)
                    previous_song = current_song
                else:
                    pass
            driver.quit()
            time.sleep(30)




run_scraping(time_frame_in_minutes=3)

