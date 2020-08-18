import requests
import json

#Login
response = requests.post('http://localhost:8000/token-auth/', data = {'username': 'luisg', 'password':'luis9325'})
r = json.loads(response.text)
token = r['access']

#Header with token
header = {'Authorization': 'Bearer '+token}

#Insert new user
new_user = {
    'username':'test',
    'first_name':'test',
    'last_name': 'test2',
    'address': 'Dirección de prueba',
    'country': 'México',
    'postal_code': '11100',
    'studies': 'Ingeniería',
    'occupation': 'Programador'
}
response = requests.post('http://localhost:8000/users/', data = new_user, headers = header)
user = json.loads(response.text)
print (response.text)

#Update the new user
new_user = {
    'address': 'Dirección de prueba actualizada',
}
response = requests.patch('http://localhost:8000/users/{}/'.format(user['id'],), data = new_user, headers = header)
user = json.loads(response.text)
print (response.text)

#Get all users
response = requests.get('http://localhost:8000/users/', headers=header)
users = json.loads(response.text)
print ("Listado de usuarios")
for user in users:
    print ('{} {}\nDirección: {}\nPaís: {}\nCP: {}\nEstudios: {}\nOcupación: {}\n'.format(
        user['first_name'],
        user['last_name'],
        user['address'],
        user['country'],
        user['postal_code'],
        user['studies'],
        user['occupation'],
    ))


#Delete the new user
response = requests.delete('http://localhost:8000/users/{}/'.format(user['id'],), headers = header)
print (response)