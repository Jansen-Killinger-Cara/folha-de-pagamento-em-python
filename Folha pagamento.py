#Desenvolvido em aula em 18/08/2023 por Jansen K Cara
#Calculando o valor do salário descontando o INSS e o Vale Transporte

import math

salarioB = float(input("Digite o salário: "))
vale =  input("Descontar o Vale Transporte? ")
if salarioB <1302.00:
    inss = salarioB*0.075
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)
    print ("Seu salário liquído é de: R$", salarioL)
elif salarioB <2571.29:
    inss = salarioB*0.09
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)
    print ("Seu salário liquído é de: R$", salarioL)
elif salarioB <3856.94:
    inss = salarioB*0.12
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)
    print ("Seu salário liquído é de: R$", salarioL)
elif salarioB <7507.49:
    inss = salarioB*0.14
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)
    print ("Seu salário liquído é de: R$", salarioL)
elif salarioB >7507.50:
    inss = salarioB-876.95
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)
    print ("Seu salário liquído é de: R$", salarioL)
else:
    print("Sem comentários!")
#print(salarioB, "  ", salarioL)
if vale == "s" or vale == "S":
    valVale = salarioL*0.06
    print (f"Desconto do vale transporte é de R${valVale}")
    salarioL = salarioL - valVale
    print ("Seu salário liquído é de: R$", salarioL)
    
    
    
    
    
    
    
    
    







