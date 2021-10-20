import requests


class Address:
    street: str
    city: str
    state: str
    zip: int


def main():
    r = requests.get("https://raw.githubusercontent.com/MrGallo/pbd-python/master/web-files/fake-addresses.txt")
    file_lines = r.text.split("\n")

    addresses = []
    if len(file_lines) <= 18:
        for i in range(0, 18, 3):
            address = Address()
            address.street = file_lines[i]
            address.city   = file_lines[i + 1]
            address.state = file_lines[i + 2][:2]
            address.zip    = int(file_lines[i + 2][3:])
            addresses.append(address)

    if len(file_lines) <= 18:
        for i in range(6):
            address = addresses[i]
            print(f"{address.street}, {address.city}, {address.state} {address.zip}")


if __name__ == "__main__":
    main()
