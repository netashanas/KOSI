from  scrape import scrape_current_song
from datetime import  datetime, timedelta
import csv

def run_scraping(time_frame_in_hours:int):
    '''
    runs the scraping loop until gets to time_frame_in_hours
    :param time_frame_in_hours:
    :return:
    '''
    time_zero = datetime.now()
    time_end =  time_zero + timedelta(hours=time_frame_in_hours)
    while True:
        if datetime.now() > time_end:
            break
        else:
            artist_and_title = scrape_current_song()
            write_results_to_file(artist_and_title)
            print('yalla')

    pass

def write_results_to_file():
    if:

    pass

run_scraping(time_frame_in_hours=0)