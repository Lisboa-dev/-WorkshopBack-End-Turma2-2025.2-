from exercicio5 import Animal, Gato, Cachorro

class Zoologico:
   def __init__(self):
      self.data=[]


   def adicionar_animal(self,animal):
      if isinstance(animal, Animal):
         self.data.append(animal)

   def listar_animais(self):
       Data={'list':[]}
       for animal in self.data:
          objeto={
            "nome":animal.nome,
            "idade": animal.idade,
            "sons": animal.falar()
          }

          Data['list'].append(objeto)
       return Data 
          
   def filtrar_por_tipo(self,tipo):
      Data=[]
      for animal in self.data:
         if isinstance(animal, tipo):
            Data.append(animal)
      return Data
   
 
def main():
    zoo = Zoologico()

    zoo.adicionar_animal(Gato("Felix", 3))
    print(zoo.listar_animais())
    print(zoo.filtrar_por_tipo(Gato))
if __name__ == "__main__":
  main()
  