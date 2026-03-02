Pepol = {"Pancho", "Juan", "Pedro", "Maria", "Ana"}

entr = input("Quien esta ingresado a trabajar hoy?: ")

if entr in Pepol:
    print(f"Bienvenido al trabajo {entr}")
else:
    print(f"{entr}, vos no sos de estas tierras")