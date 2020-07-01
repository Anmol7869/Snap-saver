from bs4 import *
import requests as requests
import os

r2 = rq.get("URL OF THE WEBSITE")
soup2 = BeautifulSoup(r2.text, "html.parser")

links = []

x = soup2.select('img[src^="Common path of every picture that has to be downloaded"]')

for img in x:
    links.append(img['src'])

os.mkdir('snaps')
i = 1

for index, img_link in enumerate(links):
    if i == 15:
        img_data = rq.get(img_link).content
        with open('snaps/' + str(index + 1) + '.jpg', 'wb+') as f:
            f.write(img_data)
        i += 1
    else:
        f.close()
        break        

# After running this file you will get 15 files downloaded in the folder snaps that will contain your downloaded photos