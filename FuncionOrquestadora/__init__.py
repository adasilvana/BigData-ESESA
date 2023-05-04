import logging
import requests
import azure.functions as func
import pandas as pd

datos_libros = pd.DataFrame(columns = ["Título", "Autor", "Precio"])

def main(mytimer: func.TimerRequest) -> None:
    # Leo la tabla
    #tabla_urls.find('status eq 0')
    # Leo las 10 primeras filas
    lista_urls = ['https://www.librerialuces.com//es/libro/human-retail_705700',
 'https://www.librerialuces.com//es/libro/no-son-cuentos-chinos_704850',
 'https://www.librerialuces.com//es/libro/shakespeare-and-company_706057',
 'https://www.librerialuces.com//es/libro/trabajar-en-llamas_705837',
 'https://www.librerialuces.com//es/libro/manual-de-finanzas-inmobiliarias_705828',
 'https://www.librerialuces.com//es/libro/l-oreal-le-roi-c-est-moi_705704',
 'https://www.librerialuces.com//es/libro/tiktok_705681',
 'https://www.librerialuces.com//es/libro/no-trabajes-en-creatividad_705233',
 'https://www.librerialuces.com//es/libro/como-delegar_705103',
 'https://www.librerialuces.com//es/libro/management-tips-2-serie-management-en-20-minutos_705099',
 'https://www.librerialuces.com//es/libro/equipos-innovadores_705098',
 'https://www.librerialuces.com//es/libro/pon-un-beatle-en-tu-empresa_705019', 'https://www.librerialuces.com//es/libro/human-retail_705700',
 'https://www.librerialuces.com//es/libro/no-son-cuentos-chinos_704850',
 'https://www.librerialuces.com//es/libro/shakespeare-and-company_706057',
 'https://www.librerialuces.com//es/libro/trabajar-en-llamas_705837',
 'https://www.librerialuces.com//es/libro/manual-de-finanzas-inmobiliarias_705828',
 'https://www.librerialuces.com//es/libro/l-oreal-le-roi-c-est-moi_705704',
 'https://www.librerialuces.com//es/libro/tiktok_705681',
 'https://www.librerialuces.com//es/libro/no-trabajes-en-creatividad_705233',
 'https://www.librerialuces.com//es/libro/como-delegar_705103',
 'https://www.librerialuces.com//es/libro/management-tips-2-serie-management-en-20-minutos_705099',
 'https://www.librerialuces.com//es/libro/equipos-innovadores_705098',
 'https://www.librerialuces.com//es/libro/pon-un-beatle-en-tu-empresa_705019']

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
    for encargo in lista_urls:
        r = requests.get("https://prueba0305.azurewebsites.net/api/funcion_orquestadora?url=" + encargo)
        datos_libros = pd.concat([datos_libros, r])

    logging.info(datos_libros)
    
