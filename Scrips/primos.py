import argparse

parser = argparse.ArgumentParser()
parser.add_argument("n", type=int)

args = parser.parse_args()
n = args.n

if n <= 0: 
    print("Ingrese un numero Natural")
elif n <= 2:
    print(f"El {n} es primo")
else:
    escompuesto = False
    divisor = 2
    while divisor < n:  # Cambiado de <= a <
        if n % divisor == 0:
            escompuesto = True
            break
        divisor += 1
    if not escompuesto:
        print(f"El {n} es primo")
    else:
        print(
            f"El {n} es compuesto.\nSe cumple que {divisor}*{int(n/divisor)}={n}"
        )