#Desenvolvido em aula em 18/08/2023 por Jansen K Cara
#Calculando o valor do salário descontando o INSS e o Vale Transporte

import math
salarioB = float(input("Digite o Salário Bruto: "))
vale = input("Desncontar Vale Transporte? ")
dep  = input ("Quantos dependetes possui? ")
dep = 189.90

#INSS
if salarioB < 1320.01:
    inss = float(salarioB*0.075)
    print (f"Desconto de INSS: R${inss}")
elif salarioB < 2571.30:
    inss = float((salarioB-1320.00)*0.09 +99.00)
    print (f"Desconto de INSS: R${inss}")
elif salarioB < 3856.95:
    inss = float((salarioB-2571.29)*0.12 + 211.62)
    print (f"Desconto de INSS: R${inss}")
elif salarioB < 7507.49:
    inss = float((salarioB-3856.94)*0.14 + 365.9)
    print (f"Desconto de INSS: R${inss}")
else:
    salarioB > 7507.50
    inss = float( 876.95)
    print (f"Desconto de INSS: R${inss}")

#Vale Transporte
if vale == "Sim" or vale == "sim":
    Descvale = salarioB*0.06
    print (f"Desconto do Vale Transporte: R${Descvale}")
else:
     Descvale = 0
     print (f"Desconto do Vale Transporte: R${Descvale}")

#IRRF
bcirrf = salarioB - inss
bcirrf = bcirrf - dep
if bcirrf < 2112.01:
    irrf = float(bcirrf*0)
    print (f"Desconto de IRRF R${irrf}")
elif bcirrf < 2826.66:
    irrf = float(bcirrf*0.075 - 158.40)
    print (f"Desconto de IRRF R${irrf}")
elif bcirrf < 3751.06:
    irrf = float(bcirrf*0.15 - 370.40)
    print (f"Desconto de IRRF R${irrf}")
elif bcirrf <= 4664.68:
    irrf = float(bcirrf*0.2250 - 651.73)
    print (f"Desconto de IRRF R${irrf}")
else:
    bcirrf >= 4664.69 
    irrf = float(bcirrf*0.275 - 876.95)
    print (f"Desconto de IRRF R${irrf}")

    #sALDO
desconto = float(inss + irrf + Descvale)
salarioL = float(salarioB - desconto)
print (f"Seu salário líquido é de R${salarioL}")

