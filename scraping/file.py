from cgitb import html
import bs4, requests, webbrowser
from pprint import pprint

link = "https://www.subito.it/annunci-italia/vendita/telefonia/?q=iphone+rotto&order=datedesc"
prefisso = "https://www.subito.it/telefonia"

response = requests.get(link)
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, "html.parser")

div_annunci= soup.find("div", class_="container ItemListContainer_container__SjEc1")

p_annunci= div_annunci.find_all("p", class_="index-module_price__N7M2x SmallCard-module_price__yERv7 price index-module_small__4SyUf")
a_annunci = div_annunci.find_all("a")

link_annunci=[]

for x in a_annunci:
    for y in p_annunci:

        link_annuncio = str(x.get("href"))
        if prefisso in link_annuncio:
            link_annunci.append(link_annuncio)

        price = str(y)
        price_annuncio = price[99:104]
        link_annunci.append(price_annuncio+"\n")






f = open("telefoni.txt", "a")
old_links = [riga.rstrip("\n") for riga in open ("telefoni.txt")]
new_links = []
for link_annuncio in link_annunci:
    if link_annuncio not in old_links:
        new_links.append(link_annuncio)
        f.write('%s\n' % link_annuncio)

f.close()

if new_links:
    print('annunci aggiornati...\naprire il file "telefoni.txt"')
    domanda=input('\n\nper visualizzare solo i nuovi annunci digitare "si"...')
    if domanda == "si":
        for new_link in new_links:
            webbrowser.open(new_link)
    else:
        pass
else:
    print('nessun nuovo annuncio...\n aprire il file "telefoni.txt" per visualizzare tutti gli annunci')

