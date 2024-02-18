import azure.functions as func
import logging
from azure.cosmos import CosmosClient, exceptions, partition_key
import json 

URL="https://sitedb-2.documents.azure.com:443/"
KEY="Hsv5c61KdKUX5vybw3nDvrTKjy6uJFeIBlwCBaoEIRvEbhnwUgvSqScvF9VZBsUi68quI1sxcm4uACDbudW4WQ=="

DATABASE_NAME='ToDoList'
CONTAINER_NAME='Items'



app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    try:
        
        client=CosmosClient(URL,credential=KEY)
        database = client.get_database_client(DATABASE_NAME)
        container=database.get_container_client(CONTAINER_NAME)
        
        query='SELECT VALUE Items.visit  FROM Items'
        
        counter=container.read_item(query=query, enable_cross_partition_query=True)
        
        counter = counter + 1 
        container.upsert_item(counter)
        
        return func.HttpResponse(f"site visit tracked this is visit{counter} :]", status_code=200)
    except Exception as e:
        return func.HttpResponse(f"error: {str(e)}")