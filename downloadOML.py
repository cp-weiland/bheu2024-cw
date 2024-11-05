#from huggingface_hub import list_datasets 
import requests
import pandas as pd
import numpy as np
import requests
import logging
import json
from pathlib import Path
import os, sys, re

openml_datasets = [1464, 333, 1510, 1489, 1487, 1485, 1130, 1142, 1138, 1161]

for i in openml_datasets:
    #url_openml =f'https://www.openml.org/api/v1/json/data/{i}'
    #print(url_openml)
    url_openml = f'https://openml1.win.tue.nl/datasets/0000/{i}/dataset_{i}_croissant.json'
    print(url_openml)
    #https://openml1.win.tue.nl/datasets/0000/1464/dataset_1464_croissant.json
    directory = Path('OpenML_EU')
    directory.mkdir(parents=True, exist_ok=True)
    #dirpath = os.path.abspath('OpenML_EU')
    filename = 'dataset_'+str(i)+ '.jsonld'
    otput = os.path.join(directory, filename)
    print(otput)
    # Make a request to download the dataset
    response_openml = requests.get(url_openml)    # Check if the request was successful
    if response_openml.status_code == 200:
        # Save the content to a file
        with open(otput, 'wb') as file:
            file.write(response_openml.content)
        # print("Dataset downloaded successfully in Croissant format!")
    else:
        print("Error: Unable to download the dataset.")
        print("Status code:", response_openml.status_code)
