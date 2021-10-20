import requests


class Address:
    street: str
    city: str
    state: str
    zip: int

# If you change __str__ to anything else it just shows the objects place in memory (location)
    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.state} {self.zip}"

        # The self parameter is used to represent the instance of the class


def main():
    r = requests.get("https://raw.githubusercontent.com/MrGallo/pbd-python/master/web-files/fake-addresses.txt")
    file_lines = r.text.split("\n")

    addresses = []
    for i in range(0, 18, 3):
        address = Address()
        address.street = file_lines[i]
        address.city   = file_lines[i + 1]
        address.state = file_lines[i + 2][:2]
        address.zip    = int(file_lines[i + 2][3:])
        addresses.append(address)

    for i in range(5):
        address = addresses[i]
        print(f"{i+1}. {address}")


if __name__ == "__main__":
    main()
