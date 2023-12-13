import sys

def key_from_value(dict: dict, value):
    for key, val in dict.items():
        if val == value:
            return key
    return None

def print_state(value: str):

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver",
    }

    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO",
    }

    value = key_from_value(capital_cities, value)
    if not value:
        print("Unknown capital city")
        return
    print(key_from_value(states, value))


def main():
    if len(sys.argv) == 2:
        print_state(sys.argv[1])


if __name__ == '__main__':
    main()
