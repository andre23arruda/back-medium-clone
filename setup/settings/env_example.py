# rename this file do env.py

import os, json, socket

def get_ip_address():
    '''Return IP adress'''
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_allowed_hosts():
    '''Create a list of alowed hosts'''
    hosts = [
        '127.0.0.1',
        'localhost',
        get_ip_address()
    ]
    return hosts


os.environ['SECRET_KEY'] = 'your key'
os.environ['DEBUG'] = 'true' #'true' # '' is False
os.environ['ALLOWED_HOSTS'] = json.dumps(get_allowed_hosts())
os.environ['BASE_URL'] = f'http://{ get_ip_address() }:8000'
os.environ['HEROKU_URL'] = 'https://andre23arruda-ch.herokuapp.com'
os.environ['LANGUAGE_CODE'] = 'pt-br'
os.environ['TIME_ZONE'] = 'America/Sao_Paulo'

os.environ['CLOUDINARY'] = '' # true is True / '' is False
os.environ['CLOUD_NAME'] = 'your-clod-name'
os.environ['API_KEY'] = 'your-api-key'
os.environ['API_SECRET'] = 'your-api-secret'