import requests
from loguru import logger


kwargs={'email': 'web_user@gmail.com', 'password': 'strongpassword', 'lang': 'ua'}

url = 'http://api_app:5000/add_new_user'
response = requests.post(url, data=kwargs)
logger.info(response.text)