#!/usr/bin/ruby

require "HTTPClient"
require "net/http"
require "uri"
require "json"

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 3e0df28fcee55ed9d9bfbfda999ac5428e1ab96c'
}

clnt = HTTPClient.new

url = 'https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc'
uri = URI(url)
response = Net::HTTP.get(uri)
obj = JSON.parse(response)

puts obj['items'][0]['full_name']
puts obj['items'].map {|allitems| allitems['full_name']}
