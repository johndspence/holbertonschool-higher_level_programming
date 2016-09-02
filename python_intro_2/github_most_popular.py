import urllib2

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc'

"""Prints standard url request to standard output"""
request_headers = {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 3e0df28fcee55ed9d9bfbfda999ac5428e1ab96c'
}

req = urllib2.Request(url, headers=request_headers)
response = urllib2.urlopen(req)
the_page = response.read()
print the_page
