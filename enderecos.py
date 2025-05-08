

def mapear_rede():
    for andar in range (1,25):
        #for servico in range (0,8):
        andar_ = andar if len(str(andar)) == 2 else f'0{andar}'

        print(f'{andar} :LAD_IMOBE_SWACC{andar_}-01: 10.138.254.{andar}0') 
        print(f'{andar} :LAD_IMOBE_SWACC{andar_}-02: 10.138.254.{andar}1') 
        print(f'{andar} :LAD_IMOBE_SWACC{andar_}-03: 10.138.254.{andar}2')
        print(f'{andar} :LAD_IMOBE_AP{andar_}-04: 10.138.254.{andar}3')
        print(f'{andar} :LAD_IMOBE_AP{andar_}-05: 10.138.254.{andar}4')
        print(f'{andar} : LAD_IMOBE_AP{andar_}-06: 10.138.254.{andar}5')


def mapear_rede_():
    for andar in range (1,25):
        #for servico in range (0,8):
        andar_ = andar if len(str(andar)) == 2 else f'0{andar}'

        print(f'{andar}º') 
        print(f'{andar}º') 
        print(f'{andar}º')
        print(f'{andar}º')
        print(f'{andar}º')
        print(f'{andar}º')
        print(f'{andar}º')

mapear_rede_()