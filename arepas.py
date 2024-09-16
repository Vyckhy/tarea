# Solicitar al usuario la cantidad de ingredientes
harina_str = input("Ingrese la cantidad de harina (en gramos): ")
agua_str = input("Ingrese la cantidad de agua (en mililitros): ")
sal_str = input("Ingrese la cantidad de sal (en gramos): ")
aceite_str = input("Ingrese la cantidad de aceite (en mililitros): ")

# Convertir las entradas a enteros
harina = int(harina_str)
agua = int(agua_str)
sal = int(sal_str)
aceite = int(aceite_str)

# Calcular la masa de la mezcla (bol)
bol = harina + agua + sal

# Calcular la masa total en el budare
budare = bol + aceite

# Mostrar los resultados
print(f"La cantidad total de la mezcla (bol) es: {bol} gramos.")
print(f"La cantidad total en el budare es: {budare} gramos.")
Vyckhy Sarmiento 32245067