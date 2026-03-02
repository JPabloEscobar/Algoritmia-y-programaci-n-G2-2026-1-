ban = {"Cuchillos", "Armas", "Drogas"}

i = "Cuchillos"

if i in ban:
    print(f"El item {i} está prohibido")
# else:
#     print(f"{i}, vos no sos de estas tierras")

elif i not in ban:
    print("Ahora si pase")