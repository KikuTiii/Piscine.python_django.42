def read_file():
    try:
        with open("Piscine.python_django.42/D01/numbers.txt", "r") as f:
            lines = f.readlines()
            print_line(lines)
    except FileNotFoundError:
        print("Erro: O arquivo 'numbers.txt' não foi encontrado.")


def print_line(lines):
    for line in lines:
        elements = line.strip().split(",")
        print('\n'.join(elements))


if __name__ == '__main__':
    read_file()
