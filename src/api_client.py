import requests
import logging

def get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    logging.info("Calling Users API")

    response = requests.get(url)

    if response.status_code != 200:
        logging.error(f"API failed with status {response.status_code}")
        raise Exception(f"API failed with status {response.status_code}")
    logging.info("API call successful")
    
    return response.json()