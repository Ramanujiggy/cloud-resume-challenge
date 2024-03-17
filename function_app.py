import azure.functions as func
import logging
from azure.cosmos import CosmosClient, exceptions 

URL="https://sitedb-2.documents.azure.com:443/"
KEY="Hsv5c61KdKUX5vybw3nDvrTKjy6uJFeIBlwCBaoEIRvEbhnwUgvSqScvF9VZBsUi68quI1sxcm4uACDbudW4WQ=="
DATABASE_NAME='ToDoList'
CONTAINER_NAME='Items'




app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    count = 0
    query= "SELECT * FROM c WHERE c.id = '1'"
    try:
        client=CosmosClient(URL,credential=KEY)
        database = client.get_database_client(DATABASE_NAME)
        container=database.get_container_client(CONTAINER_NAME)
        
        for item in container.query_items(query=query, enable_cross_partition_query=True):
            updated_item = item
            count = int(item['count'])
            count +=1 
            updated_item['count']=count
            container.upsert_item(item, updated_item)
    
    except exceptions.CosmosHttpResponseError as e:
        logging.error(f"An error occured: {e.status_code} +  {e.message}")
        count = e.message
    
    return func.HttpResponse(body=str(count),status_code=200)
