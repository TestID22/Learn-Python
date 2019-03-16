import socket 

URLS = {
    '/':'Lena I love you <3',
    '/blog':'hello blog'
}

def parse_request(request):
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]
    return(method, url)

def generate_headers(method, url):
    if not method == 'GET':
        return('HTTP/1.1 405 Method not allowed\n\n', 405)
    
    if not url in URLS:
        return ('HTTP/1.1 404 Not Found\n\n', 404)
    
    return('HTTP/1.1 200 OK\n\n', 200)

def generate_content(code, url):
    if code == 404:
        return '<h1>404</h1><p>Not Found it</p>'
    if code == 405:
        return '<h1>405</h1><p>Method nor allowed</p>' 
    return '<h1>{}</h1>'.format(URLS[url])   

def generate_response(requset):
    method, url = parse_request(requset)
    headers, code = generate_headers(method, url)
    body = generate_content(code, url)
    return (headers + body).encode()

def run():
    #субъект кто принимает ADRESS FAMILY INET - протокол v4 (12.11.11.11)
    #Cоздаём объект сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    #слушаем порт на вхождение пакетов
    server_socket.listen()
    
    while True:
        #accept вернёт сокет клиента
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        #декодируем ответ в utf-8 это даст нам удобочитаемость
        print(request.decode('utf-8'))
        print()
        print()
        print(request)
        print(addr)
        response = generate_response(request.decode('utf-8'))
        #отправим на клиента строку encode в байтах
        client_socket.sendall(response)
        client_socket.close()

        


if __name__ == '__main__':
    run()