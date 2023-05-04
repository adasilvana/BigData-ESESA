import logging
from azure.data.tables import TableClient
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    MY_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=prueba2704;AccountKey=5GgjmOEHx2lTpJ+vE2yO1GSQ8ZyuK4PWvWHPFgi2z9DFzn6+3d5PKr1qZ/GdIjJ6LQO41RLvSB8O+AStzFMQtw==;EndpointSuffix=core.windows.net"

    # Leer la tabla
    table_client = TableClient.from_connection_string(conn_str=MY_CONNECTION_STRING, table_name="Clientes")
    entities = table_client.query_entities("")
    pagina = "<html><body><table><tr><th>Id</th><th>Provincia</th><th>Apellidos</th><th>Nombre</th></tr>"
    for entity in entities:
        fila = "<tr><td>" + entity["Id"] + "</td><td>" + entity["Provincia"] + "</td><td>" + entity["Apellidos"] + "</td><td>" + entity["Nombre"] + "</td></tr>"
        pagina = pagina + fila
    pagina = pagina + "</table></body></html>"
    return func.HttpResponse(pagina, mimetype="text/html")