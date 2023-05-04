import logging
from azure.data.tables import TableClient
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    MY_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=prueba2704;AccountKey=5GgjmOEHx2lTpJ+vE2yO1GSQ8ZyuK4PWvWHPFgi2z9DFzn6+3d5PKr1qZ/GdIjJ6LQO41RLvSB8O+AStzFMQtw==;EndpointSuffix=core.windows.net"

    id = req.params.get('id')
    if id != None:
        # Leer la tabla
        my_filter = "RowKey eq '" + id + "'"
        table_client = TableClient.from_connection_string(conn_str=MY_CONNECTION_STRING, table_name="Clientes")
        entities = table_client.query_entities(my_filter)
        for entity in entities:
            dato = {
                "MiId": entity["Id"],
                "MiProvincia": entity["Provincia"],
                "MiApellidos": entity["Apellidos"],
                "MiNombre": entity["Nombre"]
            }
            return func.HttpResponse(str(dato))
        return func.HttpResponse("No hay nadie")
    else:
        return func.HttpResponse("Me falta el id", status_code=200)
