import requests
print("Version Requests : ")
print(requests.__version__)

res = requests.get('http://wwww.google.com/')
print(res)

res2 = requests.get('https://raw.githubusercontent.com/s-mag/Lab1/main/versions.py')
print(res2)
