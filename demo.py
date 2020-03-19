from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pandas as pd

#browser = webdriver.Chrome()
url="https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_3&otracker1=AS_QueryStore_OrganicAutoSuggest_0_3&as-pos=0&as-type=RECENT&as-searchtext=lap&page="
page_no=1
no_of_pages=1
urlf=url+ str(page_no)
products=[] #List to store name of the product
prices=[] #List to store price of the product

while page_no<=no_of_pages:
    source = requests.get(urlf).text
    soup = BeautifulSoup(source,'lxml')
    
    for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
        name=a.find('div', attrs={'class':'_3wU53n'})
        p1=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
        price=p1.text[1:]
        products.append(name.text)
        prices.append(price)

    if(page_no==1):
        n=soup.find('div',attrs={'class':'_2zg3yZ'})
        n1=n.find('span').text
        n2=n1.split(' ')
        no_of_pages=int(n2[3])
    page_no+=1
    urlf=url+ str(page_no)
 

df = pd.DataFrame({'Product Name':products,'Price':prices}) 
df.to_csv('products_file1.csv', index=True, index_label='Sr. No.', encoding='utf-8')
print('successfully')