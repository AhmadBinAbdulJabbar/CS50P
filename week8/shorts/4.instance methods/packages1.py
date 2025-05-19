class Package:
    ids = []
    def __init__(self, number, sender, recipient, weight):
        self.number = Package.check_number(number)
        self.sender = sender
        self.recipient = recipient
        self.weight = Package.check_weight(weight)


    @property
    def number(self):
        return self._number

    @property
    def sender(self):
        return self._sender

    @property
    def recipient(self):
        return self._recipient

    @property
    def weight(self):
        return self._weight

    @number.setter
    def number(self, number):

        self._number = number

    @sender.setter
    def sender(self, sender):
        self._sender = sender

    @recipient.setter
    def recipient(self, recipient):
        self._recipient = recipient

    @weight.setter
    def weight(self, weight):
        self._weight = weight

    @classmethod
    def check_number(cls, id):
        if id in cls.ids:
            raise ValueError("number id already exists")
        else:
            cls.ids.append(id)

        return id


    @classmethod
    def check_weight(cls, weight_value):
        if type(weight_value) is not int and type(weight_value) is not float:
            try:
                convert = float(weight_value)
            except:
                raise ValueError("weight value must be a number")
            else:
                return convert

        return weight_value

    def __str__(self):
        return f"Package {self.number}: {self.sender} to {self.recipient}, {self.weight}kg"

    def calcualte_cost(self, cost_per_kg):
        return self.weight * cost_per_kg


def main():
    packages = [
        Package(number=1, sender="Alice", recipient="Bob", weight=10),
        Package(number=2, sender="Bob", recipient="Charlie", weight="5")
    ]

    for package in packages:
        print(f"{package} costs ${package.calcualte_cost(cost_per_kg=2)}")

if __name__ == "__main__":
    main()
