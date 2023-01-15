
from faker import Faker
fake = Faker()

#print(dir(fake))
print(type(fake))

for _ in range(10):
  print(fake.name())

print()
test_variable = fake.name()
print(test_variable)
 
#faker = BusinessCard(imie = fake.name(), nazwisko =fake.name(), nazwa_firmy=fake.company(), stanowisko =fake.job(), adres_email= fake.email())

#from faker import Faker
#fake = Faker()

from datetime import date

today = date.today()
print("Today's date:", today)