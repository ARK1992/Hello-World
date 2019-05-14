# exec is python3!
import urllib.request
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

def p_tag_to_file(file_path, url):

    try:
        html = urllib.request.urlopen(url)

        soup = BeautifulSoup(html, "html.parser")
        p = soup.findAll("p")

        file = open(file_path, 'at', newline = '', encoding = 'utf-8')

        for p in soup.findAll("p"):
            file.write(p.get_text())
            #print(p)
        file.close()
    except urllib.error.HTTPError as e:
        with open('HTTPerr.txt', 'a') as f:
            f.write('several issues arise：{}\n'.format(e.code))
    except urllib.error.URLError as e:
        with open('URLerr.txt', 'a') as f:
            f.write('several issues arise：{}\n'.format(e.reason))

with open('url_list.txt', 'rt') as fr:
    for url in fr:
        while True:
            url = fr.readline().strip('\n')
            if not url:
                break
            try:
                p_tag_to_file("p_tag.txt", url)
            except requests.exceptions.RequestException as e:
                with open('err.txt', 'a') as fe:
                    fe.write('several issues arise：{}'.format(e))
