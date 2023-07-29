import cloudsearch
from google.oauth2 import service_account
from googleapiclient.discovery import build
# import schema_create_or_update

credentials = service_account.Credentials.from_service_account_file("service.json",scopes=["https://www.googleapis.com/auth/cloud_search"])
delegated_credentials = credentials.with_subject("akshit.baunthiyal@delta.cloudtoolkit.com")
service = build("cloudsearch","v1",credentials=delegated_credentials)

item_service = cloudsearch.ItemsService(service=service,datasources="5b7a3dc600a8e9240dfbe863381d7385")
# schema_json = schema_create_or_update.cloud_search_get_schema(service=service,datasources="5b7a3dc600a8e9240dfbe863381d7385")

# print(schema_json)

# items = item_service.list()
# for item in items:
#     print(item.get("version"))
# print(len(items))