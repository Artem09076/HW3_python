n = int(input())

morse_tuz = '0'

while len(morse_tuz) < n: #Генерация нулей и единиц пока не будет равнятся n

    for symbol in morse_tuz:  #Мы перебираем в значении morse_tuz

        if symbol == '0': #если 0, то добавляется 1

            morse_tuz += '1'

        else:

            morse_tuz += '0' 

print(morse_tuz[:n]) #Удаляем последний фрагмент