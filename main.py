import os
from dotenv import load_dotenv # pip install python-dotenv

load_dotenv() # path defaults to ".env"
# load_dotenv('./configs/config.env') # specific "./path/to/*.env"

secret_key = os.getenv('SECRET_KEY')

print(f'Your secret is here: {secret_key}')
