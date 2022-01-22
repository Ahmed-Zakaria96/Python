import random
from selenium import webdriver

webs = ['https://www.facebook.com/A7medZaKariaAli/',
        'https://github.com/Ahmed-Zakaria96',
        'https://twitter.com/A7medZakariaAli',
        'https://www.linkedin.com/in/ahmedzakaria96/',
        'https://codeforces.com/profile/Simple-Z',
        'https://www.researchgate.net/profile/Ahmed-Zakaria-17']

ranWeb = random.choice(webs)

PATH = r"E:\Programs\edge_driver\msedgedriver.exe"
driver = webdriver.Edge(PATH)
driver.get(ranWeb)
