import os
from azure.identity import DefaultAzureCredential
from azure.identity import VisualStudioCodeCredential
from azure.mgmt.resource import SubscriptionClient
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

# Import the client object from the SDK library
from azure.storage.blob import BlobClient

## Easiest
# https://github.com/Azure/azure-sdk-for-net/issues/13228
credential = DefaultAzureCredential(exclude_shared_token_cache_credential=True)

# Who is making this request
#subscription_client = SubscriptionClient(credential)
#subscription = next(subscription_client.subscriptions.list())
#print(subscription.id)
#print(subscription.subscription_id)
#print(subscription.display_name)

# Retrieve the storage blob service URL, which is of the form
# https://pythonsdkstorage12345.blob.core.windows.net/
storage_url = 'https://msdocspythonflaskvmagelo.blob.core.windows.net'
container_name = 'blob-container-01'

container_client = ContainerClient(account_url=storage_url, container_name=container_name, credential=credential)
try:
    # List the blobs in the container
    blob_list= container_client.list_blobs()
    bloblist = ''
    for blob in blob_list:
        bloblist += blob.name + ' '

except Exception as ex:
    bloblist = 'error'

print(bloblist)