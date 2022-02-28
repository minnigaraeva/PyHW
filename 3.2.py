def user(name=0, surname=0, birth_year=0, city=0, email=0, ph_num=0):
    "Выводит данные"
    print(f'Name: {name}\nSurname: {surname}\nBirthdate: {birth_year}\nCity: {city}\nEmail: {email}\nPhone: {ph_num}')


user(input('Enter your name'), input('Surname'), input('Year of birth'), input('City of birth'), input('email'), input('Phone number'))
