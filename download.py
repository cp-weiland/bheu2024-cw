""" Download script by https://github.com/Dhwanisolanki12 """

from huggingface_hub import list_datasets 
import requests
import pandas as pd
import numpy as np
import requests
import logging
import json
from pathlib import Path
import os, sys, re

def get_datasetids_HF():
    # from datasets import list_datasets
    all_datasets = list_datasets()
    datasetid_list = list(all_datasets)
    #columns defined from HF datasets
    columns = ['id', 'author', 'sha','created_at','tzinfo','last_modified','private','gated','disabled','downloads','downloads_all_time','paperswithcode_id',
    'tags','trending_score','card_data','siblings']

    #converting to dataframe for detailed and readable information
    df = pd.DataFrame(datasetid_list, columns=columns)
    datasets_ids = df['id'].tolist()
    return datasets_ids



def create_outputdir(dir_name:str):
    '''
    Parameters:
    dir_name (int): Name of the folder to store output files.

    Returns:
    Creates folder in the current directory if does not exist.
    '''
    # current_dir_path= Path.cwd()
    # Create the directory
    try:
        directory = Path(dir_name)
        directory.mkdir(parents=True, exist_ok=True)
        
        return os.path.abspath(dir_name)   
        # return (f"Directory '{dir_name}' created successfully",dir_name)
        # print(f"Directory created or already exists at: {directory.resolve()}")
   
    except PermissionError:
        return(f"Permission denied: Unable to create '{dir_name}'.")
    except Exception as e:
        return(f"An error occurred: {e}")

def setup_logging(log_file: str, log_level: int = logging.INFO):
    """
    Set up logging configuration.

    Parameters:
    log_file (str): The filename for the log file.
    log_level (int): The logging level. Default is logging.INFO.

    Example:
    >>> setup_logging('my_log.log', logging.DEBUG)
    """
    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # Create a file handler that appends to the log file
    file_handler = logging.FileHandler(log_file)  # Default mode is 'a' (append)
    
    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

def fetch_croissant_metadata(output_dir:str, log_file:str):
    
    #calling previous functions
    data_id = get_datasetids_HF()
    outputpath=create_outputdir(output_dir)

    print(outputpath)
    
    setup_logging(log_file)

    print(len(data_id))
    #first_20_items = data_id[:4]
    sys.exit(0)
    
    # Write each item to a separate file
    for i, data_id in enumerate(first_20_items):
    # for i in data_id:
        # Define the URL for the JSON-LD metadata
        url = f"https://huggingface.co/api/datasets/{data_id}/croissant/"
        # params = {'limit': 20,  # Limit the number of results to 20
        #           'sort': 'likes','offset': 0} 
        # Make a request to get the dataset metadata
        response = requests.get(url)
        filename = data_id.replace('/','_') +'.jsonld'
        # print(filename)
        output_filepath = os.path.join(outputpath, filename)
        #print(output_filepath)
    
        # Check if the request was successful
        if response.status_code == 200:  
            # Save the JSON-LD metadata to a file
            with open(output_filepath, 'w', encoding="utf-8") as file:
                json_data = response.json()
                pretty_jsonld = json.dumps(json_data, indent=2, ensure_ascii=False)
                # The JSON-LD data to pretty print.
                file.write(pretty_jsonld)
                # file.write(response.text)
                print("Dataset metadata downloaded successfully! :", data_id)
                logging.info(f"Dataset metadata downloaded successfully for {data_id}: {response.status_code}")
                print('--------------------------------------------------------------------------------------------')
        else:
            print("Error: Unable to download the dataset metadata:", data_id)
            logging.error(f"Error fetching response {data_id}: {response.status_code}")
            print("Status code:", response.status_code, data_id)
            print('--------------------------------------------------------------------------------------------')
            
if __name__ == "__main__":
    fetch_croissant_metadata("json", "err.log")
