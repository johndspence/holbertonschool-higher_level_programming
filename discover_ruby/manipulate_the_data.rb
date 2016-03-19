require "HTTPClient"
require "net/http"
require "uri"
require "json"

extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 3e0df28fcee55ed9d9bfbfda999ac5428e1ab96c'
}

clnt = HTTPClient.new

# fname = "/tmp/44"
# somefile = File.open(fname, "w")
# somefile.puts clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc')
# somefile.close
# somefile = File.read("/tmp/44")

url = 'https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc'
uri = URI(url)
response = Net::HTTP.get(uri)
obj = JSON.parse(response)

puts obj['items'][0]['full_name']
puts obj['items'].map {|allitems| allitems['full_name']}
