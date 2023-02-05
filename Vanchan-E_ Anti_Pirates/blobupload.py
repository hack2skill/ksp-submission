from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobClient, BlobServiceClient, PublicAccess

account_url = "https://kspstorage1.blob.core.windows.net/"

creds = DefaultAzureCredential()
service_client = BlobServiceClient(
    account_url=account_url,
    credential=creds
)

container_name="sgf"
try:
    new_container = service_client.create_container(container_name, public_access=PublicAccess.Container)
except Exception as e:
    print(e)
    new_container = service_client.get_container_client(container_name)
for blob in new_container.list_blobs():
    print(blob)

blob_name = "testblob1"
blob_url = f"{account_url}/{container_name}/{blob_name}"

blob_client = BlobClient(account_url, container_name, blob_name)

with open("hist1.png", "rb") as blob_file:
    blob_client.upload_blob(data=blob_file)

