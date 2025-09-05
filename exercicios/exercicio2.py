import math 

def arredondador(num: float):

 if num and isinstance(num,float):
    floor = math.floor(num)
    ceil = math.ceil(num)
    round_result=round(num)
 
 if floor  and ceil and round_result:
   return(f"o arredondo para cima é {floor}\n o arredondamento para baixo é {ceil}\n o arredondamento para o mais proximo é {round_result}\n")
 else:
   return(f"o valor {num} nao é valido")