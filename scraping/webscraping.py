from bs4 import BeautifulSoup
import requests

url = requests.get('http://teddework.ddns.com.br:8090/').content
#objeto url recebendo o counteudo da requisição http do site
soup = BeautifulSoup(url, 'html.parser')
#objeto soup baixando do site o html
#print(soup.prettify())
#transformar o html em string e o print vai exibir o hmtl

#temperatura = soup.find("div", class_="_flex _margin-t-sm-10 _gap-10")
#print(temperatura.string)
#print(soup.title.string)
print(soup.find('cnpj'))
