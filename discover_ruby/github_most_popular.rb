require "HTTPClient"
require "net/http"
require "uri"

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 3e0df28fcee55ed9d9bfbfda999ac5428e1ab96c'
}


clnt = HTTPClient.new

puts clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc')
