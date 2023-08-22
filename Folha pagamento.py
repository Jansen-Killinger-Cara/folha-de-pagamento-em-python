#Desenvolvido em aula em 18/08/2023 por Jansen K Cara
#Calculando o valor do salário descontando o INSS e o Vale Transporte

import math

salarioB = float(input("Digite o salário: "))
vale =  input("Descontar o Vale Transporte? ")
irrf = 0.00
if salarioB <1320.01:
    inss = salarioB*0.075
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)
    print ("Seu salário liquído é de: R$", salarioL)
elif salarioB > 1320.00 and salarioB <2571.30:
    inss = (salarioB - 1320)*0.09 + 99
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)
    print ("Seu salário liquído é de: R$", salarioL)
elif salarioB > 2571.29 and salarioB < 3856.95:
    inss = (salarioB - 2571.29) * 0.12 + 99 + 112.62
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)
    print ("Seu salário liquído é de: R$", salarioL)
elif salarioB > 3856.94 and salarioB < 7507.50:
    inss = (salarioB - 3856.95) * 0.14 + 99 + 112.62 + 154.28
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)
    print ("Seu salário liquído é de: R$", salarioL)
elif salarioB >7507.49:
    inss = (salarioB - 3856.95) * 0.14 + 99 + 112.62 + 154.28
    print (f"Calculo do INSS R${inss}")
    salarioL = (salarioB-inss)
    print ("Seu salário liquído é de: R$", salarioL, " antes do IRRF")
else:
    print("Ops! Algo deu errado contacte seu programador! INSS")

# aqui começo a calcular o IRRF
if salarioL > 2112.00 and salarioL <2826.66:
    irrf = (salarioL * 0.075) - 148.40
    print (f"Calculo do IRRF R${irrf}, salario líquido: R${salarioL}")
elif salarioL > 2826.65 and salarioL < 3751.06:
    irrf = (salarioL * 0.15) - 370.40
    print (f"Calculo do IRRF R${irrf}, salario líquido: R${salarioL}")
elif salarioL > 3751.05 and salarioL < 4664.69:
    irrf = (salarioL * 0.225)-651.73
    print (f"Calculo do IRRF R${irrf}, salario líquido: R${salarioL}")
elif salarioL > 4664.68:
    irrf = (salarioL * 0.275) -884.96
    print (f"Calculo do IRRF R${irrf}, salario líquido: R${salarioL}")
else:
    print("Ops! Algo deu errado contacte seu programador! IRRF")

print (f"Calculo do IRRF R${irrf}")
salarioL = (salarioB-inss) - irrf
print ("Seu salário liquído é de: R$", salarioL)

#    irrf = (salarioB - 3856.95) * 0.14 + 99 + 112.62 + 154.28
#    print (f"Calculo do INSS R${inss}")
#    salarioL = (salarioB-inss)
#    print ("Seu salário liquído é de: R$", salarioL)

if vale == "s" or vale == "S":
    valVale = (salarioB-inss)*0.06
    print (f"Desconto do vale transporte é de R${valVale}")
    salarioL = (salarioB-inss) - valVale
    print ("Seu salário liquído é de: R$", salarioL)
    

    
    
    
    
    
    
    
    







