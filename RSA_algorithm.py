def is_prime(n):
    '''
    Проверяем является ли число простым
    '''
    for i in range(2,int(n/2)):
        if n%i==0:
            return False
    return True


def vzaimno_prost(a,b):
    '''
    Проверяем являются ли числа взаимно простыми
    '''
    for i in range(2,int(a/2)):
        if a%i == 0 and b%i == 0:
            return False
    return True


def get_rsa_keys(p,q):
    '''
    Вычисляем пары открытого и закрытого ключей
    '''
    n = p*q
    phi = (p-1)*(q-1)

    #Выбираем открытую экспоненту для открытого ключа
    open_exponent = -1
    for a in range(phi-1, 0, -1):
        if is_prime(a) and vzaimno_prost(a,phi)!=0:
            open_exponent = a
            break
    e = open_exponent

    #Вычисляем закрытый ключ
    d = -1
    for i in range(3,1000000):
        if (i*e)%phi==1:
            d = i
            break

    return e,d,n


def rsa_encrypt(e,n,data):
    '''
    Шифруем данные
    '''
    return (data**e)%n

def rsa_decrypt(d,n,data):
    '''
    Расшифровываем данные
    '''
    return (data**d)%n
