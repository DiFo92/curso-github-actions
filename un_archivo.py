import os
from datetime import datetime


def main():
    nombre = os.getenv("USERNAME") | "DiFo"
    print(f"¡Hola, {nombre} desde GitHub!")
    print("Hola mundo desde python actualizado en: ")
    print(datetime.now())


if __name__ == "__main__":
    main()
