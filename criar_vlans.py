def mapear_rede():

    dados = ['DADOS','VOZ', 'WIFI_CORP','WIFI_GUEST']

    for andar in range (1,25):
        for i,servico in enumerate(dados):
            print(f'vlan {andar}{i}')  
            print(f' name [{servico}-{andar}-ANDAR]' ) 
            print('!')


mapear_rede()




