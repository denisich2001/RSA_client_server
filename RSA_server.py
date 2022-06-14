import socket
from RSA_algorithm import rsa_encrypt

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 3030))
s.listen(1)
conn, addr = s.accept()

#ЧИСЛО КОТОРОЕ БУДЕМ ПЕРЕДАВАТЬ
data = 134
print("СЕРВЕР. Число, которое мы будем передавать: ", data)

while True:
    open_key = conn.recv(1024) # Получаем открытый ключ от клиента.
    open_key = open_key.decode('utf-8')
    if open_key:
        i=0
        print("СЕРВЕР. Полученный открытый ключ: ", open_key)
        e, n = map(int, open_key.split())
        encrypted_data = rsa_encrypt(e, n, data)
        print("СЕРВЕР. Зашифрованные данные: ", encrypted_data)
        conn.sendall(str(encrypted_data).encode('utf-8')) # Отправляем данные в сокет.
        break
conn.close()
