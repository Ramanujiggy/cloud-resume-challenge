import os
from azure.cosmos import CosmosClient, exceptions PartitionKey

#from azure.cosmos.aio import CosmosClient 
import json
import asyncio

#accessing the cosmos db

URL="https://sitedb-2.documents.azure.com:443/"
KEY="Hsv5c61KdKUX5vybw3nDvrTKjy6uJFeIBlwCBaoEIRvEbhnwUgvSqScvF9VZBsUi68quI1sxcm4uACDbudW4WQ=="


client=CosmosClient(URL,credential=KEY)
DATABASE_NAME='ToDoList'
database = client.get_database_client(DATABASE_NAME)
CONTAINER_NAME='Items'
container=database.get_container_client(CONTAINER_NAME)

