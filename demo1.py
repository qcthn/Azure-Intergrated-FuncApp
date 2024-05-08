import os
from azure.storage.blob import BlobServiceClient
from azure.data.tables import TableServiceClient
from azure.core.credentials import AzureNamedKeyCredential
from datetime import datetime
# Thông tin kết nối với Blob Storage
storage_connection_string = '<YOUR CONNECTION STRING>'
blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)

# Thông tin kết nối với Table Storage
accountname = '<YOUR ACCOUNT NAME>'
key = 'YOUR KEY'
endpoint = 'YOUR ENDPOINT OF TABLE STORAGE'
credential = AzureNamedKeyCredential(accountname, key)
table_service_client = TableServiceClient(endpoint=endpoint, credential=credential)

# Tạo một container trong Blob Storage
container_name = 'YOUR NAME OF CONTAINER'
current_time = datetime.now()
partition_key = current_time.strftime("%Y%m%d%H%M%S") # Khởi tạo khóa phân vùng
count = 1
table_client = table_service_client.get_table_client("YOUR NAME TABLE")
entity = {
   'PartitionKey': partition_key,  # Giả sử một khóa phân vùng cố định cho ví dụ này
   'RowKey': 'Upload',  # RowKey là tên tập tin
   'System': 'Completed' # Trường System là kích thước tập tin  
}
table_client.create_entity(entity)