"""
Sistema de Control de Acceso a un Parqueadero Universitario
-------------------------------------------------------------
CUPOS_TOTALES = 30

N = int(input("Ingrese la cantidad de vehiculos a simular: "))

respuesta_sabado = input("¿Es sabado? (S/N): ")
es_sabado = (respuesta_sabado.upper() == "S")

contador_validos = 0
total_recaudado = 0.0
contador_estudiantes = 0
contador_docentes = 0
contador_visitantes = 0
suma_horas = 0.0

vehiculo_actual = 0

print("\n====== INICIO DEL REGISTRO ======\n")

while vehiculo_actual < N and contador_validos < CUPOS_TOTALES:

    vehiculo_actual += 1
    print(f"--- Vehiculo #{vehiculo_actual} ---")

    placa = input("Placa: ")
    tipo_usuario = input("Tipo de usuario (E=estudiante, D=docente, V=visitante): ")
    tipo_usuario = tipo_usuario.upper()

    hora_entrada = int(input("Hora de entrada (0-23): "))
    horas_permanencia = float(input("Horas que permanecera parqueado: "))

    if hora_entrada < 0 or hora_entrada > 23:
        print(f"ERROR: hora de entrada invalida ({hora_entrada}). "
              f"Vehiculo {placa} NO se contabiliza.\n")

    elif horas_permanencia <= 0:
        print(f"ERROR: horas de permanencia invalidas ({horas_permanencia}). "
              f"Registro de {placa} rechazado.\n")

    else:
        advertencia_tipo = False
        if tipo_usuario != "E" and tipo_usuario != "D" and tipo_usuario != "V":
            tipo_usuario = "V"
            advertencia_tipo = True

        if tipo_usuario == "E":
            if horas_permanencia <= 2:
                tarifa = 0.0
            else:
                tarifa = (horas_permanencia - 2) * 800

        elif tipo_usuario == "D":
            tarifa = horas_permanencia * 500

        else:
            if es_sabado:
                precio_primera_hora = 1500 * 0.8
                precio_hora_adicional = 1200 * 0.8
            else:
                precio_primera_hora = 1500
                precio_hora_adicional = 1200
1s
