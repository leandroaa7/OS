myprocesses = [None]
def mensagem():
    print(" ")
    print("Digite o processo ou 0 para executar")
    print(" ")
def main():
	process = inputProcess()
	while(process != 0):
		myprocesses.append(process)
		process = inputProcess()
	print(myprocesses)


def inputProcess():
    mensagem()
    process=input(" Entrada: ")
    if(process == 0):
        return 0
    tp = tuple(process.split(' '))
    if(len(tp) != 5):
        print("Entrada incorreta")
        return 0
    
    
    return 0
def fifo( process ):
    pass
def sjf( process ):
    pass
def rr( process ):
    pass
def prior( process ):
    pass
main()
