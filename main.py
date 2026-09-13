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
            classe = "Guerreiro"
            print(f"Voce escolheu Guerreiro!\n Vida: {vida}\n Ataque: {ataque}\n Defesa: {defesa}\n")
            break
        case 2:
            vida = 80
            ataque = 40
            defesa = 10
            classe = "Mago"
            print(f"Voce escolheu Mago!\n Vida: {vida}\n Ataque: {ataque}\n Defesa: {defesa}\n")
            break
        case 3:
            vida = 100
            ataque = 30
            defesa = 15
            classe = "Arqueiro"
            print(f"Voce escolheu Arqueiro!\n Vida: {vida}\n Ataque: {ataque}\n Defesa: {defesa}\n")
            break
        case _:
            print("Opcao invalida!\n")

#Sorteio do boss para o combate
primeiro_boss = random.randint(1, 3)
match primeiro_boss:
    case 1:
        vida_boss = 60
        ataque_boss = 15
        print(f"Um Goblin apareceu!\n Vida do inimigo: {vida_boss}\n Dano por ataque do inimigo: {ataque_boss}")
    case 2:
        vida_boss = 50
        ataque_boss = 20
        print(f"Um Lobo apareceu!\n Vida do inimigo: {vida_boss}\n Dano por ataque do inimigo: {ataque_boss}\n")
    case 3:
        vida_boss = 80
        ataque_boss = 12
        print(f"Um Esqueleto apareceu!\n Vida do inimigo: {vida_boss}\n Dano por ataque do inimigo: {ataque_boss}")

#Início do combate
combate = '''
COMBATE!

1- Atacar
2- Defender
3- Usar pocao

'''
print(combate)

qtde_pocao = 2
pocao = 30
vida_max = vida

while True:
    opcao = int(input("Sua escolha: \n"))
    chance_critica = random.randint(1, 10)
    match opcao:
        case 1:
            vida_boss -= ataque
            if vida_boss < 0:
                vida_boss = 0
            print(f"Voce deu um dano de {ataque} no boss, vida restante do boss {vida_boss}\n")
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
                
    if vida <= 0 or vida_boss <= 0:
        print(f"Parabéns, voce derrotou o boss!\nVida restante: {vida}\n")
        break 