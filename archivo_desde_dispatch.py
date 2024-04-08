import os


def main():
    nombre = os.getenv("NOMBRE")
    edad = os.getenv("EDAD")
    print(f"¡Hola, {nombre} con la edad en categoria {edad}")

if __name__ == "__main__":
    main()
