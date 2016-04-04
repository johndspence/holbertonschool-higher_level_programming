import urllib2
import json

"""Parses the json request with a loop from 0 to 29 on the index"""
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'

request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 3e0df28fcee55ed9d9bfbfda999ac5428e1ab96c'
}

req = urllib2.Request(url, headers=request_headers)

response = urllib2.urlopen(req)
the_page = response.read()
parsed_json = json.loads(the_page)

for i in range(0, 30):
    print(parsed_json['items'][i]['full_name'])
