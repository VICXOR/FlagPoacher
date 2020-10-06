import requests
import sys

def request(url):
        try:
                return requests.get(url)
        except requests.exceptions.ConnetionError:
                pass

turl = sys.argv[1]
wordList = sys.argv[2]
flagFormat = sys.argv[3]

file = open(wordList, 'r')
for line in file:
        word = line.strip()
        full_url = turl + word
        r = requests.get(full_url)
        if r:
                if flagFormat in r.text:
                        print('[+]There is a flag here >> ' + full_url)
                        print('-----------------------')
