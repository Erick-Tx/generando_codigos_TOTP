import random
import time
import csv

def generar_codigo(codigos_generados):
    while True:
        codigo = ''.join(str(random.randint(0, 9)) for _ in range(6))
        if codigo not in codigos_generados:
            codigos_generados.add(codigo)
            return codigo

tiempo_limite = 30  # segundos
inicio_tiempo = time.time()
contador = 0  # Inicializar el contador
codigos_generados = set()

while time.time() - inicio_tiempo < tiempo_limite:
    contador += 1
    codigo = generar_codigo(codigos_generados)
    print(f'{contador} Código generado: {codigo}')
    #time.sleep(0.1)  # Reducido a 0.1 segundos

# Guardar los códigos en un archivo CSV
nombre_archivo = 'codigos_generados_no_repetidos.csv'
campos = ['Número', 'Código']
codigos = [{'Número': i+1, 'Código': codigo} for i, codigo in enumerate(codigos_generados)]

with open(nombre_archivo, 'w', newline='') as archivo_csv:
    escritor_csv = csv.DictWriter(archivo_csv, fieldnames=campos)
    
    # Escribir la cabecera
    escritor_csv.writeheader()
    
    # Escribir los datos
    for codigo in codigos:
        escritor_csv.writerow(codigo)

print(f"Fin del programa. Total de códigos generados: {contador}")
print(f"Los códigos únicos han sido guardados en el archivo '{nombre_archivo}'")
