def horario(h, m):

    if 0 <= h <= 12:
        h = h + 12
        if h == 24:
            h = 0
        print(f"sao {h}:{m} P.M")
    elif 12 <= h < 24:
        h = h - 12
        print(f"sao {h}:{m} A.M")


def end():
    from time import sleep
    while True:
        hora = int(input("digite a hora: "))
        if hora < 0:
            break
        minutos = int(input("digite os min: "))
        print('-'*22)
        print("CONVERTENDO O HORÁRIO")
        print('-' * 22)
        sleep(1.5)
        horario(hora, minutos)


end()