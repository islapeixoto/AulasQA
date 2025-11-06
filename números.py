nome = input ("Digite seu nome:")
idade = int (input ("Digite sua idade:"))




if idade < 12:
    print ("Você é uma criança.")

elif idade < 18: 
        print ("Você é um adolescente.")

elif idade < 60:
    print ("Você é um adulto.")

else:
    print ("Você é um idoso.")

print (f'Olá, {nome}, você tem {idade} anos. Você se enquadra na categoria acima.')