for num in range(10, 56):
    contador = 0
    for div in range(2, num-1):
        if num % div == 0:
            contador += 1

    if contador > 0:
        print(end=" ")
    else:
        print(num,end=" ")