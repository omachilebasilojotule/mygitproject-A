import requests
import os
from urllib.parse import urlparse
import uuid

def fetch_image():
    url = input("Enter the image URL:").strip()
    #create directory folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        parsed_url=urlparse(url)
        filename =os.path.basename(parsed_url.path)
        if not filename or '.' not in filename:
            filename= f"image_{uuid.uuid4().hex}.jpg"
            filepath =os.path.join(folder, filename)
            with
    open(filepath, "wb") as file:
file.write(response.content)
print(f"image save as: {filepath}")
except
requests.exceptions.RequestException as e:
print("failed to fetch image.")
print(f"error: {e}")
if __name__=="_main_":
    fetch_image()