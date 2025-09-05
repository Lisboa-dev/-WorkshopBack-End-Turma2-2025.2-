
class Animal():
    def falar(self):
      return("o animal faz algum som")
      
class gato(Animal):
  def falar(self):
     return "Miau!"

class cachorro(Animal):
  def falar(self):
    return "AUAU!"

def main():
  animais = [gato(), cachorro()]

  for animal in animais:
    print (animal.falar())

if __name__ == "__main__":
  main()
  
