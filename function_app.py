import azure.functions as func
import logging
import subprocess
def run_demo():
    subprocess.call(["python", "demo1.py"])
app = func.FunctionApp()

@app.blob_trigger(arg_name="myblob", path="funcappdemo8",
                               connection="funcappdemo8_STORAGE") 
def blob_trigger(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes")
    run_demo()
