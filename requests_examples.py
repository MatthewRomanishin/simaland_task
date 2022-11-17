import requests

# LOGIN ###
query = {
    'login':'matthew',
    'password':'matthew'

}
response = requests.post("http://localhost:8080/login", params=query)
print(response.text)

### ADD USER ###
# query = {
#     'name':'Matthew',
#     'surname':'Romanishin',
#     'login':'matthew',
#     'password':'matthew',
#     'date_of_birth':'1998-09-15',
#     'permission':'readonly',
#     'token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6ImFkbWluIiwidXNlcl9pZCI6IjAiLCJwZXJtaXNzaW9uIjoiVHJ1ZSJ9.kub_TA2WGLKGYCviug0YInsxNHCluWAOoCjWWquiVfs'
# }
# response = requests.post("http://localhost:8080/create", params=query)
# print(response.text)

### DELETE USER ###
# query = {
#     'login_to_delete':'matthew_admin',
#     'token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6Im1hdHRoZXdfYWRtaW4iLCJ1c2VyX2lkIjoiMSIsInBlcm1pc3Npb24iOiJUcnVlIn0.9NITbAyWJBHmjHIEG5CjD7PbvdcymFUghOTB4DrCdpk'
# }

# response = requests.delete("http://localhost:8080/delete", params=query)
# print(response.text)

### READ ###

# query = {
#     'token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6ImFkbWluIiwidXNlcl9pZCI6IjAiLCJwZXJtaXNzaW9uIjoiVHJ1ZSJ9.kub_TA2WGLKGYCviug0YInsxNHCluWAOoCjWWquiVfs'
# }

# response = requests.get("http://localhost:8080/read", params=query)
# print(response.text)

### UPDATE ###

# query = {
#     'login_to_update':'matthew',
#     'password':'21358413',
#     'name':'mat',
#     'token':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbiI6ImFkbWluIiwidXNlcl9pZCI6IjAiLCJwZXJtaXNzaW9uIjoiVHJ1ZSJ9.kub_TA2WGLKGYCviug0YInsxNHCluWAOoCjWWquiVfs'
# }

# response = requests.put("http://localhost:8080/update", params=query)




