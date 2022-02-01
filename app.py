from azure.identity import DefaultAzureCredential
from azure.storage.blob import ContainerClient, __version__

from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')


@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   storage_url = 'https://msdocspythonflaskvmagelo.blob.core.windows.net'
   container_name = 'blob-container-01'
   credential = DefaultAzureCredential(exclude_shared_token_cache_credential=True)
   container_client = ContainerClient(account_url=storage_url, container_name=container_name, credential=credential)

   try:
      bloblist = ''
      for blob in container_client.list_blobs():
         bloblist += blob.name + ' '

   except Exception as ex:
      bloblist = 'error'

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name, bloblist = bloblist)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()