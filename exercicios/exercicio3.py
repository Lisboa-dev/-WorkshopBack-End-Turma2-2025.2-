
import math

class FiguraGeometrica():
  
 @staticmethod
 def areaTriangulo(base=float, altura=float):
   return (base*altura)/2
 @staticmethod
 def hipotenusa(cateto1:float, cateto2:float):
   return pow(cateto1,2)*pow(cateto2,2)
   
 @staticmethod
 def areaCirculo(raio: float)->float:
   return math.pi*math.pow(raio, 2)
   
 
 def menu():
   num=1
   while(num==1):
     num=int(input("insira qual operação que fazer\n\n insira a numeração da lista: \n\n 1-area de um triangulo retangulo;\n 2- area de um sirculo\n 3- uma hipotenusa \n 4- sair do loop"))
     figura= FiguraGeometrica
     match (num):
       case 1:
   
        base =float(input("insira um valor real da base do triangulo"))
        altura =float(input("insira um valor real da altura do triangulo"))
        
        valor=figura.areaTriangulo(base, altura)
        print(f"a hipotenusa é {valor}")
       case 2:
         raio=float(input("insira um raio"))
         
         valor=figura.areaCirculo(raio)
         print(f"a hipotenusa é {valor}")
       case 3:
          cateto1 = float(input("insira o cateto 1"))
          cateto2 = float(input("insira o cateto 2"))

          valor=figura.hipotenusa(cateto1, cateto2)
          print(f"a hipotenusa é {valor}")
       case 4:
          num==0
       case _:
         print("valor inserido não se encontra nas opções")
