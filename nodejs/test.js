http = require('http')
url  = require('url')

onRequest = (request, response) ->
    pathname = url.parse(request.url).pathname
    console.log "Request for " + pathname + " received."
    
    response.writeHead 200, {"Content-Type": "text/html"}
    response.write 'Hello, World!'
    response.end();

http.createServer(onRequest).listen 8888
console.log 'Server started on port 8888'
