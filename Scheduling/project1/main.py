import fifo
import sjf
import rr
import prior

myprocesses = []
def mensagem():
    print(" ")
    print("Digite o processo ou 0 para executar")
    print(" ")
def inputProcess():
    mensagem()
    process = 1
    while(process != 0):
        process=input("Processo: ")
        if(process == 0):
            return 0
        tp = tuple(process.split(' '))
        if(len(tp) != 3):
            print("Entrada incorreta")
            return 1
        myprocesses.append(tp)
        print(myprocesses)    
    return 0
def main():
    inputProcess()
    print(myprocesses)

main()
