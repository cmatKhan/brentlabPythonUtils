# standard library
import requests
import json
from urllib.request import HTTPError
import sys
import re
import time
import os
# third party
import numpy as np
import pandas as pd

def postNewFastqSheet(fastq_sheet_path, fastq_url):
    """
    
    """
    fastq_sheet = pd.read_excel(fastq_sheet_path)
    for index, row in fastq_sheet.iterrows():
        data = row.to_dict()
        keys_to_delete = []
        for key, value in data.items():
            if key == "readsObtained":
                try:
                    value = value.replace(",","")
                    data[key] = int(value)
                except Exception as e:
                    print(key + " : %s" %str(value))
            if isinstance(value, np.integer):
                data[key] = int(value)
            if isinstance(value, np.float):
                data[key] = float(value)
            if key == "runNumber":
                try:
                    data[key] = str(int(value))
                except ValueError:
                    data[key] = ""
            if key == "tapestationConc":
                data[key] = float(value)
            if key == "volumePooled":
                data[key] = float(value)
            if not type(value) == str:
                try:
                    if np.isnan(float(value)):
                        keys_to_delete.append(key)
                except:
                    sys.exit(row_dict)
        for key in keys_to_delete:
            del data[key]
        try:
            r = requests.post(fastq_url, data = data)
            r.raise_for_status()
            print(r.reason)
        except HTTPError:
            print("error:  %s with:  %s " %(r.reason, data))