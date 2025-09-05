def raizQuadrada(num: int):
 if num!=0 and num>0:
  return(num)
 return ("erro: number invalido")

def calculatorRaiz():
 num=1
 while num:
    num = int(input("insira um numero inteiro"))
    num = raizQuadrada(num)

    if num and isinstance(num, str):
        print(num)
        return(num)
    
    print(f"o resultado é{num}")
    return(num)

