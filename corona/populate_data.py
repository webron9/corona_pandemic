import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','corona.settings')

import django
django.setup()

import requests
import random
from bs4 import BeautifulSoup
from my_app.models import Leacher
from faker import Faker

fake = Faker()
locations = ['bhokar','nanded','udgir','pune','mumbai','delhi','nagpur','patna','hyderabad','bangalore']

def populate(n=10):
    for i in range(n):
        fake_name = fake.name()
        fake_address = fake.address()
        
        l = Leacher.objects.get_or_create(name=fake_name,address=fake_address,location=random.choice(locations))[0]
        l.save()
    
if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(100)
    print('Populating Complete')

