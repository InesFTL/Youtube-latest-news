

import json
import urllib.request 
from urllib.request import  urlopen
from selenium import webdriver
import time

def check_for_new_video():
	#Find it at : https://console.developers.google.com/apis/api/youtube/overview
    API_KEY = str(input("Enter your API key: "))
    #Enter the channel ID
    channel_id = "UC8butISFwT-Wl7EV0hUK0BQ"
    root_video_url = 'https://www.youtube.com/watch?v='
    root_search_url = 'https://www.googleapis.com/youtube/v3/search?'
    url = root_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(API_KEY, channel_id)
    #Webppage request
    webpage =urlopen(url)
    response = json.load(webpage)
    vidID= response['items'][0]['id']['videoId']
    #Checking if the videoID is different from the latest video, if it is, 
    #open the new video in the browser
    new_video = False
    with open('videoid.json', 'r') as json_file:
        data = json.loads(json_file.read())
        if data['videoId'] != vidID:
        	#For Safari, it is required to activate the remote automation in Safari Preferences
            driver = webdriver.Safari() #Can change it to Firefox or Chrome for Firefox add GeckoDriver
            driver.get(root_video_url + vidID)
            new_video = True

    if new_video:
        with open('videoid.json', 'w') as json_file:
            data = {'videoId' : vidID}
            json.dump(data, json_file)

try:
    while True:
        check_for_new_video()
        time.sleep(10)
except KeyboardInterrupt:
    print('Stop')