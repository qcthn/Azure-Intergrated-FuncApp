

# Azure Blob and Table Storage Interaction

![Azure Storage](https://docs.microsoft.com/en-us/azure/storage/common/media/storage-introduction/storage-introduction.png)

## Overview

This project facilitates interaction between Azure Blob Storage, Blob Trigger, and Table Storage. Upon uploading a blob to Blob Storage, a trigger is activated to notify the system, and simultaneously, a new entry is created in Table Storage.

## Project Structure

- **Function App Code**: The source code for the Function App is available in the file `function_app.py`.
- **Blob Trigger Code**: The blob trigger function is defined in `function_app.py`, which is responsible for processing uploaded blobs and invoking the demo.
- **Demo Code**: The demo functionality is implemented in the file `demo1.py`, where connections to Blob Storage and Table Storage are established, and a new entity is created in Table Storage upon blob upload.

## Blob Trigger Functionality

The `blob_trigger` function in `function_app.py` is triggered upon blob upload. It logs information about the uploaded blob and invokes the demo functionality.

## Demo Functionality

The `demo1.py` script demonstrates the interaction with Azure Blob Storage and Table Storage. It performs the following tasks:

1. Establishes connections to Blob Storage and Table Storage using connection strings and credentials.
2. Creates a container in Blob Storage and initializes a partition key for Table Storage.
3. Creates a new entity in Table Storage with details of the uploaded blob, such as partition key, row key (file name), and system status.

## Dependencies

- Python 3
- Azure Functions SDK
- Azure Storage Blob SDK
- Azure Data Tables SDK

## Configuration

Ensure to configure the following parameters before running the project:

- **Blob Storage Connection String**: Update `storage_connection_string` in `demo1.py` with your Blob Storage connection string.
- **Table Storage Account Details**: Update `accountname`, `key`, and `endpoint` in `demo1.py` with your Table Storage account details.
- **Container Name**: Update `container_name` in `demo1.py` with the desired name for the Blob Storage container.
- **Table Name**: Update `"YOUR NAME TABLE"` in `demo1.py` with the name of your Table Storage table.

## Usage

1. Deploy the Function App to Azure Functions.
2. Upload a blob to the specified Blob Storage container.
3. Check Table Storage for the newly created entity with details of the uploaded blob.

---

Feel free to customize the README further based on additional details or specific instructions related to your project.
