temperatura = int(input("ingrese temperatura:"))
escala = input("Celcius(c) o  Farenheid(f):").lower()
if escala == "c":
     print((temperatura - 32) / 1.8)
elif escala == "f":
     print((temperatura + 32) * 1.8)
else :
     print("escala no existe")