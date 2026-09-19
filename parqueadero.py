"""
Sistema de Control de Acceso a un Parqueadero Universitario
-------------------------------------------------------------
Simula el registro de entrada de vehiculos durante un dia, calcula
tarifas segun el tipo de usuario, aplica descuentos y lleva estadisticas.

Restricciones respetadas:
- Sin funciones definidas por el usuario.
- Sin listas ni diccionarios.
- Sin POO.
- Usa while (con corte por cupos), if-elif-else anidado,
  operadores logicos (and/or/not) y conversion explicita de tipos.
"""

# ---------------------------------------------------------------
# Configuracion inicial
# ---------------------------------------------------------------
CUPOS_TOTALES = 30

N = int(input("Ingrese la cantidad de vehiculos a simular: "))

respuesta_sabado = input("¿Es sabado? (S/N): ")
es_sabado = (respuesta_sabado.upper() == "S")

# Acumuladores / estadisticas
contador_validos = 0
total_recaudado = 0.0
contador_estudiantes = 0
contador_docentes = 0
contador_visitantes = 0
suma_horas = 0.0

vehiculo_actual = 0

print("\n====== INICIO DEL REGISTRO ======\n")

# ---------------------------------------------------------------
# Ciclo principal: while con doble condicion de corte
# (vehiculos por procesar Y cupos disponibles)
# ---------------------------------------------------------------
while vehiculo_actual < N and contador_validos < CUPOS_TOTALES:

    vehiculo_actual += 1
    print(f"--- Vehiculo #{vehiculo_actual} ---")

    placa = input("Placa: ")
    tipo_usuario = input("Tipo de usuario (E=estudiante, D=docente, V=visitante): ")
    tipo_usuario = tipo_usuario.upper()

    hora_entrada = int(input("Hora de entrada (0-23): "))
    horas_permanencia = float(input("Horas que permanecera parqueado: "))

    # -------------------------------------------------------
    # Validaciones (operador logico en validacion combinada)
    # -------------------------------------------------------
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

        # -----------------------------------------------
        # Calculo de tarifa: if-elif-else anidado
        # -----------------------------------------------
        if tipo_usuario == "E":
            if horas_permanencia <= 2:
                tarifa = 0.0
            else:
                tarifa = (horas_permanencia - 2) * 800

        elif tipo_usuario == "D":
            tarifa = horas_permanencia * 500

        else:  # Visitante
            if es_sabado:
                precio_primera_hora = 1500 * 0.8
                precio_hora_adicional = 1200 * 0.8
            else:
                precio_primera_hora = 1500
                precio_hora_adicional = 1200

            if horas_permanencia <= 1:
                tarifa = precio_primera_hora
            else:
                tarifa = precio_primera_hora + (horas_permanencia - 1) * precio_hora_adicional

        # -----------------------------------------------
        # Descuento nocturno (no aplica el sabado, bonus)
        # -----------------------------------------------
        es_horario_nocturno = hora_entrada >= 19 or hora_entrada < 6
        if es_horario_nocturno and not es_sabado:
            tarifa = tarifa * 0.9

        tarifa = round(tarifa, 2)

        # -----------------------------------------------
        # Acumuladores de estadisticas
        # -----------------------------------------------
        contador_validos += 1
        total_recaudado += tarifa
        suma_horas += horas_permanencia

        if tipo_usuario == "E":
            contador_estudiantes += 1
        elif tipo_usuario == "D":
            contador_docentes += 1
        else:
            contador_visitantes += 1

        if advertencia_tipo:
            print(f"ADVERTENCIA: tipo de usuario invalido, tratado como visitante.")

        print(f"Registro OK -> Placa: {placa} | Tipo: {tipo_usuario} | "
              f"Cobro: ${tarifa}\n")

# ---------------------------------------------------------------
# Aviso de cupo lleno
# ---------------------------------------------------------------
if contador_validos == CUPOS_TOTALES:
    print("PARQUEADERO LLENO\n")

# ---------------------------------------------------------------
# Estadisticas finales
# ---------------------------------------------------------------
if contador_validos > 0:
    promedio_horas = suma_horas / contador_validos
else:
    promedio_horas = 0.0

ocupacion = (contador_validos / CUPOS_TOTALES) * 100

print("====== RESUMEN DEL DIA ======")
print(f"Vehiculos registrados: {contador_validos}/{CUPOS_TOTALES}")
print(f"Ocupacion: {round(ocupacion, 1)}%")
print(f"Recaudo total: ${round(total_recaudado, 2)}")
print(f"Estudiantes: {contador_estudiantes} | Docentes: {contador_docentes} | "
      f"Visitantes: {contador_visitantes}")
print(f"Promedio de permanencia: {round(promedio_horas, 1)} horas")
print("==============================")
