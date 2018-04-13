myprocesses = []
def mensagem():
    print(" ")
    print("Atenção! o formato do processo deve ser:")
    print(" tempos de chegada <espaço> duração <espaço>  prioridade")
    print("exemplo")
    print(" 3  20  3")
    print(" ")
def main():
    try:
        mensagem()
        states =  input(" digite um processo")
        asd = tuple(states.split (' '))
        print(len(states))
        if(len(states) != 5): # 5 pois conta os 3 processos + espaços
            raise Exception("Entrada Incorreta")
        
    except Exception as error:
        print(error)
def fifo( process ):
    pass
def sjf( process ):
    pass
def rr( process ):
    pass
def prior( process ):
    pass
main()
