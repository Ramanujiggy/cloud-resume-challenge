import os 
import azure.functions as func
import logging
from azure.cosmos import CosmosClient, exceptions 

url = os.environ["ACCOUNT_URI"]
key = os.environ["ACCOUNT_KEY"]
DATABASE_NAME= os.environ["DATABASE_NAME"]
CONTAINER_NAME = os.environ["CONTAINER_NAME"]


client=CosmosClient(url,key)
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)



@app.cosmos_db_input(arg_name="documents", 
    database_name=os.environ["DATABASE_NAME"],
    collection_name=os.environ["CONTAINER_NAME"],
    id="1",
    partition_key="/Visits",
    connection_string_setting="AccountEndpoint=https://sitedb-2.documents.azure.com:443/;AccountKey=Hsv5c61KdKUX5vybw3nDvrTKjy6uJFeIBlwCBaoEIRvEbhnwUgvSqScvF9VZBsUi68quI1sxcm4uACDbudW4WQ==;")

@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    count = 0
    query= "SELECT * FROM c WHERE c.id = '1'"
    try:
        database = client.get_database_client(DATABASE_NAME)
        container=database.get_container_client(CONTAINER_NAME)
        
        for item in container.query_items(query=query, enable_cross_partition_query=True):
            updated_item = item
            count = int(item['count'])
            count +=1 
            updated_item['count']=count
            container.upsert_item(updated_item)
    
    except exceptions.CosmosHttpResponseError as e:
        logging.error(f"An error occured: {e.status_code} + {e.message}")
        count = e.message
    
    return func.HttpResponse(body=str(count),status_code=200)
