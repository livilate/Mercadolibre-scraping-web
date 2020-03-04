from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as link_open

my_link = "https://listado.mercadolibre.com.ar/monitor"

#abrir la pagina y conseguir la informacion y cerrar.
client = link_open(my_link)

#pasando la pagina a soup
page_soup = soup(client.read(), "html.parser")
client.close()

ml_productos = page_soup.find_all("li", {"class":"results-item highlighted article grid product item-info-height-185"})

#Create a cvs file
archivo = "Monitores.cvs"
f = open(archivo, "w")

titulos = "Producto, Precio, Link\n"
f.write(titulos)

for producto in ml_productos:
    #scraping de los links
    link = producto.div.div.div["item-url"]

    #scraping precio
    precio = producto.find_all("div", {"class":"item__price"})[0].text.strip().replace(".", "")

    #scraping nombre
    nombre = producto.find_all("h2", {"class":"item__title list-view-item-title"})[0].text.strip().replace("Monitor", "")

    #escribir en el archivo cvs los productos
    f.write(nombre.replace(",", "|") + "," + precio + "," + link + "\n")

f.close()