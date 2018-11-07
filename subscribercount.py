import requests, webbrowser
from time import sleep

channel = 'pewdiepie'
key = open(r'key.txt', 'r').read().strip()

url = r'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername='+channel+r'&key='+key

tmp = 0
print("Channel: PewDiePie\n\n")
while True:
  res = requests.get(url)

  subscnt = res.json()['items'][0]['statistics']['subscriberCount']
  if(subscnt == '69696969'):
    print("OH YEAH!")
    webbrowser.open(r'https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw')
    break
  if(tmp != subscnt):
    print("Subs Count change occurred: "+subscnt)
    tmp = subscnt
  sleep(5)
