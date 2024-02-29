import os


def main():
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, {nombre} desde GitHub!")
    print("Hola mundo desde python")


if __name__ == "__main__":
    main()
