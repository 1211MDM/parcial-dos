
cargo = input("Ingrese su cargo: ")

def calcular_bonificacion(nivel_directivo, bonificacion, desempeño,sueldo,total):

    if nivel_directivo == 'directivo':
       if desempeño == "alto":
           sueldo = 3000000
           bonificacion = sueldo * 0.20
           total = sueldo + bonificacion
       elif desempeño == "medio":
           sueldo = 2500000
           bonificacion = sueldo * 0.10
           total = sueldo + bonificacion
       else:
           print("Opcion Invalida")
    elif nivel_directivo == 'operativo':
        sueldo = 1750000
        if desempeño == 'alto':
            bonificacion = sueldo * 0.15
            total = sueldo + bonificacion
        elif desempeño == 'medio':
            bonificacion = sueldo * 0.05
            total = sueldo + bonificacion
        else:
            print("Opcion invalida")
    elif nivel_directivo == 'auxiliar':
        sueldo = 1300000
        if desempeño == 'alto':
            bonificacion = sueldo * 0.15
            total = sueldo + bonificacion
        elif desempeño == 'medio':
            bonificacion = sueldo * 0.05
            total = sueldo + bonificacion
        else:
            print("No hay bonificacion")
    else:
        print("Opcion invalida")
    return{
    sueldo,total,desempeño, bonificacion
    }
def generar_mensaje(cargo,desempeño,salario,total):
    print(f"-----Resumen de pago-----\n"
          f"Cargo: {cargo} \n"
          f"Nivel de desempeño: {desempeño} \n"
          f"Salario Base: {salario}\n"
          f"Total a recibir: {total}")
