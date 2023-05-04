import logging
import pandas as pd
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    i = req.params.get('url')

    def nueva_info(url):
        r = requests.get(url, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'})
        luces = r.content
        luces = str(luces)
        #print(luces)
        inicio = r'id="titulo">'
        final = r'</h1>'
        titulo = luces[luces.find(inicio)+len(inicio) : luces.find(final)]
        
        inicio = r'"author": "'
        final = r'",\\n                        "publisher":'
        autor = luces[luces.find(inicio)+len(inicio) : luces.find(final)]
        print(titulo)    
        precio = float((str(luces).split('class="despues">')[1][0:5]).replace(',', '.'))
        
        return(pd.DataFrame(data = [[titulo, autor, precio]], columns = ["Título", "Autor", "Precio"]))

    logging.info(nueva_info(i))
    