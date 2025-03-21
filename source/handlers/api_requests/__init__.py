import requests
import json
from loguru import logger



def sites_analysis(**kwargs):
    url = 'http://api_app:5000/sites'
    response = requests.post(url, data=kwargs)
    data = None
    
    logger.info(response.text)
    if response.text != None:
        data = json.loads(response.text)
    else:
        return None
        
    return data


def article_analysis(**kwargs):
    url = 'http://api_app:5000/article'
    response = requests.post(url, data=kwargs)
    data = None
    
    logger.info(response.text)
    if response.text != None:
        data = json.loads(response.text)
    else:
        return None
        
    return data
    
    
def url_analysis(**kwargs):
    url = 'http://api_app:5000/url'
    response = requests.post(url, data=kwargs)
    data = None
    
    logger.info(response.text)
    if response.text != None:
        data = json.loads(response.text)
    else:
        return None
        
    return data


def telegram_channels(**kwargs):
    url = 'http://api_app:5000/telegram_channels'
    response = requests.post(url, data=kwargs)
    data = None
    
    logger.info(response.text)
    if response.text != None:
        data = json.loads(response.text)
    else:
        return None

    return data


def get_user(**kwargs):
    url = 'http://api_app:5000/get_user'
    response = requests.post(url, data=kwargs)
    data = None
    
    logger.info(response.text)
    if response.text != None:
        data = json.loads(response.text)
    else:
        return None
        
    return data


def add_new_user(**kwargs):
    url = 'http://api_app:5000/add_new_user'
    response = requests.post(url, data=kwargs)
    data = None
    
    logger.info(response.text)
    if response.text != None:
        data = json.loads(response.text)
    else:
        return None
        
    return data


def set_user_language(**kwargs):
    url = 'http://api_app:5000/set_user_language'
    response = requests.post(url, data=kwargs)
    data = None
    
    logger.info(response.text)
    if response.text != None:
        data = json.loads(response.text)
    else:
        return None
        
    return data


def add_new_domain(**kwargs):
    url = 'http://api_app:5000/add_new_domain'
    response = requests.post(url, data=kwargs)
    data = None

    logger.info(response.text)
    if response.text != None:
        data = json.loads(response.text)
    else:
        return None
        
    return data



def site_trust_feedback(**kwargs):
    url = 'http://api_app:5000/site_trust_feedback'
    response = requests.post(url, data=kwargs)
    data = None
    
    logger.info(response.text)
    if response.text != None:
        data = json.loads(response.text)
    else:
        return None
        
    return data



def get_domain(**kwargs):
    url = 'http://api_app:5000/get_domain'
    response = requests.post(url, data=kwargs)
    data = None
    
    logger.info(response.text)
    if response.text != None:
        data = json.loads(response.text)
    else:
        return None
        
    return data



def add_new_request(**kwargs):
    url = 'http://api_app:5000/add_new_request'
    response = requests.post(url, data=kwargs)
    data = None
    
    logger.info(response.text)
    if response.text != None:
        data = json.loads(response.text)
    else:
        return None
        
    return data



def get_requests(**kwargs):
    url = 'http://api_app:5000/get_requests'
    response = requests.get(url, data=kwargs)
    data = None
    
    logger.info(response.text)
    if response.text != None:
        data = json.loads(response.text)
    else:
        return None
        
    return data


def count_requests_last_month(**kwargs):
    url = 'http://api_app:5000/count_requests_last_month'
    response = requests.get(url, data=kwargs)
    data = None
    
    logger.info(response.text)
    if response.text != None:
        data = json.loads(response.text)
    else:
        return None
        
    return data