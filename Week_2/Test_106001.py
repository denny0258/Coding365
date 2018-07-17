import abc
class part:
    @abc.abstractmethod
    def name(self):
        return NotImplemented

    @abc.abstractmethod
    def price(self):
        return NotImplemented


class CPU(part):
    def name(self):
        return "CPU"

    def price(self):
        return 50


class RAM(part):
    def name(self):
        return "RAM"

    def price(self):
        return 20


class HD(part):
    def name(self):
        return "HD"

    def price(self):
        return 70


class Register:
    def __init__(self):
        self.List_ALL = []

    def ADD(self, part):
        self.List_ALL.append(part)

    def Print_Price(self):
        total = 0
        for i in self.List_ALL:
            total += i.price()
        print("total:", total)


def main():
    Reg = Register()
    Reg.ADD(HD())
    Reg.ADD(RAM())
    Reg.ADD(CPU())

    Reg.Print_Price()


if __name__ == "__main__":
    main()
