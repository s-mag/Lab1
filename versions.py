import requests
print("Version Requests : ")
print(requests.__version__)

res = requests.get('http://wwww.google.com/')
print(res)
