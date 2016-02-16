var https = require('https');

var options = {
    hostname: 'api.github.com',
    path: '/search/repositories?q=language:javascript&sort=stars&order=desc',
    headers: {
  'User-Agent': 'Holberton_School',
  'Authorization': 'token 3e0df28fcee55ed9d9bfbfda999ac5428e1ab96c',
    }}

var callback1 = function(res) {
   streamToString(res, printToConsole  );
 } 

var req = https.request(options,callback1);

var printToConsole = function(x) {
    console.log("string");  
    console.log(x);
}

function streamToString(stream, cb) {
  const chunks = [];
  stream.on('data', (chunk) => {
    chunks.push(chunk);
  });
  stream.on('end', () => {
    cb(chunks.join(''));
  });
}

req.end();

req.on('error', function(e) {
  console.error(e);
});

var longString = function(jsonString){                   
    console.log(typeof jsonString);
    console.log(jsonString);
}