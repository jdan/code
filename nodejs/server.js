var http = require('http');
var url  = require('url');

function start() {
    function onRequest(request, response) {
        var pathname = url.parse(request.url).pathname;
        console.log("Request for " + pathname + " received.");
        response.writeHead(200, {'Content-Type': 'text/plain'});
        response.end('Hello World\n');
    }
    
    http.createServer(onRequest).listen(8888);
    console.log('Server started on port 8888');
}

exports.start = start;
