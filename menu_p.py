import pickle
from time import sleep
########################################################################################
def menu():
    print("MENU:")
    print("1 - Cadastrar")
    print("2 - Consultar todos os funcionarios")
    print("3 - Excluir Funcionario")
    print("8 - Sair")
############################################################################
def cadastrar():
    try:
        f=open("funcionarios100.bi","rb")
        lista_funcionarios=pickle.load(f)
        f.close()
    except IOError:
        lista_funcionarios=[] 
    opcao='S'
    while opcao=='s' or opcao=='S':
        lista=[None]*3
        lista[0]=input(f"Entre com o nome do funcionario: ")
        lista[1]=float(input(f"Entre com o salario funcionario: "))
        lista[2]=int(input(f"Entre com numero de dependentes do funcionario: "))
        lista_funcionarios.append(lista) 
        opcao=input("Quer cadastrar outro funcionario S/N: ")
    with open("funcionarios100.bi",'wb') as f:     
        pickle.dump(lista_funcionarios,f) 
######################################################################################
def consultar_total_dos_salarios():
    try:
        f=open("funcionarios100.bi","rb")
        lista_funcionarios=pickle.load(f)
        f.close()
        total=0
        for i in range(len(lista_funcionarios)):
            total=total+lista_funcionarios[i][1]
            for j in range(len(lista_funcionarios[i])): 
                print("{}\t\t" .format(lista_funcionarios[i][j]), end=' ') 
            print("")
        print(f"O total dos salarios = {total}")    
    except IOError:
        print(" Nao tem dados de funcionarios cadastrados")         
#######################################################################################          
def excluir_funcionario():
    try:
        f=open("funcionarios100.bi","rb")
        lista_funcionarios=pickle.load(f)
        f.close()
        naoencontrou=True
        nome=input("Entre com o nome do funcionario para excluir ")
        for i in range(len(lista_funcionarios)):
            if nome==lista_funcionarios[i][0]:
                lista_funcionarios.pop(i)
                naoencontrou=False
                break
        if naoencontrou:
            print(f"Nao existe o funcionario {nome}")
            sleep(1)   
        else:
            with open("funcionarios100.bi",'wb') as f: 
                pickle.dump(lista_funcionarios,f)           
    except IOError:
        print(" Erro no arquivo")    
###################################################################################
opc=True
while opc:
    menu()
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        cadastrar()  
        sleep(1)   
    elif escolha == "2":
        consultar_total_dos_salarios()  
        sleep(3)   
    elif escolha == "3":
        excluir_funcionario()  
        sleep(3)    
    elif escolha == "8":
        print("Saindo ...")
        sleep(1)
        opc=False
    else:
        print(f"Opção {escolha} inválida. Tente novamente.")
        x=input('Digite uma tecla para voltar ao menu: ')
        
