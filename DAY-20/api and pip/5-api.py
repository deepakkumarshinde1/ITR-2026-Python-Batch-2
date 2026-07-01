import requests

# we pip => package manager for python
# pip => Preferred installer program.

# install , delete , update

# api
url = 'https://jsonplaceholder.typicode.com/comments'
response = requests.get(url)

# requests.post()
# requests.put()
# requests.delete()
# print(response.status_code)
data = response.json()
print(len(data))

