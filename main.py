# -*- coding: utf-8 -*-
import random
print "Bem vindo ao jogo Zombie Dice!"
comecarJogo = raw_input("Pronto para começar a jogar ZombieDice? (S/N)\n")
if comecarJogo.lower() != "s":
    regras = raw_input("Precisa reler as regras? Posso te passar um link.(S/N)\n")
    if regras.lower() == "s":
        print "https://learn-us-east-1-prod-fleet02-xythos.content.blackboardcdn.com/5df7dfcfaf23d/559110?X-Blackboard-Expiration=1646352000000&X-Blackboard-Signature=rIsf3%2FgFvM6ZTjvZEgB4YaXmROGseZ0atNLwgz00uGg%3D&X-Blackboard-Client-Id=528696&response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%27RegrasDoJogo_ZombieDice.pdf&response-content-type=application%2Fpdf&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQD4hIFezFTz1m0QnChc3PDnUdZgsT4K1j9YlJ3Crsx4hAIhALmZf9u%2Bdm4hxAEKBLZa0vVgMIQvi3ZNCHKMxxBeuGE%2BKvoDCEsQAhoMNjM1NTY3OTI0MTgzIgzU7rNp4bIgtxmy2r8q1wPxbX3lx4lk6RBeY1KfvRb%2FY2%2BX3VSoBYmmeFv0OmmjhQDSjWwgWnQmFh0%2BU1lKysVcJ0rZmSw2dDnZChVUdxpKSI4kEff3gGJoWe5eKg68S8Zxyx4DH1d4iyCxp4j6lhNdJ7b4dDKdOILEjP41%2BDcZdOStfUZMzfwIsohhXAxOKkNRYKDXmOhGWt7HZIpPwVr%2BFgXUR1c3xmvq2sxJgAhNol%2Fnf3zWUrcyKAYj5pino3T6ztZOjlpXlw2SiatO7V%2FdrVl6Ro%2BBKo6CIyOeXGzBSiDv6KxlLJFSyfWT097kR6E1yU8dpqN6zUQ3k86Q%2ByV4%2F4edgUceHss7cJub1M7%2FTUxam48Arn7f4F5RrLE5%2FEkkfmGXRsAXc2wBhkrZzvhN4ulLW7VhWhe7RBWBpXKNYa4cu8Uof0obyc1bnL0o0kZFknme2avKjL%2FXDLjQtWpKfAc0OCWIV7zX45pdZeHcu%2F1bmKGICX1F8vMghd8aCoKaP4JKZMVnTzlCErwzyqwwaZYJiKCAMDm6iwnS1Ux1gYYVp%2Bi5FOl%2B3ZGV52Lp3eBJs1OtkAsRFr1CYHu5I0rxaxT%2BGV4jnyNseBQzZFiod8PT1gxBMGIDfUrSouF6emTjijwDHh8wh4yEkQY6pAF4Tsvtjd%2BtvxV5lLMuNsRbF7TX1cwK6o2%2B71%2FvyFVsvlrT38Wv1guKPyYsctEkDjG%2Fcu6ZLgehfY85mG5yDTkyJTIBXQfqfNMpsK%2FHfRpyHh%2BJ7o%2FozeD3z1Z9pfOqAfzXE6XYbVbJsaP1UXx25HkXIHHG3WC5N2VvzpiGUpMI92qQpfPEEAdx7CxD52l2u4XbLw6ezdOZMGQYm392xqbXjftMCw%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220303T180000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=ASIAZH6WM4PLRGNKLKGD%2F20220303%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=54eba0f1ea4188b6729a799e8c52ec408f49735f2155327e4473934a04245417\n"

numero_jogadores = int(input("Quantas pessoas vão jogar?\n"))
while numero_jogadores < 2:
    numero_jogadores = int(input("No minimo 2 jogadores. Quantos jogaores?"))

lista_jogadores = []
for i in range (numero_jogadores):
    nome = raw_input("Qual o nome do {}º jogador?" .format(i+1))
    lista_jogadores.append(nome)

print "\nOkay. Lembrando que temos 6 verdes (mais faceis), 4 amarelos (meio termo) e 3 vermelhos (mais difíceis). And may the odds be ever in your favor.\n"

dado_verde = "CPCTPC"
dado_amarelo = "TPCTPC"
dado_vermelho = "TPTCPT"

lista_dados = [dado_verde, dado_verde, dado_verde, dado_verde, dado_verde, dado_verde,
               dado_amarelo, dado_amarelo, dado_amarelo, dado_amarelo,
               dado_vermelho, dado_vermelho, dado_vermelho]

tiros = 0
passos = 0
cerebros = 0

dados_sorteados = []
jogador_atual = 0

while (True):
    print "Vez dx jogadorx", lista_jogadores[jogador_atual]
    for i in range(0,3):
        nummero_sorteado = random.randint(0,12)
        dado_sorteado = lista_dados[nummero_sorteado]
        dados_sorteados.append(dado_sorteado)
        if dado_sorteado == "CPCTPC":
            cor_dado = "Verde"
        elif dado_sorteado == "TPCTPC":
            cor_dado = "Amarelo"
        else:
            cor_dado = "Vermelho"
        print "O seu dado sorteado é da cor {}." .format(cor_dado)

    print "\nAgora vamos ver qual face você sorteou: \n"
    for dado_sorteado in dados_sorteados:
        numero_face_dado = random.randint(0,5)
        if dado_sorteado[numero_face_dado] == "C":
            print "Céééééérebro!!!"
            cerebros = cerebros + 1
        elif dado_sorteado[numero_face_dado] == "T":
            print "POW! Levou um tiro."
            tiros = tiros + 1
        else:
            print "Passos cada vez mais longe, fugiu."
            passos = passos + 1

    print "\nVamos ver como está o seu score:"
    print ("Cérebros: {}\nTiros: {}\nPassos:{}\n" .format(cerebros, tiros, passos))
    continuar_partida = raw_input("Quer continuar jogando os dados ou vamos para o próximo kogador? (S para sim e N para não)")
    if continuar_partida.lower() == "n":
        jogador_atual = jogador_atual + 1
        dados_sorteados = []
        cerebros = 0
        tiros = 0
        passos = 0
        print ("_____________________________")
    else:
        print ("Continuando então o turno atual")
        dados_sorteados = []
        print ("_____________________________")
