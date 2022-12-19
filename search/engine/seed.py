from .models import *

from faker import Faker
fake=Faker()

def seed_db(n):
    for i in range (0,n):

        Searchname.objects.create(name=fake.name())
