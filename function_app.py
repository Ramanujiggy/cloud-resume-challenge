import azure.functions as func
import logging
from azure.cosmos import CosmosClient, exceptions
import json 

URL="https://sitedb-2.documents.azure.com:443/"
KEY="Hsv5c61KdKUX5vybw3nDvrTKjy6uJFeIBlwCBaoEIRvEbhnwUgvSqScvF9VZBsUi68quI1sxcm4uACDbudW4WQ=="


client=CosmosClient(URL,credential=KEY)
DATABASE_NAME='ToDoList'
database = client.get_database_client(DATABASE_NAME)
CONTAINER_NAME='Items'
container=database.get_container_client(CONTAINER_NAME)




app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        container.upsert_item(body={'id':'sitevisit', 'visits':1})
        return func.HttpResponse("site visit tracked :]", status_code=200)
    except exceptions.CosmosHttpResponseError :
        return func.HttpResponse("Error: This didn't work")
    

        