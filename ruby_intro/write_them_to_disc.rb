#!/usr/bin/ruby

require "HTTPClient"
require "net/http"


extheaders = {
  'User-Agent' => 'Holberton_School',
  'Authorization' => 'token 3e0df28fcee55ed9d9bfbfda999ac5428e1ab96c'
}

clnt = HTTPClient.new

fname = "/tmp/44"
somefile = File.open(fname, "w")
somefile.puts clnt.get_content('https://api.github.com/search/repositories?q=language:ruby&sort=stars&order=desc')
somefile.close

puts "The file was saved!"
