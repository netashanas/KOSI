from scrape import scrape_current_song
from datetime import datetime, timedelta
import csv

def run_scraping(time_frame_in_minutes:int):
    '''
    runs the scraping loop until gets to time_frame_in_hours
    :param time_frame_in_minutes:
    :return:
    '''
    time_zero = datetime.now()
    time_end =  time_zero + timedelta(minutes= time_frame_in_minutes)
    with open('kosi.csv', 'w', newline = '\n') as file:
        writer = csv.writer(file)
        writer.writerow(["Artist", "Title"])
        while True:
            if datetime.now() > time_end:
                break
            else:
                scrape_current_song(writer=writer)


run_scraping(time_frame_in_minutes=2)