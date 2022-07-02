import requests

Youtube_trending_url="https://www.youtube.com/feed/trending"

response=requests.get(Youtube_trending_url)

print('Status Code:',response.status_code)
print(len(response.text))

with open ('trending.html','w') as file:
  file.write(response.text)