import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request



webpage = 'https://ebible.org/asv/JHN'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

page_verses = soup.findAll('div', class_='main')

for verses in page_verses:
    verse_list = verses.text.split(".")
    print(verses)

mychoice = random.choice(verse_list[:-5])

verse = f'Chapter: {random_chapter} Verse: {mychoice}'

print(verse)

import keys
from twilio.rest import Client

client = Client(keys.accountSID, keys.authToken)

TwilioNumber = "+2525090001"

mycellphone = "+12149247435"

textmessage = client.messages.create(to=mycellphone, from_=TwilioNumber, body=verse)

