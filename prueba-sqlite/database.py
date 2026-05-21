import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

db_name = os.getenv("DB_NAME")
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# insertar datos a la bd
productos = [
    ("Blusa", 500, 100),
    ("Pantalón",  300, 50),
    ("Camisa",   200, 75),
    ("Buzo",     450, 30),
]
cursor.executemany("""
    INSERT INTO stock (nombre, precio, cantidad)
    VALUES (?, ?, ?)
""", productos)

conn.commit()
print("Datos insertados correctamente")

# vista de los datos desde la terminal
cursor.execute("SELECT * FROM stock")
for fila in cursor.fetchall():
    print(fila)

conn.close()