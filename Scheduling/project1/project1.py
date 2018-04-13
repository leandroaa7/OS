
def mensagem():
    print(" ")
    print("Atenção! o formato do processo deve ser:")
    print(" tempos de chegada <espaço> duração <espaço>  prioridade")
    print("exemplo")
    print(" 3  20  3")
    print(" ")
def main():
    mensagem()
    process =  input(" digite um processo")
    asd = tuple(states.split (' '))
    print(asd[0])
main()
