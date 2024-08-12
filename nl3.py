import math
def menu():
    print("""
=============================================================
              Bem-vindo ao Simulador de Filtros Ópticos!       
=============================================================
Este programa simula o comportamento da luz ao passar por diferentes 
tipos de filtros ópticos, permitindo explorar como a intensidade da 
luz é afetada após a aplicação desses filtros.

Desenvolvido por:
- Victor Merker BInda (RA: 242230860)
- Paulo Andre de Oliveira Hirata (RA: 241230861)
- Diogo Santos Linna (RA: 241230036)

Por favor, escolha uma das opções abaixo para iniciar:
=============================================================
""")

def calcular_intensidade_apos_primeiro_filtro(i0, angulo_filtro):
    rad = math.radians(angulo_filtro)
    teta = math.cos(rad)
    return i0 / 2, teta

def calcular_intensidade_apos_segundo_filtro(i, teta):
    return i * (teta ** 2)

def calcular_intensidade_apos_terceiro_filtro(i, teta):
    return i * (teta ** 2)

def calcular_intensidade_apos_filtro(i0):
    return i0 / 2

def calcular_intensidade_nao_polarizada_apos_filtro(i_filtrada):
    return i_filtrada * 2

def filtro1_1():
    i0 = float(input("Intensidade inicial da luz (W/cm²): "))
    i_filtrada = calcular_intensidade_apos_filtro(i0)
    print('Intensidade da luz após passar pelo filtro: %.3f W/cm²' % i_filtrada)

def filtro1_2():
    i_filtrada = float(input("Intensidade da luz após passar pelo filtro (W/cm²): "))
    i0 = calcular_intensidade_nao_polarizada_apos_filtro(i_filtrada)
    print('Intensidade da luz não polarizada: %.3f W/cm²' % i0)


def _2filtros_naopolarizado():
    raio_incidente = float(input(" fale Raio incidente: \n"))
    angulo_filtro1 = float(input("qual é Angulo do primeiro filtro: \n"))
    angulo_filtro2 = float(input("qual é Angulo do segundo filtro: \n"))
    
    i1, teta2 = calcular_intensidade_apos_primeiro_filtro(raio_incidente, angulo_filtro2)
    i2 = calcular_intensidade_apos_segundo_filtro(i1, teta2)
    
    print('Intensidade da luz após o primeiro filtro: %.3f'% i1 +" W/c^2")
    print('Intensidade da luz após o segundo filtro: %.3f'% i2 +" W/c^2")

def _2filtrospolarizadoi1():
    i1_apos_primeiro_filtro = float(input("Raio após o primeiro filtro: \n"))
    angulo_filtro1 = float(input("qual é Angulo do primeiro filtro: \n"))
    angulo_filtro2 = float(input("qual é Angulo do segundo filtro:\n"))
    
    _, teta2 = calcular_intensidade_apos_primeiro_filtro(i1_apos_primeiro_filtro * 2, angulo_filtro2)
    i2 = calcular_intensidade_apos_segundo_filtro(i1_apos_primeiro_filtro, teta2)   
    
    print('Intensidade da luz incidente: %.3f'% (i1_apos_primeiro_filtro * 2) +" W/c^2")
    print('Intensidade da luz após o segundo filtro: %.3f'% i2 +" W/c^2") 

def _2filtrospolarizadosi2():
    i2_apos_segundo_filtro = float(input("Raio após o segundo filtro: \n"))
    angulo_filtro1 = float(input("qual é Angulo do primeiro filtro: \n"))
    angulo_filtro2 = float(input("qual é Angulo do segundo filtro: \n"))
    
    i1 = i2_apos_segundo_filtro / (math.cos(math.radians(angulo_filtro2)) ** 2)    
    i0 = i1 * 2  
    
    print('Intensidade da luz incidente: %.3f'% i0 +" W/c^2")
    print('Intensidade da luz após o primeiro filtro: %.3f'% i1 +" W/c^2")

def i0_nao_polarizado_3filtros():
    raio_incidente = float(input("Raio incidente: \n"))
    angulo_filtro1 = float(input("qual é Angulo do primeiro filtro: \n"))
    angulo_filtro2 = float(input("qual é Angulo do segundo filtro: \n"))
    angulo_filtro3 = float(input("qual é Angulo do terceiro filtro: \n"))
    
    i1, teta2 = calcular_intensidade_apos_primeiro_filtro(raio_incidente, angulo_filtro2)
    i2 = calcular_intensidade_apos_segundo_filtro(i1, teta2)
    _, teta3 = calcular_intensidade_apos_primeiro_filtro(i2, angulo_filtro3 - angulo_filtro2)
    # Corrigindo a chamada da função para calcular a intensidade após o terceiro filtro
    i3 = calcular_intensidade_apos_terceiro_filtro(i2, teta3) 
    
    print('Intensidade da luz após o primeiro filtro: %.3f'% i1 +" W/c^2")
    print('Intensidade da luz após o segundo filtro: %.3f'% i2 +" W/c^2")
    print('Intensidade da luz após o terceiro filtro: %.3f'% i3 +" W/c^2")

def i1_polarizado_3filtros():
    i1_apos_primeiro_filtro = float(input("Raio após o primeiro filtro: \n"))
    angulo_filtro1 = float(input("qual é Angulo do primeiro filtro: \n"))
    angulo_filtro2 = float(input("qual é Angulo do segundo filtro: \n"))
    angulo_filtro3 = float(input("qual é Angulo do terceiro filtro: \n"))
    
    _, teta2 = calcular_intensidade_apos_primeiro_filtro(i1_apos_primeiro_filtro * 2, angulo_filtro2)
    i2 = calcular_intensidade_apos_segundo_filtro(i1_apos_primeiro_filtro, teta2)   
    _, teta3 = calcular_intensidade_apos_primeiro_filtro(i2, angulo_filtro3 - angulo_filtro2)
    i3 = calcular_intensidade_apos_terceiro_filtro(i2, teta3)
    
    print('Intensidade da luz incidente: %.3f'% (i1_apos_primeiro_filtro * 2) +" W/c^2")
    print('Intensidade da luz após o segundo filtro: %.3f'% i2 +" W/c^2")
    print('Intensidade da luz após o terceiro filtro: %.3f'% i3 +" W/c^2")

def i2_polarizado_3filtros():
    i2_apos_segundo_filtro = float(input("Raio após o segundo filtro: \n"))
    angulo_filtro1 = float(input("qual é Angulo do primeiro filtro: \n"))
    angulo_filtro2 = float(input("qual é Angulo do segundo filtro: \n"))
    angulo_filtro3 = float(input("qual é Angulo do terceiro filtro: \n"))
    
    i1 = i2_apos_segundo_filtro / (math.cos(math.radians(angulo_filtro2)) ** 2)
    i0 = i1 * 2
    _, teta3 = calcular_intensidade_apos_primeiro_filtro(i2_apos_segundo_filtro, angulo_filtro3 - angulo_filtro2)
    i3 = calcular_intensidade_apos_terceiro_filtro(i2_apos_segundo_filtro, teta3)
    
    print('Intensidade da luz incidente: %.3f'% i0 +" W/c^2")
    print('Intensidade da luz após o primeiro filtro: %.3f'% i1 +" W/c^2")
    print('Intensidade da luz após o terceiro filtro: %.3f'% i3 +" W/c^2")

def i3_polarizado_3filtros():
    i3_apos_terceiro_filtro = float(input("Raio após o terceiro filtro: \n"))
    angulo_filtro1 = float(input("qual é Angulo do primeiro filtro: \n"))
    angulo_filtro2 = float(input("qual é Angulo do segundo filtro: \n"))
    angulo_filtro3 = float(input("qual é Angulo do terceiro filtro: \n"))
    
    # Ângulos relativos
    angulo_entre_filtro1_e_filtro2 = angulo_filtro2 - angulo_filtro1
    angulo_entre_filtro2_e_filtro3 = angulo_filtro3 - angulo_filtro2
    
    # Calcular cossenos
    cos_filtro2 = math.cos(math.radians(angulo_entre_filtro1_e_filtro2))
    cos_filtro3 = math.cos(math.radians(angulo_entre_filtro2_e_filtro3))
    
    # Calcular intensidades
    i2 = i3_apos_terceiro_filtro / (cos_filtro3 ** 2)
    i1 = i2 / (cos_filtro2 ** 2)
    i0 = i1 * 2
    
    print('Intensidade da luz incidente: %.3f W/cm^2' % i0)
    print('Intensidade da luz após o primeiro filtro: %.3f W/cm^2' % i1)
    print('Intensidade da luz após o segundo filtro: %.3f W/cm^2' % i2)

def main():
    while True:
        print('\n==================== Menu ====================\n')
        print('🔵  1 - Filtro 1')
        print('🔵  2 - Dois Filtros')
        print('🔴  3 - Três Filtros')
        print('⚪  4 - Sair')
        print('\n==============================================\n')

        menu = input('Escolha uma das opções: ')

        if menu == '1':
            print('\n================ Filtro 1 ===================\n')
            print('🟢  1 - Calcular Intensidade Após Filtro')
            print('🟣  2 - Calcular Intensidade Não Polarizada Após Filtro')
            print('⬅️  3 - Voltar')
            print('\n==============================================\n')
            sub_menu = input('Escolha uma das opções: ')

            if sub_menu == '1':
                filtro1_1()
            elif sub_menu == '2':
                filtro1_2()
            elif sub_menu == '3':
                continue
            else:
                print('Opção inválida!')

        elif menu == '2':
            print('\n================ Dois Filtros =================\n')
            print('🟢  1 - Raio Incidente e Ângulo 1 e 2')
            print('🟣  2 - Raio 2 e Ângulo 1 e 2')
            print('🟠  3 - Raio Final e Ângulo 1 e 2')
            print('⬅️  4 - Voltar')
            print('\n==============================================\n')
            sub_menu = input('Escolha uma das opções: ')

            if sub_menu == '1':
                _2filtros_naopolarizado()
            elif sub_menu == '2':
                _2filtrospolarizadoi1()
            elif sub_menu == '3':
                _2filtrospolarizadosi2()
            elif sub_menu == '4':
                continue
            else:
                print('Opção inválida!')

        elif menu == '3':
            print('\n================ Três Filtros ================\n')
            print('🟢  1 - Raio Incidente e Ângulo 1, 2 e 3')
            print('🟣  2 - Raio 1 e Ângulo 1, 2 e 3')
            print('🟠  3 - Raio 2 e Ângulo 1, 2 e 3')
            print('🟤  4 - Raio 3 e Ângulo 1, 2 e 3')
            print('⬅️  5 - Voltar')
            print('\n==============================================\n')
            sub_menu = input('Escolha uma das opções: ')

            if sub_menu == '1':
                i0_nao_polarizado_3filtros()
            elif sub_menu == '2':
                i1_polarizado_3filtros()
            elif sub_menu == '3':
                i2_polarizado_3filtros()
            elif sub_menu == '4':
                i3_polarizado_3filtros()
            elif sub_menu == '5':
                continue
            else:
                print('Opção inválida!')

        elif menu == '4':
            print('Saindo do programa...')
            break
        else:
            print('Opção inválida!')
menu()
main()