class Package:
    def __init__(self, number, sender, recipient, weight):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight



def main():
    # packages = ["Package 1: Alice to Bob, 10kg", "Package 2: Bob to Charlie, 5kg"]

    packages = [
        # Package(1, "Alice", "Bob", 10)
        Package(number=1, sender="Alice", recipient="Bob", weight=10)
        Package(number=2, sender="Bob", recipient="Charlie", weight=5)
    ]


main()
