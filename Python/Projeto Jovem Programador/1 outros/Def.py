



def is_prime(number):
    c = 0
    for i in range(1,number+1):
        if number % i == 0:
            c += 1
        if c > 2:
            print('Não e primo')
            return False
    if c == 2:
        print('È primo')
        return True
    
while True:
    r = int(input('Digite um numero: '))
    print(is_prime(r))
    if r == 0:
        break






