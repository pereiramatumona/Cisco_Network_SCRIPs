def mapear_rede():

    dados = ['DADOS','VOZ', 'WIFI_CORP','WIFI_GUEST']

    for andar in range (1,25):
        for i,servico in enumerate(dados):
            print(f'ip dhcp excluded-address 10.138.{andar}{i}.1 10.138.{andar}{i}.63 ')  
            print('!')
            print(f' ip dhcp pool {servico}_{andar}ªANDAR') 
            pool(andar,i,servico)
            print('!')



def pool(andar, i,servico):
    print(f' network 10.138.{andar}{i}.0 255.255.255.0')  
    print(f' default 10.138.{andar}{i}.254' ) 
    print(f' dns 10.129.100.29 10.129.122.1' )
    print(f' domain minfin.gov.ao' )
    if servico == 'VOZ':
        print(f' option 150 ip 10.129.100.183 192.168.8.10' )
    


mapear_rede()