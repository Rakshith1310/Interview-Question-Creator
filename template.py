import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='----%(asctime)s %(message)s----')
#logging.info("Hello world")

folder_template = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "app.py"
]

for folder in folder_template:
    filepath = Path(folder) #converts forward slashes to backslashes based on OS
    filedir, filename = os.path.split(filepath) #splits 'filepath' into directory and filename
    
    if (filedir != ""):
        os.makedirs(filedir, exist_ok=True) #creates directory only if it doesn't exist
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    if ((not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0)):
        logging.info(f"going here for the file: {filepath}")
        with open(filepath, "w") as f:
            logging.info(f"Created file: {filepath}")
            pass
            
    else:
        logging.info(f"File named {filepath} already exists.")