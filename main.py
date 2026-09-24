import random

texto = '''
Seja bem-vindo ao biel's RPG!
Para iniciarmos, escolha sua classe:

  1- Guerreiro
      - Vida:   120
      - Ataque: 25
      - Defesa: 20
  2- Mago
      - Vida:   80
      - Ataque: 40
      - Defesa: 10
  3- Arqueiro
      - Vida:   100
      - Ataque: 30
      - Defesa: 15
'''
print(texto)

#Escolha do personagem
while True: 
    escolha = int(input("Sua escolha: \n"))
    match escolha:
        case 1:
            vida = 120
            ataque = 25
            defesa = 20
            qtde_pocao = 2
            pocao = 30
            qtde_moedas = 0
            classe = "Guerreiro"
            print(f"Voce escolheu Guerreiro!\n Vida: {vida}\n Ataque: {ataque}\n Defesa: {defesa}\n")
            break
        case 2:
            vida = 80
            ataque = 40
            defesa = 10
            qtde_pocao = 2
            pocao = 30
            qtde_moedas = 0
            classe = "Mago"
            print(f"Voce escolheu Mago!\n Vida: {vida}\n Ataque: {ataque}\n Defesa: {defesa}\n")
            break
        case 3:
            vida = 100
            ataque = 30
            defesa = 15
            qtde_pocao = 2
            pocao = 30
            qtde_moedas = 0
            classe = "Arqueiro"
            print(f"Voce escolheu Arqueiro!\n Vida: {vida}\n Ataque: {ataque}\n Defesa: {defesa}\n")
            break
        case _:
            print("Opcao invalida!\n")

#Sorteio do boss para o combate
primeiro_boss = random.randint(1, 3)
match primeiro_boss:
    case 1:
        nome_boss = "Goblin"
        vida_boss = 60
        ataque_boss = 15
        print(f"Um Goblin apareceu!\n Vida do inimigo: {vida_boss}\n Dano por ataque do inimigo: {ataque_boss}")
    case 2:
        nome_boss = "Lobo"
        vida_boss = 50
        ataque_boss = 20
        print(f"Um Lobo apareceu!\n Vida do inimigo: {vida_boss}\n Dano por ataque do inimigo: {ataque_boss}\n")
    case 3:
        nome_boss = "Esqueleto"
        vida_boss = 80
        ataque_boss = 12
        print(f"Um Esqueleto apareceu!\n Vida do inimigo: {vida_boss}\n Dano por ataque do inimigo: {ataque_boss}")
    case _:
        print("Opcao invalida!\n")

#Início do combate
combate = '''
COMBATE!

1- Atacar
2- Defender
3- Usar pocao

'''
print(combate)

vida_max = vida

while True:
    opcao = int(input("Sua escolha: \n"))
    chance_critica = random.randint(1, 10)
    match opcao:
        case 1:
            if chance_critica == 1 or chance_critica == 2:
                ataque = ataque * 2
                vida_boss -= ataque
                print(f"Voce conseguiu um ATAQUE CRITICO!\nVoce causou {ataque} de dano, vida restante do boss: {vida_boss}.\n")
            else:
                vida_boss -= ataque
                print(f"Voce deu um dano de {ataque} no boss, vida restante do boss {vida_boss}\n")
            if vida_boss > 0:
                vida -= ataque_boss
                print(f"{nome_boss} atacou!\nVoce recebeu {ataque_boss} de dano.\nSua vida: {vida}\nVida do {nome_boss}: {vida_boss}")
            else:
                vida_boss = 0
        case 2:
            ataque_boss_defendido = ataque_boss / 2
            vida -= ataque_boss
            print(f"O boss atacou voce causando {ataque_boss_defendido}.\nVoce se defendeu!\nDano recebido: {ataque_boss_defendido}\nVida restante: {vida}.\n")  
        case 3:
            qtde_pocao -= 1
            if vida + 30 > vida_max:
                cura = vida_max - vida
                vida += cura
                print(f"Foi curado: {cura}\nVida total: {vida}")
            else:
                cura = 30
                vida += cura
                print(f"Foi curado: {cura}\nVida total: {vida}")
        case _:
            print("Opcao invalida!\n")
                
    if vida <= 0 or vida_boss <= 0:
        print(f"Parabéns, voce derrotou o boss!\nVida restante: {vida}\n")
        break 

portas = ''''
Voce encontrou duas portas, escolha qual das duas voce irá entrar!

1- Porta de madeira
2- Porta de pedra

'''
print(portas)
escolha_portas = int(input("Sua escolha: \n"))

match escolha_portas:
    case 1:
        recompensa = random.randint(1, 2)
        if recompensa == 1:
            qtde_pocao += 1
            print("Voce encontrou uma pocao!")
        else:
            print("A porta estava presa. Nada aconteceu.")
    case 2:
        recompensa = random.randint(1, 2)
        if recompensa == 1:
            qtde_moedas += 50
            print("Voce encontrou 50 moedas!")
        else:
            vida -= 20
            print("Uma armadilha foi ativada, voce perdeu 20 de vida.")
    case _:
        print("Opcao invalida!\n")

finalgame = f'''
========== STATUS FINAL ==========

Classe: {classe}
Vida: {vida}
Poções restantes: {qtde_pocao}
Inimigo derrotado: {nome_boss}
Moedas encontradas: {qtde_moedas}

==================================

Você conseguiu escapar da masmorra!

'''
print(finalgame)