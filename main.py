import random
s = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
n = int(input('Введите длину вашело пароля: '))
m = ''
a = 'Нет'
while a == 'Нет':
    m = ''
    for i in range(n):
        m += s[random.randrange(len(s))]
    print(m)
    a = input('Вам нравиться ваш пароль?')
