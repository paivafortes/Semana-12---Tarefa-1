#O dodô é uma ave não voadora, extinta atualmente, e que era endêmica da Ilha Maurítius, na costa leste da África. A partir do ano 1600, durante cada ano, 6% dos animais dos animais vivos no começo do ano morreram e o número de animais nascidos ao longo do ano que sobreviveram foi de 1% da população inicial.

def controle_populacao(populacao):

    risco_de_extincao = populacao * 0.10
    populacao_nascida = 0
    populacao_morta = 0
    ano = 1600
    while(populacao >= risco_de_extincao):
        populacao_nascida = populacao * 0.01
        populacao_morta = populacao * 0.06
        
        populacao -= populacao * 0.05

        
        print(ano, round(populacao_nascida), round(populacao_morta), round(populacao), sep=',')
        ano += 1



def main():
    populacao_aves = input()
    populacao_aves = int(populacao_aves)

    controle_populacao(populacao_aves)



if __name__ == '__main__':
    main()