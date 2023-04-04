import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://www.tudogostoso.com.br"




def openPageAndScrapping(urlOnly):
    
    dr = webdriver.Chrome()
    dr.get(f"{url}{urlOnly}")
    bs = BeautifulSoup(dr.page_source,"html.parser")
    title = bs.find('h1', attrs={'tabindex': '0'}, string=True).text.strip()
    ingredientsArray = bs.select('.col-lg-8.ingredients-card ul li span p')
    if ingredientsArray.__len__() == 0:
        ingredientsArray = bs.select('.col-lg-8.ingredients-card ul li span')
    ingredients = ', '.join([str(x.text.strip()) for x in ingredientsArray])
    preparoArray = bs.select('.instructions.e-instructions ol li span p ')
    if preparoArray.__len__() == 0:
        preparoArray = bs.select('.instructions.e-instructions  ol li span')
    preparo = ', '.join([str(x.text.strip()) for x in preparoArray])
    dr.close()
    
    print(f"{title} \n INGREDIENTES: \n {ingredients} \n PREPARO: \n {preparo}" )
    return  f"{title} \n INGREDIENTES: \n {ingredients} \n PREPARO: \n {preparo}" 
    # teste

    
    

def main(typeReceipt):
    dr = webdriver.Chrome()
    dr.get(f"{url}/busca?q={typeReceipt}")
    bs = BeautifulSoup(dr.page_source,"html.parser")
    contain = bs.select(".row .col-lg-5 .rounded")[0]
    links = contain.find_all("a", href=re.compile("/receita/"))
    dr.close()
    receitas = []
    for link in links:
        receitas.append(openPageAndScrapping(link.get('href')))
       

    body = f"Receitas {typeReceipt} \n"
    receitasFormatted = '\n \n'.join([str(x) for x in receitas])
    body += receitasFormatted
    file = open(f"receitas {typeReceipt}.txt", "w",  encoding="utf-8")
    file.write(body)
    file.close()

    # teste
    # openPageAndScrapping("/receita/82059-biscoito-salgado-caseiro.html")




    


main('doce')
main('salgado');




