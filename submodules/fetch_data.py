# this is a template file for a fetch data function
# USAGE notebook
# from submodules.fetch import fetch_data()
# fetch_data()

import os
import zipfile
import urllib.request

# URL that hosts the data
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/<repo>"
# full path to the archive file
DATASET_URL = DOWNLOAD_ROOT + "datasets/sepsis/archive.zip"
# local file path
DATASET_PATH = os.path.join("datasets", "sepsis")

# function to fetch data
def fetch_data(url=DATASET_URL, path=DATASET_PATH):
    # if ./datasets/sepsis doesn't exists, create it
    if not os.path.isdir(path):
        os.makedirs(path)
    # join the ./datasets/sepsis/archive.zip
    tgz_path = os.path.join(path, "archive.zip")
    # retrieve and save the archive file from https://raw.githubusercontent.com/<repo>/datasets/sepsis/archive.zip
    urllib.request.urlretrieve(url, tgz_path)
    # Create a ZipFile Object and load it
    with zipfile.ZipFile(tgz_path, 'r') as zipObj:
        # Extract all the contents of zip file in current directory
        zipObj.extractall()