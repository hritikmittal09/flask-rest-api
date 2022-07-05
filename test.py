import requests
base = "http://127.0.0.1:5000/"
reespone = requests.get(base+"books")
reespone2 = requests.post(base+'/createbook 3 java')
print(reespone.json())
input()