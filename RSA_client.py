import socket
from RSA_algorithm import get_rsa_keys
from RSA_algorithm import rsa_decrypt

p = 127
q = 137
e, d, n = get_rsa_keys(p,q)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 3030))
open_key = '{0} {1}'.format(e,n)
s.sendall(open_key.encode('utf-8'))

data = s.recv(1024)
print("Клиент. Зашифрованные данные, полученные от сервера: ", data.decode('utf-8'))
data = int(data)
data = rsa_decrypt(d,n,data)
print("Клиент. Расшифрованные данные от сервера: ", data)

s.close()
