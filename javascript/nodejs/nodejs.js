
var http = require('http');

function HtmlResponse(response, body) {    
    response.writeHead(200, [
        ['Content-Type', 'text/html'],
        ['Content-Length', Buffer.byteLength(body, 'utf8')]
    ]);
    response.write(body, 'utf8');
    response.end();
}

var server = http.createServer(function (request, response) {
    if (request.url == '/') {
        HtmlResponse(response, 'Hello <a href="./world">World</a>!');
    } else if (request.url == '/world') {
        HtmlResponse(response, '<a href="./">Hello</a> World!');
    }
});

var port = 8000;
server.listen(port);
console.log('Server running at http://127.0.0.1:'+port+'/');

