import sys
from time import time

fib_count = 0


def fib(n):
    # Rekursiv
    global fib_count
    fib_count += 1

    # Default Fälle abdecken
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Bei Rest berechnen
    else:
        return fib(n - 1) + fib(n - 2)


def fib_it(n):
    # Iterativ
    fib1 = 0
    fib2 = 1
    for _ in range(0, n):
        fib1, fib2 = fib2, fib1 + fib2
    return fib1


def fib_calc(n):
    # Default Fälle abdecken
    if n == 0:
        return 1
    elif n == 1:
        return 1
    # Bei Rest berechnen
    else:
        return fib_calc(n - 1) + fib_calc(n - 2) + 1


def main():
    while True:
        global fib_count
        fib_count = 0

        while True:
            user_input = input("Welche Fibonacci-Zahl möchten Sie erhalten? (\"quit\" um zu beenden)")

            if user_input == "quit":
                sys.exit(0)

            try:
                user_input = int(user_input)
                break
            except ValueError:
                print("Bitte eine ganze Zahl, oder \"quit\" eingeben.")

        # Aufgabe 4 - Zeitberechnung
        start_time = time()
        fib_number = fib(user_input)
        end_time = time()

        print(">Die " + str(user_input) + "-te Fibonacci Zahl ist: " + str(fib_number))
        print(">Um die Zahl zu erhalten, wurde die fin(n)-Funktion " + str(fib_calc(user_input)) + "mal aufgerufen.")
        print("fib_counter als Check: " + str(fib_count) + ")")
        print(">Die Berechnung hat " + str((end_time - start_time)) + " Sekunden gedauert. (Rekursiv)")

        start_time2 = time()
        fib_number2 = fib_it(user_input)
        end_time2 = time()

        print(">Iterativ Berechnet, dauert es: " + str(end_time2 - start_time2) + " Sekunden.")
        print("Zahl: " + str(fib_number2))


if __name__ == '__main__':
    main()
