import os
from azure.identity import DefaultAzureCredential
from azure.identity import VisualStudioCodeCredential
from azure.mgmt.resource import SubscriptionClient

# Import the client object from the SDK library
from azure.storage.blob import BlobClient

## Easiest
credential = VisualStudioCodeCredential()

## Specify environment variables
# SET AZURE_TENANT_ID=
# SET AZURE_CLIENT_ID=
# SET AZURE_CLIENT_SECRET=
#credential = DefaultAzureCredential()

# Who is making this request
subscription_client = SubscriptionClient(credential)
subscription = next(subscription_client.subscriptions.list())
print(subscription.id)
print(subscription.subscription_id)
print(subscription.display_name)

# Retrieve the storage blob service URL, which is of the form
# https://pythonsdkstorage12345.blob.core.windows.net/
storage_url = os.environ["AZURE_STORAGE_BLOB_URL"]

# Create the client object using the storage URL and the credential
blob_client = BlobClient(storage_url,
    container_name="blob-container-01", blob_name="sample-blob.txt", credential=credential)

# Open a local file and upload its contents to Blob Storage
with open("./sample-source.txt", "rb") as data:
    blob_client.upload_blob(data)