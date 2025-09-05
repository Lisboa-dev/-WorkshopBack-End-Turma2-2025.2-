class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Meu nome é {self.nome} e minha idade é {self.idade}"

    def falar(self):
        return "ANIMAIS FALAM"


class Gato(Animal):
    def __init__(self, nome, idade):
     super().__init__(nome, idade)
    def falar(self):
        return "Miau"


class Cachorro(Animal):
    def __init__(self, nome, idade):
     super().__init__(nome, idade)
    def falar(self):
        return "Au Au!"


def main():
    animais = [
        Gato("Felix", 3),
        Cachorro("Rex", 5)
    ]

    for animal in animais:
        print(animal.apresentar())
        print(animal.falar())


if __name__ == "__main__":
    main()
