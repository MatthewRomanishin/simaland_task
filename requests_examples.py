import requests

# ### LOGIN ###
query = {
    'login':'matthew1',
    'password':'matthew'

}
response = requests.post("http://localhost:8080/login", params=query)
print(response.text)

## ПОСЛЕ АВТОРИЗАЦИИ ПОЛУЧЕННЫЙ ТОКЕН ЗАПИСАТЬ В ПЕРЕМЕННУЮ "token"

token = 'ВАШ ТОКЕН'
#---------------------------------------------------------------------------#

### CREATE USER ###
# query = {
#     'name':'Matthew',
#     'surname':'Romanishin',
#     'login':'matthew1',
#     'password':'matthew',
#     'date_of_birth':'1998-09-15',
#     'permission':'readonly', 
#     'token':token
# }
# response = requests.post("http://localhost:8080/create", params=query)
# print(response.text)

#---------------------------------------------------------------------------#

# ### READ ###

# query = {
#     'token':token
# }

# response = requests.get("http://localhost:8080/read", params=query)
# print(response.text)

#---------------------------------------------------------------------------#

# ### UPDATE ###

# query = {
#     'login_to_update':'matthew',
#     'password':'21358413',
#     'name':'mat',
#     'token':token
# }

# response = requests.put("http://localhost:8080/update", params=query)
# print(response.text)

#---------------------------------------------------------------------------#

# ### DELETE USER ###
# query = {
#     'login_to_delete':'matthew',
#     'token':token
# }

# response = requests.delete("http://localhost:8080/delete", params=query)
# print(response.text)








