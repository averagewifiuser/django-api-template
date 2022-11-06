### helper functions
import os
from dotenv import load_dotenv

load_dotenv()

def is_in_development(): #temporal to check if hosted on heroku or not
    return os.getenv('DEV_ENV', 'Production').startswith('Development')