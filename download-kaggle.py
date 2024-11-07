# -*- coding: utf-8 -*-

import requests
import pandas as pd
import numpy as np
import requests
import logging
import json
from pathlib import Path
import os, sys, re, math
import base64

import kaggle

kaggle.api.authenticate()

#tag_ids = [ "diseases" ]

tagids = "diseases"
dset_range = 500
pages = math.ceil(dset_range/20)

urls_kgl = []
jsonld_kgl = []

for p in range(pages):
    datasets = kaggle.api.dataset_list(page=p+1, tag_ids=tagids)
    for dset in datasets:
        url_kgl = f'https://www.kaggle.com/datasets/{dset}/croissant/download'
        urls_kgl.append(url_kgl)
        
for ukgl in urls_kgl:
#    print(ukgl)
    response_kgl = requests.get(ukgl)
    try:
        x = response_kgl.json()
        jsonld_kgl.append(x)
    except Exception:
        pass
print(json.dumps(jsonld_kgl, indent=4))

sys.exit(0)

