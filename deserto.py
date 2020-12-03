# MÓDULO "DESERTO"

###########################################################################################################

import Batalha # Importando o módulo "Batalha"

# Definição de funções

def enter(): # "botão" para prosseguir
    return input('\naperte enter para continuar')

def dunas(objetos_coletados): # função que representa a trajetória do jogador nas dunas de areia do deserto
    i = 0
    j = 0
    if "pedra" and "poção" in objetos_coletados:
        print("Você ja coletou o objeto que necessitava aqui!")
    elif "pedra" in objetos_coletados and "poção" not in objetos_coletados:
        while i < 1:
            escolha = int(input("Você encontrou uma poção! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                objetos_coletados.append("poção")
                print("Poção coletada!")
                i += 1
            elif escolha == 2:
                i += 1
            else:
                print("Digite uma opção válida!")
                i = 0
    elif "poção" in objetos_coletados and "pedra" not in objetos_coletados:
        while j < 1:
            escolha = int(input("Você encontrou uma pedra! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                objetos_coletados.append("pedra")
                print("Pedra coletada!")
                j += 1
            elif escolha == 2:
                j += 1
            else:
                print("Digite uma opção válida!")
                j = 0
    else:
        while i < 1:
            escolha = int(input("Você encontrou uma poção! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                objetos_coletados.append("poção")
                print("Poção coletada!")
                i += 1
            elif escolha == 2:
                i += 1
            else:
                print("Digite uma opção válida!")
                i = 0
        while j < 1:
            escolha = int(input("Você encontrou uma pedra! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                objetos_coletados.append("pedra")
                print("Pedra coletada!")
                j += 1
            elif escolha == 2:
                j += 1
            else:
                print("Digite uma opção válida!")
                j = 0
 
    return objetos_coletados

def topo_da_montanha(objetos_coletados): # funçao que representa a trajetória do jogador no topo de uma montanha no deserto
    i = 0
    j = 0
    if "flor" and "chave" in objetos_coletados:
        print("Você ja coletou o objeto que necessitava aqui!")
    elif "flor" in objetos_coletados and "chave" not in objetos_coletados:
        while i < 1:
            escolha = int(input("Você encontrou uma chave! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                objetos_coletados.append("chave")
                print("Chave coletada!")
                i += 1
            elif escolha == 2:
                i += 1
            else:
                print("Digite uma opção válida!")
                i = 0
    elif "chave" in objetos_coletados and "flor" not in objetos_coletados:
        while j < 1:
            escolha = int(input("Você encontrou uma flor do deserto! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                objetos_coletados.append("flor")
                print("Flor coletada!")
                j += 1
            elif escolha == 2:
                j += 1
            else:
                print("Digite uma opção válida!")
                j = 0
    else:
        while i < 1:
            escolha = int(input("Você encontrou uma chave! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                objetos_coletados.append("chave")
                print("Chave coletada!")
                i += 1
            elif escolha == 2:
                i += 1
            else:
                print("Digite uma opção válida!")
                i = 0
        print("Descrição do caminho pelas dunas")
        while j < 1:
            escolha = int(input("Você encontrou uma flor do deserto! Deseja coletá-la? 1 - Sim ou 2 - Não"))
            if escolha == 1:
                objetos_coletados.append("flor")
                print("Flor coletada!")
                j += 1
            elif escolha == 2:
                j += 1
            else:
                print("Digite uma opção válida!")
                j = 0
 
    return objetos_coletados

def oasis(objetos_coletados, atributos): # função que representa a trajetória do jogador em um oasis no deserto
    # puzzle
    i = -1
    desbloqueio = False
    combinacao_correta = ["poção", "flor", "runa", "pedra"]
    print("Apresente a combinação de 4 objetos que é o código para desbloquear a passagem ao oasis!")
    objeto_1 = input("Qual o primeiro objeto da sequência?")
    if objeto_1 not in objetos_coletados:
        return(f'Você não possui o objeto {objeto_1}! Continue sua caminhada pelo deserto e colete-o. Em seguida, tente conseguir acesso ao oasis novamente!')
    else:
        objeto_2 = input("Qual o primeiro objeto da sequência?")
        if objeto_2 not in objetos_coletados:
            return(f'Você não possui o objeto {objeto_2}! Continue sua caminhada pelo deserto e colete-o. Em seguida, tente conseguir acesso ao oasis novamente!')
        else:
            objeto_3 = input("Qual o primeiro objeto da sequência?")
            if objeto_3 not in objetos_coletados:
                return(f'Você não possui o objeto {objeto_3}! Continue sua caminhada pelo deserto e colete-o. Em seguida, tente conseguir acesso ao oasis novamente!')
            else:
                objeto_4 = input("Qual o primeiro objeto da sequência?")
                if objeto_4 not in objetos_coletados:
                    return(f'Você não possui o objeto {objeto_4}! Continue sua caminhada pelo deserto e colete-o. Em seguida, tente conseguir acesso ao oasis novamente!')
                else:
                    if(objeto_1 == combinacao_correta[0] and objeto_2 == combinacao_correta[1] and objeto_3 == combinacao_correta[2] and objeto_4 == combinacao_correta[3]):
                        desbloqueio = True
                        while i < len(atributos) - 1:
                             i += 1
                             if atributos[i] < 5:
                                 atributos[i] += 2
                        #print(
                        return(f'Parabéns! Você desbloqueou o acesso ao oasis e seus atributos melhoraram! Força: {atributos[0]}; destreza: {atributos[1]}; inteligência: {atributos[2]}; sorte: {atributos[3]}; carisma:  {atributos[4]}.') 


############################################################################################################################

x = 0 # Variável utilizada para o mecanismo de repetição de perguntas caso o jogador não informe uma escolha válida

meus_objetos_coletados = [] # Lista para incluir os objetos que o jogador coleta ao logo da trajetória no deserto
meus_atributos =  # Valores dos atributos do jogador: força, destreza, inteligência, sorte e carisma, respectivamente 
hp = 

# Introdução do ambiente (deserto) ao jogador
print("Você chegou ao deserto!")
print("ADICIONAR DESCRIÇÃO INTRODUTÓRIA DO DESERTO")
enter()

# O jogador escolhe para qual local deseja ir primeiro (dunas de areia, topo da montanha ou oasis)
escolha_1 = int(input("Qual local deseja explorar primeiro? 1 - Dunas de areia / 2 - Topo da montanha / 3 - Oasis"))

# Se a escolha for dunas de areia:
if escolha_1 == 1:

# CAMINHO 1
# O jogador escolhe seguir para as dunas de areia primeiro:
    print("Você está nas dunas!")

    # Descrição do ambiente ao jogador
    print("ADICIONAR DESCRIÇÃO DAS DUNAS DE AREIA")
    enter()

    # Chama função dunas()
    dunas(meus_objetos_coletados)
    print("Você está prosseguindo sua caminhada...")

    # O jogador escolhe para onde ir em seguida
    escolha_2 == int(input("Qual é o seu próximo destino? 1 - Topo da montanha / 2 - Oasis"))

    if escolha_2 == 1:
# O jogador escolhe seguir das dunas para o topo da montanha:
        
        # Descrição do caminho
        print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE AS DUNAS E O TOPO DA MONTANHA")

        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
        coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")

        # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
        if coleta_de_objetos == 1:
            Batalha.batalha(Serpente, jogador) # chamada da função "batalha" do módulo "Batalha"
        else:
            enter()

        # Verifica se o jogador já coletou o objeto "chave" anteriormente ou não
        if "chave" not in meus_objetos_coletados:
            # Se ainda não foi coletado, o objeto aparece no caminho entre as dunas e o topo da montanha e o jogador escolhe se quer coletá-lo
            coleta_de_objetos = int(input("Você encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não"))
            # Se o jogador optar por coletá-lo, o objeto será adicionado a lista de objetos coletados
            if coleta_de_objetos == 1:
                meus_objetos_coletados.append("chave")
            # Se não, o jogador continua o caminho pelo deserto
            else:
                enter()
        else:
            enter()
	print("ADICIONAR DESCRIÇÃO DO TOPO DA MONTANHA")
        print("Você está chegando ao topo da montanha...")
        enter()
        print("ADICIONAR DESCRIÇÃO DO TOPO DA MONTANHA")
        topo_da_montanha(meus_objetos_coletados)
        print("Você está prosseguindo sua caminhada...")
        enter()
        print("Só resta um local para explorar agora...")
        
# Finalmente, o jogador segue do topo da montanha a um oasis

	print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O TOPO DA MONTANHA ATÉ O ENCONTRO DE UM OASIS NO DESERTO")		
        print("Há um oasis a alguns metros!")
        if "runa" not in meus_objetos_coletados:
            coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não")
            if coleta_de_objetos == 1:
                meus_objetos_coletados.append("runa")
            else:
                enter()
        else:
            enter()
        oasis(meus_objetos_coletados, meus_atributos)     
				    
        elif escolha_2 == 2:
# CAMINHO 2:
# O jogador escolhe seguir das dunas de areia ao oasis:

            # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
            coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
            # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
            if coleta_de_objetos == 1:
                Batalha.batalha(Serpente, jogador) # chamada da função "batalha" do módulo "Batalha"
            else:
                enter()
            print("Você chegou a um oasis!")
            oasis(meus_objetos_coletados, meus_atributos)
            print("Você está prosseguindo sua caminhada...")
            enter()
            print("Só resta um local para explorar agora...")

# Finalmente, o jogador segue do oasis ao topo da montanha

            # Descrição do caminho
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O OASIS E O TOPO DA MONTANHA")
            if "runa" not in meus_objetos_coletados:
            coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não")
                if coleta_de_objetos == 1:
                    meus_objetos_coletados.append("runa")
                else:
                    enter()
            else:
                enter()
            
            print("Você chegou ao topo da montanha!")
            print("ADICIONAR DESCRIÇÃO DO TOPO DA MONTANHA")
            topo_da_montanha(meus_objetos_coletados)
            print("Você está prosseguindo sua caminhada...")
            enter()

elif escolha_1 == 2:

# CAMINHO 3:
# O jogador escolhe seguir para o topo da montanha primeiro
				    
    print("Você está no topo da montanha!")
    print("ADICIONAR DESCRIÇÃO DO TOPO DA MONTANHA")
    enter()
    #chama função topo_da_montanha()
    topo_da_montanha(meus_objetos_coletados)
    print("Você está prosseguindo sua caminhada...")
    escolha_2 == int(input("Qual é o seu próximo destino? 1 - Dunas / 2 - Oasis"))

    if escolha_2 == 1:
# O jogador segue do topo da montanha às dunas

        print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O TOPO DA MONTANHA E AS DUNAS DE AREIA")

        # Descrição do caminho
        print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O TOPO DA MONTANHA E AS DUNAS")

         # Verifica se o jogador já coletou o objeto "chave" anteriormente ou não
        if "chave" not in meus_objetos_coletados:
            # Se ainda não foi coletado, o objeto aparece no caminho entre as dunas e o topo da montanha e o jogador escolhe se quer coletá-lo
            coleta_de_objetos = int(input("Você encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não")
            # Se o jogador optar por coletá-lo, o objeto será adicionado a lista de objetos coletados
            if coleta_de_objetos == 1:
                meus_objetos_coletados.append("chave")
            # Se não, o jogador continua o caminho pelo deserto
            else:
                enter()
        else:
            enter()

        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
        coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
        # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
        if coleta_de_objetos == 1:
            Batalha.batalha() # Chamada da função "batalha" do módulo "Batalha"
        else:
            enter()
        print("Você chegou às dunas!")
	print("ADICIONAR DESCRIÇÃO DAS DUNAS DE AREIA")
        enter()
    	#chama função "dunas"
	dunas(meus_objetos_coletados)
	print("Você está prosseguindo sua caminhada...")
	print("Só resta um local para explorar agora...")
	enter()
        
# Finalmente, o jogador segue das dunas de areia ao oasis

        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
        coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
        # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
        if coleta_de_objetos == 1:
            Batalha.batalha() # Chamada da função "batalha" do módulo "Batalha"
        else:
            enter()
         
        print("Há um oasis a alguns metros!")
        print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE AS DUNAS DE AREIA E O OASIS")
        oasis(meus_objetos_coletados, meus_atributos)
        

        elif escolha_2 == 2:
# O jogador segue do topo da montanha ao oasis

            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O TOPO DA MONTANHA E O OASIS")
            print("Há um oasis a alguns metros!")

            if "runa" not in meus_objetos_coletados:
                coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não")
                if coleta_de_objetos == 1:
                    meus_objetos_coletados.append("runa")
                else:
                    enter()
            else:
                enter()
            print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O TOPO DA MONTANHA ATÉ O ENCONTRO DE UM OASIS NO DESERTO")
            oasis(meus_objetos_coletados, meus_atributos)     
            print("Você está prosseguindo sua caminhada...")
            enter()

# Finalmente, o jogador segue do oasis às dunas de areia

        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
        coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
        # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
        if coleta_de_objetos == 1:
            Batalha.batalha() # Chamada da função "batalha" do módulo "Batalha"
        else:
            enter()
				
        print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O OASIS E AS DUNAS DE AREIA")
        if "runa" not in meus_objetos_coletados:
            coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não")
            if coleta_de_objetos == 1:
                meus_objetos_coletados.append("runa")
            else:
                enter()
        else:
            enter()
        print("Você chegou às dunas de areia!")
        dunas(meus_objetos_coletados, meus_atributos)  
        print("Você está prosseguindo sua caminhada...")
        enter()
    
if escolha_1 == 3:

# CAMINHO 4: 
# O jogador escolhe seguir ao oasis primeiro 

    print("Você chegou a um oasis!")
    enter()
    # chama função "oasis"
    oasis(meus_objetos_coletados)
    print("Você está prosseguindo sua caminhada...")
    escolha_2 == int(input("Qual é o seu próximo destino? 1 - Dunas / 2 - Topo da montanha"))
				    
        if escolha_2 == 1:
# O jogador segue do oasis às dunas de areia

        print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O OASIS E AS DUNAS DE AREIA")
        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
        coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")
        # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
        if coleta_de_objetos == 1:
            Batalha.batalha() # Chamada da função "batalha" do módulo "Batalha"
        else:
            enter()
        print("Você chegou às dunas de areia!")
        dunas(meus_objetos_coletados)  
        print("Você está prosseguindo sua caminhada...")
        print("Só resta um local para explorar agora...")
	enter()
    
# Finalmente, o jogador segue das dunas de areia ao topo da montanha
        # Descrição do caminho entre as dunas de areia ao topo da montanha
        print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE AS DUNAS E O TOPO DA MONTANHA")
        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
        coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")

        # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
        if coleta_de_objetos == 1:
            Batalha.batalha() # Chamada da função "batalha" do módulo "Batalha"
        else:
            enter()

        # Verifica se o jogador já coletou o objeto "chave" anteriormente ou não
        if "chave" not in meus_objetos_coletados:
            # Se ainda não foi coletado, o objeto aparece no caminho entre as dunas e o topo da montanha e o jogador escolhe se quer coletá-lo
            coleta_de_objetos = int(input("Você encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não")
            # Se o jogador optar por coletá-lo, o objeto será adicionado a lista de objetos coletados
            if coleta_de_objetos == 1:
                meus_objetos_coletados.append("chave")
            # Se não, o jogador continua o caminho pelo deserto
            else:
                enter()
        else:
            enter()
        print("Você está chegando ao topo da montanha...")
        enter()
        print("ADICIONAR DESCRIÇÃO DO TOPO DA MONTANHA")
        topo_da_montanha(meus_objetos_coletados)
        print("Você está prosseguindo sua caminhada...")
        enter()

    elif escolha_2 == 2:

# CAMINHO 5:
# O jogador segue do oasis ao topo da montanha

        if "runa" not in meus_objetos_coletados:
            coleta_de_objetos = int(input("Você encontrou uma runa! Deseja coletá-la? 1 - Sim / 2 - Não")
            if coleta_de_objetos == 1:
                meus_objetos_coletados.append("runa")
            else:
                enter()
        else:
            enter()

        print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE O OASIS E O TOPO DA MONTANHA")
        print("Você chegou ao topo da montanha!")
        enter()
        print("Descrição de ambiente - Topo da montanha")
        topo_da_montanha(meus_objetos_coletados)
        print("Você está prosseguindo sua caminhada...")
        print("Só resta um local para explorar agora...")
        enter()
        
# O jogador segue do topo da montanha às dunas de areia

         # Descrição do caminho entre o topo da montanha e as dunas de areia
        print("ADICIONAR DESCRIÇÃO DO CAMINHO ENTRE AS DUNAS E O TOPO DA MONTANHA")

        # O jogador encontra uma serpente no caminho e decide se deseja coletá-la ou não
        coleta_de_objetos = int(input("Você encontrou uma serpente! Deseja coletá-la? 1 - Sim ou 2 - Não")

        # Se o jogador optar por coletar a serpente, haverá uma batalha com ela
        if coleta_de_objetos == 1:
            Batalha.batalha() # Chamada da função "batalha" do módulo "Batalha"
        else:
            enter()

        # Verifica se o jogador já coletou o objeto "chave" anteriormente ou não
        if "chave" not in meus_objetos_coletados:
            # Se ainda não foi coletado, o objeto aparece no caminho entre as dunas e o topo da montanha e o jogador escolhe se quer coletá-lo
            coleta_de_objetos = int(input("Você encontrou uma chave! Deseja coletá-la? 1 - Sim / 2 - Não")
            # Se o jogador optar por coletá-lo, o objeto será adicionado a lista de objetos coletados
            if coleta_de_objetos == 1:
                meus_objetos_coletados.append("chave")
            # Se não, o jogador continua o caminho pelo deserto
            else:
                enter()
        else:
            enter()
        print("Você está chegando às dunas de areia...")
        enter()
        print("ADICIONAR DESCRIÇÃO DAS DUNAS DE AREIA")
        dunas(meus_objetos_coletados)
        print("Você está prosseguindo sua caminhada...")
        enter()

while x < 1:
    if x == -1:
        escolha = int(input("2 - Retornar às dunas ou 3 - Retornar ao topo da montanha?"))
    else:
        escolha = int(input("1 - Prosseguir no caminho, 2 - Retornar às dunas ou 3 - Retornar ào topo da montanha?"))
    # continua o caminho ao oasis
    if escolha == 1:
        x += 1
    # retorna às dunas
    elif escolha == 2:
        print("Você retornou às dunas de areia.")
        dunas(meus_objetos_coletados)    
        escolha = int(input("1 - Prosseguir no caminho ou 2 - Retornar a um dos locais anteriores?"))  
        if escolha == 1:
            x += 1
        else: 
            x = -1
    # retorna ao topo da montanha
    elif escolha == 3:
        print("Você retornou ao topo da montanha.")
        topo_da_montanha(meus_objetos_coletados)    
        escolha = int(input("1 - Prosseguir no caminho ou 2 - Retornar a um dos locais anteriores"))  
        if escolha == 1:
            if x == 0:
                x += 1
            if x == -1:
                x += 2
        else:
            x = -1