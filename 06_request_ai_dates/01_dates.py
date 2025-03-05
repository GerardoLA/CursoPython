# Trabajando con fechas y horas en Python

from datetime import datetime, timedelta

now = datetime.now()
print(f"Fecha y hora actual: {now}")

# Crear una fecha y hora especifica
specific_date = datetime(2025, 2, 12, 15, 30, 0)
print(f"Fecha y hora especifica: {specific_date}")

# Formatear fechas
# método strftime() para formatear fechas
# pasarle el objeto datetime y el formato especiufico
# Formato:

format_date = now.strftime("%d/%m/%y %H:%M:%S")
print(f"Fecha formateada: {format_date}")

# Operaciones con fechas (sumar/restar días, minutos, horas, meses)
yesterday = datetime.now() - timedelta(days=1)
print(f"Ayer: {yesterday}")

tomorrow = datetime.now() + timedelta(days=1)
print(f"Mañana: {tomorrow}")

one_hour_after = datetime.now() + timedelta(hours=1)
print(f"Una hora después: {one_hour_after}")

# 5 Obtener componentes individuales de una fecha
year = now.year
print(year)

month = now.month
print(month)

# 6.