import datetime
import time
import itertools
import platform
import os
import csv
import pandas as pd
# from reportlab.pdfgen import canvas # reportlab para exportar pdf
# from reportlab.lib.pagesizes import A4  # reportlab para exportar pdf (tamanho da página)

# TAO COPYRIGHT 2023 RODRIGO DIAS
# TELA INICIAL

def home():
    while True:
        cls()
        print('\n\n\n\n\n\n\nTAO | COPYRIGHT 2023 RODRIGO DIAS - VERSÃO '+ver)
        print('PLATAFORMA OPERACIONAL PARA MEDICINA CHINESA')
        print('TCM IN DFF-PERCEPTRONS NEURAL NETWORK AI FOR BACK-END PYTHON VER. ' +
              platform.python_version())
        print(horashu)
        global shu
        def shu(x): return print('\n'+horadia+'\nHORA DO SHU ATUAL: ' +shu_agora+'\nPRÓXIMA HORA EM SHU: '+shu_proximo+'\nESTAÇÃO: '+estação)
        shu('')
        if os.path.exists('registro_acupuntura.csv') == True and os.path.exists('ailog.csv') == True:
            print('\n\nBASE DE DADOS: ATIVA')
        else:
            print('\n\nBASE DE DADOS: INATIVA')
        print('\n___________________________________________________________')
        print('MENU:')
        print('[A] EXAME COMPLETO E PRESCRIÇÃO')
        print('[B] O QUE É ACUPUNTURA')
        print('[C] DIAGNÓSTICOS OPERACIONAIS DE PROGRAMA')
        print('[D] PRESCREVER PACIENTE SEM EXAME')
        print('[E] ATUALIZAÇÕES DO PROGRAMA')
        print('[F] CID11 NA MEDICINA CHINESA')
        print('[G] CONSULTAR BANCO DE DADOS')
        print('___________________________________________________________')
        print()
        global homm
        homm = input('Selecione opção: ').upper()
        if homm == 'A':
            cls()
            print('\n\n')
            global cpf
            cpf=str(input('Digite o CPF (sem pontos, traço ou espaços): '))
            if len(cpf)!=11 or cpf.isnumeric()==False:
                print('\nVerifique número a mais ou a menos ou retire símbolos.\nCPF inválido!\n\n')
                continue
            cpf.split()
            dez=cpf[0]
            nove=cpf[1]
            oito=cpf[2]
            sete=cpf[3]
            seis=cpf[4]
            cinco=cpf[5]
            quatro=cpf[6]
            três=cpf[7]
            dois=cpf[8]
            pre_dig10=int(dez)*10+int(nove)*9+int(oito)*8+int(sete)*7+int(seis)*6+int(cinco)*5+int(quatro)*4+int(três)*3+int(dois)*2
            dig10=pre_dig10%11
            if dig10>9:
                dig10=0
            d10=11-dig10
            if d10>9:
                d10=0
            dez = cpf[1]
            nove = cpf[2]
            oito = cpf[3]
            sete = cpf[4]
            seis = cpf[5]
            cinco = cpf[6]
            quatro = cpf[7]
            três = cpf[8]
            dois = d10
            pre_dig11 = int(dez)*10+int(nove)*9+int(oito)*8+int(sete)*7+int(seis)*6+int(cinco)*5+int(quatro)*4+int(três)*3+int(dois)*2
            dig11=pre_dig11%11
            if dig11>9:
                dig11=0
            d11=11-dig11
            if d11>9:
                d11=0
            oricpf=int(cpf[8])
            def origem(x):
                if x==1:
                    return 'DF/ GO/ MS/ MT/ TO'
                elif x==2:
                    return 'AC/ AM/ AP/ PA/ RO/ RR'
                elif x==3:
                    return 'CE/ MA/ PI'
                elif x==4:
                    return 'AL/ PB/ PE/ RN'
                elif x==5:
                    return 'BA/ SE'
                elif x==6:
                    return 'MG'
                elif x==7:
                    return 'ES/ RJ'
                elif x==8:
                    return 'SP'
                elif x==9:
                    return 'PR/ SC'
                elif x==0:
                    return 'RS'
            tcp=str(cpf[0])+str(cpf[1])+str(cpf[2])+str(cpf[3])+str(cpf[4])+str(cpf[5])+str(cpf[6])+str(cpf[7])+str(cpf[8])
            tescpf=str(tcp)+str(d10)+str(d11)
            if str(cpf)==str(tescpf):
                print('CPF verificado com sucesso!')
                print('CPF gerado em estado(s): '+origem(oricpf))
                time.sleep(6)
            else:
                print('CPF inválido!')
                continue
            global nome
            nome = input('Digite nome completo: ').upper()
            if len(nome) <= 8 or nome.isnumeric() == True or ' ' not in nome:
                print()
                print('Ops! Digite identificação para prosseguir...')
                time.sleep(2)
                continue
            else:
                nome1=nome.replace('Ç','C')
                nome2=nome1.replace('Á','A')
                nome3=nome2.replace('Ã','A')
                nome4=nome3.replace('É','E')         
                nome5=nome4.replace('È','E')
                nome6=nome5.replace('À','A')
                nome7=nome6.replace('Í','I')
                nome8=nome7.replace('Ô','O')
                nome9=nome8.replace('Ú','U')
                nome=str(nome9)
                while True:
                    try:
                        # ATENÇÃO: ALTERAR ABAIXO DEVE SER DUPLICADO PARA HOMM='D'
                        global sexo
                        sexo = input('Sexo feminino(F) ou masculino(M)? F/M ').upper()
                        if sexo == 'M' or sexo == 'F':
                            ddtot = str(input('Data de Nascimento: '))
                            # codificação para aceitar: ddmmyy, dd/mm/yy, dd/mm/yyyy, ddmmyyyy
                            ano_comparador=int(ger_hor_atu.strftime("%Y"),10)
                            if len(ddtot) == 6 and ddtot.isnumeric() == True:
                                ddtot.split()
                                pra_especcodcompa_dn = ddtot[4]+ddtot[5]
                                propro_especcodcompa_dn = int(pra_especcodcompa_dn, 10)
                                pre_especcodcompa_dn = str(
                                            input('Digite A para 1900 e B para 2000: '))
                                pre_especcodcompa_dn.upper()
                                if pre_especcodcompa_dn == 'A':
                                    especcodcompa_dn = 1900+propro_especcodcompa_dn
                                    # VERIFICAÇÃO DE SÉCULO (1900 E 2000)
                                    if ano_comparador < especcodcompa_dn:
                                        print('ERRO DE DATAS!')
                                        continue
                                if pre_especcodcompa_dn == 'B':
                                    especcodcompa_dn = 2000+propro_especcodcompa_dn
                                    # VERIFICAÇÃO DE SÉCULO (1900 E 2000)
                                    if ano_comparador < especcodcompa_dn:
                                        print('ERRO DE DATAS!')
                                        continue
                                dtot = str(ddtot)
                                print('sucesso!')
                            # DD/MM/YY
                            if len(ddtot) == 8 and ddtot.isnumeric() == False:
                                subdtot = ddtot.split('/')
                                pre_especcodcompa_dn = str(
                                    input('Digite A para 1900 e B para 2000: '))
                                pre_especcodcompa_dn.upper()
                                if pre_especcodcompa_dn == 'A':
                                    pro_especcodcompa_dn = 1900
                                    # VERIFICAÇÃO DE SÉCULO (1900 E 2000)
                                    if ano_comparador < especcodcompa_dn:
                                        print('ERRO DE DATAS!')
                                        break
                                if pre_especcodcompa_dn == 'B':
                                    pro_especcodcompa_dn = 2000
                                    sub_especcodcompa_dn = subdtot[2]
                                    subsub_especcodcompa_dn = int(sub_especcodcompa_dn, 10)
                                    especcodcompa_dn = subsub_especcodcompa_dn+pro_especcodcompa_dn
                                    # VERIFICAÇÃO DE SÉCULO (1900 E 2000)
                                    if ano_comparador < especcodcompa_dn:
                                        print('ERRO DE DATAS!')
                                        break
                                parte1 = subdtot[0]
                                parte2 = subdtot[1]
                                parte3 = subdtot[2]
                                str(parte1)
                                if len(parte1) == 2:
                                    parte1_ddtot = parte1
                                if len(parte1) == 1:
                                    parte1_ddtot = '0'+parte1
                                str(parte2)
                                if len(parte2) == 2:
                                    parte2_ddtot = parte2
                                if len(parte2) == 1:
                                    parte2_ddtot = '0'+parte2
                                str(parte3)
                                if len(parte3) == 2:
                                    parte3_ddtot = parte3
                                if len(parte3) == 1:
                                    parte3_ddtot = '0'+parte3
                                dtot = parte1_ddtot+parte2_ddtot+parte3_ddtot
                                print('sucesso!')
                            # DDMMYYYY
                            if len(ddtot) == 8 and ddtot.isnumeric() == True:
                                ddtot.split()
                                pre_especcodcompa_dn = ddtot[4]+ddtot[5]+ddtot[6]+ddtot[7]
                                especcodcompa_dn = int(pre_especcodcompa_dn, 10)
                                # VERIFICAÇÃO DE SÉCULO (1900 E 2000)
                                if ano_comparador < especcodcompa_dn:
                                    print('ERRO DE DATAS!')
                                parte1 = ddtot[0]+ddtot[1]
                                str(parte1)
                                if len(parte1) == 2:
                                    parte1_ddtot = parte1
                                if len(parte1) == 1:
                                    parte1_ddtot = '0'+parte1
                                parte2 = ddtot[2]+ddtot[3]
                                str(parte2)
                                if len(parte2) == 2:
                                    parte2_ddtot = parte2
                                if len(parte2) == 1:
                                    parte2_ddtot = '0'+parte2
                                parte3 = ddtot[6]+ddtot[7]
                                str(parte3)
                                if len(parte3) == 2:
                                    parte3_ddtot = parte3
                                if len(parte3) == 1:
                                    parte3_ddtot = '0'+parte3
                                dtot = str(parte1_ddtot)+str(parte2_ddtot)+str(parte3_ddtot)
                                print('sucesso!')
                            # DD/MM/YYYY
                            if len(ddtot) == 10 and ddtot.isnumeric() == False:
                                sudd = ddtot.split('/')
                                pro_especcodcompa_dn = sudd[2]
                                especcodcompa_dn = int(pro_especcodcompa_dn, 10)
                                   # VERIFICAÇÃO DE SÉCULO (1900 E 2000)
                                if ano_comparador < especcodcompa_dn:
                                    print('ERRO DE DATAS!')
                                    continue
                                parte1_ddtot = sudd[0]
                                parte2_ddtot = sudd[1]
                                parte3_ddtot = sudd[2]
                                parte3_ddtot.split()
                                pro3 = parte3_ddtot[2]+parte3_ddtot[3]
                                dtot = parte1_ddtot+parte2_ddtot+pro3
                                print('sucesso!')

                              # fim de datação especial, saída em str 'dtot'

                            dtot.split()
                            dn1 = dtot[0]
                            str(dn1)
                            dn2 = dtot[1]
                            str(dn2)
                            dn3 = dtot[4]
                            str(dn3)
                            dn4 = dtot[5]
                            str(dn4)
                            global expodn
                            expodn = dtot[0]+dtot[1]+'/'+dtot[2]+dtot[3]+'/' + dtot[4]+dtot[5]   # STRING DE DATA DE NASCIMENTO
                            idi = dtot[4]+dtot[5]
                            idi = int(idi, 10)
                            if idi > anoge:  # vei, funcionando
                                anonew = anoge+100
                                idint = anonew-idi
                            if idi <= anoge:  # novin
                                idint = anoge-idi
                            print()
                            # IDSTR EXPORTA STR COM DATA VIA CÁLCULO DE NASCIMENTO
                            idstr = str(idint)
                            print('IDADE: '+idstr+' ANOS')
                            global idd
                            idd = int(idstr)
                            if idd > 5 or idd < 110:
                                if sexo == 'M':
                                    global acompanhante
                                    acompanhante = 'NÃO NECESSÁRIO ACOMPANHANTE'
                                    print(acompanhante)
                                    print()
                                    time.sleep(3)
                                    break
                                if sexo == 'F':
                                    print(
                                        '\n\nREGISTRO DE ACOMPANHANTE EM INFORMAÇÕES A SEGUIR:')
                                    aco1 = input(
                                        'Nome completo de acompanhante: ').upper()
                                    aco2 = input(
                                        'Vinculo com paciente (mãe, marido, amiga): ').upper()
                                    if aco2 != '':
                                        aco3 = str(input(
                                            'Data de nascimento do(a) acompanhante (obrigatório formato xx/xx/xxxx): '))
                                        ida3 = aco3.split('/')
                                        ida = int(ida3[2])
                                        idh = int(ger_hor_atu.strftime("%Y"))
                                        idade = idh-ida
                                        if idade > 0:
                                            idade1 = str(idade)
                                            aco4 = str(
                                                input('Telefone do acompanhante com DDD (sem sinais): '))
                                            if len(aco4) > 9:
                                                acompanhante = aco1+', '+aco2+', data de nascimento em ' + \
                                                    aco3+', idade: '+idade1 + \
                                                    ' anos, contato: ' + \
                                                    str(aco4)
                                                print(
                                                    'ACOMPANHADA DURANTE A SESÃO DE: '+acompanhante)
                                                print()
                                                time.sleep(6)
                                                break
                                            else:
                                                print(
                                                    'ERRO AO INSERIR NÚMERO DE TELEFONE, TENTE NOVAMENTE')
                                                continue
                                        else:
                                            print(
                                                'FORMATO DE IDADE DEVE SER EXATAMENTE COMO SOLICITADO!')
                                            continue
                                    else:
                                        continue
                    except:
                        continue
                print('\n\n')
                ben()
        if homm == 'C':
            lista()
        if homm == 'D':
            cls()
            print('\n\n')
            cpf = str(input('Digite o CPF (sem pontos, traço ou espaços): '))
            if len(cpf) != 11 or cpf.isnumeric() == False:
                print(
                    '\nVerifique número a mais ou a menos ou retire símbolos.\nCPF inválido!\n\n')
                continue
            cpf.split()
            dez = cpf[0]
            nove = cpf[1]
            oito = cpf[2]
            sete = cpf[3]
            seis = cpf[4]
            cinco = cpf[5]
            quatro = cpf[6]
            três = cpf[7]
            dois = cpf[8]
            pre_dig10 = int(dez)*10+int(nove)*9+int(oito)*8+int(sete)*7 + \
                int(seis)*6+int(cinco)*5+int(quatro)*4+int(três)*3+int(dois)*2
            dig10 = pre_dig10 % 11
            if dig10 > 9:
                dig10 = 0
            d10 = 11-dig10
            if d10 > 9:
                d10 = 0
            dez = cpf[1]
            nove = cpf[2]
            oito = cpf[3]
            sete = cpf[4]
            seis = cpf[5]
            cinco = cpf[6]
            quatro = cpf[7]
            três = cpf[8]
            dois = d10
            pre_dig11 = int(dez)*10+int(nove)*9+int(oito)*8+int(sete)*7 + \
                int(seis)*6+int(cinco)*5+int(quatro)*4+int(três)*3+int(dois)*2
            dig11 = pre_dig11 % 11
            if dig11 > 9:
                dig11 = 0
            d11 = 11-dig11
            if d11 > 9:
                d11 = 0
            oricpf = int(cpf[8])

            def origem(x):
                if x == 1:
                    return 'DF/ GO/ MS/ MT/ TO'
                elif x == 2:
                    return 'AC/ AM/ AP/ PA/ RO/ RR'
                elif x == 3:
                    return 'CE/ MA/ PI'
                elif x == 4:
                    return 'AL/ PB/ PE/ RN'
                elif x == 5:
                    return 'BA/ SE'
                elif x == 6:
                    return 'MG'
                elif x == 7:
                    return 'ES/ RJ'
                elif x == 8:
                    return 'SP'
                elif x == 9:
                    return 'PR/ SC'
                elif x == 0:
                    return 'RS'
            tcp = str(cpf[0])+str(cpf[1])+str(cpf[2])+str(cpf[3]) + \
                str(cpf[4])+str(cpf[5])+str(cpf[6])+str(cpf[7])+str(cpf[8])
            tescpf = str(tcp)+str(d10)+str(d11)
            if str(cpf) == str(tescpf):
                print('CPF verificado com sucesso!')
                print('CPF gerado em estado(s): '+origem(oricpf))
                time.sleep(6)
            else:
                print('CPF inválido!')
                continue
            nome = input('Digite nome completo: ').upper()
            if len(nome) <= 8 or nome.isnumeric() == True or ' ' not in nome:
                print()
                print('Ops! Digite identificação para prosseguir...')
                time.sleep(2)
                continue
            else:
                nome1=nome.replace('Ç','C')
                nome2=nome1.replace('Á','A')
                nome3=nome2.replace('Ã','A')
                nome4=nome3.replace('É','E')         
                nome5=nome4.replace('È','E')
                nome6=nome5.replace('À','A')
                nome7=nome6.replace('Í','I')
                nome8=nome7.replace('Ô','O')
                nome9=nome8.replace('Ú','U')
                nome=str(nome9)
                while True:
                    try:
                        # ATENÇÃO: ALTERAR ABAIXO DEVE SER DUPLICADO PARA HOMM='D'
                        sexo = input(
                            'Sexo feminino(F) ou masculino(M)? F/M ').upper()
                        if sexo == 'M' or sexo == 'F':
                            ddtot = str(input('Data de Nascimento: '))
                            # codificação para aceitar: ddmmyy, dd/mm/yy, dd/mm/yyyy, ddmmyyyy
                            ano_comparador = int(
                                ger_hor_atu.strftime("%Y"), 10)
                            if len(ddtot) == 6 and ddtot.isnumeric() == True:
                                ddtot.split()
                                pra_especcodcompa_dn = ddtot[4]+ddtot[5]
                                propro_especcodcompa_dn = int(
                                    pra_especcodcompa_dn, 10)
                                pre_especcodcompa_dn = str(
                                    input('Digite A para 1900 e B para 2000: '))
                                pre_especcodcompa_dn.upper()
                                if pre_especcodcompa_dn == 'A':
                                    especcodcompa_dn = 1900+propro_especcodcompa_dn
                                    # VERIFICAÇÃO DE SÉCULO (1900 E 2000)
                                    if ano_comparador < especcodcompa_dn:
                                        print('ERRO DE DATAS!')
                                        continue
                                if pre_especcodcompa_dn == 'B':
                                    especcodcompa_dn = 2000+propro_especcodcompa_dn
                                    # VERIFICAÇÃO DE SÉCULO (1900 E 2000)
                                    if ano_comparador < especcodcompa_dn:
                                        print('ERRO DE DATAS!')
                                        continue
                                dtot = str(ddtot)
                                print('sucesso!')
                            # DD/MM/YY
                            if len(ddtot) == 8 and ddtot.isnumeric() == False:
                                subdtot = ddtot.split('/')
                                pre_especcodcompa_dn = str(
                                    input('Digite A para 1900 e B para 2000: '))
                                pre_especcodcompa_dn.upper()
                                if pre_especcodcompa_dn == 'A':
                                    pro_especcodcompa_dn = 1900
                                    # VERIFICAÇÃO DE SÉCULO (1900 E 2000)
                                    if ano_comparador < especcodcompa_dn:
                                        print('ERRO DE DATAS!')
                                        continue
                                if pre_especcodcompa_dn == 'B':
                                    pro_especcodcompa_dn = 2000
                                    sub_especcodcompa_dn = subdtot[2]
                                    subsub_especcodcompa_dn = int(
                                        sub_especcodcompa_dn, 10)
                                    especcodcompa_dn = subsub_especcodcompa_dn+pro_especcodcompa_dn
                                    # VERIFICAÇÃO DE SÉCULO (1900 E 2000)
                                if ano_comparador < especcodcompa_dn:
                                    print('ERRO DE DATAS!')
                                    continue
                                parte1 = subdtot[0]
                                parte2 = subdtot[1]
                                parte3 = subdtot[2]
                                str(parte1)
                                if len(parte1) == 2:
                                    parte1_ddtot = parte1
                                if len(parte1) == 1:
                                    parte1_ddtot = '0'+parte1
                                str(parte2)
                                if len(parte2) == 2:
                                    parte2_ddtot = parte2
                                if len(parte2) == 1:
                                    parte2_ddtot = '0'+parte2
                                str(parte3)
                                if len(parte3) == 2:
                                    parte3_ddtot = parte3
                                if len(parte3) == 1:
                                    parte3_ddtot = '0'+parte3
                                dtot = parte1_ddtot+parte2_ddtot+parte3_ddtot
                                print('sucesso!')
                            # DDMMYYYY
                            if len(ddtot) == 8 and ddtot.isnumeric() == True:
                                ddtot.split()
                                pre_especcodcompa_dn = ddtot[4] + \
                                    ddtot[5]+ddtot[6]+ddtot[7]
                                especcodcompa_dn = int(
                                    pre_especcodcompa_dn, 10)
                                # VERIFICAÇÃO DE SÉCULO (1900 E 2000)
                                if ano_comparador < especcodcompa_dn:
                                    print('ERRO DE DATAS!')
                                parte1 = ddtot[0]+ddtot[1]
                                str(parte1)
                                if len(parte1) == 2:
                                    parte1_ddtot = parte1
                                if len(parte1) == 1:
                                    parte1_ddtot = '0'+parte1
                                parte2 = ddtot[2]+ddtot[3]
                                str(parte2)
                                if len(parte2) == 2:
                                    parte2_ddtot = parte2
                                if len(parte2) == 1:
                                    parte2_ddtot = '0'+parte2
                                parte3 = ddtot[6]+ddtot[7]
                                str(parte3)
                                if len(parte3) == 2:
                                    parte3_ddtot = parte3
                                if len(parte3) == 1:
                                    parte3_ddtot = '0'+parte3
                                dtot = str(parte1_ddtot) + \
                                    str(parte2_ddtot)+str(parte3_ddtot)
                                print('sucesso!')
                            # DD/MM/YYYY
                            if len(ddtot) == 10 and ddtot.isnumeric() == False:
                                sudd = ddtot.split('/')
                                pro_especcodcompa_dn = sudd[2]
                                especcodcompa_dn = int(
                                    pro_especcodcompa_dn, 10)
                                # VERIFICAÇÃO DE SÉCULO (1900 E 2000)
                                if ano_comparador < especcodcompa_dn:
                                    print('ERRO DE DATAS!')
                                    continue
                                parte1_ddtot = sudd[0]
                                parte2_ddtot = sudd[1]
                                parte3_ddtot = sudd[2]
                                parte3_ddtot.split()
                                pro3 = parte3_ddtot[2]+parte3_ddtot[3]
                                dtot = parte1_ddtot+parte2_ddtot+pro3
                                print('sucesso!')

                              # fim de datação especial, saída em str 'dtot'

                            dtot.split()
                            dn1 = dtot[0]
                            str(dn1)
                            dn2 = dtot[1]
                            str(dn2)
                            dn3 = dtot[4]
                            str(dn3)
                            dn4 = dtot[5]
                            str(dn4)
                            # STRING DE DATA DE NASCIMENTO
                            expodn = dtot[0]+dtot[1]+'/' + \
                                dtot[2]+dtot[3]+'/' + dtot[4]+dtot[5]
                            idi = dtot[4]+dtot[5]
                            idi = int(idi, 10)
                            if idi > anoge:  # vei, funcionando
                                anonew = anoge+100
                                idint = anonew-idi
                            if idi <= anoge:  # novin
                                idint = anoge-idi
                            print()
                            # IDSTR EXPORTA STR COM DATA VIA CÁLCULO DE NASCIMENTO
                            idstr = str(idint)
                            print('IDADE: '+idstr+' ANOS')
                            idd = int(idstr)
                            if idd > 5 or idd < 110:
                                if sexo == 'M':
                                    acompanhante = 'NÃO NECESSÁRIO ACOMPANHANTE'
                                    print(acompanhante)
                                    print()
                                    time.sleep(3)
                                    break
                                if sexo == 'F':
                                    print(
                                        '\n\nREGISTRO DE ACOMPANHANTE EM INFORMAÇÕES A SEGUIR:')
                                    aco1 = input(
                                        'Nome completo de acompanhante: ').upper()
                                    aco2 = input(
                                        'Vinculo com paciente (mãe, marido, amiga): ').upper()
                                    if aco2 != '':                                      
                                        aco3=str(input('Data de nascimento do(a) acompanhante (obrigatório formato xx/xx/xxxx): '))
                                        ida3 = aco3.split('/')
                                        ida = int(ida3[2])
                                        idh=int(ger_hor_atu.strftime("%Y"))
                                        idade = idh-ida
                                        if idade>0:
                                            idade1=str(idade)
                                            aco4 = str(input('Telefone do acompanhante com DDD (sem sinais): '))
                                            if len(aco4) > 9:
                                                acompanhante = aco1+', '+aco2+', data de nascimento em ' +aco3+', idade: '+idade1+' anos, contato: '+str(aco4)
                                                print(
                                                    'ACOMPANHADA DURANTE A SESÃO DE: '+acompanhante)
                                                print()
                                                time.sleep(6)
                                                break
                                            else:
                                                print('ERRO AO INSERIR NÚMERO DE TELEFONE, TENTE NOVAMENTE')
                                                continue
                                        else:
                                            print('FORMATO DE IDADE DEVE SER EXATAMENTE COMO SOLICITADO!')
                                            continue
                                    else:
                                        continue
                    except:
                        continue
                print('\n\n')
                only()

        if homm == 'B':
            sobre()
        if homm == 'E':
            atualiz()
        if homm == 'F':
            cid()
        if homm=='G':
            cls()
            if os.path.exists('registro_acupuntura.csv') == True:
                print('\n\n\n')
                df = pd.read_csv('registro_acupuntura.csv')
                print(df)
                #  CORREÇÃO DE ORDEM DE COLUNAS
                #  df=pd.read_csv('pip_log2.csv')
                # df['DATA DE EMISSÃO']=pd.to_datetime(df['DATA DE EMISSÃO'])
                # readydf=df.sort_values(by='DATA DE EMISSÃO')
                # readydf.to_csv('pip_log3.csv')
                time.sleep(3)
                x=input('\n\nPARA RETORNAR APERTE QUALQUER TECLA...')
                continue
            else:
                print('\n\n\nARQUIVO DE DADOS OU CONEXÃO COM BANCO DE DADOS NÃO EFETIVADA')
                print("CASO DESEJA REINICIAR BANCO DE DADOS LOCALMENTE, ACESSE OPÇÃO 'H' EM MENU")
                time.sleep(9)
                continue
        if homm=='H':
            gerar_arquivos()

def ben():
    while True:
        print('\n\nINICIANDO AVALIAÇÃO')
        cls()
        print()
        print('HISTÓRIA DA DOENÇA ATUAL \n(PRIMEIRA SESSÃO, TRATAMENTOS MÉDICOS, MEDICAMENTOS CRÔNICOS, EXPECTATIVA SOBRE A ACUPUNTURA):\n')
        global hda
        hda = input('>>> ').upper()
        cls()
        if len(hda) > 54:
            print('\n\n\n\n\nESTE EXAME SERÁ AUTOMATICAMENTE REDIRECIONADO PARA QUESTIONÁRIO DE PROTOCOLOS DEVIDO A HISTÓRIA CLÍNICA COMPLEXA')
            time.sleep(4)
            cls()
        termoquery = input(
            '\n\nOCORRE SINTOMAS TÉRMICOS? CALOR, FRIO, PELE SECA OU ÚMIDA OU MESMO EDEMA? (S/N) ').upper()
        global h3
        h3 = set()
        if termoquery == 'S':
            print('\nSENSAÇÃO DE FRIO\nA- VIRILHA/LOMBAR\nB- ABDOME\nC- MÃO E PÉ \nD- SÓ MÃO \nE- SÓ PÉ \nF- SÓ PONTAS DE DEDOS\n\nSENSAÇÃO DE CALOR\nG- CALOR COM EXTERNO QUENTE\nH- QUENTE QUE NORMALIZA AO PEGAR\nI- QUENTE EM VASOS\nJ- FRIO FORA E CALOR EM OSSO\n\nJIN YE - FLUIDOS\nK- PELE ÚMIDA E INCÔMODO DO PACIENTE\nL- PELE ÚMIDA SEM INCÔMODO\nM- PELE SECA SEM DESCAMAR\nN- PELE ÁSPERA\nO- SECA COM DESCAMAÇÃO\nP- EDEMA CACIFO POSITIVO\nQ- EDEMA CACIFO NEGATIVO\nR- PRURIDO\n\n')
            global h2
            h2 = input('DIGITE LETRAS DE QUESTIONÁRIO ACIMA: ').upper()
            if 'A' in h2:
                h3.add('DEFICIÊNCIA YANG DE ÁGUA')
            if 'B' in h2:
                h3.add('DEFICIÊNCIA YANG DE TERRA')
            if 'C' in h2:
                if sexo == 'H':
                    h3.add('DEFICIÊNCIA YANG DE TERRA')
                if sexo == 'F':
                    h3.add('DEFICIÊNCIA DE XUE')
            if 'D' in h2:
                if sexo == 'H':
                    h3.add('DEFICIÊNCIA YANG DE METAL OU DE FOGO')
                if sexo == 'M':
                    h3.add('DEFICIÊNCIA YANG DE FOGO')
            if 'E' in h2:
                if sexo == 'H':
                    h3.add('DEFICIÊNCIA YANG DE ÁGUA')
                if sexo == 'F':
                    h3.add('DEFICIÊNCIA YANG DE MADEIRA')
            if 'F' in h2:
                h3.add('ESTAGNAÇÃO DE QI DE MADEIRA')
            if 'G' in h2:
                h3.add('UMIDADE E CALOR')
            if 'H' in h2:
                h3.add('VENTO E CALOR')
            if 'I' in h2:
                h3.add('CALOR DE TA-MÉDIO OU CORAÇÃO')
            if 'J' in h2:
                h3.add('CALOR VAZIO')
            if 'K' in h2:
                h3.add('VENTO EXTERNO')
            if 'L' in h2:
                h3.add('DEFICIÊNCIA YIN DE METAL')
            if 'M' in h2:
                h3.add('DEFICIÊNCIA DE XUE DE METAL E DEFICIÊNCIA YIN DE METAL')
            if 'N' in h2:
                h4 = input('QUAL(QUAIS) O(S) MERIDIANO(S) ONDE SE LOCALIZA(M) A(S) REGIÃO(ÕES) ÁSPERA(S)? ').upper()
                h3.add('DOR DE VENTO EM '+str(h4))
            if 'O' in h2:
                h3.add('SECURA INDETERMINADA OU DEFICIÊNCIA DE XUE DE MADEIRA')
            if 'P' in h2:
                h3.add('DEFICIÊNCIA YANG DE ÁGUA E TERRA')
            if 'Q' in h2:
                h3.add('ESTAGNAÇÃO DE QI POR FLEUMA')
            if 'R' in h2:
                h3.add('DISTÚRBIO DE PO')
        if len(h3)==0:
            h3.add('Assintomático termico-sensorial'.upper())
        print('\n')
        print(h3)
        print()
        dorquery = input('\n\nESTÁ COM DOR OU TEM DOR CRÔNICA? (S/N) ').upper()
        global h8
        h8 = set()
        if dorquery == 'S':
            cls()
            print('\n\nTIPOS DE DOR:\nA- DOR CHEIA: INTENSA, DELIMITADA, MELHORA COM MOVIMENTO, INICIA MUITO RÁPIDO, PRESSÃO PIORA\nB- DOR VAZIA: DIFUSA E FRACA PORÉM NUNCA CESSA, MELHORA EM REPOUSO (AO ACORDAR NÃO SENTE), INICIA DEVAGAR, APERTAR LOCAL MELHORA DOR\nC- DOR DE FRIO: PIORA COM FRIO E MELHORA COM CALOR, LOCAL PODE ESTAR AZUL\nD- DOR DE CALOR: PIORA COM MOVIMENTO E CALOR, MELHORA COM GELO, LOCAL PODE ESTAR MAIS VERMELHO\n\nLOCALIZAÇÃO DE DOR POR MERIDIANO MAIS PRÓXIMO:\n(E) PC/TA\n        PC- MMSS, FACE ANTERIOR, 3° DEDO POSTERIOR, MEIO DE ANTEBRAÇO/BRAÇO, AXILA/TÓRAX ANTERIOR\n        TA- LATERAL DE OLHOS, TEMPORAL, ORELHA POSTERIOR, OMBRO, CLAVÍCULA, COTOVELO, FACE POSTERIOR MMSS MEDIAL, 4° DEDO POSTERIOR\n(F) C/ID\n        C- MMSS ANTERIOR, 5° DEDO ANTERIOR, FACE ANTEROINFERIOR DE MMSS, AXILA INTERNA\n        ID- MMSS POSTEROINFERIOR, 5° DEDO POSTERIOR, EPICÔNDILO MEDIAL, FACE SUPERIOR DE ESCÁPULA, ROMBÓIDES, ATM, SINUS NASAIS, TRAGUS AURICULAR\n(G) BP/E\n        BP- TÓRAX LATERAL, MAMA LATERAL, SUPERFÍCIE COSTAL, ABDOME PARAMEDIANO, PELVE, MMII ANTEROMEDIAL, MEDIAL DE JOELHOS, PÉ MEDIAL, 1° DEDO (HÁLUX)\n        E- MMII, 2° DEDO, MMII ANTEROLATERAL, JOELHO LATERAL, LATERAL DE ABDOME E TÓRAX, CLAVÍCULA, TIREÓIDE, FACE LATERAL E FACE PARAMEDIANA EM LINHA OCULAR\n(H) P/IG\n        P- PÓLUX, MMSS ANTEROSUPERIOREPICÔNDILO LATERAL E INFRACLAVICULAR\n        IG- MMSS LATEROPOSTEROSUPERIOR, 2° DEDO MMSS POSTERIOR, ACRÔMIOCLAVICULAR E PARANASAL\n(I) R/B\n        R- PLANTAR MEDIAL, CÔNDILO MEDIAL, TENDÂO CALCÂNEO MEDIAL, MMII MEDIAL MAIS AXIAL, COXA INTERNA, INGUINAL, ABDOME PARAMEDIANO, LINHA MAMÁRIA MÉDIA, LINHA MÉDIO-TROCANTÉRICA\n        B- PÉ LATERODORSAL, CÔNDILO LATERAL, CALCÂNEO LATERAL, SULCO INTERGASTROCNÊMIO, POSTERIOR MEDIAL DE PERNA/COXA, NÁDEGAS, ÂNUS, PARAESPINHAL, OCCIPTOPARIETAL, LINHA PARAMEDIANA DORSAL\n(J) F/VB\n        F- MMII, HÁLUX DORSAL (LATERAL), TÍBIA ANTEROMEDIAL, POPLÍTEO, VASTO MEDIAL MEDIAL, INSERÇÃO DE SARTÓRIO (INFEROINGUINAL), ABDOME ANTERIOR EM PONTA DE 12ª COSTELA E SUPERFÍCIE COSTO-MAMÁRIA\n        VB- LATERAL DE 4° DEDO DE MMII, PLATÔ INTERCÔNDILO DE TORNOZELO ANTERIOR, LATERAL DE FÍBULA, GASTROCNÊMIO LATERAL, JOELHO LATERAL, COXA LATERAL EM TENSOR DE FÁSCIA LATA, ASA ILÍACA, PÉLVE INTERNA POSTERIOR, ABDOME LATERAL, AXILA ANTERIOR, CRÂNIO TEMPORAL E PARIETAL, MENTO')
            h5 = input('\n\nDIGITE DOR E LOCAL (AF, AG, DI) OU X CASO A REGIÃO DE DOR SEJA DIFERENTE DE UM MERIDIANO: ').upper()
            if 'X' in h5:
                print('\nDOR EM JING JIN (CANAL TENDINOMUSCULARES)\nK- JING JIN PC- TODA ÁREA DO PC ADICIONANDO: LINHA MAMILO-MANÚBRIO E ÁREA INFEROAXILAR ABAIXO DA MAMA\nL- JING JIN TA- TODA ÁREA DO TA ADICIONANDO: ORELHA ANTERIOR, ÁREA DO TRIGÊMIO INFERIOR, ÓRBITA EXTERNA, ZONA TEMPORAL ANTERIOR (FACE SOMENTE)\nM- JING JIN C- TODA ÁREA DO C ADICIONANDO:  ZONA PERIMAMILAR E LINHA MEDIANA DE MANÚBRIO AO UMBIGO, SOBREPONDO LINHA DO REN MAI)\nN- JING JIN ID- TODA ÁREA DO ID ADICIONANDO: SUPERFÍCIE EXTERNA COMPLETA DA CLAVÍCULA, AO REDOR DA ORELHA (CIRCULAR), ROSTO LATERAL (PARALELO A CANTO EXTERNO DO OLHO, DE MENTO ATÉ CABELO)\nP- JING JIN BP- TODA ÁREA DO BP ADICIONANDO: GENITAIS, HIPOCÔNDRIO DIREITO E ESQUERDO E ARCOS COSTAIS ANTERIORES (TODOS)\nQ- JING JIN E- TODA ÁREA DO E ADICIONANDO: COXA LATERAL ANTERIOR, FLANCOS E LATERAL DE NARIZ\nR- JING JIN P- TODA ÁREA DO P ADICIONANDO: ÁREA DO M. SUPRAESPINHAL (SUPRAESCAPULAR) E INFRA-AXILAR\nS- JING JIN IG- TODA ÁREA DO IG ADICIONANDO: LATERAL DO BÍCEPS, ZONA DO ROMBÓIDE, SUPRACLAVICULAR ANTERIOR, CIRCULARMENTE EM PARTES EXTERNAS DA FACE (PLANO CORONAL DE FACE)\nT- JING JIN R- TODA ÁREA DO R ADICIONANDO: FACE PLANTAR MEDIAL, ZONA GENITOCRURAL, PARAVERTEBRAIS, PARÁBOLA ENTRE GENITAL E POUPA INFERIOR DA NÁDEGAS ATÉ REGIÃO SACRAL (PARTE INFERIOR LATERALMENTE DA ROUPA ÍNTIMA), REGIÃO ATLANTOOCCIPTAL\nU- JING JIN B- TODA ÁREA DO B ADICIONANDO: ZONA DO ÂNGULO INFERIOR DA ESCÁPULA, REGIÃO PARIETAL, ZONAS FACIAIS MENTONIANAS, SUPRA ORBICULARES, LINHA MENTOCLAVICULAR E SULCO ANTERIOR DE DELTÓIDE (COMO A ALÇA DE UMA MOCHILA)\nV- JING JIN F- TODA ÁREA DO F ADICIONANDO: REGIÃO GENITAL\nW- JING JIN VB- TODA ÁREA DO VB ADICIONANDO: ÁREA DO JOELHO, ÁREA GLÚTEA SOBREPOSTA AO GLÚTEO MÍNIMO, INTERCOSTAIS LATERAIS, REGIÃO TEMPORAL')
                hx=input('DIGITE TIPO DE DOR (SOMENTE CHEIA OU VAZIA SÃO POSSÍVEIS) E REGIÃO ACOMETIDA (AK, BW): ').upper()
                if len(hx)==0:
                    h8.add('PACIENTE NEGOU DOR PARA ESTA AVALIAÇÃO')
                    print(h8)
                else:
                    if len(hx)==2 and 'A' in hx or 'B' in hx:
                        hx.split()
                        if hx[0]=='A':
                            global hx1
                            hx1='DOR CHEIA EM JING JIN DE '
                        if hx[0]=='B':
                            hx1='DOR VAZIA EM JING JIN DE '                            
                        if hx[1]=='K':
                            h8.add(hx1+'PERICÁRDIO')
                            print('\n\n')
                            print(h8)
                        if hx[1]=='L':
                            h8.add(hx1+'TRIPLO AQUECEDOR')
                            print('\n\n')
                            print(h8)
                        if hx[1]=='M':
                            h8.add(hx1+'CORAÇÃO')
                            print('\n\n')
                            print(h8)
                        if hx[1]=='N':
                            h8.add(hx1+'INTESTINO DELGADO')
                            print('\n\n')
                            print(h8)
                        if hx[1]=='P':
                            h8.add(hx1+'BAÇO')
                            print('\n\n')
                            print(h8)
                        if hx[1]=='Q':
                            h8.add(hx1+'ESTÔMAGO')
                            print('\n\n')
                            print(h8)
                        if hx[1]=='R':
                            h8.add(hx1+'PULMÃO')
                            print('\n\n')
                            print(h8)
                        if hx[1]=='S':
                            h8.add(hx1+'INTESTINO GROSSO')
                            print('\n\n')
                            print(h8)
                        if hx[1]=='T':
                            h8.add(hx1+'RIM')
                            print('\n\n')
                            print(h8)
                        if hx[1]=='U':
                            h8.add(hx1+'BEXIGA')
                            print('\n\n')
                            print(h8)
                        if hx[1]=='V':
                            h8.add(hx1+'FÍGADO') 
                            print('\n\n')
                            print(h8)
                        if hx[1]=='W':
                            h8.add(hx1+'VESÍCULA BILIAR') 
                            print('\n\n')
                            print(h8)
                        else:
                            print('DEVE SER DIGITADO CONFORME ESPECIFICADO ACIMA!')
                            continue                                                                                                                                                                                                                                                                                                                                      
                    else:
                        print('DEVE SER DIGITADO CONFORME ESPECIFICADO ACIMA!')
                        continue
            else:
                e = 'FOGO MINISTERIAL'
                f = 'FOGO IMPERIAL'
                g = 'TERRA'
                h = 'METAL'
                i = 'ÁGUA'
                j = 'MADEIRA'
                if 'A' in h5:
                    h6 = 'ESTAGNAÇÃO DE QI, ESTAGNAÇÃO DE XUE EM '
                    if 'AE' in h5:
                        h8.add(h6+e)
                    if 'AF' in h5:
                        h8.add(h6+f)
                    if 'AG' in h5:
                        h8.add(h6+g)
                    if 'AH' in h5:
                        h8.add(h6+h)
                    if 'AI' in h5:
                        h8.add(h6+i)
                    if 'AJ' in h5:
                        h8.add(h6+j)
                if 'B' in h5:
                    h6 = 'DEFICIÊNCIA DE QI, DEFICIÊNCIA DE XUE, CALOR VAZIO OU SECURA EM '
                    if 'BE' in h5:
                        moradia.add('V')
                        h8.add(h6+e)
                        warn_pun.add('Localizar foco de dor vazia em '.upper()+e)
                    if 'BF' in h5:
                        h8.add(h6+f)
                        warn_pun.add('Localizar foco de dor vazia em '.upper()+f)
                    if 'BG' in h5:
                        h8.add(h6+g)
                        warn_pun.add('Localizar foco de dor vazia em '.upper()+g)
                    if 'BH' in h5:
                        h8.add(h6+h)
                        warn_pun.add('Localizar foco de dor vazia em '.upper()+h)
                    if 'BI' in h5:
                        h8.add(h6+i)
                        warn_pun.add('Localizar foco de dor vazia em '.upper()+i)
                    if 'BJ' in h5:
                        h8.add(h6+j)
                        warn_pun.add('Localizar foco de dor vazia em '.upper()+j)
                if 'C' in h5:
                    h6 = 'FRIO EM '
                    if 'CE' in h5:
                        h8.add(h6+e)
                    if 'CF' in h5:
                        h8.add(h6+f)
                    if 'CG' in h5:
                        h8.add(h6+g)
                    if 'CH' in h5:
                        h8.add(h6+h)
                    if 'CI' in h5:
                        h8.add(h6+i)
                    if 'CE' in h5:
                        h8.add(h6+j)
                if 'D' in h5:
                    h6 = 'CALOR DE '
                    if 'DE' in h5:
                        h8.add(h6+e)
                    if 'DF' in h5:
                        h8.add(h6+f)
                    if 'DG' in h5:
                        h8.add(h6+g)
                    if 'DH' in h5:
                        h8.add(h6+h)
                    if 'DI' in h5:
                        h8.add(h6+i)
                    if 'DJ' in h5:
                        h8.add(h6+j)
            print('\n\n')
            if len(h8)==0:
                h8.add('PACIENTE NEGOU DOR PARA ESTA AVALIAÇÃO')
            print(h8)
        global comfx
        comfx = 'COMPLEIÇÃO DESCONHECIDA'
        while True:
            try:
                comf = int(input(
                    '\n\nCOR DOMINANTE DE COMPLEIÇÃO (1-VERMELHO, 2-AMARELO, 3-BRANCO, 4-PRETO, 5-VERDE, 6-INDEFINIDO): '))
                if comf == 1:
                    comfx = 'Compleição de Coração'
                    break
                if comf == 2:
                    comfx = 'Compleição de Baço'
                    break
                if comf == 3:
                    comfx = 'Compleição de Pulmão'
                    break
                if comf == 4:
                    comfx = 'Compleição de Rim'
                    break
                if comf == 5:
                    comfx = 'Compleição de Fígado'
                    break
                if comf == 6:
                    print('\n\nDEVIDO A IMPORTÂNCIA DESTA ANÁLISE, COMO NÃO FOI IDENTIFICADO PADRÃO VISUALMENTE REALIZAREMOS ANÁLISE ALTERNATIVA\nEXAME DE DEFINIÇÃO DE COMPLEIXÃO VIA INQUÉRITO\n')
                    ques1 = input(
                        'Alteração relativa de qual sensório ou órgão sensorial (qualquer nível de alteração mesmo relativa) A-Toque B-Gustação/Boca C-Olfato/Nariz D-Audição/Orelhas E-Visão/Olho F-Nenhum ').upper()
                    x = ques1
                    if x == 'A':
                        perfil[0] += 1
                    if x == 'B':
                        perfil[1] += 1
                    if x == 'C':
                        perfil[2] += 1
                    if x == 'D':
                        perfil[3] += 1
                    if x == 'E':
                        perfil[4] += 1
                    ques2 = input(
                        'Qual tipo caracteriza melhor a voz do paciente (mesmo que relativa)? A-Risada B-Canto C-Choro D-Gemido E-Grito F-Nenhum ').upper()
                    x = ques2
                    if x == 'A':
                        perfil[0] += 1
                    if x == 'B':
                        perfil[1] += 1
                    if x == 'C':
                        perfil[2] += 1
                    if x == 'D':
                        perfil[3] += 1
                    if x == 'E':
                        perfil[4] += 1
                    ques3 = input(
                        'Qual tipo caracteriza melhor os sentimentos que recorrentemente aparecem? A-Alegria B-Introspecção C-Tristeza D-Medo E-Raiva/Indignação F-Nenhum ').upper()
                    x = ques3
                    if x == 'A':
                        perfil[0] += 1
                    if x == 'B':
                        perfil[1] += 1
                    if x == 'C':
                        perfil[2] += 1
                    if x == 'D':
                        perfil[3] += 1
                    if x == 'E':
                        perfil[4] += 1
                    ques4 = input('Qual destes locais apresenta problemas? A-Vasos(varizes, trombos) B-Peso de gordura/estrutura do corpo/Inchaços C-Pele/Cabelo D-Osso/Órgão sexual (incluso impotência e problema uterino) E-Músculos/Tendões F-Nenhum ').upper()
                    x = ques4
                    if x == 'A':
                        perfil[0] += 1
                    if x == 'B':
                        perfil[1] += 1
                    if x == 'C':
                        perfil[2] += 1
                    if x == 'D':
                        perfil[3] += 1
                    if x == 'E':
                        perfil[4] += 1
                    ques5 = input('Qual destes fatores apresenta maior aversão ou incômodo? A-Local quente sem ar condicionado B-Saunas/piscinas/estufas/ locais abafados C-Local muito secura D-Local muito frio com ar no máximo E-Ventilador ou o vento do ar condicionado F-Nenhum ').upper()
                    x = ques5
                    if x == 'A':
                        perfil[0] += 1
                    if x == 'B':
                        perfil[1] += 1
                    if x == 'C':
                        perfil[2] += 1
                    if x == 'D':
                        perfil[3] += 1
                    if x == 'E':
                        perfil[4] += 1
                    c = str(perfil[0])
                    bp = str(perfil[1])
                    p = str(perfil[2])
                    r = str(perfil[3])
                    f = str(perfil[4])
                    print('\nRESULTADO:\nXIN '+c+'\nPI '+bp +
                          '\nFEI '+p+'\nSHEN '+r+'\nGAN '+f+'\n\n')
                    comf2 = int(
                        input('MAIOR PONTUAÇÃO (1-XIN, 2-PI, 3-FEI, 4-SHEN, 5-GAN): '))
                    if comf2 == 1:
                        comfx = 'Compleição de Coração'
                        break
                    if comf2 == 2:
                        comfx = 'Compleição de Baço'
                        break
                    if comf2 == 3:
                        comfx = 'Compleição de Pulmão'
                        break
                    if comf2 == 4:
                        comfx = 'Compleição de Rim'
                        break
                    if comf2 == 5:
                        comfx = 'Compleição de Fígado'
                        break
                    else:
                        comfx = 'COMPLEIÇÃO INDETERMINADA OU NORMAL'
                        break
                else:
                    continue
            except:
                continue
        print(f'\n\nANÁLISE DO EXAME DE COMPLEIÇÃO OU EIXO PRINCIPAL DE TRATAMENTO: \n{comfx.upper()}\n\n')
        while True:
            try:
                comp_na = input(
                    '\n\nEXISTE COR CONVIDADA AO LADO DA NARINA? \n1-ABAIXO DE NARINA \n2-DIREITA \n3-ESQUERDA \n4-ALTEROU LADO COMPARATIVAMENTE OU SIMULTANEAMENTE \n9-NÃO EXISTE\n\n')
                comp_na = int(comp_na)
                if comp_na == 1:
                    break
                if comp_na == 2:
                    if sexo == 'H':
                        warn.add('SINAIS DE REVERSÃO DE QI')
                        break
                    else:
                        break
                if comp_na == 3:
                    if sexo == 'F':
                        warn.add('SINAIS DE REVERSÃO DE QI')
                        break
                    else:
                        break
                if comp_na == 4:
                    warn.add('REVERSÃO DE QI GRAVÍSSIMA')
                    break
                if comp_na == 9:
                    break
            except:
                continue
        if len(warn) != 0:
            print('\n')
            print(warn)
            print('\n')
        while True:
            try:
                a = False
                comp_so = input('\n\nEXISTE COR CONVIDADA EM FACE (OUTRA AFORA A COR DE COMPLEIÇÃO): \n1-COR BRANCA PROFUNDA COM OU SEM BRILHO \n2-BRANCA SUPERFICIAL E COM BRILHO \n3-FUNDA E TURVA \n4-QUEIXO \n5-LÁBIO EM COR DIFERENTE DA COMPLEIÇÃO \n6-COR OCULAR DIFUSAMENTE ALTERADA DA COMPLEIÇÃO\n9-SEM ALTERAÇÃO\n\n')
                comp_so = int(comp_so)
                if comp_so == 1:
                    warn.add('DETECTADO ALTERAÇÃO LOCALIZADA EM: PELE')
                    moradia.add('P')
                    a = True
                if comp_so == 2:
                    warn.add('SINAL DE VENTO INVASOR')
                    a = True
                if comp_so == 3:
                    warn.add('SINAIS DE SÍNDROME BI')
                    moradia.add('C')
                    a = True
                if comp_so == 4:
                    warn.add('SINAIS DE SÍNDROME JUE')
                    moradia.add('J')
                    a = True
                if comp_so == 5:
                    warn.add('DETECTADO ALTERAÇÃO LOCALIZADA EM: MÚSCULO')
                    moradia.add('M')
                    a = True
                if comp_so == 6:
                    warn.add('DETECTADO ALTERAÇÃO LOCALIZADA EM: TENDÃO')
                    moradia.add('T')
                    a = True                    
                if comp_so == 9:
                    ext_q9=input('\n\nEXISTE PRURIDO EM OUVIDO, TAMPAMENTO, MUITA CERA COM RECORRÊNCIA, OU PATOLOGIA GRAVE ASSOCIADA A ALGUMA ORELHA? (S/N) ').upper()
                    if ext_q9 == 'S':
                        warn.add('DETECTADO ALTERAÇÃO LOCALIZADA EM: OSSO')
                        moradia.add('O')
                        a = True
                        break
                    if ext_q9 == 'N':
                        break
                    else:
                        continue
                if a == True:
                    break
            except:
                continue
        if len(warn) != 0:
            print('\n')
            print(warn)
            print('\n')
        while True:
            try:
                a = False
                print('\n\nAO EXAME TÁTIL DO ANTEBRAÇO: ')
                antA = input('\nA-PELE PULSANTE E RÁPIDA\nB-PELE DESLIZANTE OU SUADA\nC-PELE ÁSPERA\nD-PELE QUENTE, MACIA, BRILHANTE E CLARA\nE-ÁSPERA COMO ESCAMA DE PEIXE\nF-FRIA COM PULSO FINO\nG-QUENTE AO PEGAR E SEGURANDO ESFRIA COMPLETAMENTE\nH-COTOVELO QUENTE UNICAMENTE\nI-SOMENTE MÃO QUENTE\nJ-CALOR EM LADO ANTERIOR (DOBRA) DE COTOVELO\nK-CALOR EM POSTERIOR DE COTOVELO\nL-CALOR EM FACE INTERNA/AXILAR DE BÍCEPS\nM-CALOR EM 3CUN DE COTOVELO POSTERIOR DISTALMENTE\nN-FRIO EM MÃO\nZ-INALTERADOS\n\n ').upper()
                if antA == 'A':
                    warn.add('NECESSITA TRATAR CALOR')
                    a = True
                if antA == 'B':
                    warn.add('NECESSITA TRATAR FLEUMA/UMIDADE')
                    moradia.add('A')
                    a = True
                if antA == 'C':
                    warn.add('NECESSITA TRATAR EXCESSO DE YIN')
                    a = True
                if antA == 'D':
                    warn.add('NECESSITA TRATAR VENTO')
                    a = True
                if antA == 'E':
                    warn.add(
                        'RETENÇÃO DE UMIDADE (POSSÍVEL QUADRO DE INCHAÇO) DEVIDO A DEFICIÊNCIA DE TA INFERIOR, NECESSITA TRATAMENTO')
                    moradia.add('A')
                    a = True
                if antA == 'F':
                    antA_a = input('DIARRÉIA NAS ÚLTIMAS 48H? (S/N) ').upper()
                    if antA_a == 'S':
                        warn.add('NECESSITA TRATAR FRIO CHEIO (USAR MOXA)')
                    a = True
                if antA == 'G':
                    warn.add(
                        'ANALISAR VIA WU XING COM CAUTELA DEVIDO A ALTERAÇÕES COMPLEXAS DESTE EXAME')
                    a = True
                if antA == 'H':
                    warn.add('EXCESSO DE YANG ACIMA DE LOMBAR EM DORSAL')
                    a = True
                if antA == 'I':
                    antA2 = input(
                        'QUENTE EM: A-PALMA E DORSO OU B-QUENTE SOMENTE EM PALMA? ').upper()
                    if antA2 == 'A':
                        warn.add('EXCESSO DE YANG ABAIXO DE LOMBAR')
                    if antA2 == 'B':
                        warn.add(
                            'PACIENTE APRESENTA EXCESSO DE YANG EM CAVIDADE DE ABDOME (INFECÇÃO? DIPA? ITU? SII?)')
                    a = True
                if antA == 'J':
                    warn.add('EXCESSO DE YANG EM FACE ANTERIOR DE TÓRAX')
                    a = True
                if antA == 'K':
                    warn.add('EXCESSO DE YANG EM FACE POSTERIOR DE TÓRAX')
                    a = True
                if antA == 'L':
                    warn.add('NECESSITA DE TRATAMENTO VIA DAI MAI')
                    a = True
                if antA == 'M':
                    warn.add('EXCESSO DE YANG EM INTESTINOS (CALOR CHEIO)')
                    a = True
                if antA == 'N':
                    warn.add('DEFICIÊNCIA DE QI EM AQUECEDOR MÉDIO')
                    a = True
                if antA == 'Z':
                    break
                if a == True:
                    break
            except:
                continue
        if len(warn) != 0:
            print('\n')
            print(warn)
            print('\n')
        while True:
            try:
                a = False
                print('\n\nEXAME VISUAL DO ANTEBRAÇO: ')
                antB = input('\nA-PELE FINA E FRÁGIL\nB-PELE FINA E FORTE/DURA\nC-PELE ESTICADA E MUSCULOSA\nD-PELE IRREGULAR/DISFORME/CORES ALTERADAS\nE-HIPOTÔNICA\nF-ENRUGADA SEM HIPOTONIA \nZ-SEM ALTERAÇÃO\n\n: ').upper()
                if antB == 'A':
                    warn.add('NECESSITA DE TRATAR FRIO')
                    a = True
                if antB == 'B':
                    warn.add('NECESSITA TRATAR CALOR VAZIO')
                    a = True
                if antB == 'C':
                    warn.add('NECESSITA TRATAR EXCESSO DE YANG')
                    a = True
                if antB == 'D':
                    warn.add('ANÁLISE DE ANTEBRAÇO INDICA NECESSIDADE DE ANÁLISE DE PULSOS DE ARRITMIAS')
                    a = True
                if antB == 'E':
                    warn.add(
                        'ANALISAR VIA WU XING COM CAUTELA DEVIDO A ALTERAÇÕES COMPLEXAS DESTE EXAME')
                    a = True
                if antB == 'F':
                    warn.add('VENTO ACOMETENDO ALGUMA ARTICULAÇÃO')
                    a = True
                if antB == 'Z':
                    break
                if a == True:
                    break
            except:
                continue
        if len(warn) != 0:
            print('\n')
            print(warn)
            print('\n')
        
        def f(x): return warn.add('EXAME DE RENYING: '+x)
        while True:
            try:
                print('\n\nEXAME DE RENYING: ')
                er = input('\nSE CUNKOU É MAIS FORTE:\nA-CUNKOU=2XRENYING\nB-CUNKOU=3XRENYING\nC-CUNKOU=4XRENYING\n\nSE REYING É MAIS FORTE:\nD-RENYING=2XCUNKOU\nE-RENYING=3XCUNKOU\nF-RENYING=4XCUNKOU\n\nZ-SEM ALTERAÇÕES DESCRITAS\n\n>>RESPOSTA: ').upper()
                print('\n\n')
                if er.isnumeric()==True:
                    print('ERRO! TENTE NOVAMENTE SEM INSERIR NÚMEROS.')
                else:
                    er=str(er)
                if len(er) == 1:
                    if er == 'Z':
                        f('EXAME DE RENYING NORMAL')
                        break
                    if er == 'A' or er == 'B' or er == 'C':
                        er1 = input('BATIMENTO DE JUGULAR VISÍVEL? (S/N) ').upper()
                        if er1 == 'N':
                            if estação == 'INVERNO' or estação == 'OUTONO':
                                if er == 'A':
                                    f('EXAME DE RENYING NORMAL (CORREÇÃO POR ESTAÇÃO)')
                                    break
                                elif er == 'B':
                                    f('EXAME DE RENYING APONTA PARA FÍGADO (CORREÇÃO POR ESTAÇÃO)')
                                    break
                                elif er == 'C':
                                    f('EXAME DE RENYING APONTA PARA RIM (CORREÇÃO POR ESTAÇÃO)')
                                    break
                            else:
                                if er == 'A':
                                    f('EXAME DE RENYING APONTA PARA FÍGADO')
                                    break
                                elif er == 'B':
                                    f('EXAME DE RENYING APONTA PARA RIM')
                                    break
                                elif er == 'C':
                                    f('EXAME DE RENYING APONTA PARA BAÇO')
                                    break
                        if er1 == 'S':
                            if estação == 'INVERNO' or estação == 'OUTONO':
                                if er == 'A':
                                    f('EXAME DE RENYING NORMAL (CORREÇÃO POR ESTAÇÃO)')
                                    break
                                elif er == 'B':
                                    f('EXAME DE RENYING APONTA PARA PERICÁRDIO (CORREÇÃO POR ESTAÇÃO)')
                                    break
                                elif er == 'C':
                                    f('EXAME DE RENYING APONTA PARA CORAÇÃO (CORREÇÃO POR ESTAÇÃO)')
                                    break
                            else:
                                if er == 'A':
                                    f('EXAME DE RENYING APONTA PARA PERICÁRDIO')
                                    break
                                elif er == 'B':
                                    f('EXAME DE RENYING APONTA PARA CORAÇÃO')
                                    break
                                elif er == 'C':
                                    f('EXAME DE RENYING APONTA PARA PULMÃO')
                                    break
                        else:
                            continue
                    if er == 'D' or er == 'E' or er == 'F':
                        er2 = input('BATIMENTO DE JUGULAR VISÍVEL? (S/N) ').upper()
                        if er2 == 'N':
                            if estação == 'PRIMAVERA' or estação == 'VERÃO':
                                if er == 'D':
                                    f('EXAME DE RENYING NORMAL (CORREÇÃO POR ESTAÇÃO)')
                                    break
                                elif er == 'E':
                                    f('EXAME DE RENYING APONTA PARA VESÍCULA BILIAR (CORREÇÃO POR ESTAÇÃO)')
                                    break
                                elif er == 'F':
                                    f('EXAME DE RENYING APONTA PARA BEXIGA (CORREÇÃO POR ESTAÇÃO)')
                                    break
                            else:
                                if er == 'D':
                                    f('EXAME DE RENYING APONTA PARA VESÍCULA BILIAR')
                                    break
                                elif er == 'E':
                                    f('EXAME DE RENYING APONTA PARA BEXIGA')
                                    break
                                elif er == 'F':
                                    f('EXAME DE RENYING APONTA PARA ESTÔMAGO')
                                    break
                        if er2 == 'S':
                            if estação == 'PRIMAVERA' or estação == 'VERÃO':
                                if er == 'D':
                                    f('EXAME DE RENYING NORMAL (CORREÇÃO POR ESTAÇÃO)')
                                    break
                                elif er == 'E':
                                    f('EXAME DE RENYING APONTA PARA TRIPLO AQUECEDOR (CORREÇÃO POR ESTAÇÃO)')
                                    break
                                elif er == 'F':
                                    f('EXAME DE RENYING APONTA PARA INTESTINO DELGADO (CORREÇÃO POR ESTAÇÃO)')
                                    break
                            else:
                                if er == 'D':
                                    f('EXAME DE RENYING APONTA PARA TRIPLO AQUECEDOR')
                                    break
                                elif er == 'E':
                                    f('EXAME DE RENYING APONTA PARA INTESTINO DELGADO')
                                    break
                                elif er == 'F':
                                    f('EXAME DE RENYING APONTA PARA INTESTINO GROSSO')
                                    break
                        else:
                            continue
                    else:
                        continue
                else:        
                    continue
            except:
                continue

        while True:
            try:
                er3 = input('RENYING MUITO ÁGIL? (S/N) ').upper()
                if er3 == 'S':
                    f('SÍNDROME BI DE FRIO')
                elif er3=='N':
                    pass
                else:
                    continue
                er4 = input('RENYING MUITO INTERMITENTE? (S/N) ').upper()
                if er4 == 'S':
                    f('DOENÇA LEVE E PASSAGEIRA')
                elif er4=='N':
                    pass
                else:
                    continue
                er5 = input('TURGÊNCIA JUGULAR? (S/N) ').upper()
                if er5 == 'S':
                    f('NECESSITA PURGAR YANG POR CALOR CHEIO')
                elif er5=='N':
                    pass
                else:
                    continue
                er6 = input('RENYING MUITO FRACO? (S/N) ').upper()
                if er6 == 'S':
                    f('NECESSITA DE REVIGORAR VIA MOXA POR FRIO')
                    break
                elif er6=='N':
                    break
                else:
                    continue
            except:
                continue

        while True:
            try:
                print('\n\nAO EXAME EMOCIONAL\nALGUMA CONDIÇÃO FAZ SENTIDO?')
                emo = input('\n1-CORPO TRANQUILO COM ESPÍRITO AGONIADO\n2-MAL-ESTAR EM CORPO COM ESPÍRITO ALEGRE\n3-SEM MAL-ESTAR EM CORPO E SEM AGONIA EM ESPÍRITO\n4-CORPO E ESPÍRITO CANSADOS\n\n').upper()
                emo = int(emo)
                if emo == 1:
                    warn.add(
                        'ATENÇÃO! DETECTADO ALTERAÇÃO LOCALIZADA EM: CANAL')
                    moradia.add('C')
                    break
                if emo == 2:
                    warn.add('DETECTADO ALTERAÇÃO LOCALIZADA EM: TENDÃO')
                    moradia.add('T')
                    break
                if emo == 3:
                    warn.add(
                        'ATENÇÃO! DETECTADO ALTERAÇÃO LOCALIZADA EM: MÚSCULO')
                    moradia.add('M')
                    break
                if emo == 4:
                    warn.add(
                        'GRAVE DEFICIÊNCIA DE QI, DEVE SER USADO TRATAMENTO EM REN MAI E YUAN')
                    break
            except:
                continue
        if len(warn) != 0:
            cls()
            print('\n\n\n\n\n\n')
            for i in sorted(list(warn)):
                print(i)
            print('\n')
            time.sleep(6)
        # ADIÇÃO WARN_PUN DE RECOMENDAÇÕES DE TIPO DE TRATAMENTO POR CLASSIFICAÇÃO
        if 'C' in moradia:
            warn_pun.add(
                'Aplicação contra-lateral a dor (esta deverá existir em meridiano afetado)'.upper())
            warn_pun.add(
                'Sangramento de colateral é indicado caso canal afetado com colateral congesto'.upper())
            warn_pun.add(
                'Liberado método de lunação para tratamento de síndrome bi de canal afetado'.upper())
            warn_pun.add(
                'Sintomas de vísceras deverão ser tratados via pontos yuan'.upper())
            warn_pun.add('Pode ser usado agulha de fogo'.upper())
        if 'V' in moradia:
            warn_pun.add('Aplicação rápida de agulha'.upper())
            warn_pun.add(
                'Segurar com mâo esquerda apertando após picar, e, então retirar a agulha com a mão empurrando'.upper())
            warn_pun.add(
                'Repetir em locais de dor (ou em mesmo local) até melhorar'.upper())
        if 'M' in moradia:
            warn_pun.add('Procurar meridiano com queixa de dor'.upper())
            warn_pun.add(
                '3 picadas em mesmo local em forma de pé-de-galinha, central e duas divergentes em mesmo acuponto'.upper())
        if 'O' in moradia:
            warn_pun.add(
                'Insersão por soerguimento delicada até osso, em linha reta'.upper())
            warn_pun.add(
                'Insersão em tecido conectivo do osso de junta'.upper())
        if 'J' in moradia:
            warn_pun.add(
                'Aplicar puntura em lados internos de coxa bilateralmente, em associação com R3'.upper())
        if 'A' in moradia:
            warn_pun.add(
                'Procurar nódulo/tumor/edema em meridiano com umidade'.upper())
            warn_pun.add(
                'Agulhar local e outra face do local (e.g. dorso de mão e palma de mão ou peito e costas)'.upper())
        if 'P' in moradia:
            warn_pun.add('Puntura superficial, rasa e rápida'.upper())
        if 'L' in moradia:
            warn_pun.add(
                'Delimitar área de colateral estagnado, punção sob delimitação desenhada'.upper())
        if 'T' in moradia:
            warn_pun.add('LOCALIZAR DOR EM JUNTA COM DOR E INSERIR AGULHA EM LOCAL, TOCANDO OSSO MAIS PROXIMAL DA LESÃO (INSERIR NA ÊNTESE)')
            warn_pun.add(
                'Sem cruzar lados, se dor em local de dor (fora de canal), devendo sangrar'.upper())
        if len(warn_pun) != 0:
            cls()
            print('\n\n\n\n\n\n')
            for i in sorted(list(warn_pun)):
                print(i)
            print('\n')
            time.sleep(6)
        # -------------------------------------- PULSOLOGIA - PARTE 1
        cls()
        while True:
            try:
                fc=int(input('\n\n\nDigite a frequencia cardíaca (bpm) ou batimentos/incursão completa do examinador: '))
                if fc<10:
                    if fc<3:
                        rfc=1
                        print('Pulso lento via exame MTC')
                        break
                    if fc>=3 and fc<5:
                        rfc=2
                        print('Pulso sem oscilação de velocidade via exame MTC')
                        break
                    else:
                        rfc=3
                        print('Pulso rápido via exame MTC')
                        break
                elif fc<50 and fc>25:
                    rfc=1
                    print('Pulso lento via exame ocidental')
                    break
                elif fc>=50 and fc<90:
                    rfc=2
                    print('Pulso inalterado via exame ocidental')
                    break
                elif fc>=90 and fc<300:
                    rfc=3
                    print('Pulso rápido via exame ocidental')
                    break
                else:
                    continue
            except ValueError:
                print("Vamos tentar novamente, valor distoante inserido...") 
        if rfc==1:
            print('\n\n\nPULSO BRADICÁRDICO (LENTO) DETECTADO PARA ANÁLISE!\n\n')
        if rfc==2:
            print('\n\n\nPULSO SEM ALTERAÇÃO DE FREQUÊNCIA PARA ANÁLISE!\n\n')          
        if rfc==3:
            print('\n\n\nPULSO TAQUICÁRDICO (RÁPIDO) DETECTADO PARA ANÁLISE!\n\n')
        time.sleep(4)            

        '''
    LÓGICA BÁSICA DO ALGORÍTMO - PARTE DE PULSO GERAL
    a = yang
    1- def yang e frio vazio
    3- calor cheio
    b = xue
    1- def xue
    3- estag xue
    c = yin
    1- def yin e calor vazio
    3- frio cheio
    
    a+c=
    3- estag qi
    1- def qi
        + b1 ou b2 = colapso
    '''
        cls()
        print('\nDIGITE 1 (FRACO),2 (NORMAL) OU 3 (EXAGERADO) PARA PULSOLOGIA CHINESA. \nD-DIREITA, E-ESQUERDA, 1-DISTAL, 2-MÉDIO E 3-PROXIMAL\n\n')        
#                                                                                       NÍVEL SUPERFICIAL DIR
# -------------------------------------- PULSO P/ IG
        while True:
            try:
                d1a = int(input('D1A: '))
                if d1a != 1 and d1a != 2 and d1a != 3:
                    print('Eita, presta atenção! Coloque 1, 2 ou 3!')
                    continue
                if d1a == 1:
                    pct.add(dx[15])
                    print(dx[15])
                    # def yang
                    break
                if d1a == 2:
                    print('Sem alterações no exame')
                    break
                if d1a == 3:
                    pct.add(dx[171])
                    print(dx[171])
                    break
                    # calor cheio
            except ValueError:
                print("Oops! Coloque números apenas! Vamos tentar novamente...")
# -------------------------------------- PULSO E/ BP
        while True:
            try:
                d2a = int(input('D2A: '))
                if d2a != 1 and d2a != 2 and d2a != 3:
                    print('Eita, presta atenção! Coloque 1, 2 ou 3!')
                    continue
                if d2a == 1:
                    pct.add(dx[13])
                    print(dx[13])
                    # def yang
                    break
                if d2a == 2:
                    print('Sem alterações no exame')
                    break
                if d2a == 3:
                    pct.add(dx[169])
                    print(dx[169])
                    break
                    # calor cheio
            except ValueError:
                print("Oops! Coloque números apenas! Vamos tentar novamente...")
# -------------------------------------- PULSO TA/ PC
        while True:
            try:
                d3a = int(input('D3A: '))
                if d3a != 1 and d3a != 2 and d3a != 3:
                    print('Eita, presta atenção! Coloque 1, 2 ou 3!')
                    continue
                if d3a == 1:
                    pct.add(dx[14])
                    print(dx[14])
                    # def yang
                    break
                if d3a == 2:
                    print('Sem alterações no exame')
                    break
                if d3a == 3:
                    pct.add(dx[170])
                    print(dx[170])
                    break
                    # calor cheio
            except ValueError:
                print("Oops! Coloque números apenas! Vamos tentar novamente...")

#                                                                                       NÍVEL MÉDIO DIR
        while True:
            try:
                d1b = int(input('D1B: '))
                if d1b != 1 and d1b != 2 and d1b != 3:
                    print('Eita, presta atenção! Coloque 1, 2 ou 3!')
                    continue
                if d1b == 1:
                    pct.add(dx[3])
                    print(dx[3])
                    # def xue
                    break
                if d1b == 2:
                    print('Sem alterações no exame')
                    break
                if d1b == 3:
                    pct.add(dx[57])
                    print(dx[57])
                    # estag xue
                    break
            except ValueError:
                print("Oops! Coloque números apenas! Vamos tentar novamente...")
        while True:
            try:
                d2b = int(input('D2B: '))
                if d2b != 1 and d2b != 2 and d2b != 3:
                    print('Eita, presta atenção! Coloque 1, 2 ou 3!')
                    continue
                if d2b == 1:
                    pct.add(dx[1])
                    print(dx[1])
                    # def xue
                    break
                if d2b == 2:
                    print('Sem alterações no exame')
                    break
                if d2b == 3:
                    pct.add(dx[55])
                    print(dx[55])
                    # estag xue
                    break
            except ValueError:
                print("Oops! Coloque números apenas! Vamos tentar novamente...")
        while True:
            try:
                d3b = int(input('D3B: '))
                if d3b != 1 and d3b != 2 and d3b != 3:
                    print('Eita, presta atenção! Coloque 1, 2 ou 3!')
                    continue
                if d3b == 1:
                    pct.add(dx[2])
                    print(dx[2])
                    # def xue
                    break
                if d3b == 2:
                    print('Sem alterações no exame')
                    break
                if d3b == 3:
                    pct.add(dx[56])
                    print(dx[56])
                    # estag xue
                    break
            except ValueError:
                print("Oops! Coloque números apenas! Vamos tentar novamente...")
#                                                                                       NÍVEL PROFUNDO DIR
        while True:
            try:
                d1c = int(input('D1C: '))
                if d1c != 1 and d1c != 2 and d1c != 3:
                    print('Eita, presta atenção! Coloque 1, 2 ou 3!')
                    continue
                if d1c == 1:
                    pct.add(dx[9])
                    print(dx[9])
                    # def yin
                    break
                if d1a == 1:
                    pct.add(dx[21])
                    print(dx[21])
                    # def qi
                    break
                if d1b == 1 or d1b == 3:
                    pct.add(dx[147])
                    print(dx[147])
                    # colapso
                    break
                if d1c == 2:
                    print('Sem alterações no exame')
                    break
                if d1c == 3:
                    pct.add(dx[183])
                    print(dx[183])
                    # frio cheio
                    break
                if d1a == 3:
                    pct.add(dx[63])
                    print(dx[63])
                    # estag qi
                    break
            except ValueError:
                print("Oops! Coloque números apenas! Vamos tentar novamente...")
        while True:
            try:
                d2c = int(input('D2C: '))
                if d2c != 1 and d2c != 2 and d2c != 3:
                    print('Eita, presta atenção! Coloque 1, 2 ou 3!')
                    continue
                if d2c == 1:
                    pct.add(dx[7])
                    print(dx[7])
                    # def yin
                    break
                if d2a == 1:
                    pct.add(dx[19])
                    print(dx[19])
                    # def qi
                    if d2b == 1 or d2b == 3:
                        pct.add(dx[145])
                        print(dx[145])
                        # colapso
                        break
                    break
                if d2c == 2:
                    print('Sem alterações no exame')
                    break
                if d2c == 3:
                    pct.add(dx[181])
                    print(dx[181])
                    # frio cheio
                    break
                if d2a == 3:
                    pct.add(dx[61])
                    print(dx[61])
                    # estag qi
                    break
            except ValueError:
                print("Oops! Coloque números apenas! Vamos tentar novamente...")
        while True:
            try:
                d3c = int(input('D3C: '))
                if d3c != 1 and d3c != 2 and d3c != 3:
                    print('Eita, presta atenção! Coloque 1, 2 ou 3!')
                    continue
                if d3c == 1:
                    pct.add(dx[8])
                    print(dx[8])
                    # def yin
                    break
                if d3a == 1:
                    pct.add(dx[20])
                    print(dx[20])
                    # def qi
                    break
                if d3b == 1 or d3b == 3:
                    pct.add(dx[146])
                    print(dx[146])
                    # colapso
                    break
                if d3c == 2:
                    print('Sem alterações no exame')
                    break
                if d3c == 3:
                    pct.add(dx[182])
                    print(dx[182])
                    # frio cheio
                    if d3a == 3:
                        pct.add(dx[62])
                        print(dx[62])
                        # estag qi
                        break
                    break
            except ValueError:
                print("Oops! Coloque números apenas! Vamos tentar novamente...")
        print()

# -------------------------------------- ENTRADA DE DADOS PARA PULSOS PATOLÓGICOS >>> DIR

        cls()
        print('\n\nLADO DIREITO\n\n')
        print('PULSOS PATOLÓGICOS')
        if rfc==1:
            print('(A) chi - BRADICARDIA <3bpm/irpm do examinador')
        if rfc==3:
            print('(B) shu - TAQUICARDIA >5bpm/irpm examinador')
        print('(C) xu - VAZIO, dificuldade de sentir, largura aumentada e macio')
        print('(E) hua - ESCORREGA nos dedos e desliza')
        print('(F) se - ÁSPERO, serrilhado')
        print('(G) chang - sensibilidade AMPLA, batem antes de apertar')
        print('(H) duan - CURTA sensibilidade, ocupa espaço menor que o habitual')
        print('(I) hong - LARGO, transbordante, aumento de calibre do vaso')
        print('(J) xi - mais FINO que o normal')
        print('(K) wei - mínimo e frágil, como um CAPILAR')
        print('(L) jin - tenso e torcido como uma CORDA grossa')
        print(
            '(M) xian - corda, mais fino e mais tenso que o L, força da corda de um VIOLÃO')
        print('(O) ge - em couro, duro, TENSO-ESTICADO, aberto, como o tambor de couro e parece vazio ao apertar por maior vazão')
        print('(Q) san - QUEBRADO, batimento em pontos e não inteiramente')
        print('(R) fu - PROFUNDO e aderido ao osso, sem mobilidade')
        print('(S) dong - ANEURISMA, semelhante a feijão com frêmitos ao batimento')
        print('(T) cu - precipitado, RÁPIDO-INTERROMPIDO em intervalos regulares')
        print('(U) jie - LENTO-INTERROMPIDO em intervalos regulares')
        print('(V) dai - ora ritmo fisiológico ora INTERROMPIDO')
        print()
        print('Pulsos Fu, Chen, Shi, Kou, Huan, Lao, Ruo, Ru e Ji já são definidos por algorítmos. FC influencia em análise de pulsos Chi e Shu, podendo ficar indisponíveis.\n\n')
        if rfc==1:
            print('ATENÇÃO! Paciente apresenta tipo A em algum pulso, tente analisar corretamente!')
        if rfc==3:
            print('ATENÇÃO! Paciente apresenta tipo B em algum pulso, tente analisar corretamente!')
        if antB == 'D':
            print(
                'ATENÇÃO! Atenção nesta análise, paciente supostamente apresentará pulsos T ou U ou V (COMPATIBILIDADE COM ARRITMIAS). Tente fazer com mais tempo o exame.')
        print()
        ppd_inp = str(
            input('Adicione os pulsos anormais do lado DIREITO: (e.g. d1f d3s...) ')).upper()
        ppd_lis = ppd_inp.split()

        ppd1_pre = [item for item in ppd_lis if 'D1' in item]
        ppd1_liq = [i.split('D1')[1] for i in ppd1_pre]
        ppd1 = [item for item in ppd1_liq if len(item) == 1]

        ppd2_pre = [item for item in ppd_lis if 'D2' in item]
        ppd2_liq = [i.split('D2')[1] for i in ppd2_pre]
        ppd2 = [item for item in ppd2_liq if len(item) == 1]

        ppd3_pre = [item for item in ppd_lis if 'D3' in item]
        ppd3_liq = [i.split('D3')[1] for i in ppd3_pre]
        ppd3 = [item for item in ppd3_liq if len(item) == 1]

        print()
        print('Adicionado em D1:')
        if len(ppd1) < 1:
            print('Sem adição')
        else:
            print(ppd1)
        print('Adicionado em D2:')
        if len(ppd2) < 1:
            print('Sem adição')
        else:
            print(ppd2)
        print('Adicionado em D3:')
        if len(ppd3) < 1:
            print('Sem adição')
        else:
            print(ppd3)

        global subpulto
        subpulto=str(ppd1)+'|'+str(ppd2)+'|'+str(ppd3)+'|'+str(ppe1)+'|'+str(ppe2)+'|'+str(ppe3)
        s1=subpulto.replace('A','CHI')
        s2=s1.replace('B','SHU')
        s3=s2.replace('C','XU')
        s4=s3.replace('E','HUA')
        s5=s4.replace('F','SE')
        s6=s5.replace('G','CHANG')
        s7=s6.replace('H','DUAN')
        s8=s7.replace('J','XI')
        s9=s8.replace('K','WEI')
        s10=s9.replace('L','JIN')
        s11=s10.replace('M','XIAN')
        s12=s11.replace('O','GE')

        time.sleep(3)
        cls()
        print()
        print('\nDIGITE 1 (FRACO),2 (NORMAL) OU 3 (EXAGERADO) PARA PULSOLOGIA CHINESA. \nD-DIREITA, E-ESQUERDA, 1-DISTAL, 2-MÉDIO E 3-PROXIMAL\n\n')

# -------------------------------------- PULSO C/ ID                                   NÍVEL SUPERFICIAL ESQ
        while True:
            try:
                e1a = int(input('E1A: '))
                if e1a != 1 and e1a != 2 and e1a != 3:
                    print('Eita, presta atenção! Coloque 1, 2 ou 3!')
                    continue
                if e1a == 1:
                    pct.add(dx[12])
                    print(dx[12])
                    # def yang
                    break
                if e1a == 2:
                    print('Sem alterações no exame')
                    break
                if e1a == 3:
                    pct.add(dx[168])
                    print(dx[168])
                    break
                    # calor cheio
            except ValueError:
                print("Oops! Coloque números apenas! Vamos tentar novamente...")

# -------------------------------------- PULSO F/ VB
        while True:
            try:
                e2a = int(input('E2A: '))
                if e2a != 1 and e2a != 2 and e2a != 3:
                    print('Eita, presta atenção! Coloque 1, 2 ou 3!')
                    continue
                if e2a == 1:
                    pct.add(dx[17])
                    print(dx[17])
                    # def yang
                    break
                if e2a == 2:
                    print('Sem alterações no exame')
                    break
                if e2a == 3:
                    pct.add(dx[173])
                    print(dx[173])
                    break
                    # calor cheio
            except ValueError:
                print("Oops! Coloque números apenas! Vamos tentar novamente...")

# -------------------------------------- PULSO R/ B
        while True:
            try:
                e3a = int(input('E3A: '))
                if e3a != 1 and e3a != 2 and e3a != 3:
                    print('Eita, presta atenção! Coloque 1, 2 ou 3!')
                    continue
                if e3a == 1:
                    pct.add(dx[16])
                    print(dx[16])
                    # def yang
                    break
                if e3a == 2:
                    print('Sem alterações no exame')
                    break
                if e3a == 3:
                    pct.add(dx[172])
                    print(dx[172])
                    break
                    # calor cheio
            except ValueError:
                print("Oops! Coloque números apenas! Vamos tentar novamente...")
#                                                                                        NIVEL MEDIO ESQ

        while True:
            try:
                e1b = int(input('E1B: '))
                if e1b != 1 and e1b != 2 and e1b != 3:
                    print('Eita, presta atenção! Coloque 1, 2 ou 3!')
                    continue
                if e1b == 1:
                    pct.add(dx[0])
                    print(dx[0])
                    # def xue
                    break
                if e1b == 2:
                    print('Sem alterações no exame')
                    break
                if e1b == 3:
                    pct.add(dx[54])
                    print(dx[54])
                    # estag xue
                    break
            except ValueError:
                print("Oops! Coloque números apenas! Vamos tentar novamente...")

        while True:
            try:
                e2b = int(input('E2B: '))
                if e2b != 1 and e2b != 2 and e2b != 3:
                    print('Eita, presta atenção! Coloque 1, 2 ou 3!')
                    continue
                if e2b == 1:
                    pct.add(dx[5])
                    print(dx[5])
                    # def xue
                    break
                if e2b == 2:
                    print('Sem alterações no exame')
                    break
                if e2b == 3:
                    pct.add(dx[59])
                    print(dx[59])
                    # estag xue
                    break
            except ValueError:
                print("Oops! Coloque números apenas! Vamos tentar novamente...")

        while True:
            try:
                e3b = int(input('E3B: '))
                if e3b != 1 and e3b != 2 and e3b != 3:
                    print('Eita, presta atenção! Coloque 1, 2 ou 3!')
                    continue
                if e3b == 1:
                    pct.add(dx[4])
                    print(dx[4])
                    # def xue
                    break
                if e3b == 2:
                    print('Sem alterações no exame')
                    break
                if e3b == 3:
                    pct.add(dx[58])
                    print(dx[58])
                    # estag xue
                    break
            except ValueError:
                print("Oops! Coloque números apenas! Vamos tentar novamente...")

#                                                                                   NÍVEL PROFUNDO ESQ

        while True:
            try:
                e1c = int(input('E1C: '))
                if e1c != 1 and e1c != 2 and e1c != 3:
                    print('Eita, presta atenção! Coloque 1, 2 ou 3!')
                    continue
                if e1c == 1:
                    pct.add(dx[6])
                    print(dx[6])
                    # def yin
                    if e1a == 1:
                        pct.add(dx[18])
                        print(dx[18])
                        # def qi
                        if e1b == 1 or e1b == 3:
                            pct.add(dx[144])
                            print(dx[144])
                            # colapso
                            break
                        break
                    break
                if e1c == 2:
                    print('Sem alterações no exame')
                    break
                if e1c == 3:
                    pct.add(dx[180])
                    print(dx[180])
                    # frio cheio
                    if e1a == 3:
                        pct.add(dx[60])
                        print(dx[60])
                        # estag qi
                        break
                    break
            except ValueError:
                print("Oops! Coloque números apenas! Vamos tentar novamente...")

        while True:
            try:
                e2c = int(input('E2C: '))
                if e2c != 1 and e2c != 2 and e2c != 3:
                    print('Eita, presta atenção! Coloque 1, 2 ou 3!')
                    continue
                if e2c == 1:
                    pct.add(dx[11])
                    print(dx[11])
                    # def yin
                    if e2a == 1:
                        pct.add(dx[23])
                        print(dx[23])
                        # def qi
                        if e2b == 1 or e2b == 3:
                            pct.add(dx[149])
                            print(dx[149])
                            # colapso
                            break
                        break
                    break
                if e2c == 2:
                    print('Sem alterações no exame')
                    break
                if e2c == 3:
                    pct.add(dx[185])
                    print(dx[185])
                    # frio cheio
                    if e2a == 3:
                        pct.add(dx[65])
                        print(dx[65])
                        # estag qi
                        break
                    break
            except ValueError:
                print("Oops! Coloque números apenas! Vamos tentar novamente...")

        while True:
            try:
                e3c = int(input('E3C: '))
                if e3c != 1 and e3c != 2 and e3c != 3:
                    print('Eita, presta atenção! Coloque 1, 2 ou 3!')
                    continue
                if e3c == 1:
                    pct.add(dx[10])
                    print(dx[10])
                    # def yin
                    if e3a == 1:
                        pct.add(dx[22])
                        print(dx[22])
                        # def qi
                        if e3b == 1 or e3b == 3:
                            pct.add(dx[148])
                            print(dx[148])
                            # colapso
                            break
                        break
                    break
                if e3c == 2:
                    print('Sem alterações no exame')
                    break
                if e3c == 3:
                    pct.add(dx[184])
                    print(dx[184])
                    # frio cheio
                    if e3a == 3:
                        pct.add(dx[64])
                        print(dx[64])
                        # estag qi
                        break
                    break
            except ValueError:
                print("Oops! Coloque números apenas! Vamos tentar novamente...")

# -------------------------------------- ENTRADA DE DADOS PARA PULSOS PATOLÓGICOS >>> ESQ

        cls()
        print('\n\nLADO ESQUERDO\n\n')
        print('PULSOS PATOLÓGICOS')
        if rfc==1:
            print('(A) chi - BRADICARDIA <3bpm/irpm do examinador')
        if rfc==3:
            print('(B) shu - TAQUICARDIA >5bpm/irpm examinador')
        print('(C) xu - VAZIO, dificuldade de sentir, largura aumentada e macio')
        print('(E) hua - ESCORREGA nos dedos e desliza')
        print('(F) se - ÁSPERO, serrilhado')
        print('(G) chang - sensibilidade AMPLA, batem antes de apertar')
        print('(H) duan - CURTA sensibilidade, ocupa espaço menor que o habitual')
        print('(I) hong - LARGO, transbordante, aumento de calibre do vaso')
        print('(J) xi - mais FINO que o normal')
        print('(K) wei - mínimo e frágil, como um CAPILAR')
        print('(L) jin - tenso e torcido como uma CORDA grossa')
        print(
            '(M) xian - corda, mais fino e mais tenso que o L, força da corda de um VIOLÃO')
        print('(O) ge - em couro, duro, TENSO-ESTICADO, aberto, como o tambor de couro e parece vazio ao apertar por maior vazão')
        print('(Q) san - QUEBRADO, batimento em pontos e não inteiramente')
        print('(R) fu - PROFUNDO e aderido ao osso, sem mobilidade')
        print('(S) dong - ANEURISMA, semelhante a feijão com frêmitos ao batimento')
        print('(T) cu - precipitado, RÁPIDO-INTERROMPIDO em intervalos regulares')
        print('(U) jie - LENTO-INTERROMPIDO em intervalos regulares')
        print('(V) dai - ora ritmo fisiológico ora INTERROMPIDO')
        print()
        print('Pulsos Fu, Chen, Shi, Kou, Huan, Lao, Ruo, Ru e Ji já são definidos por algorítmos. FC influencia em análise de pulsos Chi e Shu, podendo ficar indisponíveis.\n\n')
        if rfc==1:
            print('ATENÇÃO! Paciente apresenta tipo A em algum pulso, tente analisar corretamente!')
        if rfc==3:
            print('ATENÇÃO! Paciente apresenta tipo B em algum pulso, tente analisar corretamente!')
        if antB == 'D':
            print(
                'ATENÇÃO! Atenção nesta análise, paciente supostamente apresentará pulsos T ou U ou V (COMPATIBILIDADE COM ARRITMIAS). Tente fazer com mais tempo o exame.')
        print()

        ppe_inp = str(input(
            'Adicione os pulsos anormais do lado ESQUERDO: (e.g. e3f e2y...) ')).upper()
        ppe_lis = ppe_inp.split()

        ppe1_pre = [item for item in ppe_lis if 'E1' in item]
        ppe1_liq = [i.split('E1')[1] for i in ppe1_pre]
        ppe1 = [item for item in ppe1_liq if len(item) == 1]

        ppe2_pre = [item for item in ppe_lis if 'E2' in item]
        ppe2_liq = [i.split('E2')[1] for i in ppe2_pre]
        ppe2 = [item for item in ppe2_liq if len(item) == 1]

        ppe3_pre = [item for item in ppe_lis if 'E3' in item]
        ppe3_liq = [i.split('E3')[1] for i in ppe3_pre]
        ppe3 = [item for item in ppe3_liq if len(item) == 1]

        print()
        print('Adicionado em E1:')
        if len(ppe1) < 1:
            print('Sem adição')
        else:
            print(ppe1)
        print('Adicionado em E2:')
        if len(ppe2) < 1:
            print('Sem adição')
        else:
            print(ppe2)
        print('Adicionado em E3:')
        if len(ppe3) < 1:
            print('Sem adição')
        else:
            print(ppe3)

        if 'C' in moradia:
            if d1a == 1 and d1b == 1:
                cls()
                print('\n\n\n\n\n')
                warn.add('ATENÇÃO! DETECTADO ALTERAÇÃO LOCALIZADA EM: CANAL P/IG')
            if d2a == 1 and d2b == 1:
                cls()
                print('\n\n\n\n\n')
                warn.add('ATENÇÃO! DETECTADO ALTERAÇÃO LOCALIZADA EM: CANAL BP/E')
            if d3a == 1 and d3b == 1:
                cls()
                print('\n\n\n\n\n')
                warn.add('ATENÇÃO! DETECTADO ALTERAÇÃO LOCALIZADA EM: CANAL PC/TA')
            if e1a == 1 and e1b == 1:
                cls()
                print('\n\n\n\n\n')
                warn.add('ATENÇÃO! DETECTADO ALTERAÇÃO LOCALIZADA EM: CANAL C/ID')
            if e2a == 1 and e2b == 1:
                cls()
                print('\n\n\n\n\n')
                warn.add('ATENÇÃO! DETECTADO ALTERAÇÃO LOCALIZADA EM: CANAL F/VB')
            if e3a == 1 and e3b == 1:
                cls()
                print('\n\n\n\n\n')
                warn.add('ATENÇÃO! DETECTADO ALTERAÇÃO LOCALIZADA EM: CANAL R/B')
            time.sleep(3)

# -------------------------------------- ENDEREÇAMENTO DE PULSOS CAPTADOS

        det_1 = set()
        det_2 = set()
        det_3 = set()
        det_4 = set()
        det_5 = set()
        det_6 = set()
        det_7 = set()
        det_8 = set()
        det_9 = set()
        det_10 = set()
        det_11 = set()
        det_12 = set()
        det_13 = set()
        det_14 = set()
        det_15 = set()
        det_16 = set()
        det_17 = set()
        det_18 = set()
        det_19 = set()
        det_20 = set()
        det_21 = set()
        det_22 = set()
        det_23 = set()
        det_24 = set()
        det_25 = set()
        det_26 = set()
        det_27 = set()
        det_28 = set()

        '''
        def (x):
            if len(det_x)==0:
                return str(0)
            else:
                for i in det_x:
                    return i
        '''

        x = 'A'
        if x in ppe1:
            det_3.add('C')
        if x in ppe2:
            det_3.add('F')
        if x in ppe3:
            det_3.add('R')
        if x in ppd1:
            det_3.add('P')
        if x in ppd2:
            det_3.add('BP')
        if x in ppd3:
            det_3.add('PC')

        if 'B' in ppe1:
            det_4.add('C')
        if 'B' in ppe2:
            det_4.add('F')
        if 'B' in ppe3:
            det_4.add('R')
        if 'B' in ppd1:
            det_4.add('P')
        if 'B' in ppd2:
            det_4.add('BP')
        if 'B' in ppd3:
            det_4.add('PC')

        if 'C' in ppe1:
            det_5.add('C')
        if 'C' in ppe2:
            det_5.add('F')
        if 'C' in ppe3:
            det_5.add('R')
        if 'C' in ppd1:
            det_5.add('P')
        if 'C' in ppd2:
            det_5.add('BP')
        if 'C' in ppd3:
            det_5.add('PC')

        x = 'E'
        if x in ppe1:
            det_7.add('C')
        if x in ppe2:
            det_7.add('F')
        if x in ppe3:
            det_7.add('R')
        if x in ppd1:
            det_7.add('P')
        if x in ppd2:
            det_7.add('BP')
        if x in ppd3:
            det_7.add('PC')

        x = 'F'
        if x in ppe1:
            det_8.add('C')
        if x in ppe2:
            det_8.add('F')
        if x in ppe3:
            det_8.add('R')
        if x in ppd1:
            det_8.add('P')
        if x in ppd2:
            det_8.add('BP')
        if x in ppd3:
            det_8.add('PC')

        x = 'G'
        if x in ppe1:
            det_9.add('C')
        if x in ppe2:
            det_9.add('F')
        if x in ppe3:
            det_9.add('R')
        if x in ppd1:
            det_9.add('P')
        if x in ppd2:
            det_9.add('BP')
        if x in ppd3:
            det_9.add('PC')

        x = 'H'
        if x in ppe1:
            det_10.add('C')
        if x in ppe2:
            det_10.add('F')
        if x in ppe3:
            det_10.add('R')
        if x in ppd1:
            det_10.add('P')
        if x in ppd2:
            det_10.add('BP')
        if x in ppd3:
            det_10.add('PC')

        x = 'I'
        if x in ppe1:
            det_11.add('C')
        if x in ppe2:
            det_11.add('F')
        if x in ppe3:
            det_11.add('R')
        if x in ppd1:
            det_11.add('P')
        if x in ppd2:
            det_11.add('BP')
        if x in ppd3:
            det_11.add('PC')

        x = 'J'
        if x in ppe1:
            det_12.add('C')
        if x in ppe2:
            det_12.add('F')
        if x in ppe3:
            det_12.add('R')
        if x in ppd1:
            det_12.add('P')
        if x in ppd2:
            det_12.add('BP')
        if x in ppd3:
            det_12.add('PC')

        x = 'K'
        if x in ppe1:
            det_13.add('C')
        if x in ppe2:
            det_13.add('F')
        if x in ppe3:
            det_13.add('R')
        if x in ppd1:
            det_13.add('P')
        if x in ppd2:
            det_13.add('BP')
        if x in ppd3:
            det_13.add('PC')

        x = 'L'
        if x in ppe1:
            det_14.add('C')
        if x in ppe2:
            det_14.add('F')
        if x in ppe3:
            det_14.add('R')
        if x in ppd1:
            det_14.add('P')
        if x in ppd2:
            det_14.add('BP')
        if x in ppd3:
            det_14.add('PC')

        x = 'M'
        if x in ppe1:
            det_15.add('C')
        if x in ppe2:
            det_15.add('F')
        if x in ppe3:
            det_15.add('R')
        if x in ppd1:
            det_15.add('P')
        if x in ppd2:
            det_15.add('BP')
        if x in ppd3:
            det_15.add('PC')

        x = 'O'
        if x in ppe1:
            det_18.add('C')
        if x in ppe2:
            det_18.add('F')
        if x in ppe3:
            det_18.add('R')
        if x in ppd1:
            det_18.add('P')
        if x in ppd2:
            det_18.add('BP')
        if x in ppd3:
            det_18.add('PC')

        x = 'Q'
        if x in ppe1:
            det_22.add('C')
        if x in ppe2:
            det_22.add('F')
        if x in ppe3:
            det_22.add('R')
        if x in ppd1:
            det_22.add('P')
        if x in ppd2:
            det_22.add('BP')
        if x in ppd3:
            det_22.add('PC')

        x = 'R'
        if x in ppe1:
            det_23.add('C')
        if x in ppe2:
            det_23.add('F')
        if x in ppe3:
            det_23.add('R')
        if x in ppd1:
            det_23.add('P')
        if x in ppd2:
            det_23.add('BP')
        if x in ppd3:
            det_23.add('PC')

        x = 'S'
        if x in ppe1:
            det_24.add('C')
        if x in ppe2:
            det_24.add('F')
        if x in ppe3:
            det_24.add('R')
        if x in ppd1:
            det_24.add('P')
        if x in ppd2:
            det_24.add('BP')
        if x in ppd3:
            det_24.add('PC')

        x = 'T'
        if x in ppe1:
            det_25.add('C')
        if x in ppe2:
            det_25.add('F')
        if x in ppe3:
            det_25.add('R')
        if x in ppd1:
            det_25.add('P')
        if x in ppd2:
            det_25.add('BP')
        if x in ppd3:
            det_25.add('PC')

        x = 'U'
        if x in ppe1:
            det_26.add('C')
        if x in ppe2:
            det_26.add('F')
        if x in ppe3:
            det_26.add('R')
        if x in ppd1:
            det_26.add('P')
        if x in ppd2:
            det_26.add('BP')
        if x in ppd3:
            det_26.add('PC')

        x = 'V'
        if x in ppe1:
            det_27.add('C')
        if x in ppe2:
            det_27.add('F')
        if x in ppe3:
            det_27.add('R')
        if x in ppd1:
            det_27.add('P')
        if x in ppd2:
            det_27.add('BP')
        if x in ppd3:
            det_27.add('PC')

        cls()

# -------------------------------------- TAXAS DE VARIÂNCIA E ANÁLISE DE PADRÔES DE FLUXO

        var_max_d1 = d1a+d1b+d1c
        var_max_d2 = d2a+d2b+d2c
        var_max_d3 = d3a+d3b+d3c
        var_max_e1 = e1a+e1b+e1c
        var_max_e2 = e2a+e2b+e2c
        var_max_e3 = e3a+e3b+e3c
        var_min_d1 = d1a-d1b-d1c
        var_min_d2 = d2a-d2b-d2c
        var_min_d3 = d3a-d3b-d3c
        var_min_e1 = e1a-e1b-e1c
        var_min_e2 = e2a-e2b-e2c
        var_min_e3 = e3a-e3b-e3c

        if var_max_d1 > 6:
            pct.add(dx[57])
        if var_max_d2 > 6:
            pct.add(dx[55])
        if var_max_d3 > 6:
            pct.add(dx[56])
        if var_max_e1 > 6:
            pct.add(dx[54])
        if var_max_e2 > 6:
            pct.add(dx[59])
        if var_max_e3 > 6:
            pct.add(dx[58])
        if var_min_d1 <= 4:
            pct.add(dx[147])
        if var_min_d2 <= 4:
            pct.add(dx[145])
        if var_min_d3 <= 4:
            pct.add(dx[146])
        if var_min_e1 <= 4:
            pct.add(dx[144])
        if var_min_e2 <= 4:
            pct.add(dx[149])
        if var_min_e3 <= 4:
            pct.add(dx[148])

# -------------------------------------- CÁLCULO VECTOR PARA CORREÇÃO DE ERROS E ANÁLISE DE FLUXO

        # YANG-YIN +CC -FV
        vector1[0] = d3a-d3c  # TA
        vector1[1] = e1a-e1c  # C
        vector1[2] = d2a-d2c  # BP
        vector1[3] = d1a-d1c  # P
        vector1[4] = e3a-e3c  # R
        vector1[5] = e2a-e2c  # F

        # YIN-YANG +FC -CV
        vector2[0] = d3c-d3a  # TA
        vector2[1] = e1c-e1a  # C
        vector2[2] = d2c-d2a  # BP
        vector2[3] = d1c-d1a  # P
        vector2[4] = e3c-e3a  # R
        vector2[5] = e2c-e2a  # F

# -------------------------------------- COLETA DE DADOS PARA AUTOMATIZAÇÃO

        a = 'A'
        if a in ppd1 or a in ppd2 or a in ppd3 or a in ppe1 or a in ppe2 or a in ppe3:
            pool.add(tipo_p[3])
        a = 'B'
        if a in ppd1 or a in ppd2 or a in ppd3 or a in ppe1 or a in ppe2 or a in ppe3:
            pool.add(tipo_p[4])
        a = 'C'
        if a in ppd1 or a in ppd2 or a in ppd3 or a in ppe1 or a in ppe2 or a in ppe3:
            pool.add(tipo_p[5])
        a = 'E'
        if a in ppd1 or a in ppd2 or a in ppd3 or a in ppe1 or a in ppe2 or a in ppe3:
            pool.add(tipo_p[7])
        a = 'F'
        if a in ppd1 or a in ppd2 or a in ppd3 or a in ppe1 or a in ppe2 or a in ppe3:
            pool.add(tipo_p[8])
        a = 'G'
        if a in ppd1 or a in ppd2 or a in ppd3 or a in ppe1 or a in ppe2 or a in ppe3:
            pool.add(tipo_p[9])
        a = 'H'
        if a in ppd1 or a in ppd2 or a in ppd3 or a in ppe1 or a in ppe2 or a in ppe3:
            pool.add(tipo_p[10])
        a = 'I'
        if a in ppd1 or a in ppd2 or a in ppd3 or a in ppe1 or a in ppe2 or a in ppe3:
            pool.add(tipo_p[11])
        a = 'J'
        if a in ppd1 or a in ppd2 or a in ppd3 or a in ppe1 or a in ppe2 or a in ppe3:
            pool.add(tipo_p[12])
        a = 'K'
        if a in ppd1 or a in ppd2 or a in ppd3 or a in ppe1 or a in ppe2 or a in ppe3:
            pool.add(tipo_p[13])
        a = 'L'
        if a in ppd1 or a in ppd2 or a in ppd3 or a in ppe1 or a in ppe2 or a in ppe3:
            pool.add(tipo_p[14])
        a = 'M'
        if a in ppd1 or a in ppd2 or a in ppd3 or a in ppe1 or a in ppe2 or a in ppe3:
            pool.add(tipo_p[15])
        a = 'O'
        if a in ppd1 or a in ppd2 or a in ppd3 or a in ppe1 or a in ppe2 or a in ppe3:
            pool.add(tipo_p[18])
        a = 'Q'
        if a in ppd1 or a in ppd2 or a in ppd3 or a in ppe1 or a in ppe2 or a in ppe3:
            pool.add(tipo_p[22])
        a = 'R'
        if a in ppd1 or a in ppd2 or a in ppd3 or a in ppe1 or a in ppe2 or a in ppe3:
            pool.add(tipo_p[23])
        a = 'S'
        if a in ppd1 or a in ppd2 or a in ppd3 or a in ppe1 or a in ppe2 or a in ppe3:
            pool.add(tipo_p[24])
        a = 'T'
        if a in ppd1 or a in ppd2 or a in ppd3 or a in ppe1 or a in ppe2 or a in ppe3:
            pool.add(tipo_p[25])
        a = 'U'
        if a in ppd1 or a in ppd2 or a in ppd3 or a in ppe1 or a in ppe2 or a in ppe3:
            pool.add(tipo_p[26])
        a = 'V'
        if a in ppd1 or a in ppd2 or a in ppd3 or a in ppe1 or a in ppe2 or a in ppe3:
            pool.add(tipo_p[27])

        # -------------------------------------- AUTOMATIZAÇÃO DE PULSOS PATOLÓGICOS

        # RISCO DE TUMOR POR ESTASE - IMPERADOR PÁG. 241
        if 'H' in ppe3 or 'M' in ppe3:
            if 'H' in ppe2 or 'M' in ppe2:
                if 'C' in ppe1 or 'H' in ppe1:
                    warn.add(
                        'Risco de tumor devido a estase de xue - método da qi lun de su wen'.upper())
        # FU/ RU
        cls()
        if d1a != 1 and d1b == 1:
            while True:
                try:
                    d1 = input(
                        'D1 com pulso macio, elástico e levemente pérvio - indicando pulso encharcado (S/N)? ').upper()
                    if d1 == 'S':
                        det_20.add('P')
                        pool.add(tipo_p[20])
                        if d1c == 1:
                            pct.add(dx[27])
                        else:
                            pct.add(dx[21])
                            pct.add(dx[117])
                        break
                    else:
                        pool.add(tipo_p[1])
                        det_1.add('P')
                        if vector2[3] > 0:
                            pct.add(dx[135])
                        break
                except:
                    break

        if d2a != 1 and d2b == 1:
            while True:
                try:
                    d2 = input(
                        'D2 com pulso macio, elástico e levemente pérvio - indicando pulso encharcado (S/N)? ').upper()
                    if d2 == 'S':
                        det_20.add('BP')
                        pool.add(tipo_p[20])
                        if d2c == 1:
                            pct.add(dx[25])
                        else:
                            pct.add(dx[19])
                            pct.add(dx[115])
                        break
                    else:
                        pool.add(tipo_p[1])
                        det_1.add('BP')
                        if vector2[2] > 0:
                            pct.add(dx[133])
                        break
                except:
                    break

        if d3a != 1 and d3b == 1:
            while True:
                try:
                    d3 = input(
                        'D3 com pulso macio, elástico e levemente pérvio - indicando pulso encharcado (S/N)? ').upper()
                    if d3 == 'S':
                        det_20.add('PC')
                        pool.add(tipo_p[20])
                        if d3c == 1:
                            pct.add(dx[26])
                        else:
                            pct.add(dx[20])
                            pct.add(dx[116])
                        break
                    else:
                        pool.add(tipo_p[1])
                        det_1.add('PC')
                        if vector2[0] > 0:
                            pct.add(dx[134])
                        break
                except:
                    break

        if e1a != 1 and e1b == 1:
            while True:
                try:
                    e1 = input(
                        'E1 com pulso macio, elástico e levemente pérvio - indicando pulso encharcado (S/N)? ').upper()
                    if e1 == 'S':
                        det_20.add('C')
                        pool.add(tipo_p[20])
                        if e1c == 1:
                            pct.add(dx[24])
                        else:
                            pct.add(dx[18])
                            pct.add(dx[114])
                        break
                    else:
                        pool.add(tipo_p[1])
                        det_1.add('C')
                        if vector2[1] > 0:
                            pct.add(dx[132])
                        break
                except:
                    break

        if e2a != 1 and e2b == 1:
            while True:
                try:
                    e2 = input(
                        'E2 com pulso macio, elástico e levemente pérvio - indicando pulso encharcado (S/N)? ').upper()
                    if e2 == 'S':
                        det_20.add('F')
                        pool.add(tipo_p[20])
                        if e2c == 1:
                            pct.add(dx[29])
                        else:
                            pct.add(dx[23])
                            pct.add(dx[119])
                        break
                    else:
                        pool.add(tipo_p[1])
                        det_1.add('F')
                        if vector2[5] > 0:
                            pct.add(dx[137])
                        break
                except:
                    break

        if e3a != 1 and e3b == 1:
            while True:
                try:
                    e3 = input(
                        'E3 com pulso macio, elástico e levemente pérvio - indicando pulso encharcado (S/N)? ').upper()
                    if e3 == 'S':
                        det_20.add('R')
                        pool.add(tipo_p[20])
                        if e3c == 1:
                            pct.add(dx[28])
                        else:
                            pct.add(dx[22])
                            pct.add(dx[118])
                        break
                    else:
                        pool.add(tipo_p[1])
                        det_1.a7dd('R')
                        if vector2[4] > 0:
                            pct.add(dx[136])
                        break
                except:
                    break

#  JI/ SHU
            if 'P' in det_4:
                if var_max_d1 > 7:
                    pct.add(dx[217])
                    pct.add(dx[9])
                    pool.add(tipo_p[28])
                    det_28.add('P')
                else:
                    pool.add(tipo_p[4])
                    if 'P' in det_1:
                        pct.add(dx[177])
                        pct.discard(dx[171])
                    if 'P' in det_6:
                        pct.add(dx[171])
                        pct.discard(dx[177])
                    else:
                        pass

            if 'BP' in det_4:
                if var_max_d2 > 7:
                    pct.add(dx[215])
                    pct.add(dx[7])
                    pool.add(tipo_p[28])
                    det_28.add('BP')
                else:
                    pool.add(tipo_p[4])
                    if 'BP' in det_1:
                        pct.add(dx[175])
                        pct.discard(dx[169])
                    if 'BP' in det_6:
                        pct.add(dx[169])
                        pct.discard(dx[175])
                    else:
                        pass

            if 'PC' in det_4:
                if var_max_d3 > 7:
                    pct.add(dx[216])
                    pct.add(dx[8])
                    pool.add(tipo_p[28])
                    det_28.add('PC')
                else:
                    pool.add(tipo_p[4])
                    if 'PC' in det_1:
                        pct.add(dx[176])
                        pct.discard(dx[170])
                    if 'PC' in det_6:
                        pct.add(dx[170])
                        pct.discard(dx[176])
                    else:
                        pass

            if 'C' in det_4:
                if var_max_e1 > 7:
                    pct.add(dx[214])
                    pct.add(dx[6])
                    pool.add(tipo_p[28])
                    det_28.add('C')
                else:
                    pool.add(tipo_p[4])
                    if 'C' in det_1:
                        pct.add(dx[174])
                        pct.discard(dx[168])
                    if 'C' in det_6:
                        pct.add(dx[168])
                        pct.discard(dx[174])
                    else:
                        pass

            if 'F' in det_4:
                if var_max_e2 > 7:
                    pct.add(dx[219])
                    pct.add(dx[11])
                    pool.add(tipo_p[28])
                    det_28.add('F')
                else:
                    pool.add(tipo_p[4])
                    if 'F' in det_1:
                        pct.add(dx[179])
                        pct.discard(dx[173])
                    if 'C' in det_6:
                        pct.add(dx[173])
                        pct.discard(dx[179])
                    else:
                        pass

            if 'R' in det_4:
                if var_max_e3 > 7:
                    pct.add(dx[218])
                    pct.add(dx[10])
                    pool.add(tipo_p[28])
                    det_28.add('R')
                else:
                    pool.add(tipo_p[4])
                    if 'R' in det_1:
                        pct.add(dx[178])
                        pct.discard(dx[172])
                    if 'R' in det_6:
                        pct.add(dx[172])
                        pct.discard(dx[178])
                    else:
                        pass

# SHI
        def shi(a, b, c):
            if a >= 2:
                d = 0
            else:
                d = 1
            if b >= 2:
                e = 0
            else:
                e = 1
            if c >= 2:
                f = 0
            else:
                f = 1
            return d+e+f
        a = 0
        if shi(d1a, d1b, d1c) == 0:
            det_6.add('P')
            a = 1
        if shi(d2a, d2b, d2c) == 0:
            det_6.add('BP')
            a = 1
        if shi(d3a, d3b, d3c) == 0:
            det_6.add('PC')
            a = 1
        if shi(e1a, e1b, e1c) == 0:
            det_6.add('C')
            a = 1
        if shi(e2a, e2b, e2c) == 0:
            det_6.add('F')
            a = 1
        if shi(e3a, e3b, e3c) == 0:
            det_6.add('R')
            a = 1
        if a == 1:
            pool.add(tipo_p[6])

#  RUO
        def ruo(x, y, z):
            if x == 1:
                m = 0
            else:
                m = 1
            if y > 1:
                n = 0
            else:
                n = 1
            if z > 1:
                o = 0
            else:
                o = 1
            return m+n+o

            if ruo(d1a, d1b, d1c) == 0:
                det_21.add('P')
                pct.add(dx[15])
                pct.add(dx[3])
            if ruo(d2a, d2b, d2c) == 0:
                det_21.add('BP')
                pct.add(dx[1])
                pct.add(dx[13])
            if ruo(d3a, d3b, d3c) == 0:
                det_21.add('PC')
                pct.add(dx[14])
                pct.add(dx[2])
            if ruo(e1a, e1b, e1c) == 0:
                det_21.add('C')
                pct.add(dx[12])
                pct.add(dx[0])
            if ruo(e2a, e2b, e2c) == 0:
                det_21.add('F')
                pct.add(dx[17])
                pct.add(dx[5])
            if ruo(e3a, e3b, e3c) == 0:
                det_21.add('R')
                pct.add(dx[16])
                pct.add(dx[4])
            if len(det_21) > 0:
                pool.add(tipo_p[21])

#  CHEN
        if var_max_d1 < 6 and d1c != 1:
            det_2.add('P')
            if 'P' in det_21:
                pct.add(dx[21])
            if 'P' in det_6:
                pct.add(dx[63])
        if var_max_d2 < 6 and d2c != 1:
            det_2.add('BP')
            if 'BP' in det_21:
                pct.add(dx[19])
            if 'BP' in det_6:
                pct.add(dx[61])
        if var_max_d3 < 6 and d3c != 1:
            det_2.add('PC')
            if 'PC' in det_21:
                pct.add(dx[20])
            if 'PC' in det_6:
                pct.add(dx[62])
        if var_max_e1 < 6 and e1c != 1:
            det_2.add('C')
            if 'C' in det_21:
                pct.add(dx[18])
            if 'C' in det_6:
                pct.add(dx[60])
        if var_max_e2 < 6 and e2c != 1:
            det_2.add('F')
            if 'F' in det_21:
                pct.add(dx[23])
            if 'F' in det_6:
                pct.add(dx[65])
        if var_max_e3 < 6 and e3c != 1:
            det_2.add('R')
            if 'R' in det_21:
                pct.add(dx[22])
            if 'R' in det_6:
                pct.add(dx[64])
        if len(det_2) > 0:
            pool.add(tipo_p[2])

#  KOU
        def kou(x, y, z):
            if x > 1:
                m = 0
            else:
                m = 1
            if y == 1:
                n = 0
            else:
                n = 1
            if z > 1:
                o = 0
            else:
                o = 1
            return m+n+o
        if kou(d1a, d1b, d1c) == 0 or kou(d2a, d2b, d2c) == 0 or kou(d3a, d3b, d3c) == 0 or kou(e1a, e1b, e1c) == 0 or kou(e2a, e2b, e2c) == 0 or kou(e3a, e3b, e3c) == 0:
            pool.add(tipo_p[17])
            warn.add('Risco de hemorragia grave'.upper())

#  LAO
        def lao(x, y, z):
            if x == 1:
                m = 0
            else:
                m = 1
            if y == 1:
                n = 0
            else:
                n = 1
            if z > 1:
                o = 0
            else:
                o = 1
            return m+n+o
            a = 0
            if lao(d1a, d1b, d1c) == 0:
                a = 1
                if 'P' in det_14 or 'P' in det_9:
                    pct.add(dx[57])
                if 'P' in det_3:
                    warn.add(
                        'Possibilidade de estar sentindo dor tipo frio em meridiano P/IG'.upper())
            if lao(d2a, d2b, d2c) == 0:
                a = 1
                if 'BP' in det_14 or 'BP' in det_9:
                    pct.add(dx[55])
                if 'BP' in det_3:
                    warn.add(
                        'Possibilidade de estar sentindo dor tipo frio em meridiano BP/E'.upper())
            if lao(d3a, d3b, d3c) == 0:
                a = 1
                if 'PC' in det_14 or 'PC' in det_9:
                    pct.add(dx[56])
                if 'PC' in det_3:
                    warn.add(
                        'Possibilidade de estar sentindo dor tipo frio em meridiano PC/TA'.upper())
            if lao(e1a, e1b, e1c) == 0:
                a = 1
                if 'C' in det_14 or 'C' in det_9:
                    pct.add(dx[54])
                if 'C' in det_3:
                    warn.add(
                        'Possibilidade de estar sentindo dor tipo frio em meridiano C/ID'.upper())
            if lao(e2a, e2b, e2c) == 0:
                a = 1
                if 'F' in det_14 or 'F' in det_9:
                    pct.add(dx[59])
                if 'F' in det_3:
                    warn.add(
                        'Possibilidade de estar sentindo dor tipo frio em meridiano F/VB'.upper())
            if lao(e3a, e3b, e3c) == 0:
                a = 1
                if 'R' in det_14 or 'R' in det_9:
                    pct.add(dx[58])
                if 'R' in det_3:
                    warn.add(
                        'Possibilidade de estar sentindo dor tipo frio em meridiano R/B'.upper())
            if a == 1:
                pool.add(tipo_p[19])

# CHI/ HUAN
        def k(): return pool.add(tipo_p[16])
        if d1a >= 2 and d1b >= 2 and d1c >= 2:
            if 'P' in det_21:
                k()
            elif 'P' in det_6:
                pct.discard(dx[189])
                pct.add(dx[183])
        else:
            if 'P' in det_21:
                pct.discard(dx[183])
                pct.add(dx[189])
        if d2a >= 2 and d2b >= 2 and d2c >= 2:
            if 'BP' in det_21:
                k()
            elif 'BP' in det_6:
                pct.discard(dx[187])
                pct.add(dx[181])
        else:
            if 'BP' in det_21:
                pct.discard(dx[181])
                pct.add(dx[187])

        if d3a >= 2 and d3b >= 2 and d3c >= 2:
            if 'PC' in det_21:
                k()
            elif 'PC' in det_6:
                pct.discard(dx[188])
                pct.add(dx[182])
        else:
            if 'PC' in det_21:
                pct.discard(dx[182])
                pct.add(dx[188])
        if e1a >= 2 and e1b >= 2 and e1c >= 2:
            if 'C' in det_21:
                k()
            elif 'C' in det_6:
                pct.discard(dx[186])
                pct.add(dx[180])
        else:
            if 'C' in det_21:
                pct.discard(dx[180])
                pct.add(dx[186])
        if e2a >= 2 and e2b >= 2 and e2c >= 2:
            if 'F' in det_21:
                k()
            elif 'F' in det_6:
                pct.discard(dx[191])
                pct.add(dx[185])
        else:
            if 'F' in det_21:
                pct.discard(dx[191])
                pct.add(dx[185])
        if e3a >= 2 and e3b >= 2 and e3c >= 2:
            if 'R' in det_21:
                k()
            elif 'R' in det_6:
                pct.discard(dx[190])
                pct.add(dx[184])
        else:
            if 'R' in det_21:
                pct.discard(dx[184])
                pct.add(dx[190])

# XU
        a = 1
        b = 1
        if 'P' in det_5:
            pct.add(dx[21])
            a = 2
        if 'BP' in det_5:
            pct.add(dx[19])
            a = 2
        if 'PC' in det_5:
            pct.add(dx[20])
            a = 2
        if 'C' in det_5:
            pct.add(dx[18])
            a = 2
        if 'F' in det_5:
            pct.add(dx[23])
            a = 2
        if 'R' in det_5:
            pct.add(dx[22])
            a = 2
        if a == 2:
            pool.add(tipo_p[5])

# HUA
        if 'P' in det_7:
            pct.add(dx[117])
            b = 2
        if 'BP' in det_7:
            pct.add(dx[115])
            b = 2
        if 'PC' in det_7:
            pct.add(dx[116])
            b = 2
        if 'C' in det_7:
            pct.add(dx[114])
            b = 2
        if 'F' in det_7:
            pct.add(dx[119])
            b = 2
        if 'R' in det_7:
            pct.add(dx[118])
            b = 2
        if b == 2:
            pool.add(tipo_p[7])

# SE
        a = 'P'
        if a in det_8:
            if a in det_15 or a in det_26:
                pct.add(dx[57])
            else:
                pct.add(dx[3])
                pct.add(dx[123])
        a = 'BP'
        if a in det_8:
            if a in det_15 or a in det_26:
                pct.add(dx[55])
            else:
                pct.add(dx[1])
                pct.add(dx[121])
        a = 'PC'
        if a in det_8:
            if a in det_15 or a in det_26:
                pct.add(dx[56])
            else:
                pct.add(dx[2])
                pct.add(dx[122])
        a = 'C'
        if a in det_8:
            if a in det_15 or a in det_26:
                pct.add(dx[54])
            else:
                pct.add(dx[0])
                pct.add(dx[120])
        a = 'F'
        if a in det_8:
            if a in det_15 or a in det_26:
                pct.add(dx[59])
            else:
                pct.add(dx[5])
                pct.add(dx[125])
        a = 'R'
        if a in det_8:
            if a in det_15 or a in det_26:
                pct.add(dx[58])
            else:
                pct.add(dx[4])
                pct.add(dx[124])

# CHANG
        a = 'G'
        b = 0
        if a in ppd1:
            if dx[105] not in pct and dx[177] not in pct and dx[171] not in pct:
                dxconf.add('Pulso chang indica calor não localizado em Pulmão')
                b = 1
        if a in ppd2:
            if dx[103] not in pct and dx[175] not in pct and dx[169] not in pct:
                dxconf.add(
                    'Pulso chang indica calor não localizado em Baço/Pâncreas')
                b = 1
        if a in ppd3:
            if dx[104] not in pct and dx[176] not in pct and dx[170] not in pct:
                dxconf.add(
                    'Pulso chang indica calor não localizado em Triplo Aquecedor')
                b = 1
        if a in ppe1:
            if dx[103] not in pct and dx[175] not in pct and dx[169] not in pct:
                dxconf.add(
                    'Pulso chang indica calor não localizado em Coração')
                b = 1
        if a in ppe2:
            if dx[107] not in pct and dx[179] not in pct and dx[173] not in pct:
                dxconf.add('Pulso chang indica calor não localizado em Fígado')
                b = 1
        if a in ppe3:
            if dx[106] not in pct and dx[178] not in pct and dx[172] not in pct:
                dxconf.add('Pulso chang indica calor não localizado em Rim')
                b = 1
        if b == 1:
            pool.add(tipo_p[9])

# DUAN
        a = 'H'
        b = 0
        if a in ppd1:
            pct.add(dx[21])
            pct.add(dx[19])
            b = 1
        if a in ppd2:
            pct.add(dx[19])
            b = 1
        if a in ppd3:
            pct.add(dx[20])
            pct.add(dx[19])
            b = 1
        if a in ppe1:
            pct.add(dx[18])
            pct.add(dx[19])
            b = 1
        if a in ppe2:
            pct.add(dx[23])
            pct.add(dx[19])
            b = 1
        if a in ppe3:
            pct.add(dx[22])
            pct.add(dx[19])
            b = 1
        if b == 1:
            pool.add(tipo_p[10])

# HONG

        def a(): return pool.add(tipo_p[11])
        x = 'P'
        b = 'Pulmão/ Intestino Grosso'
        c = 183  # frio cheio
        if x in det_11:
            a()

            def uli(w, c):
                if w == True:
                    r = pct.discard(dx[int(c)])  # frio cheio
                    s = pct.discard(dx[int(c+6)])  # frio vazio
                    t = pct.discard(dx[int(c-6)])  # calor vazio
                    u = pct.add(dx[int(c-12)])  # calor cheio
                elif w == False:
                    r = pct.discard(dx[int(c)])  # frio cheio
                    s = pct.discard(dx[int(c+6)])  # frio vazio
                    t = pct.discard(dx[int(c-12)])  # calor cheio
                    u = pct.add(dx[int(c-6)])  # calor vazio
                return r, s, t, u
            if x in det_6:
                while True:
                    try:
                        perg_diferencial = input(
                            'Sugerida febre infecciosa ou calor cheio. Há presença de algum foco infeccioso em meridiano de '+b+' (S/N)? ').upper()
                        if perg_diferencial == 'S':
                            warn.add(
                                ('Sugestão de infecção com febre ('+b+')').upper())
                            break
                        if perg_diferencial == 'N':
                            uli(True, int(c))
                            break
                    except:
                        continue
            elif x in det_5:
                uli(False, int(c))
            elif x in det_4:
                pct.add(dx[int(c+28)])  # fleuma-fogo
                uli(True, int(c))
        x = 'BP'
        b = 'Baço/ Estômago'
        c = 181  # frio cheio
        if x in det_11:
            def uli(w, c):
                if w == True:
                    r = pct.discard(dx[int(c)])  # frio cheio
                    s = pct.discard(dx[int(c+6)])  # frio vazio
                    t = pct.discard(dx[int(c-6)])  # calor vazio
                    u = pct.add(dx[int(c-12)])  # calor cheio
                elif w == False:
                    r = pct.discard(dx[int(c)])  # frio cheio
                    s = pct.discard(dx[int(c+6)])  # frio vazio
                    t = pct.discard(dx[int(c-12)])  # calor cheio
                    u = pct.add(dx[int(c-6)])  # calor vazio
                return r, s, t, u
            a()
            if x in det_6:
                while True:
                    try:
                        perg_diferencial = input(
                            'Sugerida febre infecciosa ou calor cheio. Há presença de algum foco infeccioso em meridiano de '+b+' (S/N)? ').upper()
                        if perg_diferencial == 'S':
                            warn.add(
                                ('Sugestão de infecção com febre ('+b+')').upper())
                            break
                        if perg_diferencial == 'N':
                            uli(True, int(c))
                            break
                    except:
                        continue
            elif x in det_5:
                uli(False, int(c))
            elif x in det_4:
                pct.add(dx[int(c+28)])  # fleuma-fogo
                uli(True, int(c))
        x = 'PC'
        b = 'Pericárdio/ Triplo Aquecedor'
        c = 182  # frio cheio
        if x in det_11:
            def uli(w, c):
                if w == True:
                    r = pct.discard(dx[int(c)])  # frio cheio
                    s = pct.discard(dx[int(c+6)])  # frio vazio
                    t = pct.discard(dx[int(c-6)])  # calor vazio
                    u = pct.add(dx[int(c-12)])  # calor cheio
                elif w == False:
                    r = pct.discard(dx[int(c)])  # frio cheio
                    s = pct.discard(dx[int(c+6)])  # frio vazio
                    t = pct.discard(dx[int(c-12)])  # calor cheio
                    u = pct.add(dx[int(c-6)])  # calor vazio
                return r, s, t, u
            a()
            if x in det_6:
                while True:
                    try:
                        perg_diferencial = input(
                            'Sugerida febre infecciosa ou calor cheio. Há presença de algum foco infeccioso em meridiano de '+b+' (S/N)? ').upper()
                        if perg_diferencial == 'S':
                            warn.add(
                                ('Sugestão de infecção com febre ('+b+')').upper())
                            break
                        if perg_diferencial == 'N':
                            uli(True, int(c))
                            break
                    except:
                        continue
            elif x in det_5:
                uli(False, int(c))
            elif x in det_4:
                pct.add(dx[int(c+28)])  # fleuma-fogo
                uli(True, int(c))
        x = 'C'
        b = 'Coração/ Intestino Delgado'
        c = 180  # frio cheio
        if x in det_11:
            def uli(w, c):
                if w == True:
                    r = pct.discard(dx[int(c)])  # frio cheio
                    s = pct.discard(dx[int(c+6)])  # frio vazio
                    t = pct.discard(dx[int(c-6)])  # calor vazio
                    u = pct.add(dx[int(c-12)])  # calor cheio
                elif w == False:
                    r = pct.discard(dx[int(c)])  # frio cheio
                    s = pct.discard(dx[int(c+6)])  # frio vazio
                    t = pct.discard(dx[int(c-12)])  # calor cheio
                    u = pct.add(dx[int(c-6)])  # calor vazio
                return r, s, t, u
            a()
            if x in det_6:
                while True:
                    try:
                        perg_diferencial = input(
                            'Sugerida febre infecciosa ou calor cheio. Há presença de algum foco infeccioso em meridiano de '+b+' (S/N)? ').upper()
                        if perg_diferencial == 'S':
                            warn.add(
                                ('Sugestão de infecção com febre ('+b+')').upper())
                            break
                        if perg_diferencial == 'N':
                            uli(True, int(c))
                            break
                    except:
                        continue
            elif x in det_5:
                uli(False, int(c))
            elif x in det_4:
                pct.add(dx[int(c+28)])  # fleuma-fogo
                uli(True, int(c))
        x = 'F'
        b = 'Fígado/ Vesícula Biliar'
        c = 185  # frio cheio
        if x in det_11:
            def uli(w, c):
                if w == True:
                    r = pct.discard(dx[int(c)])  # frio cheio
                    s = pct.discard(dx[int(c+6)])  # frio vazio
                    t = pct.discard(dx[int(c-6)])  # calor vazio
                    u = pct.add(dx[int(c-12)])  # calor cheio
                elif w == False:
                    r = pct.discard(dx[int(c)])  # frio cheio
                    s = pct.discard(dx[int(c+6)])  # frio vazio
                    t = pct.discard(dx[int(c-12)])  # calor cheio
                    u = pct.add(dx[int(c-6)])  # calor vazio
                return r, s, t, u
            a()
            if x in det_6:
                while True:
                    try:
                        perg_diferencial = input(
                            'Sugerida febre infecciosa ou calor cheio. Há presença de algum foco infeccioso em meridiano de '+b+' (S/N)? ').upper()
                        if perg_diferencial == 'S':
                            warn.add(
                                ('Sugestão de infecção com febre ('+b+')').upper())
                            break
                        if perg_diferencial == 'N':
                            uli(True, int(c))
                            break
                    except:
                        continue
            elif x in det_5:
                uli(False, int(c))
            elif x in det_4:
                pct.add(dx[int(c+28)])  # fleuma-fogo
                uli(True, int(c))
        x = 'R'
        b = 'Rim/ Bexiga'
        c = 184  # frio cheio
        if x in det_11:
            def uli(w, c):
                if w == True:
                    r = pct.discard(dx[int(c)])  # frio cheio
                    s = pct.discard(dx[int(c+6)])  # frio vazio
                    t = pct.discard(dx[int(c-6)])  # calor vazio
                    u = pct.add(dx[int(c-12)])  # calor cheio
                elif w == False:
                    r = pct.discard(dx[int(c)])  # frio cheio
                    s = pct.discard(dx[int(c+6)])  # frio vazio
                    t = pct.discard(dx[int(c-12)])  # calor cheio
                    u = pct.add(dx[int(c-6)])  # calor vazio
                return r, s, t, u
            a()
            if x in det_6:
                while True:
                    try:
                        perg_diferencial = input(
                            'Sugerida febre infecciosa ou calor cheio. Há presença de algum foco infeccioso em meridiano de '+b+' (S/N)? ').upper()
                        if perg_diferencial == 'S':
                            warn.add(
                                ('Sugestão de infecção com febre ('+b+')').upper())
                            break
                        if perg_diferencial == 'N':
                            uli(True, int(c))
                            break
                    except:
                        continue
            elif x in det_5:
                uli(False, int(c))
            elif x in det_4:
                pct.add(dx[int(c+28)])  # fleuma-fogo
                uli(True, int(c))

# XI/ WEI

        def xifx(a, b, c):
            if b in det_12:
                if vector1[int(c)] < vector2[int(c)] and b not in det_11:
                    r = int(a)+18
                    return pct.add(dx[int(r)])
                elif vector2[int(c)] < vector1[int(c)]:
                    r = int(a)
                    return pct.add(dx[int(r)])
            if b in det_13:
                t = int(a)
                u = int(a)+18
                return pct.add(dx[int(t)]), pct.add(dx[int(u)])

        xifx(3, 'P', 3)
        xifx(1, 'BP', 2)
        xifx(2, 'PC', 0)
        xifx(0, 'C', 1)
        xifx(5, 'F', 5)
        xifx(4, 'R', 4)
        # c=vector, a=dx

# JIN

        # a=dx-frio_externo b=meridiano c=pulso+c(d1c, d2c, e1c)
        def jinfx(a, b, c):
            if b in det_14:
                if b in det_1 and b in det_6:
                    return pct.add(dx[int(a)])
                if b in det_2:
                    if b in det_6:
                        return pct.add(dx[int(a+84)])
                        return pct.discard(dx[int(a+90)])
                    elif b in det_1:
                        if str(c) == 3 or dx[int(a)+84] in pct:
                            x = input(
                                'Paciente é portador de DPOC ou asma? (S/N) ').upper()
                            if x == 'S':
                                warn.add(
                                    'Possível descompensação de asma'.upper())
                            pct.add(
                                'Possibilidade de dor de frio em meridiano de'+b)

                        else:
                            return pct.add(dx[int(a)+90])
                            return pct.add(dx[int(a)+84])
        jinfx(99, 'P', d1c)
        jinfx(97, 'BP', d2c)
        jinfx(98, 'PC', d3c)
        jinfx(96, 'C', e1c)
        jinfx(101, 'F', e2c)
        jinfx(100, 'R', e3c)

# XIAN

        if tipo_p[15] in pool:
            if tipo_p[6] in pool or tipo_p[26] in pool:
                pct.add(dx[54])
                pct.add(dx[60])
            elif e2b == 3 or e2c == 3:
                pct.add(dx[119])
            else:
                pct.add(dx[59])

# GE
        a = 'O'
        if a in ppe1:
            pct.add(dx[24])
        if a in ppd2:
            pct.add(dx[25])
        if a in ppd3:
            pct.add(dx[26])
        if a in ppd1:
            pct.add(dx[27])
        if a in ppe3:
            pct.add(dx[28])
        if a in ppe2:
            pct.add(dx[29])
        if tipo_p[18] in pool:
            pct.add(dx[10])
            pct.discard(dx[184])
            warn.add(
                'Recomendável Tonificar Ming Mei - Deficiência de Yuan Qi Grave'.upper())
# RU

        def rufx(a, b, c, d):
            if b in det_20:
                pool.add(tipo_p[20])
                if d < 2:
                    return pct.add(dx[a+84])
                if c < 2:
                    return pct.add(dx[a])
        rufx(33, 'P', d1c, d1a)
        rufx(31, 'BP', d2c, d2a)
        rufx(32, 'PC', d3c, d3a)
        rufx(30, 'C', e1c, e1a)
        rufx(35, 'F', e2c, e2a)
        rufx(34, 'R', e3c, e3a)

# SAN

        def sanf(a, b):
            if b in det_22:
                return pct.add(dx[int(a)])
                return pct.add(dx[int(a)+18])
                return pct.add(dx[22])
                return pct.add(dx[int(a)+144])
        sanf(3, 'P')
        sanf(1, 'BP')
        sanf(2, 'PC')
        sanf(0, 'C')
        sanf(5, 'F')
        sanf(4, 'R')

# FUA

        def fuaf(a, b):
            if b in det_23:
                pct.add(dx[int(a)])
                pct.discard(dx[int(a)+156])
        fuaf(15, 'P')
        fuaf(13, 'BP')
        fuaf(14, 'PC')
        fuaf(12, 'C')
        fuaf(17, 'F')
        fuaf(16, 'R')

# DONG
        if tipo_p[24] in pool:
            warn.add(
                'Choque emocional grave prévio (tratar algum shen?) ou dor extrema no momento'.upper())

# JIE
        if tipo_p[26] in pool:
            pct.add(dx[12])
            pct.discard(dx[168])
            pct.discard(dx[102])

# CU
        def cufx(a, b):
            if b in det_25:
                if dx[int(a)] in pct:
                    return pct.discard(dx[int(a)+12])
                    return pct.discard(dx[int(a)+18])
                if dx[int(a)+12] in pct or dx[int(a)+18] in pct:
                    return pct.add(dx[18])
                else:
                    return pct.add(dx[int(a)])
        cufx(171, 'P')
        cufx(169, 'BP')
        cufx(170, 'PC')
        cufx(168, 'C')
        cufx(173, 'F')
        cufx(172, 'R')

# DAI
        if tipo_p[27] in pool:
            warn.add(
                'Pulso Dai indica colapso de xue e qi em 2 órgãos Yin (Zhong)'.upper())
        print()

#  ALGORÍTMO DIAGNÓSTICO (A.I.) PARA CRUZAMENTO DE TENSORES - PARTE 1

        w = 'Localizado padrão de dor de frio em vazio. Caso paciente apresente dor difusa e sensível a frio, localizar meridiano próximo e usar moxa em local'
        if tipo_p[1] in pool:
            lista1 = [6, 7, 8, 9, 10, 11, 132, 133, 134, 135, 136, 137]
            map(lambda x: tensor.add(dx[x]), lista1)
        if tipo_p[2] in pool:
            if tipo_p[21] in pool:
                lista2a = [18, 19, 20, 21, 22, 23, 12, 13, 14, 15, 16, 17]
                map(lambda x: tensor.add(dx[x]), lista2a)
            if tipo_p[6] in pool:
                lista2b = [60, 61, 62, 63, 64, 65]
                map(lambda x: tensor.add(dx[x]), lista2b)
        if tipo_p[3] in pool:
            if tipo_p[21] in pool:
                lista3a = [186, 187, 188, 190, 191]
                map(lambda x: tensor.add(dx[x]), lista3a)
            if tipo_p[6] in pool:
                lista3b = [180, 181, 182, 183, 184, 185]
                map(lambda x: tensor.add(dx[x]), lista3b)
        if tipo_p[4] in pool:
            if tipo_p[1] in pool:
                lista4a = [174, 175, 176, 177, 178, 179]
                map(lambda x: tensor.add(dx[x]), lista4a)
            if tipo_p[6] in pool:
                lista4b = [168, 169, 170, 171, 172, 173]
                map(lambda x: tensor.add(dx[x]), lista4b)
        if tipo_p[5] in pool:
            lista5 = [18, 19, 20, 21, 22, 23]
            map(lambda x: tensor.add(dx[x]), lista5)
        if tipo_p[7] in pool:
            lista7 = [208, 209, 210, 211, 212,
                      213, 114, 155, 116, 117, 118, 119]
            map(lambda x: tensor.add(dx[x]), lista7)
        if tipo_p[8] in pool:
            lista8 = [120, 121, 122, 123, 124, 125, 36, 37, 38, 39, 40, 41]
            map(lambda x: tensor.add(dx[x]), lista8)
        if tipo_p[9] in pool:
            lista9 = [102, 103, 104, 105, 106, 107]
            map(lambda x: tensor.add(dx[x]), lista9)
        if tipo_p[10] in pool:
            lista10 = [18, 19, 20, 21, 22, 23]
            map(lambda x: tensor.add(dx[x]), lista10)
            dxconf.add(dx[19])
        if tipo_p[11] in pool:
            if tipo_p[6] in pool:
                lista11a = [168, 169, 170, 171, 172, 173]
                map(lambda x: tensor.add(dx[x]), lista11a)
                if tipo_p[25] in pool or tipo_p[4] in pool:
                    lista11d = [214, 215, 216, 217, 218, 219]
                    map(lambda x: tensor.add(dx[x]), lista11d)
            if tipo_p[5] in pool:
                lista11b = [174, 175, 176, 177, 178, 179]
                map(lambda x: tensor.add(dx[x]), lista11b)
            if tipo_p[4] in pool:
                lista11c = [208, 209, 210, 211, 212, 213]
                map(lambda x: tensor.add(dx[x]), lista11c)
        if tipo_p[12] in pool:
            lista12 = [18, 19, 20, 21, 22, 23, 0, 1, 2,
                       3, 4, 5, 114, 155, 116, 117, 118, 119]
            map(lambda x: tensor.add(dx[x]), lista12)
        if tipo_p[13] in pool:
            lista13 = [60, 61, 62, 63, 64, 65]
            map(lambda x: tensor.add(dx[x]), lista13)
        if tipo_p[14] in pool:
            if tipo_p[6] in pool and tipo_p[2] in pool:
                lista14a = [180, 181, 182, 183, 184, 185]
                map(lambda x: tensor.add(dx[x]), lista14a)
            if tipo_p[6] in pool and tipo_p[1] in pool:
                lista14b = [96, 97, 98, 99, 100, 101]
                map(lambda x: tensor.add(dx[x]), lista14b)
            if tipo_p[2] in pool and tipo_p[1] in pool:
                lista14c = [186, 187, 188, 189, 190, 191]
                map(lambda x: tensor.add(dx[x]), lista14c)
                print()
                warn.add(w.upper())
                print()
        if tipo_p[15] in pool:
            if tipo_p[6] in pool or tipo_p[26] in pool:
                dxconf.add(dx[54])
            else:
                dxconf.add(dx[59])
                print()
                warn.add(w.upper())
        if tipo_p[18] in pool:
            dxconf.add(dx[28])
            tensor.add(dx[190])
        if tipo_p[19] in pool:
            if tipo_p[9] in pool:
                lista19a = [54, 55, 56, 57, 58, 59]
                map(lambda x: tensor.add(dx[x]), lista19a)
            if tipo_p[3] in pool:
                lista19b = [90, 91, 92, 93, 94, 95]
                map(lambda x: tensor.add(dx[x]), lista19b)
                print()
                warn.add(w.upper())
        if tipo_p[20] in pool:
            lista20 = [18, 19, 20, 21, 22, 23, 6, 7, 8, 9, 10, 11]
            map(lambda x: tensor.add(dx[x]), lista20)
        if tipo_p[21] in pool:
            lista21 = [12, 13, 14, 15, 16, 17, 1, 2, 3, 4, 5]
            map(lambda x: tensor.add(dx[x]), lista21)
        if tipo_p[22] in pool:
            lista22 = [18, 19, 20, 21, 22, 23, 1, 2, 3, 4, 5]
            map(lambda x: tensor.add(dx[x]), lista22)
            dxconf.add(dx[22])
        if tipo_p[23] in pool:
            lista23 = [12, 13, 14, 15, 16, 17]
            map(lambda x: tensor.add(dx[x]), lista23)
        if tipo_p[25] in pool:
            lista25 = [108, 109, 110, 111, 112, 113]
            map(lambda x: tensor.add(dx[x]), lista25)
            pct.add(dx[18])
        if tipo_p[26] in pool:
            tensor.add(dx[196])
            dxconf.add(dx[196])
        if tipo_p[27] in pool:
            lista = [186, 187, 188, 190, 191]
            map(lambda x: tensor.add(dx[x]), lista)
        if tipo_p[28] in pool:
            lista28 = [168, 169, 170, 171, 172,
                       173, 186, 187, 188, 189, 190, 191]
            map(lambda x: tensor.add(dx[x]), lista28)


# -------------------------------------- LÍNGUA - PARTE 2

        cls()
        print()
        print('ANÁLISE DE LÍNGUA\n')
        print('• FORMA')
        print('(A) Longa, (B) Curta, (C) Fina, (D) Grossa')
        print('Língua normal não deve ser inserida')
        print('• MOVIMENTO')
        print('(E) Duro, (F) Flácido, (G) Trêmulo, (H) Desviado')
        print('• RACHADURA')
        print(
            '(I) Linha média, (J) Periférico, (K) Afta, (L) Marca de dente, (M) Petéquias')
        print('• SABURRA')
        print('SE EXCESSO -- (N) Saburra Branca, (O) Saburra Amarela/Laranja, (P) Saburra Cinza')
        print('SE FALTA -- (Q) Hemilíngua, (R) Central, (S) Parcial, (T) Ausência Total de saburra')
        print('O normal é ter saburra fina, homogênea e levemente branca, nesse caso, não inserir')
        print('• COR DA LÍNGUA')
        print('(U) Vermelha, (V) Azul-branco, (W) Roxo-escuro, (X) Branca\n A cor normal é rosa e não deve ser adicionada\nNão confunda com a cor de saburra (cama acima de língua)')
        print('• UMIDADE')
        print('(Y) Sialorréia, (Z) Pegajosa, (Ç) Xerostomia')
        print()
        while True:
            try:
                lin = input('Insira parâmetros alterados: ').upper()
                if len(lin) > 1 and lin.isalpha() == True:
                    break
                else:
                    print('Insira conforme orientado!')
                    continue
            except:
                continue
        global pureli
        pureli=set()
        def f(x,y): return pureli.add(y.upper()) if x.upper() in lin else None
        if 'M' in lin:
            while True:
                try:
                    cls()
                    print('\n\n\n\nFoi selecionado locais com petéquias em língua. Qual é a localização da(s) lesão(lesões)?\n\n')
                    print('LOCALIZAÇÃO ANATÔMICA\n1- Próxima a Glote, 2- 1/3 proximal de língua, 3- Centro de língua, 4- Laterais de língua, 5- 1/3 anterior, 6- Ponta de língua, 7- Curvatura anterior da língua')
                    querym = input(int(
                        'Adicione o local de petéquias:\n\n1-R/B\n2-IG/ID\n3-BP/E\n4-F/VB\n5-P\n6-C\n7-Mama\n '))
                    if len(querym) == 1 and querym.isnumeric() == True and querym != 0 and querym != 8 and querym != 9:
                        if querym == 1:
                            f('m','petéquias em zona de R-B')
                        if querym==2:
                            f('m', 'petéquias em zona de IG-ID')
                        if querym==3:
                            f('m','petéquias em zona de BP-E')
                        if querym==4:
                            f('m','petéquias em zona de F-VB')
                        if querym==5:
                            f('m','petéquias em zona de P')
                        if querym==6:
                            f('m','petéquias em zona de C')
                        if querym==7:
                            f('m','petéquias em zona de mamas')
                        break
                    else:
                        print('Insira conforme orientado!')
                        continue
                except:
                    continue
        print()
        f('a','longa')
        f('b','curta')
        f('c','fina')
        f('d','grossa')
        f('e','dura')
        f('f','flácida')
        f('g','trêmula')
        f('h','desviada')
        f('i','rachadura em linha médica')
        f('j','rachadura periférica')
        f('k','ulcerada')
        f('l','marcas dentais')
        f('n','saburra branca')
        f('o','saburra amarelo-laranja')
        f('p','saburra cinza')
        f('q','falha de preenchimento na hemilíngua de saburra')
        f('r','falha de preenchimento central de saburra')
        f('s','falha de preenchimento parcial de saburra')
        f('t','falha de preenchimento total de saburra')
        f('u','língua vermelha')
        f('v','língua azul-branca')
        f('w','língua roxa-escura')
        f('x','língua branca')
        f('y','sialorréia')
        f('z','saliva pegajosa')
        f('ç','xerostomia')
        #map(lambda x: tensor.add(dx[x]), lista2a)
            
        # -------------------------------------- PROTOCOLO WU FU PARA VENTO-FRIO - MULTIMODAL
        def e(a, b): return smt.add(a+' de '+str(b))
        a = 0
        if a == 0 and tipo_p[2] in pool and tipo_p[3] in pool and tipo_p[21] in pool:
            if 'P' in det_2 and 'P' in det_3 and 'P' in det_21:
                if 'N' in lin or 'Z' in lin:
                    dxconf.add(dx[205]+' em meridiano de Pulmão')
                    x = 'DISTENSÃO ABDOMINAL, FRIO, ANOREXIA E VÔMITOS, DIARRÉIA, NÃO SENTE VONTADE DE BEBER ÁGUA, FADIGA'
                    y = dx[205]
                    e(x, y)
                    a = 1
                elif 'V' in lin or 'X' in lin or 'N' in lin:
                    dxconf.add(dx[206]+' em meridiano de Pulmão')
                    x = 'CALAFRIOS, VONTADE DE DEITAR FETALMENTE, APATIA, SONO/CANSAÇO CRÔNICO, FRIO EM EXTREMIDADES, DIARRÉIA, POUCA SEDE, POLIÚRIA CLARA'
                    y = dx[206]
                    e(x, y)
                    a = 1
            if 'BP' in det_2 and 'BP' in det_3 and 'BP' in det_21:
                if 'N' in lin or 'Z' in lin:
                    dxconf.add(dx[205]+' em meridiano de Baço')
                    x = 'DISTENSÃO ABDOMINAL, FRIO, ANOREXIA E VÔMITOS, DIARRÉIA, NÃO SENTE VONTADE DE BEBER ÁGUA, FADIGA'
                    y = dx[205]
                    e(x, y)
                    a = 1
                elif 'V' in lin or 'X' in lin or 'N' in lin:
                    dxconf.add(dx[206]+' em meridiano de Baço')
                    x = 'CALAFRIOS, VONTADE DE DEITAR FETALMENTE, APATIA, SONO/CANSAÇO CRÔNICO, FRIO EM EXTREMIDADES, DIARRÉIA, POUCA SEDE, POLIÚRIA CLARA'
                    y = dx[206]
                    e(x, y)
                    a = 1
            if 'PC' in det_2 and 'PC' in det_3 and 'PC' in det_21:
                if 'N' in lin or 'Z' in lin:
                    dxconf.add(
                        dx[205]+' em meridiano de Pericárdio e Triplo Aquecedor')
                    x = 'DISTENSÃO ABDOMINAL, FRIO, ANOREXIA E VÔMITOS, DIARRÉIA, NÃO SENTE VONTADE DE BEBER ÁGUA, FADIGA'
                    y = dx[205]
                    e(x, y)
                    a = 1
                elif 'V' in lin or 'X' in lin or 'N' in lin:
                    dxconf.add(
                        dx[206]+' em meridiano de Pericárdio e Triplo Aquecedor')
                    x = 'CALAFRIOS, VONTADE DE DEITAR FETALMENTE, APATIA, SONO/CANSAÇO CRÔNICO, FRIO EM EXTREMIDADES, DIARRÉIA, POUCA SEDE, POLIÚRIA CLARA'
                    y = dx[206]
                    e(x, y)
                    a = 1
            if 'C' in det_2 and 'C' in det_3 and 'C' in det_21:
                if 'N' in lin or 'Z' in lin:
                    dxconf.add(dx[205]+' em meridiano de Coração')
                    x = 'DISTENSÃO ABDOMINAL, FRIO, ANOREXIA E VÔMITOS, DIARRÉIA, NÃO SENTE VONTADE DE BEBER ÁGUA, FADIGA'
                    y = dx[205]
                    e(x, y)
                    a = 1
                elif 'V' in lin or 'X' in lin or 'N' in lin:
                    dxconf.add(dx[206]+' em meridiano de Coração')
                    x = 'CALAFRIOS, VONTADE DE DEITAR FETALMENTE, APATIA, SONO/CANSAÇO CRÔNICO, FRIO EM EXTREMIDADES, DIARRÉIA, POUCA SEDE, POLIÚRIA CLARA'
                    y = dx[206]
                    e(x, y)
                    a = 1
            if 'F' in det_2 and 'F' in det_3 and 'F' in det_21:
                if 'N' in lin or 'Z' in lin:
                    dxconf.add(dx[205]+' em meridiano de Fígado')
                    x = 'DISTENSÃO ABDOMINAL, FRIO, ANOREXIA E VÔMITOS, DIARRÉIA, NÃO SENTE VONTADE DE BEBER ÁGUA, FADIGA'
                    y = dx[205]
                    e(x, y)
                    a = 1
                elif 'V' in lin or 'X' in lin or 'N' in lin:
                    dxconf.add(dx[206]+' em meridiano de Fígado')
                    x = 'CALAFRIOS, VONTADE DE DEITAR FETALMENTE, APATIA, SONO/CANSAÇO CRÔNICO, FRIO EM EXTREMIDADES, DIARRÉIA, POUCA SEDE, POLIÚRIA CLARA'
                    y = dx[206]
                    e(x, y)
                    a = 1
            if 'R' in det_2 and 'R' in det_3 and 'R' in det_21:
                if 'N' in lin or 'Z' in lin:
                    dxconf.add(dx[205]+' em meridiano de Rim')
                    x = 'DISTENSÃO ABDOMINAL, FRIO, ANOREXIA E VÔMITOS, DIARRÉIA, NÃO SENTE VONTADE DE BEBER ÁGUA, FADIGA'
                    y = dx[205]
                    e(x, y)
                    a = 1
                elif 'V' in lin or 'X' in lin or 'N' in lin:
                    dxconf.add(dx[206]+' em meridiano de Rim')
                    x = 'CALAFRIOS, VONTADE DE DEITAR FETALMENTE, APATIA, SONO/CANSAÇO CRÔNICO, FRIO EM EXTREMIDADES, DIARRÉIA, POUCA SEDE, POLIÚRIA CLARA'
                    y = dx[206]
                    e(x, y)
                    a = 1
            if 'C' in h3 or 'D' in h3 or 'E' in h3 or 'F' in h3 or 'G' in h3 or 'H' in h3 or 'I' in h3:
                if 'P' in det_15:
                    dxconf.add(dx[207]+' em meridiano de Pulmão')
                    x = 'SEDE PERSISTENTE, SENSAÇÃO DE ALGO ANDANDO NO PEITO, DOR EM TÓRAX, FOME COM PERDA DE PESO, EXTREMIDADES FRIAS, DIARRÉIA E VÔMITOS'
                    y = dx[207]
                    e(x, y)
                    a = 1
                if 'BP' in det_15:
                    dxconf.add(dx[207]+' em meridiano de Baço')
                    x = 'SEDE PERSISTENTE, SENSAÇÃO DE ALGO ANDANDO NO PEITO, DOR EM TÓRAX, FOME COM PERDA DE PESO, EXTREMIDADES FRIAS, DIARRÉIA E VÔMITOS'
                    y = dx[207]
                    e(x, y)
                    a = 1
                if 'PC' in det_15:
                    dxconf.add(
                        dx[207]+' em meridiano de Pericárdio e Triplo Aquecedor')
                    x = 'SEDE PERSISTENTE, SENSAÇÃO DE ALGO ANDANDO NO PEITO, DOR EM TÓRAX, FOME COM PERDA DE PESO, EXTREMIDADES FRIAS, DIARRÉIA E VÔMITOS'
                    y = dx[207]
                    e(x, y)
                    a = 1
                if 'C' in det_15:
                    dxconf.add(dx[207]+' em meridiano de Coração')
                    x = 'SEDE PERSISTENTE, SENSAÇÃO DE ALGO ANDANDO NO PEITO, DOR EM TÓRAX, FOME COM PERDA DE PESO, EXTREMIDADES FRIAS, DIARRÉIA E VÔMITOS'
                    y = dx[207]
                    e(x, y)
                    a = 1
                if 'F' in det_15:
                    dxconf.add(dx[207]+' em meridiano de Fígado')
                    x = 'SEDE PERSISTENTE, SENSAÇÃO DE ALGO ANDANDO NO PEITO, DOR EM TÓRAX, FOME COM PERDA DE PESO, EXTREMIDADES FRIAS, DIARRÉIA E VÔMITOS'
                    y = dx[207]
                    e(x, y)
                    a = 1
                if 'R' in det_15:
                    dxconf.add(dx[207]+' em meridiano de Rim')
                    x = 'SEDE PERSISTENTE, SENSAÇÃO DE ALGO ANDANDO NO PEITO, DOR EM TÓRAX, FOME COM PERDA DE PESO, EXTREMIDADES FRIAS, DIARRÉIA E VÔMITOS'
                    y = dx[207]
                    e(x, y)
                    a = 1
        if a == 0 and dorquery == 'S':
            if 'P' in det_1:
                dxconf.add(dx[202]+' em meridiano de Pulmão')
                x = 'AVERSÃO A FRIO, CEFALÉIA, RIGIDEZ CERVICAL, OLIGÚRIA'
                y = dx[202]
                e(x, y)
                a = 1
            if 'BP' in det_1:
                dxconf.add(dx[202]+' em meridiano de Baço')
                x = 'AVERSÃO A FRIO, CEFALÉIA, RIGIDEZ CERVICAL, OLIGÚRIA'
                y = dx[202]
                e(x, y)
                a = 1
            if 'PC' in det_1:
                dxconf.add(
                    dx[202]+' em meridiano de Pericárdio e Triplo Aquecedor')
                x = 'AVERSÃO A FRIO, CEFALÉIA, RIGIDEZ CERVICAL, OLIGÚRIA'
                y = dx[202]
                e(x, y)
                a = 1
            if 'C' in det_1:
                dxconf.add(dx[202]+' em meridiano de Coração')
                x = 'AVERSÃO A FRIO, CEFALÉIA, RIGIDEZ CERVICAL, OLIGÚRIA'
                y = dx[202]
                e(x, y)
                a = 1
            if 'F' in det_1:
                dxconf.add(dx[202]+' em meridiano de Fígado')
                x = 'AVERSÃO A FRIO, CEFALÉIA, RIGIDEZ CERVICAL, OLIGÚRIA'
                y = dx[202]
                e(x, y)
                a = 1
            if 'R' in det_1:
                dxconf.add(dx[202]+' em meridiano de Rim')
                x = 'AVERSÃO A FRIO, CEFALÉIA, RIGIDEZ CERVICAL, OLIGÚRIA'
                y = dx[202]
                e(x, y)
                a = 1
        if a == 0 and tipo_p[4] in pool and tipo_p[11] in pool:
            if 'P' in det_4 and 'P' in det_11:
                dxconf.add(dx[203]+' em meridiano de Pulmão')
                x = 'TRANSPIRAÇÃO PROFUSA PELA TARDE, URINA ESCURA, SEDE, IRRITABILIDADE'
                y = dx[203]
                e(x, y)
                a = 1
            if 'BP' in det_4 and 'BP' in det_11:
                dxconf.add(dx[203]+' em meridiano de Baço')
                x = 'TRANSPIRAÇÃO PROFUSA PELA TARDE, URINA ESCURA, SEDE, IRRITABILIDADE'
                y = dx[203]
                e(x, y)
                a = 1
            if 'PC' in det_4 and 'PC' in det_11:
                dxconf.add(
                    dx[203]+' em meridiano de Pericárdio e Triplo Aquecedor')
                x = 'TRANSPIRAÇÃO PROFUSA PELA TARDE, URINA ESCURA, SEDE, IRRITABILIDADE'
                y = dx[203]
                e(x, y)
                a = 1
            if 'C' in det_4 and 'C' in det_11:
                dxconf.add(dx[203]+' em meridiano de Coração')
                x = 'TRANSPIRAÇÃO PROFUSA PELA TARDE, URINA ESCURA, SEDE, IRRITABILIDADE'
                y = dx[203]
                e(x, y)
                a = 1
            if 'F' in det_4 and 'F' in det_11:
                dxconf.add(dx[203]+' em meridiano de Fígado')
                x = 'TRANSPIRAÇÃO PROFUSA PELA TARDE, URINA ESCURA, SEDE, IRRITABILIDADE'
                y = dx[203]
                e(x, y)
                a = 1
            if 'R' in det_4 and 'R' in det_11:
                dxconf.add(dx[203]+' em meridiano de Rim')
                x = 'TRANSPIRAÇÃO PROFUSA PELA TARDE, URINA ESCURA, SEDE, IRRITABILIDADE'
                y = dx[203]
                e(x, y)
                a = 1
        if a == 0 and tipo_p[15] in pool and tipo_p[12] in pool:
            if 'P' in det_15 and 'P' in det_12:
                dxconf.add(dx[204]+' em meridiano de Pulmão')
                x = 'CALAFRIOS ALTERNADOS COM CALOR, GOSTO AMARGO, GARGANTA SECA, TURVOR VISUAL, ANOREXIA E NÁUSEAS'
                y = dx[204]
                e(x, y)
                a = 1
            if 'BP' in det_15 and 'BP' in det_12:
                dxconf.add(dx[204]+' em meridiano de Baço')
                x = 'CALAFRIOS ALTERNADOS COM CALOR, GOSTO AMARGO, GARGANTA SECA, TURVOR VISUAL, ANOREXIA E NÁUSEAS'
                y = dx[204]
                e(x, y)
                a = 1
            if 'PC' in det_15 and 'PC' in det_12:
                dxconf.add(
                    dx[204]+' em meridiano de Pericárdio e Triplo Aquecedor')
                x = 'CALAFRIOS ALTERNADOS COM CALOR, GOSTO AMARGO, GARGANTA SECA, TURVOR VISUAL, ANOREXIA E NÁUSEAS'
                y = dx[204]
                e(x, y)
                a = 1
            if 'C' in det_15 and 'C' in det_12:
                dxconf.add(dx[204]+' em meridiano de Coração')
                x = 'CALAFRIOS ALTERNADOS COM CALOR, GOSTO AMARGO, GARGANTA SECA, TURVOR VISUAL, ANOREXIA E NÁUSEAS'
                y = dx[204]
                e(x, y)
                a = 1
            if 'F' in det_15 and 'F' in det_12:
                dxconf.add(dx[204]+' em meridiano de Fígado')
                x = 'CALAFRIOS ALTERNADOS COM CALOR, GOSTO AMARGO, GARGANTA SECA, TURVOR VISUAL, ANOREXIA E NÁUSEAS'
                y = dx[204]
                e(x, y)
                a = 1
            if 'R' in det_15 and 'R' in det_12:
                dxconf.add(dx[204]+' em meridiano de Rim')
                x = 'CALAFRIOS ALTERNADOS COM CALOR, GOSTO AMARGO, GARGANTA SECA, TURVOR VISUAL, ANOREXIA E NÁUSEAS'
                y = dx[204]
                e(x, y)
                a = 1
        if len(det_1)!=0 or len(det_3)!=0:
            if len(lin)<=3:
                dxconf.add(dx[202]+' do tipo Vento')
                x = 'Assemelha cansaço, aumento wei (sensação de calor com incômodo de frio constante), aversão a frio, sudorese, cefaléia, tensão muscular ombros/pescoço'.upper()
                y = dx[202]+' do tipo Vento'
                e(x, y)
        if len(det_1)!=0 or len(det_14)!=0:
            if len(lin)<=3:
                dxconf.add(dx[202]+' do tipo Frio')
                x = 'aversão a frio, febre rápida, sem suar, cefaléia, rinite clara, obstrução de wei (sem suor), dor lombar, polimialgia'.upper()
                y = dx[202]+' do tipo Frio'
                e(x, y)        
        if len(det_11)!=0 or len(det_4)!=0 or len(det_15)!=0:
            if 'W' in lin or 'U' in lin or 'Ç' in lin or 'T' in lin or 'O' in lin:
                dxconf.add(dx[203])
                x = 'Aversão a frio, febre, oligúria, sede, tendência a vômitos, tremores, sintomas renais de insuficiência'.upper()
                y = dx[203]
                e(x, y) 
        if len(det_12)!=0 or len(det_15)!=0:
            if 'N' in lin or 'O' in lin:
                dxconf.add(dx[204])
                x = 'disconforto em tórax, calafrios, surdez, hiperemia ocular, vertigem, refluxo, ansiedade, borramento visual'.upper()
                y = dx[204]
                e(x, y)    
        if len(det_21)!=0 or rfc==1:
            if 'Z' in lin or 'N' in lin:
                dxconf.add(dx[205])
                x = 'parece pouco disposto (sem energia), diarréia aquosa recorrente, vômitos e tendências a vomitar, anorexia, adipsia'.upper()
                y = dx[205]
                e(x, y)          
        if len(det_12)!=0 or rfc==3:
            if 'W' in lin or 'U' in lin or 'T' in lin:
                dxconf.add(dx[206]+' do tipo Calor')
                x = 'febre, irritabilidade, insônia, boca ou garganta seca, urina escura'.upper()
                y = dx[206]+' do tipo Calor'
                e(x, y) 
        if len(det_2)!=0 or len(det_21)!=0:
            if 'W' not in lin and 'U' not in lin:
                dxconf.add(dx[206]+' do tipo Frio')
                x = 'poliúria clara (urina diluída), frio em extremidades, aversão a frio, artralgia, diarréia'.upper()
                y = dx[206]+' do tipo Frio'
                e(x, y)    
        if len(det_2)!=0 or len(det_15)!=0:
            if 'Z' in lin or 'N' in lin or 'Z' in lin:
                dxconf.add(dx[207])
                x = 'sede, dor em estômago (separação de Tao em abdome), fome com anorexia (quer comer e come, quando come, sente incômodo e pára (saciedade/dor/medo), frio em extremidades, diarréia com restos alimentares recorrentemente, dor ao evacuar (eventual)'.upper()
                y = dx[207]
                e(x, y)          

        # -------------------------------------- ANÁLISE DE VENTO-CALOR

        def e(a, b): return smt.add(a+' de '+str(b))
        a = 0

        if d3c == 3 and a == 0:
            if 'W' or 'T' in lin:
                q1 = input(
                    'Melena, hematoquezia, hematêmese ou epistaxe recente? (S/N) ').upper()
                if q1 == 'S':
                    x = 'CALOR EM CORPO, MANIA, MÁCULA ESCURA PELO CORPO, HEMATÊMESE, EPISTAXE, HEMATOQUEZIA, HEMATÚRIA'
                    y = dx[240]
                    e(x, y)
                    dxconf.add(dx[201]+' '+dx[240])
            q2 = input(
                'Pré-síncope, desmaio, convulsão já ocorrida? (S/N) ').upper()
            if q2 == 'S':
                dxconf.add(dx[201]+' '+dx[241])
                x = 'LESÃO DE ÓRGÃO, DESIDRATAÇÃO, CONFUSÃO MENTAL, PERDA DE YIN, MÁCULA COM SANGRAMENTOS'
                y = dx[201]
                e(x, y)
                x = 'CALOR EM CORPO, DESMAIO, TREMORES, CONVULSÃO, RIGIDEZ CERVICAL, OPISTÓTONO, TRISMO/BRUXISMO'
                y = dx[241]
                e(x, y)
            q3 = input('Emagrecimento fácil? (S/N) ').upper()
            if q3 == 'S':
                dxconf.add(dx[201]+' '+dx[242])
                x = 'LESÃO DE ÓRGÃO, DESIDRATAÇÃO, CONFUSÃO MENTAL, PERDA DE YIN, MÁCULA COM SANGRAMENTOS'
                y = dx[201]
                e(x, y)
                x = 'TIQUES, TREMOR, EMAGRECIMENTO INVOLUNTÁRIO, RUBOR DE FACE, AGITAÇÃO MENTAL'
                y = dx[242]
                e(x, y)
            q4 = input('Ausência de sede mesmo se lábio seco? (S/N) ').upper()
            if q4 == 'S':
                dxconf.add(dx[201]+' '+dx[243])
                x = 'LESÃO DE ÓRGÃO, DESIDRATAÇÃO, CONFUSÃO MENTAL, PERDA DE YIN, MÁCULA COM SANGRAMENTOS'
                y = dx[201]
                e(x, y)
                x = 'SUOR NOTURNO, INQUIETUDE, BOCA SECA, PERDA DE SEDE, RUBOR MALAR, CALOR EM BRAÇOS E PERNAS'
                y = dx[243]
                e(x, y)
            if 'B' and 'X' in lin:
                dxconf.add(dx[201]+' '+dx[244])
                x = 'LESÃO DE ÓRGÃO, DESIDRATAÇÃO, CONFUSÃO MENTAL, PERDA DE YIN, MÁCULA COM SANGRAMENTOS'
                y = dx[201]
                e(x, y)
                x = 'FRIO, MÃOS E PÉS GELADOS, PERDA DE COR DE PELE DEIXANDO-A BRANCA, TRANSPIRAÇÃO EM TESTA, AGITAÇÃO'
                y = dx[244]
                e(x, y)

        if a == 0 and d1a == 3 and a == 0:
            if 'U' and 'N' in lin:
                quente1 = input(
                    'Dificuldade de suar mesmo no calor? (S/N) ').upper()
                while True:
                    try:
                        if quente1 == 'S':
                            dxconf.add(dx[198]+' '+dx[230])
                            x = 'CEFALÉIA, AUSÊNCIA DE TRANSPIRAÇÃO, PESO EM CORPO, EPIGASTRALGIA, SEDE E IRRITABILIDADE'
                            y = dx[230]
                            e(x, y)
                            x = 'CALOR, AVERSÃO A FRIO, CEFALÉIA (VENTO EXTERNO), ODINOFAGIA, CORIZA, SUDORESE, MIALGIA'
                            y = dx[198]
                            e(x, y)
                            a = 1
                            break
                        elif quente1 == 'N':
                            dxconf.add(dx[198]+' '+dx[229])
                            x = 'SENSAÇÃO DE CALOR, AVERSÃO A FRIO, CEFALÉIA, ODINOFAGIA, TRANSPIRAÇÃO ESPONTÂNEA, CORIZA AMARELA, MIALGIA'
                            y = dx[229]
                            e(x, y)
                            x = 'CALOR, AVERSÃO A FRIO, CEFALÉIA (VENTO EXTERNO), ODINOFAGIA, CORIZA, SUDORESE, MIALGIA'
                            y = dx[198]
                            e(x, y)
                            a = 1
                            break
                    except:
                        continue
            if 'Ç' and 'N' in lin and a == 0:
                dxconf.add(dx[198]+' '+dx[232])
                x = 'GARGANTA E BOCA SECA, TRANSPIRAÇÃO ESPONTÂNEA, TOSSE SECA, ODINOFAGIA'
                y = dx[232]
                e(x, y)
                a = 1
            if 'U' and 'O' in lin and a == 0:
                if 'Z' in lin:
                    dxconf.add(dx[198]+' '+dx[231])
                    x = 'CALOR, AVERSÃO A FRIO, CEFALÉIA (VENTO EXTERNO), ODINOFAGIA, CORIZA, SUDORESE, MIALGIA'
                    y = dx[198]
                    e(x, y)
                    x = 'CALOR AO FINAL DA TARDE, CORPO QUENTE AO TOQUE, AVERSÃO A FRIO, ADENOPATIA, OPRESSÃO EPIGÁSTRICA E GOSTO PEGAJOSO'
                    y = dx[231]
                    e(x, y)
                    a = 1
                elif d1b == 3 or d2c == 3:
                    quente2 = input(
                        'Calor noite-tarde-dia (A) ou calor mais no final da Tarde somente (B): ').upper()
                    while True:
                        try:
                            if quente2 == 'A':
                                dxconf.add(dx[199]+' '+dx[233])
                                x = 'CALOR CONTÍNUO, NÃO SENTE FRIO, SEDE AUMENTADA, TOSSE COM ESCARRO AMARELO, DISPNÉIA, SUDORESE'
                                y = dx[233]
                                e(x, y)
                                x = 'SEDE, NÁUSEA, NÃO SENTE FRIO NUNCA'
                                y = dx[199]
                                e(x, y)
                                a = 1
                                break
                            elif quente2 == 'B':
                                dxconf.add(dx[199]+' '+dx[234])
                                x = 'CALOR AO FINAL DA TARDE, AUSÊNCIA DE FRIO, CALOR CONTINUAMENTE EM CORPO, SEDE INTENSA'
                                y = dx[234]
                                e(x, y)
                                x = 'SEDE, NÁUSEA, NÃO SENTE FRIO NUNCA'
                                y = dx[199]
                                e(x, y)
                                a = 1
                                break
                        except:
                            continue
        if d1b == 3 or d2c == 3 and a == 0:
            if 'Ç' and 'O' in lin:
                dxconf.add(dx[199]+' '+dx[235])
                x = 'SEDE, NÁUSEA, NÃO SENTE FRIO NUNCA'
                y = dx[199]
                e(x, y)
                x = 'CALOR AO FINAL DA TARDE, CONSTIPAÇÃO, ARDOR ANAL, DOR ABDOMINAL, DISTENSÃO DE ABDOME (ESTÔMAGO) E NÁUSEAS'
                y = dx[235]
                e(x, y)
                a = 1
            if 'U' and 'Z' in lin or 'U' and 'Q' in lin and a == 0:
                dxconf.add(dx[199]+' '+dx[236])
                x = 'SEDE, NÁUSEA, NÃO SENTE FRIO NUNCA'
                y = dx[199]
                e(x, y)
                x = 'CALAFRIOS, GOSTO AMARGO, SEDE, GARGANTA SECA, DOR EM HIUPOCÔNDRIO, NÁUSEAS E PLENITUDE EPIGÁSTRICA'
                y = dx[236]
                e(x, y)
                a = 1
            if 'U' not in lin and 'O' not in lin and 'N' not in lin and a == 0:
                if 'Z' in lin:
                    dxconf.add(dx[199]+' '+dx[237])
                    x = 'CALOR QUE MELHORA SUANDO, PESO EM CORPO, PESO EM CABEÇA, OPRESSÃO EM TÓRAX, NÁUSEAS E DIARRÉIAS'
                    y = dx[237]
                    e(x, y)
                    x = 'SEDE, NÁUSEA, NÃO SENTE FRIO NUNCA'
                    y = dx[199]
                    e(x, y)
                    a = 1
        if d1c == 3 and a == 0:
            if 'W' and 'T' in lin:
                if termoquery == 'N':
                    dxconf.add(dx[200]+' '+dx[238])
                    x = 'APARECIMENTO DE LESÕES EM PELE (VESÍCULAS, EXANTEMA OU MÁCULAS ESCURAS/ HEMORRAGIA)'
                    y = dx[200]
                    e(x, y)
                    x = 'CALOR EXTREMO PELA NOITE, BOCA SECA, PERDA DE VONTADE DE BEBER ÁGUA, INQUIETUDE MENTAL, INSÔNIA, CORPO QUENTE AO DEITAR COM MÃOS E PÉS FRIOS, MÁCULAS EM CORPO'
                    y = dx[238]
                    e(x, y)
                    a = 1
                elif 'C' or 'D' or 'E' or 'F' or 'G' or 'H' or 'I' in h2:
                    dxconf.add(dx[200]+' '+dx[239])
                    x = 'APARECIMENTO DE LESÕES EM PELE (VESÍCULAS, EXANTEMA OU MÁCULAS ESCURAS/ HEMORRAGIA)'
                    y = dx[200]
                    e(x, y)
                    x = 'CALOR EXTREMO PELA NOITE, CONFUSÃO MENTAL, CORPO QUENTE, MEMBROS FRIOS, MÁCULAS'
                    y = dx[239]
                    e(x, y)
                    a = 1

        # TRIPLOS AQUECEDORES

        a = 0
        if tipo_p[4] in pool and 'W' or 'T' in lin and a == 0:
            if tipo_p[1] or tipo_p[5] in pool:
                dxconf.add(dx[197]+' '+dx[250])
                x = 'CALOR NOTURNO, BOCA SECA, CALOR VESPERTINO, CALOR EM BRAÇOS E PERNAS'
                y = dx[250]
                e(x, y)
                a = 1
            if tipo_p[15] or tipo_p[12] in pool and a == 0:
                x = 'CALOR NOTURNO, CONVULSÃO, SÍNCOPE, TRISMO'
                y = dx[251]
                e(x, y)
                dxconf.add(dx[197]+' '+dx[251])
                a = 1
            if tipo_p[2] or tipo_p[12] in pool and a == 0:
                dxconf.add(dx[197]+' '+dx[252])
                x = 'TREMORES E MEMBROS FRIOS'
                y = dx[252]
                e(x, y)
                a = 1
        if a == 0 and tipo_p[1] and tipo_p[4] in pool:
            quente4 = input(
                'Cefaléia ou odinofagia há menos de 90 dias? S/N ').upper()
            if quente4 == 'S':
                dxconf.add(dx[195]+' '+dx[245])
                x = 'CALOR E AVERSÃO AO FRIO, CEFALÉIA, ODINOFAGIA'
                y = dx[245]
                e(x, y)
                a = 1
        if tipo_p[4] and tipo_p[11] in pool and a == 0:
            if 'U' and 'O' in lin:
                if 'Z' not in lin:
                    while True:
                        try:
                            quente5 = input(
                                'Tosse ou falta de ar leve? (S/N) ').upper()
                            if quente5 == 'S':
                                dxconf.add(dx[195]+' '+dx[246])
                                x = 'CALOR, SUDORESE, TOSSE, DISPNÉIA, SEDE'
                                y = dx[246]
                                e(x, y)
                                a = 1
                                break
                            elif quente5 == 'N':
                                dxconf.add(dx[196]+' '+dx[248])
                                x = 'SUDORESE, CALOR VESPERTINO, CALOR CONTÍNUO COM SEDE INTENSA'
                                y = dx[248]
                                e(x, y)
                                a = 1
                                break
                        except:
                            continue
                else:
                    dxconf.add(dx[196]+' '+dx[248])
                    x = 'SUDORESE, CALOR VESPERTINO, CALOR CONTÍNUO COM SEDE INTENSA'
                    y = dx[248]
                    e(x, y)
                    a = 1
        if tipo_p[4] and tipo_p[12] in pool and a == 0:
            if 'W' or 'E' or 'T' in lin:
                dxconf.add(dx[195]+' '+dx[247])
                x = 'CALOR NOTURNO E DOR DE ESTÔMAGO'
                y = dx[247]
                e(x, y)
                a = 1
        if tipo_p[4] and tipo_p[20] in pool and a == 0:
            if 'U' or 'O' or 'Z' in lin:
                dxconf.add(dx[196]+' '+dx[249])
                x = 'CALOR CONTÍNUO, PLENITUDE PRANDIAL, SENSAÇÃO DE PESO EM CORPO NÁUSEAS'
                y = dx[249]
                e(x, y)
                a = 1

# -------------------------------------- PROTOCOLO DE LÍNGUA
        global prepdif
        prepdif = set()
        def f(x): return dxconf.add(
            dx[x]) if dx[x] in pct else pool2.add(dx[x])

        def fx(x): return dxconf.add(dx[x])
        if 'C' and 'X' in lin:
            if d1b != 1 and d2b != 1 and d3b != 1 and e1b != 1 and e2b != 1 and e3b != 1:
                f(0)
                f(1)
                f(2)
                f(3)
                f(4)
                f(5)
                prepdif.add('DEFICIÊNCIA DE XUE POR LÍNGUA BRANCA E FINA E PULSO SEM YIN')
            elif d1b == 1:
                fx(3)
            elif d2b == 1:
                fx(1)
            elif d3b == 1:
                fx(2)
            elif e1b == 1:
                fx(0)
            elif e2b == 1:
                fx(5)
            elif e3b == 1:
                fx(4)
        if 'C' and 'U' and 'T' in lin:
            f(6)
            f(7)
            f(8)
            f(9)
            f(10)
            f(11)
            prepdif.add('DEFICIÊNCIA YIN POR LÍNGUA FINA-VERMELHA E SEM SABURRA')
        if 'D' in lin:
            f(114)
            f(115)
            f(116)
            f(117)
            f(118)
            f(119)
            prepdif.add('FLEUMA/UMIDADE POR LÍNGUA ENGROSSADA')
        if 'A' in lin:
            f(102)
            f(103)
            f(104)
            f(105)
            f(106)
            f(107)
            fx(168)
            fx(169)
            fx(170)
            fx(171)
            fx(172)
            fx(173)
            fx(174)
            fx(175)
            fx(177)
            fx(178)
            fx(179)
            prepdif.add('CALOR INTERNO POR LÍNGUA EXTENDIDA')
        if 'B' and 'X' in lin:
            f(12)
            f(13)
            f(14)
            f(15)
            f(16)
            f(17)
            f(186)
            f(187)
            f(188)
            f(189)
            f(190)
            f(191)
            prepdif.add('DEFICIÊNCIA YANG POR LÍNGUA ENCURTADA E BRANCA')
        if 'B' and 'U' and 'T' in lin:
            f(6)
            f(7)
            f(8)
            f(9)
            f(10)
            f(11)
            f(174)
            f(175)
            f(176)
            f(177)
            f(178)
            f(179)
            prepdif.add('DEFICIÊNCIA YIN POR LÍNUGA CURTA-AVERMELHADA E COMPLETAMENTE SEM SABURRA')
        if 'E' in lin:
            f(114)
            f(115)
            f(116)
            f(117)
            f(118)
            f(119)
            prepdif.add('FLEUMA/UMIDADE POR ENDURECIMENTO DE MOVIMENTO NA LÍNGUA')
            if d1b+d2b+d3b+e1b+e2b+e3b>12:
                f(54)
                f(55)
                f(56)
                f(57)
                f(58)
                prepdif.add('ESTASE DE XUE POR ENDURECIMENTO DE MOVIMENTO NA LÍNGUA')
        if 'F' in lin:
            if 'E' in lin:
                prepdif.add('FLEUMA-SECURA COM ESTASE POR LÍNGUA DURA-FLÁCIDA')
            if 'D' in lin:
                prepdif.add('FLEUMA-SECURA POR LÍNGUA FLÁCIDA E ENGROSSADA')
            else:
                f(120)
                f(121)
                f(122)
                f(123)
                f(124)
                f(125)
                prepdif.add('SECURA POR FLACIDEZ DE LÍNGUA SEM ENGROSSAMENTO E SEM ENDURECIMENTO')
        if 'G' in lin:
            f(19)
            prepdif.add('DEFICIÊNCIA DE QI DE BAÇO POR MOVIMENTOS TRÊMULOS EM LÍNGUA')
        if 'H' in lin:
            f(126)
            f(127)
            f(128)
            f(129)
            f(130)
            f(131)
            prepdif.add('VENTO INTERNO POR DESVIO  EIXO DA LÍNGUA')
        if 'I' in lin:
            f(114)
            f(115)
            f(116)
            f(117)
            f(118)
            f(119)
            prepdif.add('FLEUMA/UMIDADE POR RACHADURA EM LINHA MÉDIA DA LÍNGUA')
            if 'E' in lin:
                f(208)
                f(209)
                f(210)
                f(211)
                f(212)
                f(213)
                prepdif.add('FLEUMA-FOGO POR RACHADURA EM LINHA MÉDIA DA LÍNGUA E ENDURECIMENTO')
            if d1a+d2a+d3a+e1a+e2a+e3a >12:
                f(168)
                f(169)
                f(170)
                f(171)
                f(172)
                f(173)
                prepdif.add('CALOR CHEIO POR LÍNGUA RACHADA CENTRALMENTE E EXCESSO DE YANG EM PULSO')
        if 'J' in lin:
            f(174)
            f(175)
            f(176)
            f(177)
            f(178)
            f(179)
            prepdif.add('CALOR VAZIO POR RACHADURA EM PERIFERIA DE LÍNGUA')
        if 'K' in lin:
            f(168)
            f(169)
            f(170)
            f(171)
            f(172)
            f(173)
            prepdif.add('CALOR CHEIO POR AFTAS EM LÍNGUA')
        if 'L' in lin:
            if d2a == 1:
                fx(19)
            f(19)
            prepdif.add('DEFICIÊNCIA DE QI DE BAÇO POR MARCA DE DENTES EM LÍNGUA')
        if 'M' in lin:
            if querym == 1:
                dxconf.add(dx[106])  # CALOR INTERNO DE R
                prepdif.add('CALOR INTERNO DE RIM POR PETÉQUIAS EM ZONA CORRRESPONDENTE')
            if querym == 2:
                if d1a == 3:
                    dxconf.add(dx[105])  # CALOR INTERNO DE IG
                    prepdif.add('CALOR INTERNO DE INTESTINO GROSSO POR PETÉQUIAS EM ZONA CORRRESPONDENTE')
                if e1a == 3:
                    dxconf.add(dx[102])  # CALOR INTERNO DE ID
                    prepdif.add(
                        'CALOR INTERNO DE INTESTINO DELGADO POR PETÉQUIAS EM ZONA CORRRESPONDENTE')
            if querym == 3:
                dxconf.add(dx[103])  # CALOR INTERNO DE 
                prepdif.add('CALOR INTERNO DE BAÇO POR PETÉQUIAS EM ZONA CORRRESPONDENTE')
            if querym == 4:
                dxconf.add(dx[107])  # CALOR INTERNO DE F
                prepdif.add('CALOR INTERNO DE FÍGADO POR PETÉQUIAS EM ZONA CORRRESPONDENTE')
            if querym == 5:
                dxconf.add(dx[105])  # CALOR INTERNO DE 
                prepdif.add('CALOR INTERNO DE PULMÃO POR PETÉQUIAS EM ZONA CORRRESPONDENTE')
            if querym == 6:
                dxconf.add(dx[102])  # CALOR INTERNO DE C
                prepdif.add('CALOR INTERNO DE CORAÇÃO POR PETÉQUIAS EM ZONA CORRRESPONDENTE')
            if querym == 7 and dx[198] not in dxconf:
                dxconf.add(dx[196])  # CALOR INTERNO DE TA MEDIO
                prepdif.add('CALOR INTERNO DE TRIPLO AQUECEDOR POR PETÉQUIAS EM ZONA CORRRESPONDENTE')
        if 'N' in lin:
            f(90)
            f(91)
            f(92)
            f(93)
            f(94)
            f(95)
            prepdif.add('FRIO INTERNO POR LÍNGUA APRESENTANDO SABURRA BRANCA')
        if 'O' in lin:
            f(168)
            f(169)
            f(170)
            f(171)
            f(172)
            f(173)
            prepdif.add('CALOR CHEIO POR LÍNGUA APRESENTANDO SABURRA AMARELA OU LARANJA')
        if 'P' and 'Y' in lin:
            f(90)
            f(91)
            f(92)
            f(93)
            f(94)
            f(95)
            prepdif.add('FRIO INTERNO POR LÍNGUA APRESENTANDO SIALORRÉIA E SABURRA CINZA')
        if 'P' and 'Ç' in lin:
            f(174)
            f(175)
            f(176)
            f(177)
            f(178)
            f(179)
            prepdif.add('CALOR VAZIO POR LÍNGUA APRESENTANDO SABURRA CINZA E RESSECADA')
        if 'Ç' and 'X' in lin:
            if e2b ==3:
                f(126)
                f(127)
                f(128)
                f(129)
                f(130)
                f(131)
                prepdif.add('VENTO INTERNO POR LÍNGUA BRANCA-SECA E ESTASE DE XUE DE FÍGADO')
            if d1c ==1:
                f(120)
                f(121)
                f(122)
                f(123)
                f(124)
                f(125)
                prepdif.add('SECURA POR LÍNGUA BRANCA-SECA E DEFICIÊNCIA YIN DE PULMÃO')
            elif d1c+d2c+d3c+e1c+e2c+e3c < 12:
                if d1c == 1:
                    fx(3)
                if d2c == 1:
                    fx(1)
                if d3c == 1:
                    fx(2)
                if e1c == 1:
                    fx(0)
                if e2c == 1:
                    fx(5)
                if e3c == 1:
                    fx(4)
                prepdif.add('ESTASE DE XUE POR LÍNGUA BRANCA-SECA E DESCARTADO SECURA-VENTO')
        if 'R' in lin:
            f(19)
            prepdif.add('DEFICIÊNCIA DE QI DE BAÇO POR LÍNGUA CENTRAL SEM SABURRA')
        if 'W' in lin or 'V' in lin:
            if 'R' in lin or 'Q' in lin or 'S' in lin:
                f(54)
                f(55)
                f(56)
                f(57)
                f(58)
                f(59)
                prepdif.add('ESTASE DE XUE POR LÍNGUA ROXO-ESCURA SEM SABURRA')
            elif d1a+d2a+d3a+e1a+e2a+e3a < 12 and d1c+d2c+d3c+e1c+e2c+e3c > 12:
                f(90)
                f(91)
                f(92)
                f(93)
                f(94)
                f(95)
                prepdif.add('FRIO INTERNO POR LÍNGUA AZUL SEM MORFOLOGIA DE ESTASE DE XUE')
            elif 'V' not in lin:
                f(102)
                f(103)
                f(104)
                f(105)
                f(106)
                f(107)
                prepdif.add('CALOR INTERNO POR LÍNGUA ROXA SEM MORFOLOGIA DE FRIO-ESTASE')
        if 'S' and 'X' in lin:
            f(7)
            prepdif.add('DEFICIÊNCIA YIN DE ESTÔMAGO POR LÍNGUA BRANCA E AUSÊNCIA PARCIAL DE SABURRA')
        if 'U' in lin:
            if 'R' or 'Q' or 'S' in lin:
                f(174)
                f(175)
                f(176)
                f(177)
                f(178)
                f(179)
                prepdif.add('CALOR VAZIO POR LÍNGUA VERMELHA E AUSÊNCIA DE SABURRAS')
            elif d1a+d2a+d3a+e1a+e2a+e3a > 12:
                f(168)
                f(169)
                f(170)
                f(171)
                f(172)
                f(173)
                prepdif.add('CALOR CHEIO POR LÍNGUA VERMELHA AFASTADO PADRÃO DE CALOR VAZIO')
        if 'X' and 'Y' in lin:
            f(12)
            f(13)
            f(14)
            f(15)
            f(16)
            f(17)
            prepdif.add('DEFICIÊNCIA YANG POR LÍNGUA BRANCA-ÚMIDA')

        # EXAME DE INDÍCIO DE GRAVIDEZ
        if sexo == 'F':
            i=0
            def f(): return warn.add('COMPATIBILIDADE DE GRAVIDEZ NO EXAME REALIZADO!')
            if 'G' in ppe1 or 'L' in ppe1:
                i+=1
            if antA == 'B':
                i+=1
            if int(e1a) != int(e3c):
                i+=1
            if 'D' in lin or 'E' in lin or 'I' in lin:
                i+=1
            if i>1:
                cls()
                if idd>=12 and idd<50:
                    f()
                    cls()
                    print('\n\n\n\n\nCOMPATIBILIDADE DE GRAVIDEZ NO EXAME REALIZADO!')
                    time.sleep(3)
                cls()            

# -------------------------------------- VERIFICAÇÃO DE DIAGNÓSTICO - PARTE 4

        unisec = pct.union(pool2)
        flow = unisec.union(tensor)

        # F
        def domfig(x):
            a = False
            if dx[x] in flow:
                if dx[7] in flow:
                    a = True
                if dx[91] in flow:
                    a = True
                if dx[181] in flow:
                    a = True
                if dx[187] in flow:
                    a = True
            return a
        b = 107
        if domfig(b) == True:
            dxconf.add(dx[b])
        b = 173
        if domfig(b) == True:
            dxconf.add(dx[b])
        b = 179
        if domfig(b) == True:
            dxconf.add(dx[b])
        b = 219
        if domfig(b) == True:
            dxconf.add(dx[b])

        # C
        def domcor(x):
            a = False
            if dx[x] in flow:
                if dx[9] in flow:
                    a = True
                if dx[93] in flow:
                    a = True
                if dx[183] in flow:
                    a = True
                if dx[189] in flow:
                    a = True
            return a
        b = 102
        if domcor(b) == True:
            dxconf.add(dx[b])
        b = 168
        if domcor(b) == True:
            dxconf.add(dx[b])
        b = 174
        if domcor(b) == True:
            dxconf.add(dx[b])
        b = 214
        if domcor(b) == True:
            dxconf.add(dx[b])

        # BP
        def dombac(x):
            a = False
            if dx[x] in flow:
                if dx[10] in flow:
                    a = True
                if dx[94] in flow:
                    a = True
                if dx[184] in flow:
                    a = True
                if dx[190] in flow:
                    a = True
            return a
        b = 103
        if dombac(b) == True:
            dxconf.add(dx[b])
        b = 169
        if dombac(b) == True:
            dxconf.add(dx[b])
        b = 175
        if dombac(b) == True:
            dxconf.add(dx[b])
        b = 215
        if dombac(b) == True:
            dxconf.add(dx[b])

        # P
        def dompul(x):
            a = False
            if dx[x] in flow:
                if dx[11] in flow:
                    a = True
                if dx[95] in flow:
                    a = True
                if dx[185] in flow:
                    a = True
                if dx[191] in flow:
                    a = True
            return a
        b = 105
        if dompul(b) == True:
            dxconf.add(dx[b])
        b = 171
        if dompul(b) == True:
            dxconf.add(dx[b])
        b = 177
        if dompul(b) == True:
            dxconf.add(dx[b])
        b = 217
        if dompul(b) == True:
            dxconf.add(dx[b])

        # R
        def domrim(x):
            a = False
            if dx[x] in flow:
                if dx[6] in flow:
                    a = True
                if dx[90] in flow:
                    a = True
                if dx[180] in flow:
                    a = True
                if dx[186] in flow:
                    a = True
            return a
        b = 106
        if domrim(b) == True:
            dxconf.add(dx[b])
        b = 172
        if domrim(b) == True:
            dxconf.add(dx[b])
        b = 178
        if domrim(b) == True:
            dxconf.add(dx[b])
        b = 218
        if domrim(b) == True:
            dxconf.add(dx[b])

        # -------------------------------------- ANÁLISE DE DX DE CERTEZA POR CICLO DE CONTRA-DOMINÂNCIA - PARTE 5

        # F
        def subfig(x):
            a = False
            if dx[x] in flow:
                if dx[105] in flow:
                    a = True
                if dx[171] in flow:
                    a = True
                if dx[177] in flow:
                    a = True
                if dx[217] in flow:
                    a = True
            return a
        b = 11
        if subfig(b) == True:
            dxconf.add(dx[b])
        b = 95
        if subfig(b) == True:
            dxconf.add(dx[b])
        b = 185
        if subfig(b) == True:
            dxconf.add(dx[b])
        b = 191
        if subfig(b) == True:
            dxconf.add(dx[b])

        # C
        def subcor(x):
            a = False
            if dx[x] in flow:
                if dx[106] in flow:
                    a = True
                if dx[172] in flow:
                    a = True
                if dx[178] in flow:
                    a = True
                if dx[218] in flow:
                    a = True
            return a
        b = 6
        if subcor(b) == True:
            dxconf.add(dx[b])
        b = 90
        if subcor(b) == True:
            dxconf.add(dx[b])
        b = 180
        if subcor(b) == True:
            dxconf.add(dx[b])
        b = 186
        if subcor(b) == True:
            dxconf.add(dx[b])

        # BP
        def subbac(x):
            a = False
            if dx[x] in flow:
                if dx[107] in flow:
                    a = True
                if dx[173] in flow:
                    a = True
                if dx[179] in flow:
                    a = True
                if dx[219] in flow:
                    a = True
            return a
        b = 7
        if subbac(b) == True:
            dxconf.add(dx[b])
        b = 91
        if subbac(b) == True:
            dxconf.add(dx[b])
        b = 181
        if subbac(b) == True:
            dxconf.add(dx[b])
        b = 187
        if subbac(b) == True:
            dxconf.add(dx[b])

        # P
        def subpul(x):
            a = False
            if dx[x] in flow:
                if dx[102] in flow:
                    a = True
                if dx[168] in flow:
                    a = True
                if dx[174] in flow:
                    a = True
                if dx[214] in flow:
                    a = True
            return a
        b = 9
        if subpul(b) == True:
            dxconf.add(dx[b])
        b = 93
        if subpul(b) == True:
            dxconf.add(dx[b])
        b = 183
        if subpul(b) == True:
            dxconf.add(dx[b])
        b = 189
        if subpul(b) == True:
            dxconf.add(dx[b])

        # R
        def subrim(x):
            a = False
            if dx[x] in flow:
                if dx[103] in flow:
                    a = True
                if dx[169] in flow:
                    a = True
                if dx[175] in flow:
                    a = True
                if dx[215] in flow:
                    a = True
            return a
        b = 10
        if subrim(b) == True:
            dxconf.add(dx[b])
        b = 94
        if subrim(b) == True:
            dxconf.add(dx[b])
        b = 184
        if subrim(b) == True:
            dxconf.add(dx[b])
        b = 190
        if subrim(b) == True:
            dxconf.add(dx[b])

        #  ALGORÍTMO DIAGNÓSTICO (A.I.) PARA CRUZAMENTO DE DIAGNÓSTICOS E WU FU - PARTE 2

        def sy2(x, y, l):
            if dx[x] and dx[y] in l:
                return True
            else:
                return False

        def sy3(x, y, z, l):
            if dx[x] and dx[y] and dx[z] in l:
                return True
            else:
                return False

        def sy4(x, y, z, w, l):
            if dx[x] and dx[y] and dx[z] and dx[w] in l:
                return True
            else:
                return False

        def f(x): return dxconf.add(dx[int(x)])
        if sy3(6, 4, 7, ppe1) is True:
            f(208)
        if sy3(4, 11, 7, ppe1) is True:
            f(208)
        if sy3(4, 6, 15, ppe1) is True:
            f(208)
        if sy3(6, 4, 11, ppe1) is True:
            f(102)
        if sy3(6, 25, 11, ppe1) is True:
            f(102)
        if dx[8] in ppe1 or dx[15] in ppe1 or dx[26] in ppe1:
            if dx[7] not in ppe1:
                f(0)
            else:
                f(114)
                f(60)
        if dx[5] in ppe1 and len(ppe1) < 2:
            f(60)
        if dx[7] in ppe1 and len(ppe1) < 2:
            f(228)
        if sy2(1, 5, ppe1) == True or sy2(5, 4, ppe1) == True:
            f(6)
        if dx[8] in ppe1 or dx[12] in ppe1 and len(ppe1) < 2:
            f(54)
        if sy2(2, 21, ppe1) == True or dx[26] in ppe1 and len(ppe1) < 2:
            f(12)
        if sy2(4, 12, ppd3) == True:
            f(104)
        if dx[12] in ppe3 or dx[8] in ppe3:
            if dx[19] in ppe1:
                f(2)
        if sy3(4, 6, 11, ppd3) == True:
            f(104)
        if sy3(4, 6, 7, ppd3) == True or sy3(4, 11, 7, ppd3) == True or sy3(4, 6, 15, ppd3) == True:
            f(210)

        def f1(x, y): return dx[x] in y
        if f1(5, ppd3) == True and f1(11, ppe1) == True:
            f(62)
        if f1(8, ppd3) == True or f1(15, ppd3) == True or f1(26, ppd3) == True:
            f(56)
        if f1(15, ppe2) == True:
            f(65)
        if f1(15, ppe2) == True and f1(15, ppe3) == True:
            f(167)
        if sy2(15, 19, ppe2) == True:
            f(59)
        if sy3(6, 15, 4, ppe2) == True:
            f(107)
        if sy3(7, 4, 15, ppe2) == True:
            f(208)
        if sy3(2, 15, 3, ppe2) == True:
            f(101)
        if f1(8, ppe2) == True or f1(12, ppe2) == True:
            f(5)
        if sy2(1, 5, ppe2) == True:
            f(11)
        if f1(15, ppe2) == True:
            f(155)
        if sy2(4, 15, ppe2) == True:
            f(201)
            f(219)
        if sy2(12, 15, ppe2) == True:
            f(199)
            f(131)
        if f1(15, ppe2) == True:
            if f1(21, ppd2) == True or f1(15, ppd2) == True:
                f(167)
        if f1(8, ppe2) == True or f1(12, ppe2) == True:
            f(5)
            f(0)
        if f1(5, ppd1) == True:
            f(21)
        if sy2(1, 5, ppd1) == True:
            f(9)
        if f1(5, ppd1) == True:
            f(123)
        if sy2(1, 14, ppd1) == True:
            f(202)
            f(129)

        def sy1(x, y): return dx[x] in y
        if sy2(1, 4, ppd1) == True:
            f(198)
            f(129)
        if sy2(1, 7, ppd1) == True:
            f(129)
            f(117)
        if sy2(11, 4, ppd1) == True:
            f(171)
        if sy1(7, ppd1) == True or sy1(20, ppd1) == True:
            f(117)
        if sy2(4, 7, ppd1) == True:
            f(189)
            f(117)
        if sy2(7, 4, ppd1) == True:
            f(171)
            f(117)
        if sy2(7, 12, ppd1) == True:
            f(228)
        if sy2(7, 12, ppd1) == True or sy1(15, ppd1) == True or sy1(20, ppd1) == True:
            f(147)
        if sy1(5, ppd1) == True and sy1(5, ppe1) == True:
            f(18)
            f(21)
        if sy1(5, ppd2) == True:
            f(19)
        if sy2(2, 21, ppd2) == True:
            f(13)
        if sy1(21, ppd2) == True:
            f(157)
        if sy1(12, ppd2) == True:
            f(145)
        if sy1(8, ppd2) == True:
            f(1)
        if sy2(7, 3, ppd2) == True:
            f(97)
            f(115)
        if sy2(4, 7, ppd2) == True:
            f(115)
            f(169)
        if sy2(8, 12, ppd2) == True and sy2(8, 12, ppe1) == True:
            f(1)
            f(0)
        if sy1(5, ppd2) == True:
            f(19)
        if sy1(8, ppd2) == True or sy1(12, ppd2) == True:
            f(1)
            f(5)
        if sy2(7, 15, ppd2) == True:
            f(61)
            f(115)
        if sy2(2, 21, ppe3) == True:
            f(16)
            f(64)
        if sy2(1, 5, ppe3) == True:
            f(10)
        if sy3(2, 21, 14, ppe3) == True:
            f(22)
        if sy1(18, ppe3) == True or sy2(1, 5, ppe3) == True:
            f(28)
        if sy3(2, 3, 21, ppe3) == True:
            f(154)
        if sy2(1, 5, ppe3) == True or sy1(4, ppe3) == True:
            f(178)
            if sy2(1, 5, ppe2) == True:
                f(148)
                f(149)
        if sy3(1, 5, 4, ppe3) == True or sy2(2, 21, ppe3) == True:
            if sy3(1, 5, 4, ppd3) == True or sy2(2, 21, ppd3) == True:
                f(144)
                f(148)
        if sy1(11, ppe1) == True and sy1(11, ppd1) == True:
            f(6)
            f(10)
        if sy2(1, 5, ppe3) == True:
            f(9)
            f(10)
        if sy2(2, 21, ppe3) == True:
            f(13)
            f(16)
        if sy1(5, ppd2) == True:
            f(19)
            f(151)
        if sy3(21, 3, 2, ppd2) == True:
            f(187)
        if sy2(1, 5, ppd2) == True:
            f(175)
        if sy1(15, ppd2) == True:
            f(61)
        if sy2(4, 11, ppd2) == True:
            f(169)
        if sy3(4, 7, 11, ppd2) == True:
            f(209)
        if sy3(2, 3, 14, ppd2) == True:
            f(181)
        if sy1(14, ppd2) == True or sy1(15, ppd2) == True:
            f(151)
        if sy2(4, 7, ppd2) == True:
            f(209)
        if sy2(6, 7, ppd2) == True:
            if vector1[2] >= 0:
                f(169)
            elif vector2[2] >= 0:
                f(181)
        if sy1(15, ppd2) == True:
            f(55)
        if sy1(5, ppd2) == True:
            f(19)
        if sy2(1, 5, ppd2) == True:
            f(7)
        if sy2(11, 4, ppe1) == True:
            f(168)
        if sy2(2, 15, ppe1) == True:
            f(144)
        if len(ppe1) < 1:
            warn.add('Possibilidade de Infecção Abdominal (fogo imperial)'.upper())
        if sy3(2, 3, 21, ppe1) == True:
            f(186)
        if sy2(2, 15, ppe1) == True:
            f(144)
        if sy1(4, ppe1) == True or sy1(7, ppe1) == True or sy1(4, ppd1) == True or sy1(7, ppd1) == True:
            f(211)
        if sy2(4, 6, ppd1) == True:
            f(171)
        if sy2(2, 6, ppd1) == True:
            f(171)
            f(159)
        if sy2(2, 14, ppd1) == True:
            f(183)
        if sy1(15, ppe3) == True and sy1(15, ppd3) == True:
            f(63)
        if sy1(12, ppd1) == True:
            f(123)
        if sy2(2, 21, ppd1) == True:
            f(189)
        if sy3(12, 2, 21, ppd1) == True:
            f(147)
        if sy2(7, 15, ppe2) == True:
            f(119)
        if sy3(4, 7, 15, ppe2) == True:
            f(119)
            f(173)
        if sy1(21, ppe2) == True:
            f(23)
        if sy2(4, 7, ppe3) == True:
            f(118)
            f(172)
        if sy2(3, 7, ppe3) == True:
            f(118)
            f(100)
        if sy2(2, 21, ppe3) == True:
            f(190)

        # -------------------------------------- RESULTADOS

        cls()
        print()
        print('_____________________________________________')
        print()
        print('DATA DE EXAME: '+horadia +
              ' PROTOCOLO DE ANÁLISE DE PROGRAMA TAO V.'+ver)
        print('HDA:')
        print(hda)
        print()
        print('DIAGNÓSTICOS CONFIRMADOS DE '+nome+':')
        dxconf1 = pct.intersection(pool2)
        global dxconff
        dxconff = dxconf1.union(dxconf)
        # -------------------------------------- TESTE DE ERROS

        # CAPTURA DE STATUS - FLEUMA-FOGO
        def f(x, y): return dxconff.add(dx[x]) if dx[y] in dxconff else None
        f(102, 208)
        f(103, 209)
        f(104, 210)
        f(105, 211)
        f(106, 212)
        f(107, 213)
        # CAPTURA DE STATUS - FOGO POR ESTAGNAÇÃO DE CANAL
        f(114, 208)
        f(115, 209)
        f(116, 210)
        f(117, 211)
        f(118, 212)
        f(119, 213)

        # TRANSCRIÇÃO DE STATUS YIN/YANG PARA SÍNDROMES (E.G. DEF YIN PARA CALOR VAZIO)

        # EXC YANG = CALOR CHEIO
        # INDIRETO

        # DEF YANG = FRIO VAZIO
        f(186, 12)
        f(187, 13)
        f(188, 14)
        f(189, 15)
        f(190, 16)
        f(191, 17)

        # EXC YIN = FRIO CHEIO
        # INDIRETO

        # DEF YIN = CALOR VAZIO
        f(174, 6)
        f(175, 7)
        f(176, 8)
        f(177, 9)
        f(178, 10)
        f(179, 11)

        # ADIÇÃO DE DUPLICATA EM CASO DE INCONSISTÊNCIA PARA DEPURAR COM CÁLCULO DE ERRO
        def fx(x, y, z, a): return path.add('Duplicata gerada para inquérito em '+a) and dxconff.add(dx[y]) and dxconff.add(
            dx[z]) if dx[x] in dxconff and dx[y] not in dxconff and dx[x] in dxconff and dx[z] not in dxconff else None
        fx(90, 180, 186, 'C')  # FRIO INTERNO > +FC +FV
        fx(91, 181, 187, 'BP')
        fx(92, 182, 188, 'PC')
        fx(93, 183, 189, 'P')
        fx(94, 184, 190, 'R')
        fx(95, 185, 191, 'F')
        fx(102, 174, 168, 'C')  # CALOR INTERNO > +CC +CV
        fx(103, 175, 169, 'BP')
        fx(104, 176, 170, 'PC')
        fx(105, 177, 171, 'P')
        fx(106, 178, 172, 'R')
        fx(107, 179, 173, 'F')
        def f(x): return dxconff.discard(dx[x])
        f(90)
        f(91)
        f(92)
        f(93)
        f(94)
        f(95)
        f(102)
        f(103)
        f(104)
        f(105)
        f(106)
        f(107)

        # -------------------------------------- CORREÇÃO DE DUPLICIDADE E ERROS

        # VERIFICAÇÃO DE COLISÃO DE DIAGNÓSTICOS INCONGRUENTES POR UNIÃO DE EXAMES
        # CALOR CHEIO - CALOR VAZIO - FRIO CHEIO - FRIO VAZIO

        global ver1
        ver1 = False
        global ver2
        ver2 = False
        global ver3
        ver3 = False
        global ver4
        ver4 = False
        # C
        x = 168  # cc
        y = 174  # cv
        if dx[x] in dxconff and dx[y] in dxconff:
            path.add('Colisão de Calores C')
            if vector1[1] > 0:
                dxconff.discard(dx[y])
                ver1 = True
            if vector2[1] < 0:
                dxconff.discard(dx[x])
                ver2 = True
            if ver1 == True and ver2 == True or ver1 == False and ver2 == False:
                dxconff.add(dx[x])
                dxconff.add(dx[y])
                if vector1[1] >= 2:
                    dxconff.discard(dx[y])
                    ver3 = True
                if vector2[1] <= -2:
                    dxconff.discard(dx[x])
                    ver4 = True
                if ver3 == True and ver4 == True or ver3 == False and ver4 == False:
                    dxconff.add(dx[x])
                    dxconff.add(dx[y])
                    if e1a == 3:
                        dxconff.discard(dx[y])
                    else:
                        dxconff.discard(dx[x])
        ver1 = False
        ver2 = False
        ver3 = False
        ver4 = False
        if dx[180] in dxconff and dx[186] in dxconff:
            path.add('Colisão de Frios C')
            if vector2[1] >= 1 and vector1[1] > -1:
                dxconff.discard(dx[186])
                ver1 = True
            if vector2[1] < 1 and vector1[1] <= -1:
                dxconff.discard(dx[180])
                ver2 = True
            if ver1 == True and ver2 == True:
                dxconff.add(dx[180])
                dxconff.add(dx[186])
                if vector2[1] >= 2 and vector1[1] > -2:
                    dxconff.discard(dx[186])
                    ver3 = True
                if vector2[1] < 2 and vector1[1] <= -2:
                    dxconff.discard(dx[180])
                    ver4 = True
                if ver3 == True and ver4 == True:
                    dxconff.add(dx[180])
                    dxconff.add(dx[186])
                    if e1c == 3:
                        dxconff.discard(dx[186])
                    else:
                        dxconff.discard(dx[180])
        # BP
        x = 169  # cc
        y = 175  # cv
        ver1 = False
        ver2 = False
        ver3 = False
        ver4 = False
        if dx[x] in dxconff and dx[y] in dxconff:
            path.add('Colisão de Calores BP')
            if vector1[1] > 0:
                dxconff.discard(dx[y])
                ver1 = True
            if vector2[1] < 0:
                dxconff.discard(dx[x])
                ver2 = True
            if ver1 == True and ver2 == True or ver1 == False and ver2 == False:
                dxconff.add(dx[x])
                dxconff.add(dx[y])
                if vector1[1] >= 2:
                    dxconff.discard(dx[y])
                    ver3 = True
                if vector2[1] <= -2:
                    dxconff.discard(dx[x])
                    ver4 = True
                if ver3 == True and ver4 == True or ver3 == False and ver4 == False:
                    dxconff.add(dx[x])
                    dxconff.add(dx[y])
                    if e1a == 3:
                        dxconff.discard(dx[y])
                    else:
                        dxconff.discard(dx[x])
        ver1 = False
        ver2 = False
        ver3 = False
        ver4 = False
        if dx[181] in dxconff and dx[187] in dxconff:
            path.add('Colisão de Frios BP')
            if vector2[2] >= 1 and vector1[2] > -1:
                dxconff.discard(dx[187])
                ver1 = True
            if vector2[2] < 1 and vector1[2] <= -1:
                dxconff.discard(dx[181])
                ver2 = True
            if ver1 == True and ver2 == True:
                dxconff.add(dx[181])
                dxconff.add(dx[187])
                if vector2[2] >= 2 and vector1[2] > -2:
                    dxconff.discard(dx[187])
                    ver3 = True
                if vector2[2] < 2 and vector1[2] <= -2:
                    dxconff.discard(dx[181])
                    ver4 = True
                if ver3 == True and ver4 == True:
                    dxconff.add(dx[181])
                    dxconff.add(dx[187])
                    if d2c == 3:
                        dxconff.discard(dx[187])
                    else:
                        dxconff.discard(dx[181])
        # PC
        x = 170  # cc
        y = 176  # cv
        ver1 = False
        ver2 = False
        ver3 = False
        ver4 = False
        if dx[x] in dxconff and dx[y] in dxconff:
            path.add('Colisão de Calores PC')
            if vector1[1] > 0:
                dxconff.discard(dx[y])
                ver1 = True
            if vector2[1] < 0:
                dxconff.discard(dx[x])
                ver2 = True
            if ver1 == True and ver2 == True or ver1 == False and ver2 == False:
                dxconff.add(dx[x])
                dxconff.add(dx[y])
                if vector1[1] >= 2:
                    dxconff.discard(dx[y])
                    ver3 = True
                if vector2[1] <= -2:
                    dxconff.discard(dx[x])
                    ver4 = True
                if ver3 == True and ver4 == True or ver3 == False and ver4 == False:
                    dxconff.add(dx[x])
                    dxconff.add(dx[y])
                    if e1a == 3:
                        dxconff.discard(dx[y])
                    else:
                        dxconff.discard(dx[x])
        ver1 = False
        ver2 = False
        ver3 = False
        ver4 = False
        if dx[182] in dxconff and dx[188] in dxconff:
            path.add('Colisão de Frios PC')
            if vector2[0] >= 1 and vector1[0] > -1:
                dxconff.discard(dx[188])
                ver1 = True
            if vector2[0] < 1 and vector1[0] <= -1:
                dxconff.discard(dx[182])
                ver2 = True
            if ver1 == True and ver2 == True:
                dxconff.add(dx[182])
                dxconff.add(dx[188])
                if vector2[0] >= 2 and vector1[0] > -2:
                    dxconff.discard(dx[188])
                    ver3 = True
                if vector2[0] < 2 and vector1[0] <= -2:
                    dxconff.discard(dx[182])
                    ver4 = True
                if ver3 == True and ver4 == True:
                    dxconff.add(dx[182])
                    dxconff.add(dx[188])
                    if d3c == 3:
                        dxconff.discard(dx[188])
                    else:
                        dxconff.discard(dx[182])
        # P
        x = 171  # cc
        y = 177  # cv
        ver1 = False
        ver2 = False
        ver3 = False
        ver4 = False
        if dx[x] in dxconff and dx[y] in dxconff:
            path.add('Colisão de Calores P')
            if vector1[1] > 0:
                dxconff.discard(dx[y])
                ver1 = True
            if vector2[1] < 0:
                dxconff.discard(dx[x])
                ver2 = True
            if ver1 == True and ver2 == True or ver1 == False and ver2 == False:
                dxconff.add(dx[x])
                dxconff.add(dx[y])
                if vector1[1] >= 2:
                    dxconff.discard(dx[y])
                    ver3 = True
                if vector2[1] <= -2:
                    dxconff.discard(dx[x])
                    ver4 = True
                if ver3 == True and ver4 == True or ver3 == False and ver4 == False:
                    dxconff.add(dx[x])
                    dxconff.add(dx[y])
                    if e1a == 3:
                        dxconff.discard(dx[y])
                    else:
                        dxconff.discard(dx[x])
        ver1 = False
        ver2 = False
        ver3 = False
        ver4 = False
        if dx[183] in dxconff and dx[189] in dxconff:
            path.add('Colisão de Frios P')
            if vector2[3] >= 1 and vector1[3] > -1:
                dxconff.discard(dx[189])
                ver1 = True
            if vector2[3] < 1 and vector1[3] <= -1:
                dxconff.discard(dx[183])
                ver2 = True
            if ver1 == True and ver2 == True:
                dxconff.add(dx[183])
                dxconff.add(dx[189])
                if vector2[3] >= 2 and vector1[3] > -2:
                    dxconff.discard(dx[189])
                    ver3 = True
                if vector2[3] < 2 and vector1[3] <= -2:
                    dxconff.discard(dx[183])
                    ver4 = True
                if ver3 == True and ver4 == True:
                    dxconff.add(dx[183])
                    dxconff.add(dx[189])
                    if d1c == 3:
                        dxconff.discard(dx[189])
                    else:
                        dxconff.discard(dx[183])
        # R
        x = 172  # cc
        y = 178  # cv
        ver1 = False
        ver2 = False
        ver3 = False
        ver4 = False
        if dx[x] in dxconff and dx[y] in dxconff:
            path.add('Colisão de Calores R')
            if vector1[1] > 0:
                dxconff.discard(dx[y])
                ver1 = True
            if vector2[1] < 0:
                dxconff.discard(dx[x])
                ver2 = True
            if ver1 == True and ver2 == True or ver1 == False and ver2 == False:
                dxconff.add(dx[x])
                dxconff.add(dx[y])
                if vector1[1] >= 2:
                    dxconff.discard(dx[y])
                    ver3 = True
                if vector2[1] <= -2:
                    dxconff.discard(dx[x])
                    ver4 = True
                if ver3 == True and ver4 == True or ver3 == False and ver4 == False:
                    dxconff.add(dx[x])
                    dxconff.add(dx[y])
                    if e1a == 3:
                        dxconff.discard(dx[y])
                    else:
                        dxconff.discard(dx[x])
        ver1 = False
        ver2 = False
        ver3 = False
        ver4 = False
        if dx[184] in dxconff and dx[190] in dxconff:
            path.add('Colisão de Frios R')
            if vector2[4] >= 1 and vector1[4] > -1:
                dxconff.discard(dx[190])
                ver1 = True
            if vector2[4] < 1 and vector1[4] <= -1:
                dxconff.discard(dx[184])
                ver2 = True
            if ver1 == True and ver2 == True:
                dxconff.add(dx[184])
                dxconff.add(dx[190])
                if vector2[4] >= 2 and vector1[4] > -2:
                    dxconff.discard(dx[190])
                    ver3 = True
                if vector2[4] < 2 and vector1[4] <= -2:
                    dxconff.discard(dx[184])
                    ver4 = True
                if ver3 == True and ver4 == True:
                    dxconff.add(dx[184])
                    dxconff.add(dx[190])
                    if e3c == 3:
                        dxconff.discard(dx[190])
                    else:
                        dxconff.discard(dx[184])
        # F
        x = 173  # cc
        y = 179  # cv
        ver1 = False
        ver2 = False
        ver3 = False
        ver4 = False
        if dx[x] in dxconff and dx[y] in dxconff:
            path.add('Colisão de Calores F')
            if vector1[1] > 0:
                dxconff.discard(dx[y])
                ver1 = True
            if vector2[1] < 0:
                dxconff.discard(dx[x])
                ver2 = True
            if ver1 == True and ver2 == True or ver1 == False and ver2 == False:
                dxconff.add(dx[x])
                dxconff.add(dx[y])
                if vector1[1] >= 2:
                    dxconff.discard(dx[y])
                    ver3 = True
                if vector2[1] <= -2:
                    dxconff.discard(dx[x])
                    ver4 = True
                if ver3 == True and ver4 == True or ver3 == False and ver4 == False:
                    dxconff.add(dx[x])
                    dxconff.add(dx[y])
                    if e1a == 3:
                        dxconff.discard(dx[y])
                    else:
                        dxconff.discard(dx[x])
        ver1 = False
        ver2 = False
        ver3 = False
        ver4 = False
        if dx[185] in dxconff and dx[191] in dxconff:
            path.add('Colisão de Frios F')
            if vector2[5] >= 1 and vector1[5] > -1:
                dxconff.discard(dx[191])
                ver1 = True
            if vector2[5] < 1 and vector1[5] <= -1:
                dxconff.discard(dx[185])
                ver2 = True
            if ver1 == True and ver2 == True:
                dxconff.add(dx[185])
                dxconff.add(dx[191])
                if vector2[5] >= 2 and vector1[5] > -2:
                    dxconff.discard(dx[191])
                    ver3 = True
                if vector2[5] < 2 and vector1[5] <= -2:
                    dxconff.discard(dx[185])
                    ver4 = True
                if ver3 == True and ver4 == True:
                    dxconff.add(dx[185])
                    dxconff.add(dx[191])
                    if e2c == 3:
                        dxconff.discard(dx[191])
                    else:
                        dxconff.discard(dx[185])

        # -------------------------------------- CORREÇÃO DE CHOQUE FRIO-CALOR

        def tn(x):
            a = int(x)
            b = int(x+6)
            c = int(x+12)
            d = int(x+18)
            if dx[a] in dxconff:
                w = 1
            else:
                w = 0
            if dx[b] in dxconff:
                r = 1
            else:
                r = 0
            if dx[c] in dxconff:
                y = -1
            else:
                y = 0
            if dx[d] in dxconff:
                z = -1
            else:
                z = 0
            return w+r+y+z

        n = 'C'
        x = 168
        a = e1a
        b = e1b
        c = e1c
        p = e2a
        if tn(x) == 0:
            path.add('Cálculo de correção via Coerência - '+n)
            if a > c:
                dxconff.discard(dx[180])
                dxconff.discard(dx[186])
            if a < c:
                dxconff.discard(dx[x])
                dxconff.discard(dx[174])
            else:
                path.add('Cálculo de correção via Codominância - '+n)
                if dx[172] in dxconff or dx[178] in dxconff:
                    dxconff.discard(dx[x])
                    dxconff.discard(dx[174])
                if dx[183] in dxconff or dx[189]:
                    dxconff.discard(dx[180])
                    dxconff.discard(dx[186])
                else:
                    path.add('Cálculo de correção via Ressonância - '+n)
                    if b > 2:
                        dxconff.discard(dx[180])
                        dxconff.discard(dx[186])
                    if b < 2:
                        dxconff.discard(dx[x])
                        dxconff.discard(dx[174])
                    else:
                        path.add(
                            'Cálculo de correção via Paternidade Yang - '+n)
                        if p > 2:
                            dxconff.discard(dx[180])
                            dxconff.discard(dx[186])
                        if p < 2:
                            dxconff.discard(dx[x])
                            dxconff.discard(dx[174])
                        else:
                            path.add(
                                'Cálculo de correção via Incoerência - '+n)
                            dxconff.discard(dx[180])
                            dxconff.discard(dx[186])
                            dxconff.discard(dx[x])
                            dxconff.discard(dx[174])

        n = 'BP'
        x = 169
        a = d2a
        b = d2b
        c = d2c
        p = e1a
        if tn(x) == 0:
            path.add('Cálculo de correção via Coerência - '+n)
            if a > c:
                dxconff.discard(dx[181])
                dxconff.discard(dx[187])
            if a < c:
                dxconff.discard(dx[x])
                dxconff.discard(dx[175])
            else:
                path.add('Cálculo de correção via Codominância - '+n)
                if dx[173] in dxconff or dx[179] in dxconff:
                    dxconff.discard(dx[x])
                    dxconff.discard(dx[175])
                if dx[184] in dxconff or dx[190]:
                    dxconff.discard(dx[181])
                    dxconff.discard(dx[187])
                else:
                    path.add('Cálculo de correção via Ressonância - '+n)
                    if b > 2:
                        dxconff.discard(dx[181])
                        dxconff.discard(dx[187])
                    if b < 2:
                        dxconff.discard(dx[x])
                        dxconff.discard(dx[175])
                    else:
                        path.add(
                            'Cálculo de correção via Paternidade Yang - '+n)
                        if p > 2:
                            dxconff.discard(dx[181])
                            dxconff.discard(dx[187])
                        if p < 2:
                            dxconff.discard(dx[x])
                            dxconff.discard(dx[175])
                        else:
                            path.add(
                                'Cálculo de correção via Incoerência - '+n)
                            dxconff.discard(dx[181])
                            dxconff.discard(dx[187])
                            dxconff.discard(dx[x])
                            dxconff.discard(dx[175])

        n = 'PC'
        x = 170
        a = d3a
        b = d3b
        c = d3c
        if tn(x) == 0:
            path.add('Cálculo de correção via Coerência - '+n)
            if a > c:
                dxconff.discard(dx[182])
                dxconff.discard(dx[188])
            if a < c:
                dxconff.discard(dx[x])
                dxconff.discard(dx[176])
            else:
                path.add('Cálculo de correção via Ressonância - '+n)
                if b > 2:
                    dxconff.discard(dx[182])
                    dxconff.discard(dx[188])
                if b < 2:
                    dxconff.discard(dx[x])
                    dxconff.discard(dx[176])
                else:
                    path.add('Cálculo de correção via Incoerência - '+n)
                    dxconff.discard(dx[182])
                    dxconff.discard(dx[188])
                    dxconff.discard(dx[x])
                    dxconff.discard(dx[176])

        n = 'P'
        x = 171
        a = d1a
        b = d1b
        c = d1c
        p = d2a
        if tn(x) == 0:
            path.add('Cálculo de correção via Coerência - '+n)
            if a > c:
                dxconff.discard(dx[183])
                dxconff.discard(dx[189])
            if a < c:
                dxconff.discard(dx[x])
                dxconff.discard(dx[177])
            else:
                path.add('Cálculo de correção via Codominância - '+n)
                if dx[168] in dxconff or dx[174] in dxconff:
                    dxconff.discard(dx[x])
                    dxconff.discard(dx[177])
                if dx[185] in dxconff or dx[191]:
                    dxconff.discard(dx[183])
                    dxconff.discard(dx[189])
                else:
                    path.add('Cálculo de correção via Ressonância - '+n)
                    if b > 2:
                        dxconff.discard(dx[183])
                        dxconff.discard(dx[189])
                    if b < 2:
                        dxconff.discard(dx[x])
                        dxconff.discard(dx[177])
                    else:
                        path.add(
                            'Cálculo de correção via Paternidade Yang - '+n)
                        if p > 2:
                            dxconff.discard(dx[183])
                            dxconff.discard(dx[189])
                        if p < 2:
                            dxconff.discard(dx[x])
                            dxconff.discard(dx[177])
                        else:
                            path.add(
                                'Cálculo de correção via Incoerência - '+n)
                            dxconff.discard(dx[183])
                            dxconff.discard(dx[189])
                            dxconff.discard(dx[x])
                            dxconff.discard(dx[177])

        n = 'R'
        x = 172
        a = e3a
        b = e3b
        c = e3c
        p = d1a
        if tn(x) == 0:
            path.add('Cálculo de correção via Coerência - '+n)
            if a > c:
                dxconff.discard(dx[184])
                dxconff.discard(dx[190])
            if a < c:
                dxconff.discard(dx[x])
                dxconff.discard(dx[178])
            else:
                path.add('Cálculo de correção via Codominância - '+n)
                if dx[169] in dxconff or dx[175] in dxconff:
                    dxconff.discard(dx[x])
                    dxconff.discard(dx[178])
                if dx[186] in dxconff or dx[180]:
                    dxconff.discard(dx[184])
                    dxconff.discard(dx[190])
                else:
                    path.add('Cálculo de correção via Ressonância - '+n)
                    if b > 2:
                        dxconff.discard(dx[184])
                        dxconff.discard(dx[190])
                    if b < 2:
                        dxconff.discard(dx[x])
                        dxconff.discard(dx[178])
                    else:
                        path.add(
                            'Cálculo de correção via Paternidade Yang - '+n)
                        if p > 2:
                            dxconff.discard(dx[184])
                            dxconff.discard(dx[190])
                        if p < 2:
                            dxconff.discard(dx[x])
                            dxconff.discard(dx[178])
                        else:
                            path.add(
                                'Cálculo de correção via Incoerência - '+n)
                            dxconff.discard(dx[184])
                            dxconff.discard(dx[190])
                            dxconff.discard(dx[x])
                            dxconff.discard(dx[178])
        n = 'F'
        x = 173
        a = e2a
        b = e2b
        c = e2c
        p = e3a
        if tn(x) == 0:
            path.add('Cálculo de correção via Coerência - '+n)
            if a > c:
                dxconff.discard(dx[175])
                dxconff.discard(dx[191])
            if a < c:
                dxconff.discard(dx[x])
                dxconff.discard(dx[179])
            else:
                path.add('Cálculo de correção via Codominância - '+n)
                if dx[171] in dxconff or dx[177] in dxconff:
                    dxconff.discard(dx[x])
                    dxconff.discard(dx[179])
                if dx[187] in dxconff or dx[181]:
                    dxconff.discard(dx[175])
                    dxconff.discard(dx[191])
                else:
                    path.add('Cálculo de correção via Ressonância - '+n)
                    if b > 2:
                        dxconff.discard(dx[175])
                        dxconff.discard(dx[191])
                    if b < 2:
                        dxconff.discard(dx[x])
                        dxconff.discard(dx[179])
                    else:
                        path.add(
                            'Cálculo de correção via Paternidade Yang - '+n)
                        if p > 2:
                            dxconff.discard(dx[175])
                            dxconff.discard(dx[191])
                        if p < 2:
                            dxconff.discard(dx[x])
                            dxconff.discard(dx[179])
                        else:
                            path.add(
                                'Cálculo de correção via Incoerência - '+n)
                            dxconff.discard(dx[175])
                            dxconff.discard(dx[191])
                            dxconff.discard(dx[x])
                            dxconff.discard(dx[179])

        # CÁLCULO DE FLEUMA-FOGO E FOGO POR ESTASE
        def fto4(a):
            b = int(a-54)
            c = int(a+40)
            d = int(a-168)
            e = int(a+46)
            if dx[a] in dxconff:
                if dx[b] in dxconff:
                    return dxconff.add(dx[c])
                    return path.add('Cálculo dedutivo de diagnóstico - fleuma/fogo/estase')
                if dx[d] in dxconff:
                    return dxconff.add(dx[e])
                    return path.add('Cálculo dedutivo de diagnóstico - fleuma/fogo/estase')

        def l(x): return fto4(int(x)) if dx[int(x)] in dxconff else None
        l(168)
        l(169)
        l(170)
        l(171)
        l(172)
        l(173)
        l(174)

        # -------------------------------------- TRANSCRIÇÃO PARA SINTOMAS DIAGNÓSTICOS
        # USO DE DIAGNÓSTICOS *** DXCONFF
        def z(a, b, c): return smt.add(a+' de '+b) if c > 2 else None
        x = 'DISTENSÃO ABDOMINAL/PLENITUDE '
        y = [65, 167, 59, 213, 101, 19, 13, 157, 55, 61, 1, 97, 115,
             209, 5, 61, 78, 79, 80, 81, 82, 83, 16, 13, 175, 168, 60]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'BOLUS FARÍNGEO '
        y = [60, 62, 65, 151]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'GOSTO AMARGO '
        y = [60, 168, 170, 170, 116, 173, 213]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'PIROSE/REFLUXO '
        y = [167, 61, 169, 115, 169]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'MELENA/HEMATOQUEZIA '
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'CONSTIPAÇÃO INTESTINAL '
        y = [175, 169, 171, 63, 123]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'PRURIDO ANAL '
        y = [209]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'HALITOSE '
        y = [169, 115, 169, 169, 181, 123]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'FLATULÊNCIA '
        y = [60, 144]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'DOR ANAL '
        y = [117, 171, 171, 171, 147]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'SÍNDROME CONSUPTIVA '
        y = [123]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'PALIDEZ '
        y = [55, 19, 1, 0]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'MIALGIA '
        y = [129, 99, 129, 171, 1, 0, 30, 31, 32, 33, 34, 35]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'OSTEOPENIA '
        y = [28]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'INSÔNIA '
        y = [168, 6, 0, 2, 170, 170, 116, 5, 11, 155, 5, 117, 171, 1, 5, 168]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'DEPRESSÃO '
        y = [144, 60, 65, 5, 1, 5]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'ATAXIA MOTORA (FRAQUEZA E FORMIGAMENTO DE MEMBROS) '
        y = [62, 5, 198, 199, 200, 201, 19, 13,
             157, 55, 19, 1, 19, 1, 5, 16, 187]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'IRRITABILIDADE '
        y = [114, 168, 214, 62, 65, 167, 173, 155, 167, 19, 115, 61, 63, 213]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'ANSIEDADE '
        y = [6, 0, 1, 0, 10]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'PARESTESIA '
        y = [5, 11, 198, 199, 200, 201, 155, 131, 198,
             199, 200, 201, 5, 131, 5, 0, 1, 5, 10, 11, 213]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'TIQUE '
        y = [198, 199, 200, 201, 155, 131, 198, 199, 200, 201, 5, 131]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'AGNOSIA GUSTATIVA '
        y = [115, 97, 19, 19]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'SONHOS LÚCIDOS '
        y = [168, 6, 2, 170, 170, 116, 173, 23]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'SINTOMAS DEPENDENTES DE ESTRESSE EMOCIONAL '
        y = [63]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'EJACULAÇÃO PRECOCE '
        y = [16, 64, 16, 13]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'INCONTINÊNCIA URINÁRIA '
        y = [64, 190]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'ESPERMA FRIO '
        y = [16, 13]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'TOSSE '
        y = [144, 170, 116, 9, 123, 129, 99, 129, 171, 129, 117, 171,
             117, 189, 117, 171, 228, 117, 147, 117, 18, 21, 19, 22, 10, 9]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'PIGARRO '
        y = [154, 16]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'SURDEZ '
        y = [173, 198, 199, 200, 201, 10, 178, 10, 10, 9]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'ESPIRROS/ CORIZA '
        y = [129, 99, 129, 171, 115, 169]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'DOR EM SEIOS NASAIS '
        y = [115, 169]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'EDEMA DE MEMBROS '
        y = [13, 157, 115, 97, 154, 16, 213]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'HEMATÚRIA/COLÚRIA '
        y = [168, 119, 213, 213, 212]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'CÂIMBRAS '
        y = [5, 198, 199, 200, 201, 5, 0]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'AVERSÃO A FRIO '
        y = [16, 13]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'HIPERTERMIA NOTURNA '
        y = [170, 9]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'DIAFORESE '
        y = [22, 178]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'POLIFAGIA '
        y = [169, 115, 169]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'OLHO SECO '
        y = [10, 11]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'PROLAPSOS (HÉRNIAS, CISTOCELE, PROLAPSO ANORETAL, UTERINO, HIATO DE ESÔFAGO) '
        y = [157]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'MASSAS ABDOMINAIS '
        y = [59]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'DOR TORÁCICA/ DOR EM OPRESSÃO NO PEITO'
        y = [54, 144, 60, 114, 168, 214, 170, 62, 56, 171, 117, 189, 147, 117]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'MÃOS FRIAS '
        y = [170, 144, 60, 12, 2, 62, 56, 101, 189,
             13, 157, 22, 181, 19, 186, 189, 147]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'COLELITÍASE '
        y = [213]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'MITTELSCHMERZ '
        y = [213]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'DISTENSÃO DAS MAMAS'
        y = [167]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'HIPOMENORRÉIA (POUCO FLUXO MENSTRUAL) '
        y = [5, 11, 1, 1, 0, 1, 5]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'OLIGOMENORRÉIA (INTERVALO GRANDE ENTRE AS MENSTRUAÇÕES >35D) '
        y = [11, 1, 0]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'PROLAPSO UTERINO '
        y = [64]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'MÁCULAS '
        y = [170, 167]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'PELE RESSECADA '
        y = [167, 11, 123, 228, 117]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'UNHA FRACA '
        y = [1, 5]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'SENSAÇÃO DE AUMENTO DO TAMANHO DO CORPO '
        y = [72, 73, 74, 75, 76, 77]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        x = 'DESEJO DE RECEBER MASSAGEM ABDOMINAL '
        y = [147]
        w = str([dx[i] for i in y if dx[i] in dxconff or dx[i] in dxconf])
        t = len(w)
        z(x, w, t)
        # SINTOMAS POR TIPO DE PULSO E LOCAL (IMPERADOR AMARELO)
        if 'C' in det_4:
            pool.add('DOR MUSCULAR POR PULSO DE CORAÇÃO EM RITMO SHU-RÁPIDO')
        if 'C' in det_3:
            pool.add('RISO INCOERENTE, FOBIA SOCIAL E RISCO DE HÉRNIAS POR PULSO DE CORAÇÃO EM RITMO CHI-LENTO')
        if 'C' in det_9:
            pool.add('SENSAÇÃO DE OBJETO EM GARGANTA POR PULSO DE CORAÇÃO EM RITMO CHANG-LONGO')
        if 'C' in det_15 or 'C' in det_14:
            pool.add('SÍNDROME DE DOR OBSTRUTIVA (BI) EM COSTAS POR PULSO DE CORAÇÃO EM RITMO XIAN-CORDA OU JIN-TENSO')
        if 'C' in det_12 or 'C' in det_10:
            pool.add('RISCO DE DIABETES, TENDÊNCIA A SOLUÇOS POR PULSO DE CORAÇÃO EM RITMO XI-FINO OU DUAN-CURTO')
        if 'C' in det_7:
            pool.add('TENDÊNCIA A SEDE POR PULSO DE CORAÇÃO EM RITMO HUA-DESLIZANTE') 
        if 'C' in det_27 or 'C' in det_28 or 'C' in det_22 or 'C' in det_25 or 'C' in det_26:
            pool.add('TENDÊNCIA A MUDEZ, CEFALÉIA E HEMORRAGIAS POR PULSO DE CORAÇÃO EM RITMO SAN-DISPERSO OU CU-PRECIPITADO OU JIE-NODOSO OU DAI-INTERMITENTE OU JI-ACELERADO') 
        if 'P' in det_15 or 'P' in det_14:
            pool.add('TENDÊNCIA A EPILEPSIA E ESQUIZOFRENIA, CANSAÇO EM COSTAS E LESÕES REPETIDAS EM NARINAS POR PULSO DE PULMÃO EM RITMO JIN-TENSO')
        if 'P' in det_3:
            pool.add('DOR ESCAPULAR E SUDORESE DIFUSA POR PULSO DE PULMÃO EM RITMO CHI-LENTO') 
        if 'P' in det_11:
            pool.add('DOR/INCHAÇO EM PERNAS/PÉ OU DOR EM COSTAS COM IRRITABILIDADE AO SOL POR PULSO DE PULMÃO EM RITMO HONG-TRANSBORDANTE') 
        if 'P' in det_12 or 'P' in det_10:
            pool.add('TENDÊNCIA A DIABETES OU DIARRÉIAS POR PULSO DE PULMÃO EM RITMO DUAN-CURTO')                                    
        if 'P' in det_7:
            pool.add('RESPIRAÇÃO RÁPIDA E REVERSÃO DE QI DE PULMÃO COM RISCOS DE HEMORRAGIAS POR PULSO DE PULMÃO EM RITMO HUA-DESLIZANTE') 
        if 'P' in det_27 or 'P' in det_28 or 'P' in det_22 or 'P' in det_25 or 'P' in det_26:
            pool.add('VÔMITOS COM SANGUE, ESCRÓFULA EM PESCOÇO OU AXILAS COM CÃIMBRAS POR PULSO DE PULMÃO EM RITMO SAN-DISPERSO OU CU-PRECIPITADO OU JIE-NODOSO OU DAI-INTERMITENTE OU JI-ACELERADO')
        if 'F' in det_14:
            pool.add('AGRESSIVIDADE E VOZ ALTA POR PULSO DE FÍGADO EM RITMO JIN-TENSO') 
        if 'F' in det_3:
            pool.add('VÔMITOS E DOR DISTENSIVA AO ALIMENTAR POR PULSO DE FÍGADO EM RITMO CHI-LENTO') 
        if 'F' in det_11:
            pool.add('CARBÚNCULO, VÔMITOS, EPISTAXE E DOR EM FLANCO DIREITO OU DOR GENITAL COM LESÃO FUNDA OU DOR EM RIM AO TOSSIR POR PULSO DE FÍGADO EM RITMO HONG-TRANSBORDANTE')
        if 'F' in det_9:
            pool.add('EXCESSO DE FOME E SEDE COM INCHAÇO MUSCULAR POR PULSO DE FÍGADO EM RITMO CHANG-LONGO') 
        if 'F' in det_7:
            pool.add(
                'INCHAÇO EM ESCROTO OU INCONTINÊNCIA URINÁRIA POR PULSO DE FÍGADO EM RITMO HUA-DESLIZANTE')
        if 'BP' in det_15 or 'BP' in det_14:
            pool.add(
                'TREMOR DE EXTREMIDADES OU VÔMITOS APÓS CORRER E TENDÊNCIA A DIARRÉIA COM ESPUMA POR PULSO DE BAÇO EM RITMO JIN-TENSO OU XIAN-CORDA')
        if 'BP' in det_3:
            pool.add('FRAQUEZA DE BRAÇOS E PERNAS COM TREMOR E FLACIDEZ POR PULSO DE BAÇO EM RITMO CHI-LENTO')
        if 'BP' in det_11:
            pool.add(
                'TENDÊNCIA A DESMAIOS (SÍNDROME PIQI) E RISCO DE TUMORES DEVIDO A ESTASE POR PULSO DE BAÇO EM RITMO HONG-TRANSBORDANTE')
        if 'BP' in det_10 or 'BP' in det_12:
            pool.add('INCHAÇOS MUSCULARES RECORRENTES POR PULSO DE BAÇO EM RITMO DUAN-CURTO OU XI-FINO')
        if 'BP' in det_7:
            pool.add('INCHAÇO E QUEIMAÇÃO GENITAL COM DOR ABDOMINAL POR PULSO DE BAÇO EM RITMO HUA-DESLIZANTE')
        if 'BP' in det_27 or 'BP' in det_28 or 'BP' in det_22 or 'BP' in det_25 or 'BP' in det_26:
            pool.add('ALTERAÇÃO GINECOLÓGICA E LESÕES OCULTAS ULCERADAS INTESTINAIS POR PULSO DE BAÇO EM RITMO SAN-DISPERSO OU CU-PRECIPITADO OU JIE-NODOSO OU DAI-INTERMITENTE OU JI-ACELERADO')
        if 'R' in det_14:
            pool.add('OSSOS FRACOS, PÉ FRIO E DURO, TENDÊNCIA A DELÍRIOS, RETENÇÃO FECAL E URINÁRIA POR PULSO DE RIM EM RITMO JIN-TENSO') 
        if 'R' in det_3:
            pool.add('DOR INTENSA EM COLUNA COM REFLUXO AOS ALIMENTOS POR PULSO DE RIM EM RITMO CHI-LENTO') 
        if 'R' in det_11:
            pool.add('TENDÊNCIA A IMPOTÊNCIA E HÉRNIAS ABDOMINAIS POR PULSO DE RIM EM RITMOHONG-TRANSBORDANTE')
        if 'R' in det_10 or 'R' in det_12:
            pool.add(
                'DIARRÉIA COM URGÊNCIA E TENDÊNCIA A DIABETES POR PULSO DE RIM EM RITMO DUAN-CURTO OU XI-FINO')
        if 'R' in det_7:
            pool.add(
                'DOR E EDEMA GENITAL, TENDÊNCIA A DESMAIO ORTOSTÁTICO (HIPOTENSÃO) POR PULSO DE RIM EM RITMO HUA-DESLIZANTE')
        if 'R' in det_27 or 'R' in det_28 or 'R' in det_22 or 'R' in det_25 or 'R' in det_26:
            pool.add('TENDÊNCIA A CARBÚNCULOS E HEMORRÓIDAS POR PULSO DE RIM EM RITMO SAN-DISPERSO OU CU-PRECIPITADO OU JIE-NODOSO OU DAI-INTERMITENTE OU JI-ACELERADO')
        if tipo_p[1] in pool:
            pool.add('FU - FLUTUANTE (PALPAÇÃO SUPERFICIAL QUE SOME AO APERTAR) DETERMINA VENTO EXTERNO OU DEFICIÊNCIA DE YIN')
        if tipo_p[2] in pool:
            pool.add('CHEN - PROFUNDO (PALPAÇÃO QUASE EM OSSO), SE PROFUNDO-FRACO (RUO) DETERMINA DEFICIÊNCIA DE QI E YANG, SE PROFUNDO-CHEIO (SHI) DETERMINA ESTASE QI E YANG OU FRIO/CALOR')
        if tipo_p[3] in pool:
            pool.add('CHI - LENTO (BRADICARDIA, <3BPM/IRPM DO EXAMINADOR), SE LENTO-FRACO (RUO) DETERMINA FRIO VAZIO, SE LENTO CHEIO (SHI) DETERMINA FRIO CHEIO')
        if tipo_p[4] in pool:
            pool.add('SHU - RÁPIDO (TAQUICARDIA, >5BPM/IRPM EXAMINADOR), SE RÁPIDO-FLUTUANTE (FU) DETERMINA CALOR VAZIO, SE RÁPIDO-CHEIO (SHI) DETERMINA CALOR CHEIO')
        if tipo_p[5] in pool:
            pool.add('XU - VAZIO (DIFICULDADE DE SENTIR, LARGURA AUMENTADA E MACIO) DETERMINA DEFICIÊNCIA DE QI')
        if tipo_p[6] in pool:
            pool.add('SHI - CHEIO (NORMAL)')
        if tipo_p[7] in pool:
            pool.add(
                'HUA - DESLIZANTE (ESCORREGA NOS DEDOS, MÓVEL) DETERMINANDO OU FLEUMA OU UMIDADE OU GRAVIDEZ')
        if tipo_p[8] in pool:
            pool.add('SE - ÁSPERO (CRESPO/ÁSPERO, COM DENTES DE SERRA) DETERMINA ESGOTAMENTO DE FLUIDOS (JIN YE) OU DEFICIÊNCIA DE XUE, SE SE-XIAN OU SE-JIE MUDA PARA ESTADO DE ESTASE DE XUE')
        if tipo_p[9] in pool:
            pool.add('CHANG - LONGO (AMPLA SENSIBILIDADE, BATEM ANTES DE APERTAR, TAMANHO VERTICAL/ALTURA COM MAIS PULSO) DETERMINA CALOR DE ALGUM TIPO')
        if tipo_p[10] in pool:
            pool.add('DUAN - CURTO (INVERSO DO CHANG, OCUPA ESPAÇO MENOR QUE O HABITUAL) DETERMINA DEFICIÊNCIA GRAVE DE QI (PIOR EM ESTÔMAGO)')
        if tipo_p[11] in pool:
            pool.add('HONG - TRANSBORDANTE (AUMENTO DE CALIBRE DO VASO, MAIS GROSSO, DERRAMADO, TAMANHO HORIZONTAL/LARGURA MAIOR), SE HONG-SHI DETERMINA CALOR CHEIO OU FEBRE, SE HONG-XU DETERMINA CALOR VAZIO, SE HONG-SHU DETERMINA FLEUMA-FOGO, SE HONG-SHU-SHI OU HONG-CU-SHI DETERMINA FOGO-CALOR CHEIO')
        if tipo_p[12] in pool:
            pool.add(
                'XI - FINO (MAIS FINO QUE O NORMAL) DETERMINA ANEMIA OU DEFICIÊNCIA DE XUE OU UMIDADE COM DEFICIÊNCIA GRAVE DE QI')
        if tipo_p[13] in pool:
            pool.add('WEI - MÍNIMO (SEMELHANTE AO XI, PORÉM MAIS FRÁGIL, FINO COMO UM CAPILAR) DETERMINA DEFICIÊNCIA GRAVE DE QI E DE XUE')
        if tipo_p[14] in pool:
            pool.add('JIN - TENSO (TORCIDO COMO UMA CORDA GROSSA), SE JIN-FU-SHI DETERMINA FRIO EXTERNO, SE JIN-SHI-CHEN DETERMINA FRIO CHEIO, SE JIN-FU-CHEN DETERMINA FRIO VAZIO OU DOR POR FRIO OU MESMO ASMA')
        if tipo_p[15] in pool:
            pool.add('XIAN - CORDA (MAIS FINO E MAIS TENSO QUE O JIN, FORÇA DA CORDA DE UM VIOLÃO) DETERMINA DOR OU FLEUMA OU DEFICIÊNCIA DE XUE DE FÍGADO, SE XIAN-SE OU XIAN-JIE DETERMINA OBSTRUÇÃO DE QI COM OBSTRUÇÃO DE XUE DE CORAÇÃO')
        if tipo_p[16] in pool:
            pool.add('HUAN - RETARDADO DETERMINA PULSO NORMAL AO REPOUSO.')
        if tipo_p[17] in pool:
            pool.add('KOU - OCO (SUPERFICIALMENTE SENTIDO, AO APERTAR, INTERMEDIARIAMENTE PARA DE SENTIR E, VOLTA A SENTIR AO APERTAR PROFUNDAMENTE) DETERMINA HEMORRAGIA, IMINÊNCIA DE RUPTURA DE HEMORRAGIA OU CHOQUE. MÃO E PÉ GELADO REALMENTE REFORÇAM A POSSIBILIDADE DE RISCO LETAL A DEPENDER DA DOENÇA.')
        if tipo_p[18] in pool:
            pool.add('GE - EM COURO (DURO, TENSO E ESTICADO, ABERTO, COMO O TAMBOR DE COURO SUPERFICIALMENTE, PARECE VAZIO AO APERTAR (MAIOR VAZÃO) DETERMINA DEFICIÊNCIA DE YUAN QI, DEFICIÊNCIA GRAVE DE YIN DO RIM, BAIXA MING MEI (ANALISAR FACE)')
        if tipo_p[19] in pool:
            pool.add('LAO - FIRME (SENTIDO APENAS PROFUNDAMENTE, ROBUSTO, DURO, CHEIO MESMO APERTADO COM FORÇA, SE JIN-CHANG DETERMINA ESTASE XUE, SE LAO-CHI DETERMINA FRIO INTERNO OU DOR')
        if tipo_p[20] in pool:
            pool.add('RU - ENCHARCADO (SEMELHANTE AO FU, PORÉM MACIO, MAIS ELÁSTICO QUE O HABITUAL E NÃO TOTALMENTE DEIXADO DE SENTIR AO APERTAR) DETERMINA DEFICIÊNCIA DE QI E UMIDADE OU DEFICIÊNCIA DE YIN COM DEFICIÊNCIA DO YING QI')
        if tipo_p[21] in pool:
            pool.add('RUO - FRACO (NÃO SE SENTE SUPERFICIALMENTE, PORÉM SENTIDO INTERMEDIARIAMENTE E PROFUNDAMENTE) DETERMINA DEFICIÊNCIA DE YANG OU DEFICIÊNCIA DE XUE')
        if tipo_p[22] in pool:
            pool.add('SAN - DISPERSO (VASO PEQUENO E SUPERFICIAL COM BATIMENTO EM PONTOS E NÃO INTEIRAMENTE, COMO SE TIVESSE QUEBRADO) DETERMINA DEFICIÊNCIA DE QI E DEFICIÊNCIA DE XUE TAMBÉM COM DEFICIÊNCIA DE QI DO RIM (CONDIÇÃO GRAVE E CRÔNICA)')
        if tipo_p[23] in pool:
            pool.add(
                'FUA - ESCORREGADIO (PROFUNDO E ADERIDO AO OSSO, SEM MOBILIDADE) DETERMINA DEFICIÊNCIA GRAVE DE YANG')
        if tipo_p[24] in pool:
            pool.add('DONG - MÓVEL (EM FORMA DE FEIJÃO (ANEURISMA) COM TREMOR AO BATIMENTO (SOPRO)) DETERMINA CHOQUE EMOCIONAL, DOR EXTREMA, OU ESTRESSE PÓS-TRAUMA')
        if tipo_p[25] in pool:
            pool.add('CU - PRECIPITADO (RÁPIDO E INTERROMPIDO EM INTERVALOS REGULARES, TAQUIARRITMIAS) DETERMINA CALOR EXTREMO OU DEFICIÊNCIA DE QI DO CORAÇÃO')
        if tipo_p[26] in pool:
            pool.add(
                'JIE - NODOSO (LENTO E INTERROMPIDO EM INTERVALOS REGULARES, BRADIARRITMIAS) DETERMINA FRIO VAZIO EM CORAÇÃO')
        if tipo_p[27] in pool:
            pool.add('DAI - INTERMITENTE (NORMOCÁRDICO, INTERROMPIDO EM INTERVALOS REGULARES) DETERMINA GRAVIDADE DE QI OU XUE EM 2 ÓRGÃOS YIN')
        if tipo_p[28] in pool:
            pool.add(
                'JI - ACELERADO (TAQUICARDIA COM GRANDE FORÇA) DETERMINA EXCESSO DE YANG COM FOGO EXAURINDO O YIN')
        # FIM DE SINTOMAS PULSO-LOCAL        
        dxconff.add(comfx)
        if dx[55] in dxconff:
            warn.add('Investigar tumor em estômago a depender de sintomas'.upper())

        # --------------------------------- ANÁLISE DE PADRÕES DE DOMINÂNCIA E CONTRA-DOMINÂNCIA E GERAÇÃO

        def ana(a, b, c, d, bn, cf, ba, desc2, desc, w):
            if dx[a] in dxconff or dx[b] in dxconff:
                if dx[c] in dxconff or dx[d] in dxconff:
                    x = dxconff.add(bn+' causando '+cf+' em '+ba)
                    y = smt.add(desc+' devido a '+desc2)
                    if w != False:
                        z = warn.add(w.upper())
                    else:
                        z = False
                else:
                    x = False
                    y = False
                    z = False
            else:
                x = False
                y = False
                z = False
            return x, y, z

        ana(173, 179, 181, 187, 'Fígado', 'frio', 'Baço', 'Dominância: madeira dominando terra',
            'infecção de pele, dor muscular, dor abdominal, irritabilidade, diarréia, anorexia, face verde'.upper(), 'Aumentar ingesta de alimentos salgados')
        ana(169, 175, 184, 190, 'Baço', 'frio', 'Rim', 'Dominância: terra dominando água',
            'inchaços, respiração curta, disúria/retenção, face amarela'.upper(), 'Aumentar ingesta de alimentos picantes')
        ana(178, 172, 180, 186, 'Rim', 'frio', 'Coração', 'Dominância: água dominando fogo',
            'edema de tornozelos, lombalgia, frio, vertigem, escarro fino, palpitações'.upper(), 'Aumentar ingesta de alimentos ácidos')
        ana(168, 174, 183, 189, 'Coração', 'frio', 'Pulmão', 'Dominância: fogo dominando metal',
            'diabetes, poliúria, tosse com escarro amarelo abundante, calor, rubor facial'.upper(), 'Aumentar ingesta de alimentos amargos')
        ana(171, 177, 191, 185, 'Pulmão', 'frio', 'Fígado', 'Dominância: metal dominando madeira',
            'fadiga, irritabilidade, distensão, tosse, face esbranquiçada'.upper(), 'Aumentar ingesta de alimentos doces')
        ana(191, 185, 171, 177, 'Fígado', 'calor', 'Pulmão', 'Contra-Dominância: madeira sustentando metal',
            'medo de situações leves, epistaxe, tosse, asma, distensão de tórax/hipocôndrio'.upper(), 'Evitar alimentos picantes')
        ana(183, 189, 168, 174, 'Pulmão', 'calor', 'Coração', 'Contra-Dominância: metal sustentando fogo',
            'criação de tumores abdominais, hemorróidas, palpitação, insônia, dispnéia'.upper(), 'Evitar alimentos amargos')
        ana(180, 186, 178, 172, 'Coração', 'calor', 'Rim', 'Contra-Dominância: fogo sustentando água',
            'rubor malar, secura noturna (bucal), insônia, lombalgia, sudorese noturna'.upper(), 'Evitar alimentos salgados')
        ana(184, 190, 169, 175, 'Rim', 'calor', 'Baço', 'Contra-Dominância: água sustentando terra',
            'fezes mole, edema, fadiga, fraqueza de membros,risco de sangramentos intestinais incuráveis (pi de intestino)'.upper(), 'Evitar alimentos doces')
        ana(181, 187, 173, 179, 'Baço', 'calor', 'Fígado', 'Contra-Dominância: terra sustentando madeira',
            'polifagia, edema, icterícia, dor, distensão de hipocôndrio'.upper(), 'Evitar alimentos ácidos')

        def ger(a, b, c, d, desc2, desc):
            if dx[a] in dxconff or dx[b] in dxconff:
                if dx[c] in dxconff or dx[d] in dxconff:
                    y = smt.add(desc+' devido a '+desc2)
                else:
                    y = False
            else:
                y = False
            return y

        ger(182, 188, 181, 187, 'Não-Geração: fogo não gerando terra',
            'fezes moles, calafrios, fraqueza de membros'.upper())
        ger(182, 188, 184, 190, 'Não-Geração: terra não gerando metal',
            'fleuma em tórax (muco), tosse e fadiga'.upper())
        ger(184, 190, 185, 191, 'Não-Geração: metal não gerando água',
            'borborismos, fezes secas e paradas, tosse, dispnéia, disfonia, asma'.upper())
        ger(185, 191, 186, 192, 'Não-Geração: água não gerando madeira',
            'vertigem, borramento visual, cefaléia'.upper())
        ger(186, 192, 181, 187, 'Não-Geração: madeira não gerando fogo',
            'TOC, timidez, covardia, indecisão, palpitações e insônia matinal'.upper())

        def ger2(a, c, d, desc2, desc):
            if dx[a] in dxconff:
                if dx[c] in dxconff or dx[d] in dxconff:
                    y = smt.add(desc+' devido a '+desc2)
                else:
                    y = False
            else:
                y = False
            return y

        ger2(169, 174, 180, 'Calor de Geração: madeira queimando fogo',
             'excesso de temperatura de corpo, retenção fecal, aftas, risco de gravidade em doenças leves com fatalidades'.upper())
        ger2(172, 169, 175, 'Calor de Geração: fogo queimando metal',
             'possibilidade de doenças neurológicas e convulsões'.upper())
        ger2(173, 172, 178, 'Calor de Geração: metal queimando água',
             'possibilidade de doenças neurológicas e convulsões'.upper())
        ger2(173, 29, 224, 'Calor de Geração: gong qi queimando água',
             'hematúria'.upper())
        ger2(170, 172, 178, 'Calor de Geração: terra queimando metal',
             'polifagia e edema'.upper())

        # -------------------------------------- CAPTAÇÃO DE ÍTEM TEXTUAL EM HDA
        def f(x, y): return dxconff.add(y) if x in hda else None
        f('FÍGADO', 'Detecção em wu xing - Fígado: Fígado')
        f('HEPÁTICO', 'Detecção em wu xing - Fígado: Hepático')
        f('CORAÇÃO', 'Detecção em wu xing - Coração: Coração')
        f('CARDÍACO', 'Detecção em wu xing - Coração: Cardíaco')
        f('BAÇO', 'Detecção em wu xing - Baço: Baço')
        f('ESPLÊNICO', 'Detecção em wu xing - Baço: Esplênico')
        f('PULMÃO', 'Detecção em wu xing - Pulmão: Pulmão')
        f('PULMÕES', 'Detecção em wu xing - Pulmão: Pulmões')
        f('PULMONAR', 'Detecção em wu xing - Pulmão: Pulmonar')
        f('RIM', 'Detecção em wu xing - Rim: Rim')
        f('RINS', 'Detecção em wu xing - Rim: Rins')
        f('RENAL', 'Detecção em wu xing - Rim: Renal')
        f('AZUL', 'Detecção em wu xing - Fígado: Azul')
        f('VERDE', 'Detecção em wu xing - Fígado: Verde')
        f('VERMELHO', 'Detecção em wu xing - Coração: Vermelho')
        f('AMARELO', 'Detecção em wu xing - Baço: Amarelo')
        f('BRANCO', 'Detecção em wu xing - Pulmão: Branco')
        f('CLARO', 'Detecção em wu xing - Pulmão: Claro')
        f('PRETO', 'Detecção em wu xing - Rim: Preto')
        f('ESCURO', 'Detecção em wu xing - Rim: Escuro')
        f('NEGRO', 'Detecção em wu xing - Rim: Negro')
        f('ÁCIDO', 'Detecção em wu xing - Fígado: Ácido')
        f('AMARGO', 'Detecção em wu xing - Coração: Amargo')
        f('DOCE', 'Detecção em wu xing - Baço: Doce')
        f('PICANTE', 'Detecção em wu xing - Pulmão: Picante')
        f('PIMENTA', 'Detecção em wu xing - Pulmão: Pimenta')
        f('SALGADO', 'Detecção em wu xing - Rim: Salgado')
        f('NEFROLITÍASE', 'Detecção em wu xing - Rim: Nefrolitíase')
        f('VESÍCULA', 'Detecção em wu xing - Fígado: Vesícula')
        f('COLE', 'Detecção em wu xing - Fígado: prefixo cole')
        f('INTESTINO DELGADO', 'Detecção em wu xing - Coração: Intestino Delgado')
        f('INTESTINO GROSSO', 'Detecção em wu xing - Pulmão: Intestino Grosso')
        f('CONSTIPAÇÃO', 'Detecção em wu xing - Pulmão: Constipação')
        f('ESTÔMAGO', 'Detecção em wu xing - Baço: Estômago')
        f('GASTRITE', 'Detecção em wu xing - Baço: Gastrite')
        f('GÁSTRICO', 'Detecção em wu xing - Baço: Gástrico')
        f('BEXIGA', 'Detecção em wu xing - Rim: Bexiga')
        f('URINA', 'Detecção em wu xing - Rim: Urina')
        f('URINÁRIO', 'Detecção em wu xing - Rim: Urinário')
        f('URINÁRIA', 'Detecção em wu xing - Rim: Urinária')
        f('CISTITE', 'Detecção em wu xing - Rim: Cistite')
        f('OLHO', 'Detecção em wu xing - Fígado: Olho')
        f('OCULAR', 'Detecção em wu xing - Fígado: Ocular')
        f('VISUAL', 'Detecção em wu xing - Fígado: Visual')
        f('LÍNGUA', 'Detecção em wu xing - Coração: Língua')
        f('FALA', 'Detecção em wu xing - Coração: Fala')
        f('MUTISMO', 'Detecção em wu xing - Coração: Mutismo')
        f('AFASIA', 'Detecção em wu xing - Coração: Afasia')
        f('BOCA', 'Detecção em wu xing - Baço: Boca')
        f('GOSTO', 'Detecção em wu xing - Baço: Gosto')
        f('NARIZ', 'Detecção em wu xing - Pulmão: Nariz')
        f('CHEIRO', 'Detecção em wu xing - Pulmão: Cheiro')
        f('ORELHA', 'Detecção em wu xing - Rim: Orelha')
        f('AUDIÇÃO', 'Detecção em wu xing - Rim: Audição')
        f('SURDEZ', 'Detecção em wu xing - Rim: Surdez')
        f('MÚSCULO', 'Detecção em wu xing - Fígado: Músculo')
        f('MUSCULAR', 'Detecção em wu xing - Fígado: Muscular')
        f('TEND', 'Detecção em wu xing - Fígado: prefixo Tend-')
        f('VASCULAR', 'Detecção em wu xing - Coração: Vascular')
        f('VARI', 'Detecção em wu xing - Coração: prefixo Vari')
        f('OBESIDADE', 'Detecção em wu xing - Baço: Obesidade')
        f('PESO', 'Detecção em wu xing - Baço: Peso')
        f('EDEMA', 'Detecção em wu xing - Baço: Edema')
        f('CUTÂNEO', 'Detecção em wu xing - Pulmão: Cutâneo')
        f('DERMAT', 'Detecção em wu xing - Pulmão: prefixo Dermat')
        f('CABELO', 'Detecção em wu xing - Rim: Cabelo')
        f('CAPILAR', 'Detecção em wu xing - Rim: Capilar')
        f('PELE', 'Detecção em wu xing - Pulmão: Pele')
        f('PÊLO', 'Detecção em wu xing - Pulmão: Pêlo')
        f('CALVÍCIE', 'Detecção em wu xing - Pulmão: Calvície')
        f('OSTEO', 'Detecção em wu xing - Rim: prefixo Osteo')
        f('OSSO', 'Detecção em wu xing - Rim: prefixo Osso')
        f('RAIVA', 'Detecção em wu xing - Fígado: Raiva')
        f('IRRITA', 'Detecção em wu xing - Fígado: prefixo Irrita')
        f('AGRESS', 'Detecção em wu xing - Fígado: prefixo Agress')
        f('ALEGRIA', 'Detecção em wu xing - Coração: Alegria')
        f('BIPOLAR', 'Detecção em wu xing - Coração: Bipolar')
        f('CONVERSA', 'Detecção em wu xing - Coração: Conversa')
        f('PENSAMENTO', 'Detecção em wu xing - Baço: Pensamento')
        f('REFLEX', 'Detecção em wu xing - Baço: prefixo Reflex')
        f('ESQUECIMENTO', 'Detecção em wu xing - Coração: Esquecimento')
        f('DEMÊNCIA', 'Detecção em wu xing - Coração: Demência')
        f('DEMENC', 'Detecção em wu xing - Coração: prefixo Demenc')
        f('PREOCUPA', 'Detecção em wu xing - Baço: prefixo Preocupa')
        f('TRISTEZA', 'Detecção em wu xing - Pulmão: Tristeza')
        f('DEPRESS', 'Detecção em wu xing - Pulmão: prefixo Depress')
        f('MEDO', 'Detecção em wu xing - Rim: Medo')
        f('TEMOR', 'Detecção em wu xing - Rim: Temor')
        f('INCHAÇO', 'Detecção em wu xing - Baço: Inchaço')
        f('NEURO', 'Detecção em wu xing - Fígado: prefixo Neuro')
        f('CALOR', 'Detecção em wu xing - Coração: Calor')
        f('SEC', 'Detecção em wu xing - Pulmão: prefixo Sec')
        f('FRIO', 'Detecção em wu xing - Rim: Frio')
        f('GENIT', 'Detecção em wu xing - Fígado: prefixo Genit')
        f('CISTITE', 'Detecção em wu xing - Rim: prefixo Cistite')
        f('COSTAS', 'Detecção em wu xing - Rim: Costas')
        f('DORSAL', 'Detecção em wu xing - Rim: Dorsal')
        f('COLUNA', 'Detecção em wu xing - Rim: Coluna')
        f('CERVICAL', 'Detecção em wu xing - Rim: Cervical')
        f('LOMBAR', 'Detecção em wu xing - Rim: Lombar')
        # -------------------------------------- CRIAÇÃO DE ARQUIVO PDF COM NOME DO PACIENTE
        '''
        pdf = canvas.Canvas(str(nome+'-'+horadia+'.pdf'),pagesize=A4)
        def m2p(x):
            return x/0.352777
        # INICIAL CANTO SUPERIOR DIREITO - pdf.drawString(m2p(7),m2p(290 -4),x)
        pdf.drawString(m2p(7),m2p(290),str('TAO | COPYRIGHT 2023 RODRIGO DIAS - VERSÃO '+ver))
        pdf.drawString(m2p(7),m2p(286),str(shu('')))
        pdf.drawString(m2p(7),m2p(282),str('ACUPUNTURA MÉDICA PARA: '+nome+' EM '+horadia))
        # pdf.save() finaliza arquivo
        # pdf.drawString(0,0,'texto') iniciando em canto inferior esquerdo - A3 = 210,297 (mm)

        '''

        # -------------------------------------- APRESENTAÇÃO DE RESULTADOS
        if len(dxconff) < 1:
            dxconff.add('Não encontrado distúrbios neste exame')
        ministerial = {item for item in dxconff if 'Triplo Aquecedor' in item and not 'Xie' in item and not 'Padrão' in item}
        imperial = {item for item in dxconff if 'Coração' in item and not 'Xie' in item and n and not 'Xie' in item and not 'Padrão' in item}
        terra = {item for item in dxconff if 'Baço' in item and not 'Xie' in item and n and not 'Xie' in item and not 'Padrão' in item}
        metal = {item for item in dxconff if 'Pulmão' in item and not 'Xie' in item and not 'Padrão' in item}
        agua = {item for item in dxconff if 'Rim' in item and not 'Xie' in item and not 'Padrão' in item}
        madeira = {item for item in dxconff if 'Fígado' in item and not 'Xie' in item and not 'Padrão' in item}
        if len(ministerial) > 0:
            print('• FOGO MINISTERIAL:')
            for i, j in enumerate(list(ministerial), start=1):
                print(i, j)
        else:
            print('• FOGO MINISTERIAL:\nNormal')
        if len(imperial) > 0:
            print('• FOGO IMPERIAL:')
            for i, j in enumerate(list(imperial), start=1):
                print(i, j)
        else:
            print('• FOGO IMPERIAL:\nNormal')
        if len(terra) > 0:
            print('• TERRA:')
            for i, j in enumerate(list(terra), start=1):
                print(i, j)
        else:
            print('• TERRA:\nNormal')
        if len(metal) > 0:
            print('• METAL:')
            for i, j in enumerate(list(metal), start=1):
                print(i, j)
        else:
            print('• METAL:\nNormal')
        if len(agua) > 0:
            print('• ÁGUA:')
            for i, j in enumerate(list(agua), start=1):
                print(i, j)
        else:
            print('• ÁGUA:\nNormal')
        if len(madeira) > 0:
            print('• MADEIRA:')
            for i, j in enumerate(list(madeira), start=1):
                print(i, j)
        else:
            print('• MADEIRA:\nNomal')
        dxe = set(dxconff)
        unioesp = ministerial | imperial | terra | metal | agua | madeira
        '''
        pdf.drawString(m2p(7),m2p(278),str(unioesp))
        pdf.save()
        '''
        global excluesp
        excluesp = dxe-unioesp
        if len(excluesp) > 0:
            print('• NÃO-MERIDIONAIS:')
            for i, j in enumerate(list(excluesp), start=1):
                print(i, j)
        print('\nOBSERVAÇÕES CAUTELARES NO EXAME DE '+nome+':')
        if len(warn) < 1:
            warn.add('Sem detecção de gravidades'.upper())
        for i, j in enumerate(list(warn), 
                              start=1):
            print(i, j)
        print('\nSENSAÇÃO TÉRMICA COMPATÍVEL COM: ')
        h3 = {i.capitalize() for i in h3}
        for i, j in enumerate(list(h3), start=1):
            print(i, j)
        print('\nDOR COMPATÍVEL COM: ')
        h8 = {i.capitalize() for i in h8}
        for i, j in enumerate(list(h8), start=1):
            print(i, j)
        global reporth
        reporth= h3 | h8
        print('\nANÁLISE DE LÍNGUA EM '+nome+':')
        if len(prepdif) < 1:
            pool2.add('Não encontrado distúrbios neste exame')
        prepdif = {i.capitalize() for i in prepdif}
        for i, j in enumerate(list(prepdif), start=1):
            print(i, j)
        print('\nSENDO ACHADOS COMO ALTERADOS:')
        for i, j in enumerate(list(pureli), start=1):
            print(i, j)            
        print('\nSINTOMAS DE SÍNDROME ASSOCIADOS AO QUADRO DE '+nome+':')
        if len(smt) >= 1:
            for i, j in enumerate(list(smt), start=1):
                print(i, j)
        if len(pool) >= 1:
            print('\nPULSOLOGIA DE '+nome+':')
            for i, j in enumerate(list(pool), start=1):
                print(i, j)
        print('\nPULSOLOGIA DA ANÁLISE:')
        def yt(x):
            if int(x)==1:
                return 'INSUFICIENTE'
            if int(x)==2:
                return 'NORMAL'            
            if int(x)==3:
                return 'EXTREMO'
        pul=[
            {'ANÁLISE':'METAL','YANG':yt(d1a),'XUE':yt(d1b),'YIN':yt(d1c)},
            {'ANÁLISE':'TERRA','YANG':yt(d2a),'XUE':yt(d2b),'YIN':yt(d2c)},
            {'ANÁLISE':'FOGO MINISTERIAL','YANG':yt(d3a),'XUE':yt(d3b),'YIN':yt(d3c)},
            {'ANÁLISE':'FOGO IMPERIAL','YANG':yt(e1a),'XUE':yt(e1b),'YIN':yt(e1c)},
            {'ANÁLISE':'MADEIRA','YANG':yt(e2a),'XUE':yt(e2b),'YIN':yt(e2c)},
            {'ANÁLISE':'ÁGUA','YANG':yt(e3a),'XUE':yt(e3b),'YIN':yt(e3c)},
        ]
        pul2=[
            {'ANÁLISE':'SANJIAO SUPERIOR','ESTADO':yt(d1c)},
            {'ANÁLISE':'SANJIAO MÉDIO','ESTADO':yt(d2c)},
            {'ANÁLISE':'SANJIAO INFERIOR','ESTADO':yt(d3c)},
            {'ANÁLISE':'WEI QI','ESTADO':yt(d1a)},
            {'ANÁLISE':'ZHONG QI','ESTADO':yt(d1b)},
            {'ANÁLISE':'YING QI','ESTADO':yt(d2c)},
            {'ANÁLISE':'XUE','ESTADO':yt(d3c)},

        ]        
        global tabela
        tabela=pd.DataFrame(pul)
        print(tabela)
        print()
        global tabela2
        tabela2=pd.DataFrame(pul2)
        print(tabela2)
        global totpul
        totpul=str(d1a)+str(d1b)+str(d1c)+'|'+str(d2a)+str(d2b)+str(d2c)+'|'+str(d3a)+str(d3b)+str(d3c)+'|'+str(e1a)+str(e1b)+str(e1c)+'|'+str(e2a)+str(e2b)+str(e2c)+'|'+str(e3a)+str(e3b)+str(e3c)

        '''       
        PASSADO PARA LISTA PANDAS - MODELO APLICADO EM TABLE:
        print('D1A:'+str(d1a)+' D1B:'+str(d1b)+' D1C:'+str(d1c)+' >> PULMÃO/INTESTINO GROSSO\nD2A:'+str(d2a)+' D2B:'+str(d2b)+' D2C:'+str(d2c)+' >> BAÇO/ESTÔMAGO\nD3A:'+str(d3a)+' D3B:'+str(d3b)+' D3C:'+str(d3c)+' >> PERICÁRDIO/TRIPLO AQUECEDOR\nE1A:' +
              str(e1a)+' E1B:'+str(e1b)+' E1C:'+str(e1c)+' >> CORAÇÃO/INTESTINO DELGADO\nE2A:'+str(e2a)+' E2B:'+str(e2b)+' E2C:'+str(e2c)+' >> FÍGADO/VESÍCULA BILIAR\nE3A:'+str(e3a)+' E3B:'+str(e3b)+' E3C:'+str(d3c)+' >> RIM/BEXIGA')
        '''
        
        print('\nDIAGNÓSTICOS DESCARTADOS: ')
        global filtpct
        filtpct = pct-dxe
        for i, j in enumerate(list(filtpct), start=1):
            print(i, j)
        print('\nCÁLCULOS CORRETIVOS REALIZADOS:')
        if len(path) < 1:
            path.add('Não foi necessário correções.')
        for i, j in enumerate(list(path), start=1):
            print(i, j)
        while True:
            try:
                if len(coid)!=0:
                    for i in sorted(coid):
                        print(i)
                print()
                lemb = input('\n\nResumo de diagnósticos (digite FIM para sair): ').upper()
                if len(lemb)!=0:
                    if 'FIM' in lemb:
                        break
                    else:
                        coid.add(lemb)
                        continue
            except:
                continue
        while True:
            try:
                print()
                print()
                ques = input(
                    'Deseja seguir para prescrição do paciente? (S/N) ').upper()
                if ques == 'S':
                    only()
                if ques == 'N':
                    print()
                    zerar()
            except:
                continue

def anam():
    while True:
        try:
            if len(seta) < 1:
                metro()
            else:
                if homm=='A' and len(hda)>54:
                    break
                if idd>40:
                    qesp = input('Deseja prosseguir com questionário para pontos? (S/N) ').upper()
                    if qesp == 'N':
                        only()
                    elif qesp =='S':
                        break
                    else:
                        continue
                else:
                    only()
        except:
            continue

    while True:
        try:
            cls()
            print('\n\n')
            print('INICIANDO QUESTIONÁRIO DE SINTOMAS PARA RECOMENDAÇÃO DE PROTOCOLOS\n\n')
            qq1 = input(
                'Paciente tem sintomas/sinais neurológicos complexos ou psicossomáticos (psicológicos) importates? (S/N) ').upper()
            if qq1 == 'S':
                seta.add('Recomendado ponto janela')
                break
            if qq1 == 'N':
                break
        except:
            continue
    while True:
        try:
            qq2 = input('Paciente tem doenças graves e significativas necessitando de abordagem fracionada inicialmente e com seguimento posterior para mais pontos? (S/N) ').upper()
            if qq2 == 'S':
                seta.add('Recomendado ponto estrela')
                break
            if qq2 == 'N':
                break
        except:
            continue
    while True:
        try:
            qq3 = input(
                'Paciente tem comorbidade importante psiquiática com tratamento crônico e complexo? (S/N) ').upper()
            if qq3 == 'S':
                seta.add('Recomendado avaliar Su Si Miao')
                break
            if qq3 == 'N':
                break
        except:
            continue
    while True:
        try:
            qq4 = input(
                'Existe problema oftálmico crônico justificando tratar parte oftálmica via acupuntura? (S/N) ').upper()
            if qq4 == 'S':
                seta.add('Sugerido usar Mu Xu para Olhos')
                break
            if qq4 == 'N':
                break
        except:
            continue
    while True:
        try:
            qq5 = input(
                'Paciente adquiriu doença recentemente e ainda em tratamento? (S/N) ').upper()
            if qq5 == 'S':
                seta.add('Recomendado ponto mu para doença recente correlacionada')
                break
            if qq5 == 'N':
                break
        except:
            continue
    while True:
        try:
            qq6 = input('Possui paresia (paralisia)? (S/N) ').upper()
            if qq6 == 'S':
                seta.add('Usar ponto poço para meridiano com paresia')
                break
            if qq6 == 'N':
                break
        except:
            continue
    while True:
        try:
            qq7 = input(
                'Dor de frio (melhora com calor e piora se colocar gelo) ou artropatia (dor crônica em articulação)? (S/N) ').upper()
            if qq7 == 'S':
                seta.add('Usar ponto poço para meridiano com dor')
                break
            if qq7 == 'N':
                break
        except:
            continue
    while True:
        try:
            qq8 = input(
                'Pneumopatia (falta de ar) ou problema vocal crônico? (S/N) ').upper()
            if qq8 == 'S':
                seta.add('Avaliar usos de pontos rio')
                break
            if qq8 == 'N':
                break
        except:
            continue
    while True:
        try:
            qq9 = input(
                'Doenças crônicas de TGI (diarréia crônica, doença de intestinos) ou de pele recorrente? (S/N) ').upper()
            if qq9 == 'S':
                seta.add('Avaliar usos de pontos mar')
                break
            if qq9 == 'N':
                break
        except:
            continue
    while True:
        try:
            qq10 = int(input(
                'Alguma doença incurável ou muito séria na sua vida (correlação com qual meridiano)? (1C, 2BP, 3P, 4R, 5F ou 9 se não for o caso): '))
            if qq10 == 1:
                seta.add('Tonificar yuan de Coração')
                break
            if qq10 == 2:
                seta.add('Tonificar yuan de Baço')
                break
            if qq10 == 3:
                seta.add('Tonificar yuan de Pulmão')
                break
            if qq10 == 4:
                seta.add('Tonificar yuan de Rim')
                break
            if qq10 == 5:
                seta.add('Tonificar yuan de Fígado')
                break
            if qq10 == 9:
                break
        except:
            continue
    while True:
        try:
            qq11 = input(
                'Possui dor recorrente com nódulos de tensão ou tendinite de algum lugar? (S/N) ').upper()
            if qq11 == 'S':
                seta.add('Ver local de dor e analisar uso de Luo Mai')
                break
            if qq11 == 'N':
                break
        except:
            continue
    while True:
        try:
            qq12 = input(
                'Alguma cirurgia ou sangramentos decorrentes de doenças traumáticas ou hematológicas (mesmo que irrelevantes para serem tratadas)? (S/N) ').upper()
            if qq12 == 'S':
                seta.add('Uso de ponto Xi para hemorragia')
                break
            if qq12 == 'N':
                break
        except:
            continue
    qqhui = [i for i in seta if i.count('Estagnação') > 0]
    if qqhui == True:
        seta.add('Recomendado uso de ponto Hui')
    while True:
        try:
            qq17 = int(input('Tratar shen? (1)Hun [ID], (2)Xiang [sentimentos/distimia/shens multiplos baixos], (3)Yi [intelecto/cognição], (4)Po [empatia-aumentar/ideação-aumentar/alucinação-reduzir/fibromialgia-aumentar/coma-aumentar/alergia-reduzir/imunodeficiência-aumentar], (5)Zhi [resiliência/volemia] ou 9 para não: '))
            if qq17 == 9:
                break
            if qq17 == 4:
                qqa = input('Aumentar (+) ou Reduzir (-): ')
                if qqa == '+':
                    seta.add('Recomendado tratamento tonificado de Po')
                    break
                if qqa == '-':
                    seta.add('Recomendado tratamento sedado de Po')
                    break
                if qqa != '+' and qqa != '-':
                    print('Preste atenção. Informação inválida. Reiniciando...')
                    continue
            if qq17 == 1:
                qqaa = int(input('Mania(1) ou depressão(2)'))
                if qqaa == 1:
                    seta.add('Recomendado tratamento sedado de Hun')
                    break
                if qqaa == 2:
                    seta.add('Recomendado tratamento tonificado de Hun')
                    break
            if qq17 == 2:
                seta.add('Recomendado tratamento tonificado de Xiang')
                break
            if qq17 == 3:
                seta.add('Recomendado tratamento tonificado de Yi')
                break
            if qq17 == 5:
                seta.add('Recomendado tratamento tonificado de Zhi')
                break
        except:
            continue
    while True:
        try:
            if tipo_p[15] in pool:
                qq18 = input('Patologia de quadril ou genital? (S/N) ').upper()
                if qq18 == 'S':
                    seta.add('Recomendado tratamento via Dai Mai')
                    break
                if qq18 == 'N':
                    break
            else:
                break
        except:
            continue
    while True:
        try:
            qq19 = input('Insônia(I) ou Hiperssonia(H)? (N) ').upper()
            if qq19 == 'I':
                q20 = input(
                    'Sente-se mais introspectivo ou com ruminância de pensamento? Se homem apresenta recentemente impotência sexual? (S/N) ').upper()
                if q20 == 'S':
                    seta.add(
                        'Recomendado sedação de yang qiao e tonificar yin qiao')
                    break
                else:
                    break
            if qq19 == 'H':
                qq21 = input(
                    'Ocorre incômodo de uma mão ou pé com temperatura mais fria ou mais quente que a outra? (S/N) ').upper()
                if qq21 == 'S':
                    seta.add(
                        'Recomendado sedação de yin qiao e tonificar yang qiao')
                    break
                else:
                    break
            else:
                break
        except:
            continue
    if tipo_p[19] in pool:
        seta.add('Avaliar uso de Chong Mai (VP)')
    if tipo_p[1] and tipo_p[9] in pool:
        seta.add('Avaliar uso de Du Mai (VG)')
    while True:
        try:
            qq22 = input('Dispnéia crônica? (S/N) ').upper()
            if qq22 == 'N':
                break
            if qq22 == 'S':
                qq23 = int(
                    input('Congestão de tórax ou bronquite crônica- 1, Taquipnéia recorrente com afonia ou DPOC- 2, ou nenhuma associação (9)?'))
                if qq23 == 1:
                    seta.add('Excesso de Mar de Qi')
                    break
                if qq23 == 2:
                    seta.add('Deficiência de Mar de Qi')
                    break
                if qq23 == 9:
                    break
        except:
            continue
    while True:
        try:
            qq24 = int(input(
                'Sensação de aumento de corpo (1) ou redução de corpo (2) ao ir deitar? (9-não)'))
            if qq24 == 1:
                seta.add('Excesso de Mar de Xue')
                break
            if qq24 == 2:
                seta.add('Deficiência de Mar de Xue')
                break
            if qq24 == 9:
                break
        except:
            continue
    while True:
        try:
            qq25 = int(
                input('Plenitude prandial recorrente (1) ou fome com anorexia(2) ou não(9)? '))
            if qq25 == 1:
                seta.add('Excesso de Mar de Gu')
                break
            if qq25 == 2:
                seta.add('Deficiência de Mar de Gu')
                break
            if qq25 == 9:
                break
        except:
            continue
    while True:
        try:
            qq26 = input(
                'Vertigem com associação de pré-síncope? (S/N) ').upper()
            if qq26 == 'S':
                seta.add('Deficiência de Mar de Xiang')
                print()
                only()
            if qq26 == 'N':
                print()
                only()
        except:
            continue

def metro():
    while True:
        try:
            for i, j in enumerate(dx):
                print(i, j)
            print()
            print('Adicionados: ')
            print()
            for i, j in enumerate(seta, start=1):
                print(i, j)
            print()
            if len(coid)!=0 and homm == 'A':
                print('RESUMO DE DIAGNÓSTICO:')
                for i in sorted(coid):
                    print(i)
            print()
            doc = input(
                '\n\nConforme lista, insira numeração(ções) referente(s) ao(s) diagnóstico(s):\n\nou, para finalizar digite FIM\nou, digite * para apagar tudo ou *+seleção para apagar parcialmente: ')
            print()
            if '*' in doc:
                seta.clear()
            if ' ' in doc:
                docm = doc.split(' ')
                tamanho = int(len(docm))
                for i in range(tamanho):
                    seta.add(dx[int(docm[i])])
                    dxcid.add(toic[int(docm[i])])
                print()
                continue
            elif doc == 'FIM' or doc == 'fim' or doc == 'Fim':
                if len(seta)!=0:
                    index=25/int(len(seta))
                    if index >=3 and index <4:
                        index=int(index)    
                    if index >= 6:
                        global p
                        p='+++' # gerar >6 prescrições
                        cls()
                        print('\n\n\n\nMÉTODO DE PRESCRIÇÃO SELECIONADO AUTOMATICAMENTE: PRESCRIÇÃO COMPLETA\nNESTE MÉTODO CADA DIAGNÓSTICO GERA, EM MÉDIA, 14 AGULHAS!\n\nESTA ESCOLHA É DEVIDO A POUCOS TRATAMENTOS SIMULTANEAMENTE')
                    elif index <=3:
                        p='+' #  gerar 1-2 prescrições
                        cls()
                        print('\n\n\n\nMÉTODO DE PRESCRIÇÃO SELECIONADO AUTOMATICAMENTE: PRESCRIÇÃO MÍNIMA\nNESTE MÉTODO CADA DIAGNÓSTICO GERA, EM MÉDIA, 2 AGULHAS!\n\nESTA ESCOLHA É DEVIDO A SELEÇÃO EXTENSA DE TRATAMENTOS')
                    else:
                        p='++' # gerar 4-5 prescrições
                        cls()
                        print('\n\n\n\nMÉTODO DE PRESCRIÇÃO SELECIONADO AUTOMATICAMENTE: PRESCRIÇÃO RESUMIDA\nNESTE MÉTODO CADA DIAGNÓSTICO GERA, EM MÉDIA, 8 AGULHAS!')
                    time.sleep(4)
                    cls()
                    '''
                    LIMITADOR DE QUANTIDADE DE PONTOS, SEM ESTA CONFIGURAÇÃO 
                    8 DIAGNÓSTICOS COM 7 PONTOS DE ACUPUNTURA BILATERAIS SOLICITAM 112 AGULHAS
                    APÓS ESTA, 8 DIAGNÓSTICOS GERA PRESCRIÇÃO COM 16 AGULHAS
                    VEJA ABAIXO TABELA DE LIMITADORES MATEMÁTICOS
                    QTS. DIAGNÓSTICO (SETA) || QTD. PONTOS ACUPUNTURA || (P)
                    1 seta = 7 prescrições (14 AGULHAS) (+++) PRESCRIÇÃO COMPLETA
                    2=14 (28 AGULHAS) (+++) PRESCRIÇÃO COMPLETA
                    3=21 (42 AGULHAS) (+++) PRESCRIÇÃO COMPLETA
                    4=28 (56 AGULHAS) (+++) PRESCRIÇÃO COMPLETA
                    5=22 (44 AGULHAS) (++) PRESCRIÇÃO RESUMIDA
                    6=27 (54 AGULHAS) (++) PRESCRIÇÃO RESUMIDA
                    7=31 (++) PRESCRIÇÃO RESUMIDA
                    8=8 (+) PRESCRIÇÃO MÍNIMA
                    9=9 (+) PRESCRIÇÃO MÍNIMA
                    10=10 (+) PRESCRIÇÃO MÍNIMA
                    .
                    .
                    .
                    15=15 (+) PRESCRIÇÃO MÍNIMA
                    16=16 (+)PRESCRIÇÃO MÍNIMA
                    .
                    .
                    .
                    47=47 (+) PRESCRIÇÃO MÍNIMA

                    # ##################################### ACIMA PRONTO                             

                    # +++   >6 prescrições
                    # ++    4 prescrições
                    # +     1 prescrição
                    
                    # G: SEDAÇÃO FRIA, H: SEDAÇÃO COM MOXA, W: TONIFICAÇÃO FRIA, X: TONIFICAÇÃO COM MOXA
                    # Z: NEUTRO, Y: VENTOSA, K: SANGRIA
                    # M: UNILATERAL DIREITA - SEDADO, A: UNILATERAL DIREITA - TONIFICADO
                    # N: UNILATERAL ESQUERDA - SEDADO, D: UNILATERAL ESQUERDA - TONIFICADO

                    # POÇO/NASCENTE= -VENTO -OBSTRUÇÃO (ESTASE)
                    # MANANCIAL= -CALOR - EXCESSO (CALOR CHEIO) (EXCESSO YANG)
                    # RIACHO= -FRIO (FRIO VAZIO) (DEF YANG)
                    # RIO= - SECURA (CALOR VAZIO) (DEF YIN) #
                    # MAR= -UMIDADE -DEFICIENCIA (FRIO CHEIO) (EXCESSO YIN)

                    # ##################################### ACIMA PRONTO                        
                    '''
                def sprap(x, y=' '):
                    if dx[0] in x:
                        if p=='+++':
                            a1 = 'GC7 GVC14 GVC15 GVC4 XB17 GB15 GB20'+y
                        elif p=='++':
                            a1 = 'GC7 GVC14 GVC15 GVC4'+y
                        elif p=='+':
                            a1 = 'GC7'+y
                    else:
                        a1 = ''
                    if dx[6] in x or dx[174] in x:
                        if p=='+++' or p=='+++':
                            a2 = 'GID2 GID5 GC5 GC8 GE39'+y
                        elif p=='+':
                            a2='GID5'+y
                    else:
                        a2 = ''
                    if dx[12] in x or dx[186] in x or dx[18] in x:
                        if p=='+++':
                            a3 = 'GVC6 GVB34 GF13 GE29 GE27 GBP6 GF3'+y
                        elif p=='++':
                            a3 = 'GVC6 GE29 GID3 GF3'+y
                        elif p=='+':
                            a3= 'GID3'+y
                    else:
                        a3 = ''
                    if dx[168] in x:
                        if p=='+++':
                            a4 = 'GID2 GID5 GC5 GC8 GE39'+y
                        elif p=='++':
                            a4 = 'GID2 GC5 GC8 GE39'+y
                        elif p=='+':  
                            a4 = 'GID2'+y                
                    else:
                        a4 = ''
                    if dx[180] in x:
                        if p=='+++':
                            a5 = 'GC5 XPC6 XB15 XVC17 XVC6 XVG14 GC3'+y
                        elif p=='++':
                            a5 = 'GC3 XPC6 XVC6 XVG14'+y
                        elif p=='+':
                            a5 = 'GC3'+y
                    else:
                        a5 = ''
                    def total_estases_qi(y):
                        n = 0
                        if dx[60] in y:
                            n += 1
                        if dx[61] in y:
                            n += 1
                        if dx[62] in y:
                            n += 1
                        if dx[63] in y:
                            n += 1
                        if dx[64] in y:
                            n += 1
                        if dx[65] in y:
                            n += 1
                        return n
                    est = total_estases_qi(x)
                    if int(est) > 1:
                        if p=='+++' or p=='++':
                            a6 = 'GVC6 GE36'+y
                        elif p=='+':
                            a6 = 'GVC6'+y
                    else:
                        a6 = ''                        

                    def total_estases_xue(y):
                        n = 0
                        if dx[54] in y:
                            n += 1
                        if dx[55] in y:
                            n += 1
                        if dx[56] in y:
                            n += 1
                        if dx[57] in y:
                            n += 1
                        if dx[58] in y:
                            n += 1
                        if dx[59] in y:
                            n += 1
                        return n
                    est = total_estases_xue(x)
                    if int(est) > 1:
                        if p=='+++':
                            a7 = 'GR14 GF3 GB16 GBP10 GB17 GVC3 GE28 GB39 GB22 GBP6'+y
                        elif p=='++':
                            a7 = 'GR14 GF3 GBP10 GVC3'+y
                        elif p=='+':
                            a7 = 'GF3'+y
                    else:
                        a7 = ''
                    if dx[107] in x or dx[143] in x or dx[173] in x and dx[59] in dxconff:
                        if p=='+++'or p=='++':
                            a8 = 'GF2 GBP10 GF3 GR2 GBP11'+y
                        elif p=='+':
                            a8='GF2'+y                        
                    else:
                        a8 = ''
                    if dx[253] in x in dxconff:
                        a9 = 'GID5 GC7 WB44'+y
                    else:
                        a9 = ''
                    if dx[61] in x:
                        if p=='+++':
                            b1 = 'WE36 WB6 WVC12 GVC10 GE34 GE21 GE19 GVG20'+y
                        elif p=='++':
                            b1 = 'WVC12 GE34 GE36 GVG20'+y
                        elif p=='+':
                            b1='GVC12'+y
                    else:
                        b1 = ''
                    if dx[55] in x:
                        if p=='+++':
                            b2 = 'WVC12 WE36 WBP10 WBP3 WBP6 WB20 XB17 GE34 GE21'+y
                        elif p=='++':
                            b2 = 'WBP10 SBP6 GE34'+y
                        elif p=='+':
                            b2='SBP10'+y
                    else:
                        b2 = ''
                    if dx[1] in x:
                        if p=='+++':
                            b3 = 'XVC12 XE36 WBP3 GBP1 GBP6 GBP10'+y
                        elif p=='++':
                            b3 = 'XVC12 XE36 WBP3 GBP6'+y
                        elif p=='+':
                            b3 = 'GBP6'+y
                    else:
                        b3=''
                    if dx[7] in x or dx[175] in x:
                        if p=='+++':
                            b4 = 'WVC12 XE36 WBP6 WBP3 GBP10'+y
                        elif p=='++':
                            b4 = 'WVC12 XE36 WBP3 GBP10'+y
                        elif p=='+':
                            b4 = 'WVC12'+y                        
                    else:
                        b4 = ''
                    if dx[13] in x or dx[187] in x or dx[19] in x:
                        if p=='+++':
                            b5 = 'XVC12 XE36 XBP3 XBP6 XB20 XB21 XBP9 XE28 XVC9 WP9'+y
                        elif p=='++':
                            b5 = 'XVC12 XE36 XBP3 WP9'+y
                        elif p=='+':
                            b5 = 'XE36'+y
                    else:
                        b5 = ''                        
                    if dx[169] in x:
                        if p=='+++':
                            b6 = 'GBP2 GBP6 GVG9 GIG11 WB20 GVB34 GVC9 GVC11 GE22 GE28'+y
                        if p=='++':
                            b6 = 'GBP2 GBP6 GVG9 GIG11'+y
                        if p=='+':    
                            b6='GBP2'+y
                    else:
                        b6 = ''
                    if dx[181] in x:
                        if p=='+++' or p=='++':
                            b7 = 'WVC12 WE36 XBP6 GBP9'+y
                        elif p=='+':
                            b7 = 'WE36'+y
                    else:
                        b7 = ''
                    if dx[229] in x:
                        if p=='+++':
                            b8 = 'GIG4 GIG11 GTA5 GVG14 GB12 YP11'+y
                        elif p=='++':
                            b8 = 'GIG4 GIG11 GTA5 GVG14'+y
                        elif p=='+':
                            b8 = 'GIG4'+y
                    else:
                        b8 = ''
                    if dx[230] in x:
                        if p=='+++':
                            b9 = 'GIG4 GIG11 GTA5 GVG14 GVG26 GB40 GPC9'+y
                        elif p=='++':
                            b9 = 'GIG4 GIG11 GTA5 GVG14'+y
                        elif p=='+':
                            b9 = 'GIG4'+y
                    else:
                        b9 = ''
                    # INICIA VENTO-CALOR                    
                    if dx[231] in x:
                        if p=='+++': #>6 prescrições
                            b10 = 'GIG4 GIG11 GBP8 GBP6 GVC12 GVC9'+y
                        elif p=='++': #4 prescrições
                            b10 = 'GIG4 GIG11 GBP8 GBP6'+y
                        elif p=='+': #1 prescrição
                            b10 = 'GIG4'+y
                    else:
                        b10 = ''                        
                    if dx[232] in x:
                        if p=='+++': #>6 prescrições
                            b11 = 'GIG4 GIG11 GTA5 GBP6 GP9 GVC12 GE36'+y
                        elif p=='++': #4 prescrições
                            b11 = 'GIG4 GIG11 GTA5 GBP6'+y
                        elif p=='+': #1 prescrição
                            b11 = 'GIG4'+y
                    else:
                        b11 = ''
                    if dx[233] in x:
                        if p=='+++': #>6 prescrições
                            b12 = 'GP5 GP10 GVG14 GIG11 GP1 GB13'+y
                        elif p=='++': #4 prescrições
                            b12 = 'GP5 GP10 GVG14 GIG113'+y
                        elif p=='+': #1 prescrição
                            b12 = 'GP10'+y
                    else:
                        b12 = ''
                    if dx[234] in x:
                        if p=='+++': #>6 prescrições
                            b13 = 'GE44 GE34 GE21 GE43 GIG11 GE25'+y
                        elif p=='++': #4 prescrições
                            b13 = 'GE44 GE34 GE21 GE43'+y
                        elif p=='+': #1 prescrição
                            b13 = 'GE44'+y
                    else:
                        b13 = ''
                    if dx[235] in x:
                        if p=='+++': #>6 prescrições
                            b14 = 'GIG11 GE25 GBP15 GE37 GE39'+y
                        elif p=='++': #4 prescrições
                            b14 = 'GIG11 GE25 GBP15 GE37'+y
                        elif p=='+': #1 prescrição
                            b14 = 'GIG11'+y
                    else:
                        b14 = ''
                    if dx[236] in x:
                        if p=='+++' or p=='++': #>=4 prescrições
                            b15 = 'GVB34 GVB43 GTA6 GTA5'+y
                        elif p=='+': #1 prescrição
                            b15 = 'GVB34'+y
                    else:
                        b15 = ''
                    if dx[237] in x:
                        if p=='+++': #>6 prescrições
                            b16 = 'GVC12 GBP9 GBP6 GVC9 GE36 GIG11 GB20 GB22'+y
                        elif p=='++': #4 prescrições
                            b16 = 'GVC12 GBP6 GVC9 GE36'+y
                        elif p=='+': #1 prescrição
                            b16 = 'GE44'+y
                    else:
                        b16 = ''
                    if dx[238] in x:
                        if p=='+++': #>6 prescrições
                            b17 = 'GPC9 GPC8 GC9 GR6 GEX73'+y
                        elif p=='++': #4 prescrições
                            b17 = 'GPC9 GPC8 GC9 GR6'+y
                        elif p=='+': #1 prescrição
                            b17 = 'GPC9'+y
                    else:
                        b17 = ''
                    if dx[239] in x:
                        if p=='+++': #>6 prescrições
                            b18 = 'GPC9 GPC3 GPC8 GC9 GR6 GIG11'+y
                        elif p=='++': #4 prescrições
                            b18 = 'GPC9 GPC3 GPC8 GC9'+y
                        elif p=='+': #1 prescrição
                            b18 = 'GPC9'+y
                    else:
                        b18 = ''
                    if dx[240] in x:
                        if p=='+++': #>6 prescrições
                            b19 = 'GB17 GBP10 GF5 GBP4 GIG11 GF2 GR6 GC9'+y
                        elif p=='++': #4 prescrições
                            b19 = 'GB17 GBP10 GF5 GBP4'+y
                        elif p=='+': #1 prescrição
                            b19 = 'GB17'+y
                    else:
                        b19 = ''
                    if dx[241] in x:
                        if p=='+++': #>6 prescrições
                            b20 = 'GBP10 GIG11 GF2 GR6 GC9 GF3 GVG16 GVG20 GID3 GB62'+y
                        elif p=='++': #4 prescrições
                            b20 = 'GBP10 GIG11 GF2 GR6'+y
                        elif p=='+': #1 prescrição
                            b20 = 'GBP10'+y
                    else:
                        b20 = ''
                    if dx[242] in x:
                        if p=='+++': #>6 prescrições
                            b21 = 'GF3 GVG16 GVB20 GID3 GB62 GF8 GR6 GR3 GBP6'+y
                        elif p=='++': #4 prescrições
                            b21 = 'GF3 GVG16 GVB20 GID3'+y
                        elif p=='+': #1 prescrição
                            b21 = 'GF3'+y
                    else:
                        b21 = ''
                    if dx[243] in x:
                        if p=='+++' or p=='++':
                            b22 = 'GE36 GR3 GBP6 GR6 GVC4'+y
                        elif p=='+': #1 prescrição
                            b22 = 'GE36'+y
                    else:
                        b22 = ''
                    if dx[244] in x:
                        if p=='+++' or p=='++':
                            b23 = 'GE36 GE43 GVC6 GVC4 GVC8'+y
                        elif p=='+': #1 prescrição
                            b23 = 'GE43'+y
                    else:
                        b23 = ''
                    if dx[245] in x:
                        if p=='+++': #>6 prescrições
                            b24 = 'GIG4 GIG11 GTA5 GVG14 YB12 GP11'+y
                        elif p=='++': #4 prescrições
                            b24 = 'GIG4 GIG11 GVG14 GP11'+y
                        elif p=='+': #1 prescrição
                            b24 = 'GIG4'+y
                    else:
                        b24 = ''
                    if dx[246] in x:
                        if p=='+++': #>6 prescrições
                            b25 = 'GP5 GP10 GP1 GIG11 GB13'+y
                        elif p=='++': #4 prescrições
                            b25 = 'GP10 GP1 GIG11 GB13'+y
                        elif p=='+': #1 prescrição
                            b25 = 'GP10'+y
                    else:
                        b25 = ''
                    if dx[247] in x:
                        if p=='+++': #>6 prescrições
                            b26 = 'GPC9 GPC3 GIG11 GPC8 GC9 GR6 GEX73'+y
                        elif p=='++': #4 prescrições
                            b26 = 'GPC9 GPC3 GIG11 GPC8'+y
                        elif p=='+': #1 prescrição
                            b26 = 'GPC9'+y
                    else:
                        b26 = ''
                    if dx[248] in x:
                        if p == '+++':  # >6 prescrições
                            b27 = 'GE44 GE34 GE21 GE43 GIG11 GE25'+y
                        elif p == '++':  # 4 prescrições
                            b27 = 'GE44 GE34 GE21 GE43'+y
                        elif p == '+':  # 1 prescrição
                            b27 = 'GE44'+y
                    else:
                        b27 = ''
                    if dx[249] in x:
                        if p=='+++': #>6 prescrições
                            b28 = 'GVC12 GBP9 GBP6 GVC9 GE36 GIG11 GB20 GB22'+y
                        elif p=='++': #4 prescrições
                            b28 = 'GBP9 GBP6 GVC9 GE36'+y
                        elif p=='+': #1 prescrição
                            b28 = 'GBP2'+y
                    else:
                        b28 = ''
                    if dx[250] in x:
                        if p=='+++': #>6 prescrições
                            b29 = 'GR2 GR3 GR6 GBP6 GIG11'+y
                        elif p=='++': #4 prescrições
                            b29 = 'GR2 GR3 GR6 GBP6'+y
                        elif p=='+': #1 prescrição
                            b29 = 'GR2'+y
                    else:
                        b29 = ''
                    if dx[251] in x:
                        if p=='+++': #>6 prescrições
                            b30 = 'GF2 GF3 GVB20 GVG16 GID3 GB62 GBP10 GIG11 GR6 GC9 GEX73 GB62'+y
                        elif p=='++': #4 prescrições
                            b30 = 'GF2 GF3 GVB20 GVG16'+y
                        elif p=='+': #1 prescrição
                            b30 = 'GF2'+y
                    else:
                        b30 = ''
                    if dx[252] in x:
                        if p == '+++':  # >6 prescrições
                            b31 = 'GF2 GF3 GVB20 GVG16 GID3 GB62 GR3 GR6 GBP6 GF8'+y
                        elif p == '++':  # 4 prescrições
                            b31 = 'GF2 GF3 GVB20 GVG16'+y
                        elif p == '+':  # 1 prescrição
                            b31 = 'GVG16'+y
                    else:
                        b31 = ''
                    # FIM VENTO-CALOR
                    if dx[254] in x:
                        if p=='+++': #>6 prescrições
                            b32 = 'WB49 WVC12 WE36 WB20 WB49 WBP3'+y
                        elif p=='++': #4 prescrições
                            b32 = 'WB49 WVC12 B20 WBP3'+y
                        elif p=='+': #1 prescrição
                            b32 = 'WB20'+y
                    else:
                        b32 = ''

                    def umidade(y):
                        n = 0
                        if dx[114] in y:
                            n += 1
                        if dx[115] in y:
                            n += 1
                        if dx[116] in y:
                            n += 1
                        if dx[117] in y:
                            n += 1
                        if dx[118] in y:
                            n += 1
                        if dx[119] in y:
                            n += 1
                        return n
                    est = umidade(x)
                    if int(est) > 1:
                        if p=='+++': #>6 prescrições
                            b33 = 'WVC12 WE36 WB20 WBP9 WBP6 GPC5 GE40 GBP3 WE40'+y
                        elif p=='++': #4 prescrições
                            b33 = 'WVC12 WE36 WB20 WBP9'+y
                        elif p=='+': #1 prescrição
                            b33 = 'WBP9'+y
                    else:
                        b33 = ''
                    # VENTO-FRIO
                    if dx[202] in x:
                        if p=='+++': #>6 prescrições
                            c1 = 'GVC3 GR14 GE28 GB39 GB22 GBP10 GF3 GBP6'+y
                        elif p=='++': #4 prescrições
                            c1 = 'GVC3 GR14 GE28 GB39'+y
                        elif p=='+': #1 prescrição
                            c1 = 'GVC3'+y
                    else:
                        c1 = ''
                    if dx[203] in x:
                        if p=='+++': #>6 prescrições
                            c2 = 'GIG11 GVG14 GPC3 GE44 GE25 GBP15 GE37 GBP6'+y
                        elif p=='++': #4 prescrições
                            c2 = 'GIG11 GVG14 GPC3 GE44'+y
                        elif p=='+': #1 prescrição
                            c2 = 'GIG11'+y
                    else:
                        c2 = ''
                    if dx[204] in x:
                        if p=='+++' or p=='++':
                            c3 = 'GTA5 GTA6 GVB41 GVG13'+y
                        elif p=='+': #1 prescrição
                            c3 = 'GTA5'+y
                    else:
                        c3 = ''
                    if dx[205] in x:
                        if p=='+++': #>6 prescrições
                            c4 = 'XVC12 XB20 XE36 XE25 XBP6'+y
                        elif p=='++': #4 prescrições
                            c4 = 'XVC12 XB20 XE36 XE25'+y
                        elif p=='+': #1 prescrição
                            c4 = 'XVC12'+y
                    else:
                        c4 = ''
                    if dx[206] in x:
                        if p=='+++': #>6 prescrições
                            c5 = 'GVC4 GVC6 GR3 GR6 GBP6'+y
                        elif p=='++': #4 prescrições
                            c5 = 'GVC4 GVC6 GR3 GR6'+y
                        elif p=='+': #1 prescrição
                            c5 = 'GVC4'+y
                    else:
                        c5 = ''
                    if dx[207] in x:
                        if p=='+++' or p=='++': #>6 prescrições
                            c6 = 'GF3 GIG4 GBP4 GPC6'+y
                        elif p=='+': #1 prescrição
                            c6 = 'GF3'+y
                    else:
                        c6 = ''     
                    # FIM DE VENTO-FRIO    
                    if dx[63] in x:
                        if p == '+++' or p == '++':  # >6 prescrições
                            c7 = 'GP7 WVC7 GB12 GB13'+y
                        elif p == '+':  # 1 prescrição
                            c7 = 'GP7'+y
                    else:
                        c7 = ''
                    if dx[57] in x:
                        if p=='+++': #>6 prescrições
                            c8 = 'GP7 GIG4 WVC6 WE25 WE36 WBP3'+y
                        elif p=='++': #4 prescrições
                            c8 = 'GP7 GIG4 WVC6 WE25'+y
                        elif p=='+': #1 prescrição
                            c8 = 'GP7'+y
                    else:
                        c8 = ''
                    if dx[3] in x:
                        if p=='+++': #>6 prescrições
                            c9 = 'WP9 WVC4 WR6 WBP6 WVC12 WE36'+y
                        elif p=='++': #4 prescrições
                            c9 = 'WP9 WVC4 WR6 WBP6'+y
                        elif p=='+': #1 prescrição
                            c9 = 'WP9'+y
                    else:
                        c9 = ''
                    if dx[9] in x or dx[177] in x:
                        if p=='+++': #>6 prescrições
                            c10 = 'GP10 GIG11 WP9 WVC17 WB43 WB13 WVG12 WR6'+y
                        elif p=='++': #4 prescrições
                            c10 = 'GP10 GIG11 WP9 WVC17'+y
                        elif p=='+': #1 prescrição
                            c10 = 'GP10'+y
                    else:
                        c10 = ''
                    if dx[15] in x or dx[189] in x or dx[21] in x:
                        if p=='+++': #>6 prescrições
                            c11 = 'WP9 GIG4 XVC6 XE25 WP9 XE36 XE37 XB20'+y
                        elif p=='++': #4 prescrições
                            c11 = 'WP9 GIG4 XVC6 XE25'+y
                        elif p=='+': #1 prescrição
                            c11 = 'WP9'+y
                    else:
                        c11 = ''
                    if dx[171] in x:
                        if p=='+++': #>6 prescrições
                            c12 = 'GP10 GP5 GIG11 WVC17 WP9 WE36 WP7 XVC6 XB13 XVG12'+y
                        elif p=='++': #4 prescrições
                            c12 = 'GP10 GP5 GIG11 WVC17'+y
                        elif p=='+': #1 prescrição
                            c12 = 'GP10'+y
                    else:
                        c12 = ''
                    if dx[183] in x:
                        if p == '+++':  # >6 prescrições
                            c13 = 'GIG3 GE25 GE36 GBP6 GF3 GE27'+y
                        elif p == '++':  # 4 prescrições
                            c13 = 'GIG3 GE25 GE36 GBP6'+y
                        elif p == '+':  # 1 prescrição
                            c13 = 'GIG3'+y
                    else:
                        c13 = ''
                    if dx[255] in x:
                        c14 = 'WB42 WP7'+y
                    else:
                        c14 = ''

                    def secura(y):
                        n = 0
                        if dx[120] in y:
                            n += 1
                        if dx[121] in y:
                            n += 1
                        if dx[122] in y:
                            n += 1
                        if dx[123] in y:
                            n += 1
                        if dx[124] in y:
                            n += 1
                        if dx[125] in y:
                            n += 1
                        return n
                    est = secura(x)
                    if int(est) > 1:
                        if p=='+++': #>6 prescrições
                            c15 = 'WVC12 WVC4 WP9 WP7 WR6 GVC12 GE36 GE40 GB13'+y
                        elif p=='++': #4 prescrições
                            c15 = 'WVC12 WVC4 WP9 WR6'+y
                        elif p=='+': #1 prescrição
                            c15 = 'WP9'+y
                    else:
                        c15 = ''

                    def yuan(y):
                        n = 0
                        if dx[24] in y:
                            n += 1
                        if dx[25] in y:
                            n += 1
                        if dx[26] in y:
                            n += 1
                        if dx[27] in y:
                            n += 1
                        if dx[28] in y:
                            n += 1
                        if dx[29] in y:
                            n += 1
                        return n
                    est = yuan(x)
                    if int(est) > 1:
                        if p=='+++': #>6 prescrições
                            d1 = 'WR3 WF3 WC7 WBP3 WP9 WVG4 WVC4 XVC7 XVC6 WVC5 XVC4'+y
                        elif p=='++': #4 prescrições
                            d1 = 'WR3 WF3 WC7 WBP3'+y
                        elif p=='+': #1 prescrição
                            d1 = 'WVG4'+y
                    else:
                        d1 = ''
                    if dx[64] in x:
                        if p=='+++': #>6 prescrições
                            d2 = 'WB23 WVG4 WR3 WB52 WVC4 WVC6 WVG20 WR13 WB32'+y
                        elif p=='++': #4 prescrições
                            d2 = 'WB23 WVG4 WR3 WB52'+y
                        elif p=='+': #1 prescrição
                            d2 = 'WB23'+y
                    else:
                        d2 = ''
                    if dx[58] in x:
                        if p=='+++' or p=='++': #4 prescrições
                            d3 = 'GVG4 GVC4 GVC5'+y
                        elif p=='+': #1 prescrição
                            d3 = 'GVC5'+y
                    else:
                        d3 = ''
                    if dx[4] in x:
                        if p=='+++': #>6 prescrições
                            d4 = 'WVC4 WVG4 WB23 WR3 WB11 WE37'+y
                        elif p=='++': #4 prescrições
                            d4 = 'WVC4 WVG4 WB23 WR3'+y
                        elif p=='+': #1 prescrição
                            d4 = 'WVC4'+y
                    else:
                        d4 = ''
                    if dx[10] in x or dx[178] in x:
                        if p=='+++': #>6 prescrições
                            d5 = 'WR3 WR7 WBP6 WR9 WR10 WVC4 WVC7 WP7'+y
                        elif p=='++': #4 prescrições
                            d5 = 'WR3 WR7 WBP6 WR9'+y
                        elif p=='+': #1 prescrição
                            d5 = 'WR9'+y
                    else:
                        d5 = ''
                    if dx[16] in x or dx[190] in x or dx[22] in x:
                        if p=='+++': #>6 prescrições
                            d6 = 'XR3 XB23 XVG4 XVC4 XVC6 XR7 XB52'+y
                        elif p=='++': #4 prescrições
                            d6 = 'XR3 XB23 XVG4 XVC4'+y
                        elif p=='+': #1 prescrição
                            d6 = 'XVC4'+y
                    else:
                        d6 = ''
                    if dx[172] in x:
                        if p=='+++': #>6 prescrições
                            d7 = 'GBP9 GR3 GB22 GB28 GVC3 GB63 GB60 GE28'+y
                        elif p=='++': #4 prescrições
                            d7 = 'GBP9 GR3 GB22 GB28'+y
                        elif p=='+': #1 prescrição
                            d7 = 'GR3'+y
                    else:
                        d7 = ''
                    if dx[184] in x:
                        if p=='+++': #>6 prescrições
                            d8 = 'WB23 WVG4 HBP9 HBP6 HB22 HE28 HVC3 HVC9'+y
                        elif p=='++': #4 prescrições
                            d8 = 'WB23 WVG4 HBP9 HBP6'+y
                        elif p=='+': #1 prescrição
                            d8 = 'WB23'+y
                    else:
                        d8 = ''
                    if dx[256] in x:
                        d9 = 'WB52 WE37'+y
                    else:
                        d9 = ''
                    if dx[65] in x:
                        if p == '+++':  # >6 prescrições
                            e1 = 'GP7 GF3 GVC17 GF2 GP5 GVB34 '+y
                        elif p == '++':  # 4 prescrições
                            e1 = 'GP7 GF3 GVC17 GF2'+y
                        elif p == '+':  # 1 prescrição
                            e1 = 'GP7'+y
                    else:
                        e1 = ''
                    if dx[59] in x:
                        if p == '+++':  # >6 prescrições
                            e2 = 'GF14 GVB34 GF3 GB18 GB17 GBP10 GBP6 GBP4 GPC6 GE29'+y
                        elif p == '++':  # 4 prescrições
                            e2 = 'GF14 GVB34 GF3 GB18'+y
                        elif p == '+':  # 1 prescrição
                            e2 = 'GF14'+y
                    else:
                        e2 = ''
                    if dx[5] in x:
                        if p == '+++':  # >6 prescrições
                            e3 = 'WE36 GF8 GBP6 WE36 WVC4 WB18'+y
                        elif p == '++':  # 4 prescrições
                            e3 = 'WE36 GF8 GBP6 WE36'+y
                        elif p == '+':  # 1 prescrição
                            e3 = 'WE36'+y
                    else:
                        e3 = ''
                    if dx[11] in x or dx[179] in x:
                        if p == '+++':  # >6 prescrições
                            e4 = 'GF2 GF8 GBP6 GE36 GVC4 GR6 GR3'+y
                        elif p == '++':  # 4 prescrições
                            e4 = 'GF2 GF4 GBP6 GE36'+y
                        elif p == '+':  # 1 prescrição
                            e4 = 'GF4'+y
                    else:
                        e4 = ''
                    if dx[17] in x or dx[191] in x or dx[23] in x:
                        if p == '+++':  # >6 prescrições
                            e5 = 'WVB40 WF8 WE36 WBP6 WVC4 WB18 WB47'+y
                        elif p == '++':  # 4 prescrições
                            e5 = 'WVB40 WF8 WE36 WBP6'+y
                        elif p == '+':  # 1 prescrição
                            e5 = 'WVB40'+y
                    else:
                        e5 = ''
                    if dx[173] in x:
                        if p == '+++':  # >6 prescrições
                            e6 = 'GF2 GF3 GVB20 GVB13 GIG11 GVB1 GVB9 GVB8 GVB6 GBP6 GF1'+y
                        elif p == '++':  # 4 prescrições
                            e6 = 'GF2 GF3 GVB20 GVB13'+y
                        elif p == '+':  # 1 prescrição
                            e6 = 'GF2'+y
                    else:
                        e6 = ''
                    if dx[185] in x:
                        if p == '+++':  # >6 prescrições
                            e7 = 'GVC3 GF8 GF1 GF3'+y
                        elif p == '++':  # 4 prescrições
                            e7 = 'GVC3 GF8 GF1'+y
                        elif p == '+':  # 1 prescrição
                            e7='GF8'+y
                    else:
                        e7 = ''
                    if dx[257] in x:
                        e8 = 'WB47 GF3'+y
                    else:
                        e8 = ''

                    def vento(y):
                        n = 0
                        if dx[126] in y:
                            n += 1
                        if dx[127] in y:
                            n += 1
                        if dx[128] in y:
                            n += 1
                        if dx[129] in y:
                            n += 1
                        if dx[130] in y:
                            n += 1
                        if dx[131] in y:
                            n += 1
                        return n
                    est = vento(x)
                    if int(est) > 1:
                        if p == '+++' or p=='++':  # >6 prescrições
                            e9 = 'GF3 GVG20 GIG4 GBP6'+y
                        elif p == '+':  # 1 prescrição
                            e9 = 'GF3'+y
                    else:
                        e9 = ''
                    if dx[258] in x:
                        if p == '+++' or p=='++':  # >6 prescrições
                            f1 = 'GIG11 GBP6 GPC8 GF2'+y
                        elif p == '+':  # 1 prescrição
                            f1 = 'GIG11'+y
                    else:
                        f1 = ''
                    if dx[14] in x or dx[20] in x or dx[182] in x or dx[188] in x:
                        if p == '+++' or p=='++':  # >6 prescrições
                            f2 = 'XVG4 XVC4 XR3'+y
                        elif p == '+':  # 1 prescrição
                            f2 = 'XVG4'+y
                    else:
                        f2 = ''
                    if dx[8] in x or dx[176] in x:
                        if p == '+++':  # >6 prescrições
                            f3 = 'GPC9 GPC8 GC9 WR6 GBP6'+y
                        elif p == '++':  # 4 prescrições
                            f3 = 'GPC9 GPC8 GC9 WR6'+y
                        elif p == '+':  # 1 prescrição
                            f3 = 'GPC9'+y
                    else:
                        f3 = ''
                    if dx[2] in x:
                        f4 = 'WPC3'+y
                    else:
                        f4 = ''
                    if dx[170] in x:
                        if p == '+++':  # >6 prescrições
                            f5 = 'WPC9 WPC8 WC9 WR6 WBP6'+y
                        elif p == '++':  # 4 prescrições
                            f5 = 'WPC9 WPC8 WC9 WR6'+y
                        elif p == '+':  # 1 prescrição
                            f5 = 'WPC9'+y
                    else:
                        f5 = ''
                    if dx[220] in x:
                        if sexo == 'M':
                            f6 = 'DVB41 MTA5 '
                        if sexo == 'F':
                            f6 = 'AVB41 NTA5 '
                    else:
                        f6 = ''
                    if dx[221] in x:
                        if sexo == 'M':
                            f7 = 'DBP4 MPC6 '
                        if sexo == 'F':
                            f7 = 'ABP4 NVC6 '
                    else:
                        f7 = ''
                    if dx[222] in x:
                        if sexo == 'M':
                            f8 = 'DID3 MB62 '
                        if sexo == 'F':
                            f8 = 'AID3 NB62 '
                    else:
                        f8 = ''
                    if dx[223] in x:
                        if sexo == 'M':
                            f9 = 'DP7 MR6 '
                        if sexo == 'F':
                            f9 = 'AP7 NR6 '
                    else:
                        f9 = ''
                    if dx[224] in x:
                        if sexo == 'M':
                            f10 = 'DB62 MID3 '
                        if sexo == 'F':
                            f10 = 'AB62 NID3 '
                    else:
                        f10 = ''
                    if dx[225] in x:
                        if sexo == 'M':
                            f11 = 'DR6 MP7 '
                        if sexo == 'F':
                            f11 = 'AR6 NP7 '
                    else:
                        f11 = ''
                    if dx[226] in x:
                        if sexo == 'M':
                            f12 = 'DTA5 MVB41 '
                        if sexo == 'F':
                            f12 = 'ATA5 NVB41 '
                    else:
                        f12 = ''
                    if dx[227] in x:
                        if sexo == 'M':
                            f13 = 'DPC6 MBP4 '
                        if sexo == 'F':
                            f13 = 'APC6 NBP4 '
                    else:
                        f13 = ''
                    if dx[228] in x:
                        if p == '+++':  # >6 prescrições
                            f14 = 'GPC5 WVC12 WE26 WB20 GE40 GVG26'+y
                        elif p == '++':  # 4 prescriçõesa
                            f14 = 'GPC5 WVC12 WE26 WB20'+y
                        elif p == '+':  # 1 prescrição
                            f14 = 'GPC5'+y
                    else:
                        f14 = ''
                    return a1+a2+a3+a4+a5+a6+a7+a8+b1+b2+b3+b4+b5+b6+b7+b8+b9+b10+b11+b12+b13+b14+b15+b16+b17+b18+b19+b20+b21+b22+b23+b24+b25+b26+b27+b28+b29+b30+b31+b32+b33+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+d1+d2+d3+d4+d5+d6+d7+d8+d9+e1+e2+e3+e4+e5+e6+e7+e8+e9+f1+f2+f3+f4+f5+f6+f7+f8+f9+f10+f11+f12+f13+f14
                protocolo = sprap(seta)
                if int(len(protocolo)) > 0:
                    p1 = protocolo.split(' ')
                    t1 = int(len(p1))
                    for i in range(t1):
                        pool3.add(p1[i])
                anam()
            else:
                docnum = int(doc)
                if docnum < 259:
                    seta.add(dx[docnum])
                    dxcid.add(toic[docnum])
                    continue
                else:
                    print('\nNUMERAÇÃO INCORRETA, TENTE NOVAMENTE!\n\n\n')
                    time.sleep(2)
                    continue
        except:
            cls()
            print()
            print()
            print()
            print('\n\n\n\n\n\n\nPOR FAVOR SIGA AS INSTRUÇÕES PARA CONTINUAR')
            time.sleep(2)
            continue
        else:
            cls()

def only():
    while True:
        try:
            if len(seta) < 1:
                metro()
            else:
                cls()
                print()
                print()
                print()
                print('===========================================================')
                print('PRESCRIÇÃO DE '+nome+':')
                shu(' ')
                print('\nMETA DE TRATAMENTO:')
                print(limpar(seta))
                if homm == 'A':
                    print('\nDIAGNÓSTICOS:')
                    print(dxconff)
                else:
                    pass
                if len(pool3) == 0:
                    print('NÃO HÁ PRESCRIÇÃO AINDA...')
                else:
                    if '' in pool3:
                        pool3.discard('')
                    if ' ' in pool3:
                        pool3.discard(' ')
                    # H J L O U - não estão em uso
                    print(
                        '\n___________________________________________________________')
                    print(f'\nPRESCRIÇÃO COMPLETA: {limpar(pool3)}.')
                    acu = [i[1:] for i in pool3]
                    global acu2
                    acu2 = sorted(acu)
                    for i, elemento in enumerate(acu2):
                        if elemento in acu2[i+1:]:
                            print(f'PRESCRIÇÃO REPETIDA EM ACUPONTO: {elemento}.')
                    print(
                        '___________________________________________________________\n\n')
                    p = [item for item in pool3 if 'P' in item[1]
                         and 'C' not in item[2]]
                    if len(p) != 0:
                        print('\nMERIDIANO DE FEI (PULMÃO):')
                        print(sorted(p))
                    ig = [item for item in pool3 if 'IG' in item[1:]]
                    if len(ig) != 0:
                        print('\nMERIDIANO DE DACHANG (INTESTINO GROSSO):')
                        print(sorted(ig))
                    bp = [item for item in pool3 if 'BP' in item[1:]]
                    if len(bp) != 0:
                        print('\nMERIDIANO DE PI (BAÇO):')
                        print(sorted(bp))
                    e = [item for item in pool3 if 'E' in item[1] and not 'X' in item[2]]
                    if len(e) != 0:
                        print('\nMERIDIANO DE WEI (ESTÔMAGO):')
                        print(sorted(e))
                    pc = [item for item in pool3 if 'PC' in item[1:]]
                    if len(pc) != 0:
                        print('\nMERIDIANO DE XINBAO (PERICÁRDIO):')
                        print(sorted(pc))
                    ta = [item for item in pool3 if 'TA' in item[1:]]
                    if len(ta) != 0:
                        print('\nMERIDIANO DE SANJIAO (TRIPLO AQUECEDOR):')
                        print(sorted(ta))
                    c = [item for item in pool3 if 'C' in item[1]]
                    if len(c) != 0:
                        print('\nMERIDIANO DE XIN (CORAÇÃO):')
                        print(sorted(c))
                    id = [item for item in pool3 if 'ID' in item[1:]]
                    if len(id) != 0:
                        print('\nMERIDIANO DE XIAOXANG (INTESTINO DELGADO):')
                        print(sorted(id))
                    f = [item for item in pool3 if 'F' in item[1:]]
                    if len(f) != 0:
                        print('\nMERIDIANO DE GAN (FÍGADO):')
                        print(sorted(f))
                    vb = [item for item in pool3 if 'VB' in item[1:]]
                    if len(vb) != 0:
                        print('\nMERIDIANO DE DAN (VESÍCULA BILIAR):')
                        print(sorted(vb))
                    r = [item for item in pool3 if 'R' in item[1:]]
                    if len(r) != 0:
                        print('\nMERIDIANO DE SHEN (RIM):')
                        print(sorted(r))
                    b = [item for item in pool3 if 'B' in item[1]
                         and not 'P' in item[2]]
                    if len(b) != 0:
                        print('\nMERIDIANO DE PANGGUAN (BEXIGA):')
                        print(sorted(b))
                    vc = [item for item in pool3 if 'VC' in item[1:]]
                    if len(vc) != 0:
                        print('\nMERIDIANO DE REN MAI (VASOCONCEPÇÃO):')
                        print(sorted(vc))
                    vg = [item for item in pool3 if 'VG' in item[1:]]
                    if len(vg) != 0:
                        print('\nMERIDIANO DE DU MAI (VASOGOVERNADOR):')
                        print(sorted(vg))
                    mox = [item for item in pool3 if 'H' in item]
                    mox2 = [item for item in pool3 if 'X' in item[0]]
                    if len(mox) != 0 or len(mox2) != 0:
                        print('\nPONTOS COM MOXA:')
                        if len(mox) != 0:
                            print(sorted(mox))
                        if len(mox2) != 0:
                            print(sorted(mox2))
                    neu = [item[1:] for item in pool3 if 'Z' in item]
                    if len(neu) != 0:
                        print('\nPONTOS NEUTROS:')
                        print(sorted(neu))
                    ven = [item[1:] for item in pool3 if 'Y' in item]
                    if len(ven) != 0:
                        print('\nPONTOS COM VENTOSA:')
                        print(sorted(ven))
                    san = [item[1:] for item in pool3 if 'K' in item]
                    if len(san) != 0:
                        print('\nPONTOS COM SANGRIA:')
                        print(sorted(san))
                    dir = [item for item in pool3 if 'M' in item[0]]
                    dir2 = [item for item in pool3 if 'A' in item[0]]
                    if len(dir) != 0 or len(dir2) != 0:
                        print('\nPONTOS UNILATERAIS DIREITA:')
                        if len(dir) != 0:
                            print(sorted(dir))
                        if len(dir2) != 0:
                            print(sorted(dir2))
                    esq = [item for item in pool3 if 'D' in item[0]]
                    esq2 = [item for item in pool3 if 'N' in item[0]]
                    if len(esq) != 0 or len(esq2) != 0:
                        print('\nPONTOS UNILATERAIS ESQUERDA:')
                        if len(esq) != 0:
                            print(sorted(esq))
                        if len(esq2) != 0:
                            print(sorted(esq2))
                    extra = [item for item in pool3 if 'E' in item[1] and 'X' in item[2]]
                    if len(extra) != 0:
                        print('\nPONTOS EXTRAMERIDIANOS:')
                        print(sorted(extra))
                        l=[i[1:] for i in extra]
                        l2={}
                        for i in l:
                            if i in locex:
                                l2.update({i: locex[i]})
                        print('\nLOCALIZAÇÃO ESPECIAL:')
                        for k,v in sorted(l2.items(), key=lambda x: x[1], reverse=True):
                            print(k,'- ',v)
                    u = [item[1:] for item in pool3 if 'GEX' in item or 'HEX' in item or 'WEX' in item or 'XEX' in item or 'YEX' in item or 'ZEX' in item or 'KEX' in item or 'MEX' in item or 'NEX' in item or 'AEX' in item or 'DEX' in item] # funcionando, seleciona os extras
                    v = [item[1:] for item in pool3] # funcionando, seleciona todos p set
                    u_setado=set(u)
                    v_setado=set(v)
                    c=v_setado.difference(u_setado) # teste, contagem de todos exceto extras
                    agu = 2*len(c)
                    agu_vc = len([item for item in pool3 if 'VC' in item])
                    if agu_vc != 0:
                        agu -= agu_vc
                    agu_vg = len([item for item in pool3 if 'VG' in item])
                    if agu_vg != 0:
                        agu -= agu_vg
                    if len(dir) != 0:
                        agu -= len(dir)
                    if len(esq) != 0:
                        agu -= len(esq)
                    if len(u) != 0:
                        agu_ext={'EX1':4,'EX2':2,'EX3':2,'EX4':1,'EX5':1,'EX6':1,'EX7':2,'EX8':2,'EX9':2,'EX10':2,'EX11':2,'EX12':2,'EX13':2,'EX14':2,'EX15':2,'EX16':2,'EX17':2,'EX18':2,'EX19':2,'EX20':2,'EX21':2,'EX22':2,'EX23':1,'EX24':2,'EX25':2,'EX26':2,'EX27':2,'EX28':1,'EX29':2,'EX30':2,'EX31':2,'EX32':2,'EX33':2,'EX34':2,'EX35':2,'EX36':5,'EX37':2,'EX38':2,'EX39':2,'EX40':2,'EX41':2,'EX42':2,'EX43':2,'EX44':2,'EX45':2,'EX46':2,'EX47':2,'EX48':2,'EX49':2,'EX50':2,'EX51':8,'EX52':2,'EX53':1,'EX54':2,'EX55':2,'EX56':2,'EX57':2,'EX58':2,'EX59':2,'EX60':2,'EX61':1,'EX62':2,'EX63':2,'EX64':2,'EX65':2,'EX66':2,'EX67':1,'EX68':2,'EX69':2,'EX70':34,'EX71':2,'EX72':1,'EX73':10,'EX74':2,'EX75':8,'EX76':2,'EX77':4,'EX78':2,'EX79':2,'EX80':2,'EX81':8,'EX82':4,'EX83':2,'EX84':4,'EX85':2,'EX86':4,'EX87':2,'EX88':2,'EX89':6,'EX90':2,'EX91':2,'EX92':2,'EX93':2,'EX94':2,'EX95':2,'EX96':8,'EX97':2,'EX98':2,'EX99':2,'EX100':2,'EX101':2,'EX102':2,'EX103':2,'EX104':2,'EX105':2,'EX106':2,'EX107':2,'EX108':2,'EX109':2,'EX110':2,'EX111':2,'EX112':2,'EX113':2,'EX114':2,'EX115':2,'EX116':2,'EX117':2,'EX118':2,'EX119':2,'EX120':2,'EX121':2,'EX122':2,'EX123':2,'EX124':2,'EX125':2,'EX126':2,'EX127':2}
                        for i in u:
                            if i in agu_ext:
                                agu+=agu_ext[i]
                    print(f'\n\nTOTAL DE PONTOS: {len(pool3)}.')
                    print(f'TOTAL DE AGULHAS: {agu}.')
                    a = agu/10
                    print(f'TOTAL DE PACOTES: {round(a+0.5)}.')
                    bk1 = {item for item in pool3 if 'ID9' in item}
                    bk2 = {item for item in pool3 if 'ID10' in item}
                    u1 = bk1.union(bk2)
                    bk3 = {item for item in pool3 if 'ID11' in item}
                    u2=u1.union(bk3)
                    bk4 = {item for item in pool3 if 'ID12' in item}
                    u3=u2.union(bk4)
                    bk5 = {item for item in pool3 if 'ID13' in item}
                    u4=u3.union(bk5)
                    bk6 = {item for item in pool3 if 'ID14' in item}
                    u5=u4.union(bk6)
                    bk7 = {item for item in pool3 if 'ID15' in item}
                    u6=u5.union(bk7)
                    bk8 = {item for item in pool3 if 'VB30' in item}
                    u7=u6.union(bk8)
                    bk9 = {item for item in pool3 if 'VB19' in item}
                    u8=u7.union(bk9)
                    bk10 = {item for item in pool3 if 'VB20' in item}
                    u9=u8.union(bk10)
                    bk11 = {item for item in pool3 if 'VG' in item}
                    u10=u9.union(bk11)
                    back={item for item in pool3 if 'B' in item[1] and not 'P' in item[2]}
                    if len(back) > 0:
                        nub = int(len(back))
                        if 'B1' in back:
                            nub -= 1
                        if 'B2' in back:
                            nub -= 1
                        if 'B3' in back:
                            nub -= 1
                        if 'B4' in back:
                            nub -= 1
                        if 'B5' in back:
                            nub -= 1
                        if 'B6' in back:
                            nub -= 1
                        if 'B7' in back:
                            nub -= 1
                        if 'B8' in back:
                            nub -= 1
                        if 'B58' in back:
                            nub -= 1
                        if 'B59' in back:
                            nub -= 1
                        if 'B60' in back:
                            nub -= 1
                        if 'B61' in back:
                            nub -= 1
                        if 'B62' in back:
                            nub -= 1
                        if 'B63' in back:
                            nub -= 1
                        if 'B64' in back:
                            nub -= 1
                        if 'B65' in back:
                            nub -= 1
                        if 'B66' in back:
                            nub -= 1
                        if 'B67' in back:
                            nub -= 1
                        if nub > 0:
                            if int(len(u10))==0:
                                print('NECESSÁRIO APLICAR EM DORSAL DE PACIENTE EM MERIDIANO DE BEXIGA')
                            if int(len(u10))!=0:
                                print('NECESSÁRIO APLICAR EM DORSAL DE PACIENTE EM MERIDIANO DE BEXIGA E EM ', end='')
                                print(u10)
                    else:            
                        if int(len(u10))!=0:
                            print('NECESSÁRIO APLICAR EM DORSAL DE PACIENTE EM ', end='')
                            print(u10)
                        else:
                            print('NÃO HÁ PONTOS EM DORSAL')
                    if homm == 'A' and len(warn_pun)!=0:
                        print('\nRECOMENDAÇÕES DE TRATAMENTO: ')
                        for i in sorted(list(warn_pun)):
                            print(i)
                    if homm == 'A' and len(lembrete) != 0:
                        print('\n\nLEMBRETES DE CONSULTAS: ')
                        for i in sorted(lembrete):
                            print(i)
                    print()
                print('\n===========================================================\n')
                digprepre = input('CONSULTE: [0] TOPOGRAFIA DE COLUNA [1] PONTOS YUAN [2] PONTOS ESTRELA DE CÉU [3] PONTOS DE SU SI MIAO [4] PONTOS MU-XI \n[5] PONTOS MU [6] PONTOS SHU DORSAIS [7] PONTOS SHU ANTIGOS [8] PONTOS LUO [9] PONTOS XI [10] PONTOS HUI [11] SHENS \n[12] PONTOS HO [13] PONTOS EXTRAS [14] VENTOSA [15] PONTOS JANELA DE CÉU [16] PRESCRIÇÃO PARA PATOLOGIAS DE MEDICINA OCIDENTAL\n\nPRESCREVER PONTO(S): \nG: SEDAÇÃO FRIA, H: SEDAÇÃO COM MOXA, W: TONIFICAÇÃO FRIA, X: TONIFICAÇÃO COM MOXA,  || Z: NEUTRO, Y: VENTOSA, K: SANGRIA, \nM: UNILATERAL DIREITA - SEDADO, N: UNILATERAL ESQUERDA - SEDADO, A: UNILATERAL DIREITA - TONIFICADO, D: UNILATERAL ESQUERDA - TONIFICADO, \n\n\nDIGITE FIM PARA FINALIZAR O PROCESSO, OU,\n\n\nINSIRA PRESCRIÇÕES OU (*+PONTO) PARA APAGAR UM PONTO, (*) PARA ZERAR PRESCRIÇÃO, (@) PARA ZERAR NOTAS\nPARA APAGAR UM MERIDIANO * + MERIDIANO (IG, P, C...) (PARA EXTRAS USE *T): ')
                if digprepre.isnumeric() == True:
                    global pipe
                    pipe = int(digprepre)
                    apend()
                else:
                    digpre = str(digprepre).upper()
                    if homm == 'A' and '@' in digpre:
                        lembrete.clear()
                        continue
                    if '*' in digpre:
                        if len(digpre) == 1:
                            pool3.clear()
                            continue
                        if ' ' in digpre:
                            mulp = digpre.split(' ')
                            tam = int(len(mulp))
                            for i in range(tam):
                                pool3.discard(mulp[i[1:]])
                            continue
                        elif '*C' in digpre:
                            c = [item for item in pool3 if 'C' in item[1]]
                            for i in c:
                                pool3.discard(i)
                            continue
                        elif '*P' in digpre:
                            p = [item for item in pool3 if 'P' in item[1] and 'C' not in item[2]]
                            for i in p:
                                pool3.discard(i)
                            continue     
                        elif '*IG' in digpre:
                            ig = [item for item in pool3 if 'IG' in item[1:]]
                            for i in ig:
                                pool3.discard(i)
                            continue        
                        elif '*BP' in digpre:
                            bp = [item for item in pool3 if 'BP' in item[1:]]
                            for i in bp:
                                pool3.discard(i)
                            continue    
                        elif '*E' in digpre:
                            e = [item for item in pool3 if 'E' in item[1] and not 'X' in item[2]]
                            for i in e:
                                pool3.discard(i)
                            continue
                        elif '*PC' in digpre:
                            pc = [item for item in pool3 if 'PC' in item[1:]]
                            for i in pc:
                                pool3.discard(i)
                            continue                                                                         
                        elif '*TA' in digpre:
                            ta = [item for item in pool3 if 'TA' in item[1:]]
                            for i in ta:
                                pool3.discard(i)
                            continue                                                                            
                        elif '*ID' in digpre:
                            id = [item for item in pool3 if 'ID' in item[1:]]
                            for i in id:
                                pool3.discard(i)
                            continue   
                        elif '*F' in digpre:
                            f = [item for item in pool3 if 'F' in item[1]]
                            for i in f:
                                pool3.discard(i)
                            continue                   
                        elif '*VB' in digpre:
                            vb = [item for item in pool3 if 'VB' in item[1:]]
                            for i in vb:
                                pool3.discard(i)
                            continue 
                        elif '*R' in digpre:
                            r = [item for item in pool3 if 'R' in item[1:]]
                            for i in r:
                                pool3.discard(i)
                            continue                     
                        elif '*B' in digpre:
                            b = [item for item in pool3 if 'B' in item[1] and not 'P' in item[2]]
                            for i in b:
                                pool3.discard(i)
                            continue                    
                        elif '*VC' in digpre:
                            vc = [item for item in pool3 if 'VC' in item[1:]]
                            for i in vc:
                                pool3.discard(i)
                            continue                        
                        elif '*VG' in digpre:
                            vg = [item for item in pool3 if 'VG' in item[1:]]
                            for i in vg:
                                pool3.discard(i)
                            continue    
                        elif '*T' in digpre:
                            extra = [item for item in pool3 if 'E' in item[1] and 'X' in item[2]]
                            for i in extra:
                                pool3.discard(i)
                            continue                                            
                        else:
                            pool3.discard(digpre[1:])
                            continue
                    if ' ' in digpre:
                        cutspe = digpre.split(' ')
                        tamanho = int(len(cutspe))
                        for i in range(tamanho):
                            pool3.add(cutspe[i])
                        continue
                    if 'FIM' in digpre:
                        cls()
                        print('\n\n\n\nSALVANDO EM BANCO DE DADOS...\n')
                        time.sleep(3)
                        # ARQUIVAMENTO DE DADOS EM DB
                        data=[str(cpf),str(nome),str(expodn)+', '+str(idd)+' ANOS',str(acompanhante.upper()),str(horadia),str(comfx.upper()),str(limpar(pureli)),str(totpul),str(limpar(seta)),str(limpar(acu2))]
                        with open('registro_acupuntura.csv', 'a', encoding='UTF8', newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow(data)       
                        data=[str(cpf),str(nome),str(expodn)+', '+str(idd)+' ANOS',str(acompanhante.upper()),str(horadia),str(comfx.upper()),str(limpar(pureli)),str(totpul),str(limpar(seta)),str(limpar(acu2))]
                        with open('ailog.csv', 'a', encoding='UTF8', newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow(data)        
                        os1 = os.path.getsize('registro_acupuntura.csv')/1000000
                        os2 = os.path.getsize('ailog.csv')/1000000
                        print('\nTamanho dos arquivos salvos: ')
                        print("Base de dados: {}MB".format(str(os1)))
                        print("Base de exposição: {}MB".format(str(os2)))                 
                        print()

                        if len(pool3) < 1:
                            pool3.add('IGNORADO')
                        if homm == 'A':
                            print('\n\nTAO | COPYRIGHT 2023 RODRIGO DIAS - VERSÃO '+ver)
                            print('\n\nEXAME FINALIZADO COM SUCESSO')
                            finalque2 = input(
                                '\nAperte qualquer tecla para continuar: \n\n')
                            zerar()
                        if homm == 'D':
                            print(
                                '\n\nTAO | COPYRIGHT 2023 RODRIGO DIAS - VERSÃO '+ver)
                            print('\n\nEXAME FINALIZADO COM SUCESSO')
                            finalque2 = input(
                                '\nATENÇÃO! DADOS SERÃO APAGADOS! Aperte qualquer tecla para continuar: \n\n')
                            zerar()
                    else:
                        if len(digpre) >= 3 and digpre != 'FIM' or len(digpre) < 7:
                            cut = list(digpre)
                            if cut[0] == 'G' or cut[0] == 'H' or cut[0] == 'W' or cut[0] == 'X' or cut[0] == 'Y' or cut[0] == 'Z' or cut[0] == 'K' or cut[0] == 'M' or cut[0] == 'N' or cut[0] == 'A' or cut[0] == 'D':
                                pool3.add(digpre)
                                print()
                                continue
                            else:
                                print(
                                    'Somente aceito pontos de acupuntura. Tente novamente.')
                                time.sleep(2)
                                continue
                        else:
                            print(
                                'Somente aceito pontos de acupuntura. Tente novamente.')
                            time.sleep(6)
                            continue
        except:
            cls()
            print()
            print(
                '\n\n\n\n\n\n\nNÃO FOI POSSÍVEL ADICIONAR ESTE COMANDO, POR FAVOR TENTE NOVAMENTE!')
            time.sleep(1)
            continue
# -------------------------------------- MATRIZ OPERACIONAL PARA CONSULTA


def lista():
    print()
    print('__________________________________________')
    print()
    for i, j in enumerate(list(dx), start=0):
        print(i, j)
    print()
    print(tipo_p[1:])
    print(


    )
    print()
    finalque = input('Aperte qualquer tecla para continuar: ')


# -------------------------------------- ZERAR MEMÓRIA TEMPORÁRIA

def zerar():
    print()
    print()
    print('Apagando memória temporária para otimizar Tao...')
    if homm == 'A':
        try:
            prepdif.clear()
            tensor.clear()
            dxcid.clear()
            seta.clear()
            vector1 = [0, 0, 0, 0, 0, 0]
            vector2 = [0, 0, 0, 0, 0, 0]
            path.clear()
            pool.clear()
            pool2.clear()
            pool3.clear()
            pct.clear()
            warn.clear()
            tipo_shi.clear()
            smt.clear()
            h3.clear()
            h8.clear()
            warn_pun.clear()
            oneway.clear()
            lembrete.clear()
            coid.clear()
            time.sleep(3)
            home()
        except:
            prepdif.clear()
            tensor.clear()
            vector1 = [0, 0, 0, 0, 0, 0]
            vector2 = [0, 0, 0, 0, 0, 0]
            path.clear()
            pool.clear()
            pool2.clear()
            pct.clear()
            warn.clear()
            tipo_shi.clear()
            smt.clear()
            h3.clear()
            h8.clear()
            oneway.clear()
            lembrete.clear()
            time.sleep(3)
            home()
    if homm != 'A':
        pool3.clear()
        seta.clear()
        dxcid.clear()
        time.sleep(3)
        warn_pun.clear()
        home()

# -------------------------------------- ATUALIZAÇÕES


def atualiz():
    print()
    print('__________________________________________')
    print()
    atualizações = {'1.0.0': 'OPERACIONAL BETA', '1.0.1': 'FUNCIONAL INICIAL', '1.0.2': 'ADICIONADO DICIONÁRIO DE TERMOS DE ESCOLHAS', '1.0.3': 'ACIONADO PULSO PATOLÓGICO COMO SAÍDA', '1.0.4': 'PULSO PATOLÓGICO INTERFERE EM COLISÕES, SENDO PREFERENCIAL', '1.0.4': 'ALGORITMO DE PADRÕES PULSO NORMAIS EM PATOLÓGICOS (AUTOMATIZAÇÃO)', '1.1.0': 'ALGORÍTMO TOTALMENTE INTEGRAL DE PULSO NORMAL E PATOLÓGICO', '1.1.2': 'ADICIONADO SAÍDA DE ANÁLISE DE LÍNGUA E GERAÇÃO DE PLOTAGEM DE DADOS DE PULSO', '1.1.3': 'ADICIONADO PRESCRIÇÃO E LÓGICA DE ÁRVORE DE ESCOLHAS COM REUSO DE ÍTENS E SENHA PARA FORMATAÇÃO', '1.1.4': 'INTEGRAR BANCO DE DADOS COM MÓDULO DE PRESCRIÇÃO VIA CSV', '1.1.5': 'INTEGRAÇÃO CID11 COM SISTEMA', '1.1.6': 'MODULAÇÃO DE ETAPAS DE SALVAMENTO BIN/BIAO, REDESENHAMENTO DE DATACENTER', '1.1.7': 'CORREÇÃO DE FALHA DE SALVAMENTO EM CASO DE NÃO PRESCREVER E VER RESULTADOS DE EXAME, LIBERADO CÓDIGO PARA SALVAR', '2.0.1': 'ADIÇÃO DE QUESTIONÁRIO PARA ALGORÍTMO DE PONTOS MU/XU/LUO/YUAN/HUI/JANELA/ESTRELA/SU SI MIAO/SHU ANTIGO/SHU DORSAL/DAIS EXTRAORDINÁRIOS', '2.0.2': 'AJUSTE DE TELA DURANTE CICLOS', '2.0.3': 'NOVO ALGORÍTMO DE ANÁLISE DE DADOS DIAGNÓSTICOS COM NOVO SET DE CAPTURA DE ERROS, CORREÇÃO DE DICT DIAGNÓSTICO', '2.0.4': 'ADIÇÃO DE APÊNDICE TÉCNICO EM PRESCRIÇÃO', '2.1.0': 'MODULAÇÃO DE ALGORÍTMOS PARA INTERSECÇÃO DE DADOS PARA FORMULAR DIAGNÓSTICO DEFINITIVO E DEMAIS AJUSTES PARA O PATCH', '2.1.1': 'CORREÇÃO DE COLISÕES POR ALGORÍTMO DE ANÁLISE NOVO', '2.1.2': 'CORREÇÃO DE ERROS GERAIS QUE IMPEDIAM FUNCIONAMENTO CORRETO DO PROGRAMA (IDENTADORES E ÁRVORES DE ESCOLHAS EM LOOP, ALÉM DE INSERSÃO DE VERIFICADORES DE DATABASE), INSERÇÃO DE SLEEP EM ERROS QUE ERAM APAGADOS EM COMANDO CLS(SLEEP) NÃO SENDO LOCALIZADOS (POR MELHOR ESTÉTICA MANTIDO CLS COM SLEEP EM ERROS PARA SEREM LIDOS), NOTIFICAÇÕES EM MÓDULOS QUE USAM DATABASE CASO ARQUIVO INATIVO (CONTINGÊNCIA DE DADOS)', '2.1.3': 'ANÁLISE DE SET PARA VERIFICAR MEMÓRIA VAZIA, BLOQUEANDO COLISÕES DE DADOS DE PACIENTES DIFERENTES, OBLITERAÇÃO DE PLOTAGEM DE DADOS SIMPLIFICADA (VERSÃO ESTÁVEL)', '2.1.4': 'ADIÇÃO DE ANÁLISE DE TRIPLO AQUECEDOR E 4 NÍVEIS DE CALOR-VENTO VIA ALGORITMO AUTOMÁTICO', '2.1.5': 'ADIÇÃO DE CID11 AOS TERMOS DE TRATAMENTO AUTOMATICAMENTE', '2.1.6': 'PATCH PARA FILTRAR CAMPO UNIFICADO IRRESTRITO AUTOMATICAMENTE, UNIFICANDO CAMPOS QUE REQUERIAM SEQUÊNCIA NO EXAME FÍSICO NEM SEMPRE SEGUIDAS', '2.2.0': 'ADIÇÃO DE TENSÃO PARA CÁLCULO DE APROXIMAÇÃO OU DEFINIÇÃO EM ALGORÍTMO DIAGNÓSTICO - A.I.', '2.2.1': 'AJUSTE DE CORREÇÃO DO ALGORÍTMO PARA CASOS DE ANTAGONISMOS, PATCH DE MULTIINSERÇÃO DE TABELA DE SELEÇÃO COM ADIÇÃO DE APAGAMENTO, VERIFICAÇÃO E CORREÇÃO DE PONTOS EM CASO DE DIPLICIDADE COM MÉTODOS DISTINTOS, ADIÇÃO DE ANÁLISE DE TRIPLO AQUECEDOR COM DEFINIÇÃO DE LOCAL E ADIÇÃO DE CID, APAGAMENTO DE MEMÓRIA APÓS TÉRMINO DE ALGORÍTMO, EDIÇÃO DE SELEÇÃO DE PONTOS INDIVIDUALMENTE (INSTÁVEL)', '2.2.2': 'DEPURAÇÃO DE ERROS, ESTABILIZAÇÃO DE SCRIPT E REINTRODUÇÃO DE PLOTAGEM ELETIVA COM NOVOS DADOS DO NOVO ALGORÍTMO, PERMITINDO MELHOR USO', '2.2.3': 'CORREÇÃO DE ALGORÍTMO DE TENSORES (UNIÃO E INTERSESSÃO NÃO ERAM REALIZADAS POR DIFERENÇA DE LIST/SET E OUTRA STRING PARA PÓS AJUSTE DE ALGORÍTMO ERA INUTILIZADA)', '2.2.4': 'INSERÇÃO DE PROTOCOLO DE SÍNDROMES POR ANÁLISE DE COMBINAÇÕES DE PULSOS PATOLÓGICOS VIA REDE NEURAL NÃO-ESTRUTURADA', '2.2.5': 'TESTAGEM MACIÇA PARA CORREÇÃO DE COLISÕES DE ESCOLHAS, MUDANÇAS DE LAYOUT DO BACKEND', '2.3.0': 'VERSÃO ESTÁVEL COM SCRIPT REVISADO', '2.3.1': 'ADIÇÃO DE SINTOMATOLOGIA (160 SINTOMAS) CORRESPONDENTES À SÍNDROME GERADA NO DIAGNÓSTICO', '2.3.2': 'INTEGRAÇÃO DE DIAGNÓSTICOS GENÉRICOS A ALGORÍTMO DE ANÁLISE E TROCA PARA ESPECÍFICOS E AJUSTES DE DETECÇÃO DE ERROS',
                    '2.3.3': 'AJUSTE DE LAYOUT DE APRESENTAÇÃO DE DADOS', '2.3.4': 'NOVO ALGORÍTMO DE ANÁLISE DE FRIO+CALOR EM MESMO MERIDIANO, SENDO CORRIGIDO VIA COERÊNCIA-CODOMINÂNCIA-RESSONÂNCIA-PATERNIDADE OU CANCELAMENTO DE ANÁLISE VIA FUNÇÃO REDUTIVA INDEXADA', '2.3.5': 'AVISOS EM CORREÇÕES DE CÁLCULOS', '2.3.6': 'ANÁLISE DE PADRÕES PARA BIN/BIAO E DESCRIÇÃO DE PADRÕES COM SUGESTÕES DE ALIMENTOS', '2.3.7': 'ADIÇÃO DE HISTÓRIA CLÍNICA, ANÁLISE DE DOR E SENTIDOS TÁTEIS', '2.3.8': 'DEPURAÇÃO DE ERRO DE TAGS E SALVAMENTO, REDUÇÃO DE GLOBAIS', '2.3.9': 'REVISÃO DE PULSOS - PATCH DE CORREÇÃO POR ERROS DETECTADOS', '3.0': 'REVISÃO DE PADRÕES GLOBAIS E TROCAS POR FUNÇÕES', '3.1': 'CORREÇÃO DE LIU XIE CALOR/VENTO COM TOTALIDADE DE SINAIS SOB ANÁLISE', '3.2': 'POCKET EDITION', '3.3': 'CORREÇÃO DE BUG QUE IMPEDIA APARECER SINTOMAS - CORROMPIDO CÓDIGO', '3.4.0': 'DIAGNÓSTICOS DE FRIO/CALOR E DE TA AGORA ENTRAM DIRETO COM DIAGNÓSTICOS DE CERTEZA', 'A1': 'CORREÇÃO DE ALGORITMO DE LÍNGUA, MAIS FLUIDO. BACKUP UTILIZADO POR ERRO DE IDENTAÇÃO GRAVE, SOB DOWNGRADE E PATCH', 'A2': 'COMPATIBILIZAÇÃO E ESTABILIZAÇÃO DE MÓDULO', 'A3': 'SEPARAÇÃO DE PRESCRIÇÃO PARA CLASSES DE APLICAÇÃO', 'A4': 'ORDENAÇÃO DE CLASSES DEVIDO A COLISORES EM LOOPS E LIST COMPREHENSIONS', 'A5': 'LOOPS AMPLIADOS PARA CÁLCULOS', 'A6': 'CÁLCULO BRUTO DE PONTOS E QUANTIDADE DE AGULHAS', 'A7': 'CÁLCULO TOTALITÁRIO DE AGULHAS VIA ANÁLISE UNITÁRIA DO PONTO, CORREÇÃO DE BUG DE MÚLTIPLAS ENTRADAS DE DX EM METAS DE TRATAMENTO (FAZENDO APARECER EM VEZ DE NOME SOMENTE NÚMERO SE DADOS MÚLTIPLOS) - ESTÁVEL', 'A8': 'MELHORIA DE LISTAS E EXPOSIÇÕES DE PRINTS E TRADUÇÃO DE CID-11 APLICADA EM MTC', 'A9': 'ADIÇÃO DE DESCRIÇÃO DE SINTOMAS DE SÍNDROMES DE LIU XIE VENTO-CALOR E CORREÇÃO DE INDEXAÇÃO DAS MESMAS, ADICIONADO ANÁLISE DE COMPLEIÇÃO EM RESULTADOS', 'BETA-1': 'DELIMITAÇÃO PÓS-ANÁLISE DE NOVA TENTATIVA DE LOCALIZAR BIN', 'BETA-2': 'ATUALIZAÇÃO DE LISTA DE CID-11 PARA PORTUGUÊS', 'BETA-3': 'ADIÇÃO DE TIMEZONE EM BRASÍLIA E PROGRAMADO PONTOS SHU POR CRONOACUPUNTURA', 'BETA-4': 'ADIÇÃO DE DESCRIÇÃO DE LIU XIES ESPECÍFICAS QUANDO DETECTADAS', 'BETA-4': 'TESTES DE PATCH', 'GAMA-1': 'IMPLEMENTADO PROTOCOLOS DE TRATAMENTO ORIENTADOS POR SELEÇÃO PÓS-EXPOSITIVA', 'GAMA-2': 'CORREÇÃO DE FLUXO DE LOOP DE PATCH SEM SAÍDA VIA MÓDULO ONE-WAY', 'GAMA-3': 'TESTES DE IMPLEMENTAÇÃO DE AUTOMAÇÃO DE FLUXO DE DADOS (PRESCRIÇÕES PROTOCOLARES', 'DELTA-1': 'IMPLEMENTAÇÃO DE 74 NOVOS PROTOCOLOS AUTOMATIZADOS', 'DELTA-2': 'CORREÇÃO DE PATHWAY DESFRAGMENTADO POR NOVAS ADIÇÕES', 'DELTA-3': 'CORREÇÃO DE GRAVE ERRO DE FLUXO DE FUNÇÃO DE DISPOSIÇÃO DA TABELA DE SINTOMAS', 'DELTA-4': 'CORREÇÃO DE ERRO DE DESAPARECIMENTO DE SINTOMAS ESPECÍFICOS DE SÍNDROMES VENTO-FRIO E VENTO-CALOR', 'DELTA-5': 'CORREÇÃO DE DEGENERAÇÃO DO CÓDIGO NA FORMATAÇÃO DE IDENTAÇÃO, COM ERRO FATAL DO CÓDIGO', 'DELTA-6': 'ADIÇÃO DE ESTAÇÃO DE ANO PARA TIPOS DE PUNTURA CONFORME MEDICINA CHINESA CLÁSSICA', 'ADIÇÃO DE CONDIÇÃO CLIMÁTICA PARA TRATAMENTO DE FRIO CHEIO': 'DELTA-7', 'TAO 1.0.0': 'COMPILAÇÕES BINÁRIAS PARA EXPORTAÇÃO E SEM ACESSO VIA GOOGLE PARA COPYRIGHT', 'TAO 1.0.1': 'MELHORIA DE ANÁLISE CLIMÁTICA E WARN_PUN PARA REQUESTS GERADOS ONLINE DE TEMPO/CLIMA E PRESCRIÇÃO DE TÉCNICA', 'TAO 1.0.2': 'ADIÇÃO DE TESTE DE GRAVIDEZ, TESTE DE RENYING, EXAME COMPLEIÇÃO DE NARINA, OLHO, ENTRE SOMBRANCELHAS, EXAME DE ANTEBRAÇO E GERAÇÃO DE VARIÁVEIS DE TRATAMENTO, VISANDO TERAPIA POR TIPO DE PUNÇÃO (OSSO, MÚSCULO, TENDÃO, CANAL) CONFORME PROTOCOLO', 'TAO 1.0.3': 'ALGORÍTIMO DE CORREÇÃO VIA ESTAÇÃO PARA EXAME DE RENYING (CONFORME IMPERADOR AMARELO)', 'TAO 1.0.4': 'ADIÇÃO DE ANÁLISE TEXTUAL DE HDA PARA COLETA DE DADOS VIA WU XING TABELA GERAL, MELHORIA DE DESIGN E DISPOSIÇÃO DE FLUXO', 'TAO 1.0.5': 'DEVIDO A MOSTRUÁRIO DE PONTOS NÃO ESTAREM SEPARADOS POR MERIDIANOS E DEVIDO A ERRO QUE PERMITIA DUPLICIDADE DE PONTOS EM SEDAÇÃO E TONIFICAÇÃO, AJUSTE DE UNIFICAÇÃO DE SIGLAS DUPLAS EM CATEGORIAS SEDAÇÃO/TONIFICAÇÃO, DE MOXA E DE LATERALIDADE PERMITINDO O SPLIT [1:] ESTAR EM SET DE VERIFICAÇÃO CONFORME TIPO DE APLICAÇÃO, CONTUDO NECESSÁRIO PATCH DE CORREÇÃO DE FLUXOS DE INSERÇÃO DE PRESCRIÇÃO, CORREÇÃO DE AUTOMAÇÃO DE INSERÇÃO PARA NOVOS PARÂMETROS. RETIRADA DE TAGS DE MARCAÇÃO DE WARN_PUN (EM LETRAS), FICANDO SEM SENTIDO EM DISPLAY E JÁ IMPLEMENTADAS', 'TAO 1.0.6': 'ERRO DE CODIFICAÇÃO COMPATÍVEL COM AJUSTE EM 1.0.5, SENDO REALIZADO DOWNGRADE E MANTIDO NOVA CODIFICAÇÃO UNIFICADA PARA DUPLAS DE LETRAS EM PRESCRIÇÕES E DISPOSIÇÃO DOS PONTOS', 'TAO 1.0.7': 'AJUSTE DE DICT E DIRETÓRIOS DO CID COM FUNÇÕES DE DISPOSIÇÃO PERFEITAS E MELHORA DE ESTABILIDADE DO DOWNGRADE', 'TAO 1.0.8': 'ADIÇÃO DE ACUPUNTURA VOLTADA PARA PATOLOGIAS DA MEDICINA NÃO ORIENTAL', 'TAO 2.0.0':'ATUALIZAÇÃO DE TODOS OS PONTOS EXTRAS (UNIFICAÇÃO DE NOMENCLATURAS LITERÁRIAS COM LOCALIZAÇÃO NA PRESCRIÇÃO E INTEGRAÇÃO DE BUSCA E NOTAS)', 'TAO 2.0.1':'AJUSTE DE CONTAGEM DE PONTOS PARA NOVOS EXTRAS COM CORREÇÃO VIA SETS DIFERENCIAIS SEM NECESSITAR FLUTUAÇÕES NUMERAIS','TAO 2.0.2':'INSERÇÃO DE ANÁLISE DE BPM PARA ALGORÍTMO DE PULSOLOGIA COMPATÍVEIS','TAO 2.0.3':'NOVO PROTOCOLO DE ANÁLISE SHANG HAN LUN SEM ALTERAÇÃO DO ANTERIOR, ANALISADO VIA ESTATÍSTICA E COM DETERMINAÇÃO DE SUBTIPOS','TAO 2.0.3':'CORREÇÃO DE INDEXAÇÃO POR PESQUISA NOME-LOCAL E USO DE PANDAS PARA EXIBIR PULSOLOGIA E SANJIAO','TAO 2.0.5':'INSERÇÃO DE COMANDO DE APAGAR MERIDIANO TODO, AJUSTE DE DISPOSIÇÃO DE TEXTO DE EXPLICAÇÃO DE DORES E LOCAIS DO MERIDIANO, AJUSTE DE SEPARAÇÃO EM COMPOSIÇÃO DE PALAVRAS, TROCA DE TEXTO EXPLICATIVO SOBRE PUNTURAS RECOMENDADAS POR ESTAÇÃO E INSERÇÃO DE TEXTO DE RESUMO AO BRIEFING DE DIAGNÓSTICOS','TAO 2.0.6':'ADIÇÃO DE FUNÇÃO DELIMITANDO MAIS PONTOS ALÉM DA BEXIGA PARA AVISO DE PONTOS EM DORSAL (FAZENDO PACIENTE NÃO PERDER TEMPO NA APLICAÇÃO EM DORSO COM PONTOS DIFERENTES)','TAO 2.1.0':'APRIMORAMENTO DO ALGORÍTMO DE ESCOLHA DE PONTOS PRESCRITOS COM RESTRIÇÃO CALCULADA PARA MENOS AGULHAS QUANTO MAIS DIAGNÓSTICO FOR ACRESCIDO - NÃO PERMITINDO 200 AGULHAS PARA 5 DIAGNÓSTICOS, POR EXEMPLO; ADIÇÃO DE ESPECIFICAÇÃO DE PULSOLOGIA E DESCRIÇÕES DE SINTOMAS ESPECÍFICOS POR LOCALIZAÇÃO DE TIPOS DE PULSOS E LOCAIS (DESCRIÇÃO DE MEDICINA CLÁSSICA DO IMPERADOR AMARELO, SINTOMAS MUITO ESPECÍFICOS NÃO GENERALISTAS)','TAO 2.1.1':'CORREÇÃO DE 7 BUGS DEVIDO A ATUALIZAÇÃO, ESTABILIZAÇÃO DE FUNÇÕES ITERATIVAS, AJUSTE DE REPORTS DO PROGRAMA E RELATÓRIO FINAL EXPOSITIVO E RESUMIDO','TAO 2.1.2':'CORREÇÃO ESTRUTURAL E TEXTUAL COM REINTRODUÇÃO DE AQUIVAMENTO DE INFORMAÇÕES COM INDEXAÇÃO DE DADOS, AINDA EM OPERACIONALIZAÇÃO','TAO 2.1.3':'ADIÇÃO DE CÁLCULO DE IDADE E COMPLEMENTAÇÃO DE DADOS PARA EXPORTAR PARA ALGORÍTMO DE NÄIVE-BAYES','TAO 2.2':'IMPLEMENTAÇÃO DE ARQUIVOS DE BASE DE DADOS PARA ANÁLISE AI E PARA CONSULTA DE PACIENTES VIA .CSV EM USO LOCAL','TAO 2.3':'PATCH CORRECIONAL DEVIDO A PERDA DE COERÊNCIA COM RETIRADA DE GLOBAIS AFETANDO DEF METRO E DEF ONLY (DOWNGRADE SEGUIMENTO METRO E ONLY VIA 2.1.1) SEM ENCONTRAR ERRO E SEM RODAR - VERSÃO ESTÁVEL','TAP 2.4':'IMPLEMENTAÇÃO DA BASE DE DADOS','TAO 2.5':'ADIÇÃO DE CPF COMO IDENTIFICADOR DE CONSULTA (INCLUSO ALGORÍTMO DE VERIFICAÇÃO) E ADIÇÃO DE ANÁLISE DE JING JIN'}
    for key, value in atualizações.items():
        print(key, ' : ', value)
    print()
    finalque = input('Aperte qualquer tecla para continuar: ')

# -------------------------------------- INFO


def cid():
    print()
    print()
    for i in ciddict:
        print(i, ciddict[i])
    print()
    while True:
        try:
            pesq = input(
                'Digite código CID-11 a ser pesquisado (ou digite FIM): ').upper()
            print()
            if pesq == 'FIM':
                print()
                print()
                break
            else:
                filt1 = [ciddict[i] for i in ciddict if i.count(pesq) > 0]
                if len(filt1) > 0:
                    print(filt1)
                else:
                    c = [i for i in ape2 if pesq in i]
                    if len(c) > 0:
                        print(c)
                    else:
                        print(next((i for i in ciddict.values() if pesq in i), None))
                print('\n\n')
                continue
        except:
            continue

# -------------------------------------- INFO


def sobre():
    print()
    print()
    print('\n\nA acupuntura faz parte de uma medicina ancestral de mais de há 3 milênios antes de Cristo e foi incorporada ao método científico nos dias atuais com eficácica comprovada e algumas ressalvas na comunidade científica. Apesar da ação causar efeito não existe conhecimento completo do mecanismo. A Medicina Tradicinal Chinesa (MTC) argumenta o mecanismo através do qi, e o qi não pode ser evidenciado cientificamente por não ser medido. A acupuntura depende da aplicação conforme a lógica da medicina chinesa, não sendo independente conforme seus pontos, pois depende de avaliar os meridianos e o qi sobre cada ponto. Sem o qi não ocorre tratamento e nem efeito. Talvez seu método inicial, contendo explicação para o qi e lógica deste método tenha se perdido durante os 5.000 anos de prática devido a associação com religião de quem a praticava e associação ao misticismo por quem não a conhecida. Atualmente reconhecida pela OMS e catalogada em CID-11 como tratamento médico científico, preconizando seu uso sem uso tradicional, ao qual nem sempre ocorre efeito nenhum. O programa, em conhecimento da MTC auxilia mensurar os 14 Qis segundo a prática milenar desconhecida da Medicina Ocidental para então a prescrição.\n\nEste programa usa a MTC de literaturas Nèijing, Su Wen, Ling Shu.')
    finalque = input('\nAperte qualquer tecla para continuar: ')
    print()
    home()

# -------------------------------------- APÊNDICES

def gerar_arquivos():
    while True:
        try:
            cls()
            if os.path.exists('registro_acupuntura.csv') == True and os.path.exists('ailog.csv') == True:
                cls()
                print('\n\n\n\nBASE DE DADOS ESTÁ ATIVA!\n\nARQUIVOS ESTÃO ATUALIZADOS PARA USO E NÃO É NECESSÁRIO IMPLEMENTAÇÃO NO MOMENTO...')
                time.sleep(8)
                cls()
                break
            else:
                cls()
                print('\n\nPROCESSANDO UPLOAD DE LOG VIA CÓDIGO\n\n')
                time.sleep(2)
                print('GERANDO ARQUIVOS DE REGISTRO')
                time.sleep(3)

                # ARQUIVO DE REGISTRO GERAL DE PACIENTES
                print('Criando arquivo de log registro_acupuntura.csv...')
                header=['CPF','NOME','DATA NASCIMENTO','ACOMPANHANTE','DATA DE EMISSÃO','COMPLEIÇÃO','LÍNGUA','PULSO','DIGNÓSTICOS','PRESCRIÇÃO ACUPUNTURA']
                with open('registro_acupuntura.csv', 'w', encoding='UTF8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)

                # ARQUIVO PARA IMPLEMENTAÇÃO DE ALGORÍTMO DE ANÁLISE IA
                print('Criando arquivo de log ailog.csv...')
                header=['CPF','NOME','DATA NASCIMENTO','ACOMPANHANTE','DATA DE EMISSÃO','COMPLEIÇÃO','LÍNGUA','PULSO','DIGNÓSTICOS','PRESCRIÇÃO ACUPUNTURA']
                with open('ailog.csv', 'w', encoding='UTF8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)         
                print('\n\nPROCESSO FINALIZADO COM SUCESSO! RETORNANDO AO MENU...')
                time.sleep(4)
                break
        except:
            continue
    
def apend():
    while True:
        try:
            cls()
            print()
            print()
            print()
            if pipe == 0:
                print('\nTOPOGRAFIA DE COLUNA\n\nC7: Proeminência mais superior (supraclavicular)\nT3: Ao nível da espinha de escápula\nT7: Ao nível inferior da escápula\nL4: Ápice da espinha da crista ilíaca anterosuperior\nS2: Ápice da espinha ilíaca posterosuperior\n\n7 cervicais\n12 torácicas\n5 lombares\n5 sacrais\n5 coccígenas')
                print()
                print('Ao momento em prescrição: ')
                if len(pool3) > 0:
                    print(pool3)
                else:
                    print('Nada prescrito ainda...')
                lemb = input(
                    '\n\nAnotações para prescrição (ou enter para voltar): ').upper()
                if lemb == '':
                    print('\n\nNada foi adicionado. Retornando...\n')
                    time.sleep(1)
                else:
                    lembrete.add(lemb)
            if pipe == 1:
                print('\nPONTO YUAN\n\nP9, IG4, E42, BP3, C7, ID4, B64, R3, PC7, TA4, VB40, F3 VC15 (TECIDO ADIPOSO E TÓRAX), VC6 (MEMBRANAS E ABDOME)\nUSO PARA DIAGNÓSTICO PORQUE APARECEM REAÇÕES ANORMAIS QUANDO AFETADO ÓRGÃO NESTES PONTOS LOCAL DE DISTRIBUIÇÃO DO YUAN QI, O QI ANCESTRAL, PARA MELHORAR FUNÇAO FISIOLÓGICA DE UM ÓRGÃO YIN.\n\nVÍSCERAS (YANG) NÃO TEM UTILIDADE PARA TONIFICAR POR SEREM DE POUCA AÇÃO (MELHOR USAR MAR INFERIOR).\nVC15/TON - TRANSTORNOS MENTAIS (ANSIEDADE) DECORRENTE DE DEF DE CORAÇÃO VC6/TON - DEFICIÊNCIAS YANG (NUTRE COM YUAN QI) IG4/SED- EXPELE VENTO OU LIVRA DE FATOR OBSTRUTOR ID4/SED - MOVE QI ESTAGNADO EM FÍGADO B64/SED - EXPELE UMIDADE-CALOR DE AQUECEDOR INFERIOR VB40/SED - ESTAG QI FÍGADO E42/SED - (VENTO DA FACE) NEVRALGIA DE TRIGÊMIO, PARALISIA FACIAL TA4/SED - SURDEZ (POR SEDAR CALOR DE VB) OU REGULAR YANG MENOR TA4/TON - ATIVA O FLUXO DE QI EM TODO CORPO E NUTRE O QI COM YUAN QI\n\n')
                print('Ao momento em prescrição: ')
                if len(pool3) > 0:
                    print(pool3)
                else:
                    print('Nada prescrito ainda...')
                lemb = input(
                    '\n\nAnotações para prescrição (ou enter para voltar): ').upper()
                if lemb == '':
                    print('\n\nNada foi adicionado. Retornando...\n')
                    time.sleep(1)
                else:
                    lembrete.add(lemb)
            if pipe == 2:
                print('\nESTRELA DO CÉU\n\nCLASSIFICADOS AO SÉCULO 1, DINASTIA JIN COMO OS PONTOS QUE CURAM QUASE TODOS OS PROBLEMAS DE SAÚDE EM PESSOAS COM MUITAS DOENÇAS COMO TRATAMENTO RÁPIDO SEGUNDO O MÉDICO CRIADOR\n\nDEVE SER USADO EM PARES (SOMENTE UM PAR SE FOR LIU QI): \nE36-E44 IG11-IG4 B40-B57 F3-B60 VB30-VB34 C5-P7\n\n')
                print('Ao momento em prescrição: ')
                if len(pool3) > 0:
                    print(pool3)
                else:
                    print('Nada prescrito ainda...')
                lemb = input(
                    '\n\nAnotações para prescrição (ou enter para voltar): ').upper()
                if lemb == '':
                    print('\n\nNada foi adicionado. Retornando...\n')
                    time.sleep(1)
                else:
                    lembrete.add(lemb)
            if pipe == 3:
                print('\nPONTOS DE SUN SI MIAO \n\nUSO EM GRAVES DOENÇAS MENTAIS EM 652 D.C. 1.VG26 2.P11 3.BP1 4.PC7 5.B62 6.VG16 7.E6 8.VC24 9.PC8 10.VG23 11.VC1 12.EXT - YU MEN GUI CANG 13.IG11 14.EXT - HAI QUAN GUI FENG AGULHAR NA ORDEM ESTABELECIDA, SE HOMEM INICIAR AO LADO ESQUERDO E MULHERES LADO DIREITO. RETIRA-SE NA ORDEM INVERSA. VC1 NÃO É AGULHADO, USA-SE MOXA\n\n')
                print('Ao momento em prescrição: ')
                if len(pool3) > 0:
                    print(pool3)
                else:
                    print('Nada prescrito ainda...')
                lemb = input(
                    '\n\nAnotações para prescrição (ou enter para voltar): ').upper()
                if lemb == '':
                    print('\n\nNada foi adicionado. Retornando...\n')
                    time.sleep(1)
                else:
                    lembrete.add(lemb)
            if pipe == 4:
                print('\nPONTOS DOS OLHOS DE MU-XI \n\nDESCRITO EM C. 100 A.C. (LING SHU JING) SOBRE LOCAL DE NERVO ÓPTICO E EMULAÇÃO DE IMAGEM EM OCCIPTAL COM CONCENTRAÇÃO EM PINEAL DE QI, DESCRITO COMO PATOLOGIA DE DEFICIÊNCIA DE XUE EM CANAIS YANG DE: B/E/TA/VB, POR MEIO DE: B1, E1, TA23 E VB1. SENDO ESTES PONTOS PARA PATOLOGIAS OCULARES/VISUAIS/PINEAIS/NEUROLÓGICOS. \n\nB1, B2, VB1, TA23, E1, EXT YUYAO, VB4, VB5, VB6, VB7, E8, VG16, B10, VB20. \n\n')
                print('Ao momento em prescrição: ')
                if len(pool3) > 0:
                    print(pool3)
                else:
                    print('Nada prescrito ainda...')
                lemb = input(
                    '\n\nAnotações para prescrição (ou enter para voltar): ').upper()
                if lemb == '':
                    print('\n\nNada foi adicionado. Retornando...\n')
                    time.sleep(1)
                else:
                    lembrete.add(lemb)
            if pipe == 5:
                print('\nPONTOS MU - (PONTO DE ALARME) \n\nTONIFICAR YANG/ AQUECER (SEDAR QUENTE) TEORICAMENTE, POR ISSO DOENÇAS AGUDAS TAMBÉM USADOS PARA DIAGNÓSTICO DE MOLÉSTIAS AGUDAS, FICAM DOLORIDOS AO TOQUE OU ESPONTANEAMENTE FRONTAL: \nP(P1), PC(VC17), C(VC14), F(F14), VB(VB24), BP(F13), E(VC12), TA(VC5), R(VB25), IG(E25), ID(VC4), B(VC3)\n\n')
                print('Ao momento em prescrição: ')
                if len(pool3) > 0:
                    print(pool3)
                else:
                    print('Nada prescrito ainda...')
                lemb = input(
                    '\n\nAnotações para prescrição (ou enter para voltar): ').upper()
                if lemb == '':
                    print('\n\nNada foi adicionado. Retornando...\n')
                    time.sleep(1)
                else:
                    lembrete.add(lemb)
            if pipe == 6:
                print('\nPONTOS SHU DORSAIS\n\nDIAGNÓSTICO DE COR/VENTOSA E TONIFICAR YIN/SEDAR-DISPERSAR CALOR OU DESESTAGNAR QI ALÉM DA COR DA VENTOSA TAMBÉM PODE SER AVALIADO PORQUE É DOLOROSO LATENTE OU DOLOROSO ATIVO CRÔNICO EM LOCAL DE DEFICIÊNCIA DE ÓRGÃO TONIFICAR FÍGADO TRATA DOENÇA DE OLHOS, POR EXEMPLO AO TRAJETO DE MERIDIANO DE BEXIGA, PORTANTO, DORSAIS TEORICAMENTE, POR ISSO, PARA DOENÇAS CRÔNICAS PACIENTE SENSÍVEIS PODE TROCAR AGULHA POR MOXA TONIFICA COM MOXA CONTÍNUA E SEDA COM MOXA INTERMITENTE COM RETIRADA RÁPIDA DE CALOR DIAGNÓSTICO DE AGNOSIAS (TRATAMENTO COMO ZANG, TONIFICAR) NARIZ/ OLFATO #B13# LÍNGUA/ TOQUE #B15# OLHO/ VISÃO #B18# BOCA/ PALADAR #B20# ORELHA/ AUDIÇÃO #B23# (VER VASOS EXTRAORDINÁRIOS PARA OUTRAS VIAS) DIAGNÓSTICO ÓRGÃO/VÍSCERAS - TRATAMENTO DE ÓRGÃOS (TONIFICAR YIN OU RETIRAR CALOR) \n\nP B13 PC B14 C B15 F B18 VB B19 BP B20 E B21 TA B22 R B23 IG B25 ID B27 B B28 VG B16 DIAFRAGMA B17 MAR DE QI B24 LOMBAR E ÚTERO B26 SACRO B29 ANUS B30 \n\nCORES DIAGNÓSTICAS EM VENTOSAS MÁCULAS EM PONTOS SHU DORSAIS OU SOBRE PONTOS LUO (COU LI) \nVERDE = ESTAGNAÇÃO DE QI \nAZUL = FRIO \nVERMELHO = CALOR \nROXO = ESTAGNAÇÃO DE XUE\n\n')
                print('Ao momento em prescrição: ')
                if len(pool3) > 0:
                    print(pool3)
                else:
                    print('Nada prescrito ainda...')
                lemb = input(
                    '\n\nAnotações para prescrição (ou enter para voltar): ').upper()
                if lemb == '':
                    print('\n\nNada foi adicionado. Retornando...\n')
                    time.sleep(1)
                else:
                    lembrete.add(lemb)
            if pipe == 7:
                print('\nPONTOS SHU ANTIGOS (PASSAGEM)\n\nBRAÇOS E PERNAS PONTOS COM MAIOR ENERGIA QUE OS DEMAIS, EXTREMIDADES DE MEMBROS, SEGUNDO PONTO SHU É POLARIDADE INVERSA (FOGO VIRA ÁGUA), NASCENTE/POÇO/JING - GRAVES AGUDAS, PSIQUIÁTRICAS (EXPELE VENTO) LOCAL ONDE O QI ENCONTRA-SE MAIS INSTÁVEL, USO EM DOENÇAS AGUDAS PARA RÁPIDA RESOLUÇÃO (AVE, SÍNCOPE...). USO: PLENITUDE ABAIXO DO CORAÇÃO (ANSIEDADE, SÍNCOPE, IRRITABILIDADE), USO PARA ÓRGÃO YIN PC9- IRRITABILIDADE E INSÔNIA, C9- MANIA E PSICOSE, BP1- HISTERIA E INSÔNIA, E45- INSÔNIA E CONFUSÃO MENTAL, R1- ANSIEDADE. MANANCIAL/YIN - CALOR, RETIRA EXCESSO (EXPELE CALOR) PONTO MAIS FORTE (PÉS AINDA MAIS FORTES QUE PONTOS NA MÃO), DEVE SER USADO COM PARCIMÔNIA SE OUTROS POSSÍVEIS DE TROCA. USADO PARA ELIMINAR FATORES PATOGÊNICOS OU CALOR. USO: SENSAÇÕES QUENTES NO CORPO E FEBRE, ALTERAÇÃO DE COR DE FACE TODOS OS PONTOS (FOGO/ÁGUA) DISPERSAM CALOR. C8 E PC8 - DISPERSÃO DE CALOR DE CORAÇÃO, F2 - DISPERSÃO DE FOGO DE FÍGADO, E44 - DISPERSÃO DE CALOR DE ESTÔMAGO, R2 - DISPERSÃO DE CALOR DE RIM, P11 - LIMPA CALOR DE PULMÕES OU VENTO-CALOR. RIACHO/SHU - ARTRALGIA, VULNERÁVEL A FATOR PATOGÊNICO (EXPELE FRIO) PONTOS VULNERÁVEIS A LIU QI, LOCAL DE AGREGAÇÃO DE WEI QI, ENTRADA VERDADEIRA AO CORPO. USO: SENSAÇÕES DE PESO EM ARTICULAÇÕES, SINTOMAS INTERMITENTES USO EM OBSTRUÇÕES DOLOROSAS (SÍNDROME DOLOROSA) AO LONGO DE QUALQUER PONTO DO MERIDIANO, PRINCIPALMENTE POR UMIDADE/FRIO. RIO/JING  - PNEUMOPATIAS, AFASIAS DE FALA (EXPELE SECURA) LOCAL DE TRANSPORTE DE ENTRADA, CANAL PROFUNDO E EM MOVIMENTO DE QI. USO: FALTA DE AR, TOSSE, SENSAÇÕES DE FRIO/CALOR (PORÉM MAIS LENTA RESOLUÇÃO), USO EM DISLALIAS E DISARTRIAS. P8 - TOSSE/ASMA, BP5 - TOSSE SECA, E41 E IG5 - DOR DE GARGANTA, INVASÃO INCIPIENTE, PC5 - ALTERAÇÕES DE TEMPERATURA DE VAS, IG5 - RISO EXCESSIVO, E41 - EXCITAÇÃO EXCESSIVA, PC5 - AFONIA, EMBOTAMENTO DE FALA, BP5 - SUSPIROS, COMPROMETIMENTO DE FALA, R7 - DISARTRIA (LÍNGUA ENROLADA), TA6 - PERDA AGUDA VOCAL, F4 - SUSPIROS, C4 - AFASIA DE FALA. MAR/HE - GASTROINTESTINAL, PELE, VÍSCERAS, OMBRO, PESCOÇO, RESOLVE DEFICIÊNCIA (EXPELE UMIDADE) CANAL DE QI PROFUNDO E ESTÁVEL, EFEITO MAIS LENTO E MAIS LEVE. USO: REBELIÃO DE QI E DIARRÉIA/ DOENÇAS GÁSTRICAS, ÓRGÃOS YANG. MAR INFERIOR (NÃO SÃO PONTOS MAR) - E37, E39 E B39, REPECTIVAMENTE, IG, ID E TA. MAR SUPERIOR (NÃO SÃO PONTOS MAR) - IG11, ID8 E TA10, REPECTIVAMENTE, PESCOÇO, OMBROS E FACE E36 - CONDIÇÕES GÁSTRICAS E INTESTINAIS (TODAS CONDIÇÕES), VB35 - CONDIÇÕES GÁSTRICAS E INTESTINAIS, BP9 - ELIMINA UMIDADE EM BEXIGA E INTESTINOS (DIARRÉIA), R10 - ELIMINA UMIDADE EM BEXIGA E INTESTINOS, F8 - ELIMINA UMIDADE EM BEXIGA E INTESTINOS (DIARRÉIA), E37 - ATUA NO INTESTINO GROSSO (DIARRÉIA CRÔNICA, UMIDADE-CALOR), E39 - ATUA NO INTESTINO DELGADO E DOR INTESTINAL, B39 - ATUA NO TRIPLO AQUECEDOR/ ENURESE/ RETENÇÃO DE URINA/ EDEMA, B40 - VÔMITOS E DIARRÉIA, IG11 - PESCOÇO, DISTENSÃO COM DOR ABDOMINAL, ID8 - OMBROS, TA10 - FACE, P5 - VÔMITO, DIARRÉIA, DISTENSÃO ABDOMINAL SEM DOR, C3 - VÔMITOS COM SALIVA ESPUMOSA, R7 - DIARRÉIA COM BORBORISMO, PC3 - DIARRÉIA POR CALOR DE VERÃO, TA10 - VÔMITOS COM PUS E SANGUE OUTRAS ATRIBUIÇÕES - ÓRGÃO YIN - RIACHO E MANANCIAL DOS CANAIS YIN EM COMBINAÇÃO (F2, F3) - PELE - MAR DE CANAL YANG (IG11) - IG11: ERISIPELA, URTICÁRIA, PELE RESSECADA, ECZEMA, DESCAMAÇÃO, PRURIDO, ZÓSTER; B40: VESÍCULAS/BOLHAS; TA10: PRURIDO, ATOPIA - OSSO/TENDÃO - RIO DE CANAL YIN (BP5) - BP5 - DOR E CONTRAÇÃO DO TENDÃO, SÍNDROME BI, SENSAÇÃO DE PESO COM ARTRALGIA; C4 - ESPASMO; R7 - ATROFIA DE MMII; F4 - LOMBALGIA E CONTRATURAS - ÓRGÃO YANG (6 YANGS EXTRAORDINÁRIOS) - LUO DE CANAIS YANG- USO PARA LIU QI (FATORES PATOGÊNICOS) - POÇO/MADEIRA/VENTO, MANANCIAL/FOGO/CALOR, RIACHO/TERRA/UMIDADE, RIO/METAL/SECURA(NÃO SE USA), MAR/ÁGUA/FRIO VENTO PONTOS POÇO, SE MERIDIANO YIN, EXTINGUE VENTO INTERNO EM SITUAÇÕES AGUDAS, SE POÇO DE MERIDIANO YANG EXPELE VENTO DE OBSTRUÇÕES DOLOROSAS FOGO PONTOS MANANCIAIS, C8, P10, PC8, F2, BP2, R2, IG5, ID5, E41 - DISPERSA CALOR/FOGO ASSOCIADO A OUTROS FATORES OU ISOLADOS UMIDADE/FLEUMA PONTOS RIACHO, CURA SECURA E FLEUMA, EXCETO C7 E R3, USANDO-SE PC7 (INCLUINDO PARA CORAÇÃO), P9, BP3, F3, R3, E36, VB34, B40, IG11, ID8 (AQUECEDOR SUPERIOR), TA10 (AQUECEDOR SUPERIOR) FRIO PONTOS MAR, CURA FRIO, EXCETO C3, PC3, LIBERADOS P5, F8, BP9, R10. SECURA/ RIO - NÃO USA NESSA ABORDAGEMCORREÇÃO DE EXCESSO E DEFICIÊNCIA PELOS PONTOS SHU ANTIGOS ABORDAGEM DEVE SER ÚNICA \n\n\nAJUSTE DE ZANG FU PELO SHU ANTIGO \n\nEXCESSO: SEDAR FILHO + TONIFICAR AVÔ + SEDAR MANANCIAL(YIN/YING) +/- TONIFICAR PONTO YUAN \n\nDEFICIÊNCIA: TONIFICAR MÃE + SEDAR AVÔ + TONIFICAR MAR(HE) +/- TONIFICAR PONTO YUAN \n\nE.G.1: EXCESSO DE YIN DE PULMÃO (FRIO CHEIO) (METAL, P8, REPRESENTA O PULMÃO, COMO O C8 REPRESENTARIA O CORAÇÃO, POR SER FOGO), SEDAR FILHO (RIM/AGUA) SEDARIA O P5. TONIFICAR AVÔ EM SUA COLUNA PRÓPRIA, C8 (C8 = CORAÇÃO/FOGO). SEDAR MANANCIAL/YIN DE PULMÃO, P10. E.G.2: EXCESSO YANG (CALOR CHEIO) DE FÍGADO: TABELA YANG, FÍGADO = MADEIRA, CENTRAL=VB41, SEDAR (FILHO) VB43, TONIFICAR (AVÔ) ID1, SEDAR MANANCIAL(YING) VB43. E.G.3: DEF YIN DE RIM (TABELA YIN), CENTRAL DO RIM É ÁGUA, REPRESENTARIA O R10. TONIFICAR (MÃE) R7, SEDAR (AVÔ/COLUNA PRÓPRIA, AVÔ DE RIM É BP E SEU ELEMENTO É TERRA) BP3, TONIFICAR MAR DE RIM (HO) R10. \n\n\nTABELA DE PONTOS YIN \n\n1 MADEIRA 2 FOGO 3 TERRA 4 METAL 5 MAR \n1 POÇO 2 MANANCIAL 3 RIACHO 4 RIO 5 MAR \nPULMÃO 1 P11 2 P10 3 P9 4 P8 5 P5 \nPERICÁRDIO 1 PC9 2 PC8 3 PC7 4 PC5 5 PC3 \nCORAÇÃO 1 C9 2 C8 3 C7 4 C4 5 C3 \nBAÇO 1 BP1 2 BP2 3 BP3 4 BP5 6 BP9 \nFÍGADO 1 F1 2 F2 3 F3 4 F4 5 F8 \nRIM 1 R1 2 R2 3 R3 4 R7 5 R10 \n\n\nTABELA DE PONTOS YANG \n\n1 METAL 2 ÁGUA 3 MADEIRA 4 FOGO 5 TERRA \n1 POÇO 2 MANANCIAL 3 RIACHO 4 RIO 5 MAR \nINTESTINO GROSSO 1 IG1 2 IG2 3 IG3 4 IG5 5 IG11 \nTRIPLO AQUECEDOR 1 TA1 2 TA2 3 TA3 4 TA6 5 TA10 \nINTESTINO DELGADO 1 ID1 2 ID2 3 ID3 4 ID5 5 ID8 \nESTÔMAGO 1 E45 2 E44 3 E43 4 E41 5 E36 \nVESÍCULA 1 VB44 2 VB43 3 VB41 4 VB38 5 VB34 \nBEXIGA 1 B67 2 B66 3 B65 4 B60 5 B54\n\n')
                print('Ao momento em prescrição: ')
                if len(pool3) > 0:
                    print(pool3)
                else:
                    print('Nada prescrito ainda...')
                lemb = input(
                    '\n\nAnotações para prescrição (ou enter para voltar): ').upper()
                if lemb == '':
                    print('\n\nNada foi adicionado. Retornando...\n')
                    time.sleep(1)
                else:
                    lembrete.add(lemb)
            if pipe == 8:
                print('\nPONTOS LUO (CONEXÃO)\n\nP7, IG6, BP4, E40, ID7, C5, R4, B58, TA5, PC6, F5, VB37, BP21 (2 DO BAÇO), VC15, VG1 \n\nCONEXÃO YIN/YANG DE UM MERIDIANO AO REDOR DO CANAL, DOENÇA CRÔNICA E PROFUNDA BP/E TEM 2 LUO, ALÉM DO VG E VC LOCAIS DE FÁCIL ESTAGNAÇÃO DE QI OU XUE, HORIZONTAIS (JING MAI SÃO VERTICAIS E LUO MAI SÃO HORIZONTAIS), FICAM A NÍVEL DE COU LI. \n\nUSO DE YUAN COM LUO DE MERIDIANO COMPLEMENTAR PARA DAR FLUXO. \n\nLATERALIDADE: YUAN EM LADO ACOMETIDO E LUO EM LADO OPOSTO, AMBOS TONIFICADOS.\nP9 [YUAN=LADO ACOMETIDO]/IG6: OPRESSÃO TÓRAX, PALMA QUENTE, TOSSE, EDEMA DE OROFARINGE, RESSECAMENTO OROFARÍNGEO, SUDORESE, DOR EM OMBRO, DOR MAMÁRIA, EXPECTORAÇÃO (FLEUMA), DISPNÉIA.\nIG4 [YUAN=LADO ACOMETIDO]/P7: DOR DENTÁRIA, GENGIVITE, CONJUNTIVAS AMARELAS, XEROSTOMIA, EPISTAXE, EDEMA DE OROFARINGE, DOR EM OMBRO\nBP3 [YUAN=LADO ACOMETIDO]/E40: RIGIDEZ DE LÍNGUA, REFLUXO ÁCIDO, VÔMITOS, DISTENSÃO ABDOMINAL, SENSAÇÃO DE PESO, CONSTIPAÇÃO, ASTENIA, EDEMA DE MMII\nE42 [YUAN=LADO ACOMETIDO]/BP4: PLENITUDE E DISTENSÃO ABDOMINAL, OPRESSÃO TORÁCICA, EPISTAXE, FLEUMA, DOR EM PÉ, DOR EM TORNOZELO\nC7 [YUAN=LADO ACOMETIDO]/ID7: DOR RETROESTERNAL, RESSECAMENTO OROFARÍNGEO, SEDE, ICTERÍCIA, XEROSTOMIA, PALMAS QUENTES, PALPITAÇÕES, PAVOR, HEMATÊMESE\nID4 [YUAN=LADO ACOMETIDO]/C5: RIGIDEZ NUCAL, EDEMA E DOR OROFARÍNGEO, DOR EM OMBRO, SURDEZ, CONJUNTIVAS AMARELADAS, DOR LATERAL DE BRAÇOS\nR3 [YUAN=LADO ACOMETIDO]/B58: COMPLEIÇÃO ESCURECIDA, ADIPSIA, HIPERSSONIA, REDUÇÃO DE VISÃO, SENSAÇÃO DE CALOR, DORSALGIA, FRAQUEZA DE MMII, DISPNÉIA, TIMIDEZ\nB64 [YUAN=LADO ACOMETIDO]/R4: DOR OCULAR, DOR EM PESCOÇO/COSTAS/LOMBAR, MANIA, EPILEPSIA, OPISTÓTONO, DOR EM REGIÃO DE SOMBRANCELHAS, EPISTAXE, CONJUNTIVAS AMARELADAS, CONTRAÇÃO DE TENDÕES, PROLAPSO ANAL\nTA4 [YUAN=LADO ACOMETIDO]/PC6: TINIDO, SURDEZ, EDEMA OROFARÍNGEO, RESSECAMENTO DE OROFARINGE, EDEMA PALPEBRAL, OTALGIA, SUDORESE, DOR INTERESCAPULAR, DOR EM COTOVELO, CONSTIPAÇÃO INTESTINAL, INCONTINÊNCIA URINÁRIA, RETENÇÃO URINÁRIA\nPC7 [YUAN=LADO ACOMETIDO]/TA5: CONTRATURA DE PALMAS, DOR EM BRAÇO, OMBRO CONGELADO, PLENITUDE TORÁCICA, TUMEFAÇÃO AXILAR, PALPITAÇÕES, FACE VERMELHA, CONJUNTIVAS AMARELAS, RISOS E CHORO\nF3 [YUAN=LADO ACOMETIDO]/VB37: DISTENSÃO ABDOMINAL (UTERINA TAMBÉM), PLENITUDE TORÁCICA, HÉRNIA, RETENÇÃO, INCONTINÊNCIA URINÁRIA\nVB40 [YUAN=LADO ACOMETIDO]/F5: COMPLEIÇÃO CANSADA, CEFALÉIA, DOR OCULAR, EDEMA DE PESCOÇO, BÓCIO, DOR EM HIPOCÔNDRIOS, TUMEFAÇÃO E HIPERIDROSE AXILAR\n\nLIVRO CONVIDADO-HOSPEDEIRO, 1601. TONIFICAR AMBOS, PRIMEIRO É FONTE E SEGUNDO É CONEXÃO. PONTOS DE RELEVÂNCIA CASO USO DE 1 PONTO LUO, USAR LADO OPOSTO DO LADO DE SINTOMA.\n\nA GRANDE PICADA\nA GRANDE PICADA\nUSADO EM DOR HEMILATERAL (SÓ NO DIREITO E ESQUERDO NÃO) OU CIMA E NÃO EMBAIXO (E VICE-VERSA)\nUSO SOMENTE PARA DOR\nPONTO LUO SEDADO EM LADO DE DOR E TONIFICADO MESMO PONTO LUO EM LADO OPOSTO\n\n')
                print('Ao momento em prescrição: ')
                if len(pool3) > 0:
                    print(pool3)
                else:
                    print('Nada prescrito ainda...')
                lemb = input(
                    '\n\nAnotações para prescrição (ou enter para voltar): ').upper()
                if lemb == '':
                    print('\n\nNada foi adicionado. Retornando...\n')
                    time.sleep(1)
                else:
                    lembrete.add(lemb)
            if pipe == 9:
                print('\n\nPONTOS XI - ACÚMULO\n\nXI = DOBRA, LOCALIZAM ENTRE DEDOS E ENTRE JOELHOS/COTOVELOS, USAM EM DOENÇAS DE EXCESSO E COM DOR OU AGUDAS, USADOS PARA ESTANCAR SANGRAMENTOS\n\n\nPONTO XI: P(P6), PC(PC4), C(C6), IG(IG7), TA(TA7), ID(ID6), E(E34), VB(VB36), B(B63), BP(BP8), F(F6), R(R5), YANGQIAO(B59), YINQIAO(R8), YANGWEI(VB35), YINWEI(R9)\n\n\nLOCAL DE ACÚMULO DE XIE QI, USADO PARA DOENÇAS GRAVES INFECCIOSAS OU HEMORRÁGICAS\nUSO, POR EXEMPLO, P6-ASMA/HEMOPTISE; IG7-VOLVO, RCU; E34-GASTRITE, MASTALGIA, DOR EM JOELHO; BP8-DISMENORRÉIA, MENORRAGIA; C6-IAM; ID6-DOR INTENSA ESCAPULAR, DOR OCULAR; B63-HÉRNIA, APENDICITE; F6-MENORRAGIA (B63+F6-CISTITE); R5-HEMATÚRIA, CÁLCULO RENAL; PC4DOR TORÁCICA, EPISTAXE, IAM; TA7-DOR NO BRAÇO, FADIGA PÓS-VIRAL; VB36-DOR AO LONGO DO CANAL DE VB\n\n')
                print()
                print('Ao momento em prescrição: ')
                if len(pool3) > 0:
                    print(pool3)
                else:
                    print('Nada prescrito ainda...')
                lemb = input(
                    '\n\nAnotações para prescrição (ou enter para voltar): ').upper()
                if lemb == '':
                    print('\n\nNada foi adicionado. Retornando...\n')
                    time.sleep(1)
                else:
                    lembrete.add(lemb)
            if pipe == 10:
                print('\n\nPONTOS HUI - INFLUÊNCIA\n\nTONIFICA ÓRGÃO MOVENDO BASTANTE QI E SANGUE PARA TRATAMENTOS DE DEFICIÊNCIA COM MÚLTIPLOS PROBLEMAS EM MESMO SISTEMA, USADOS EM TONIFICAÇÃO.\n\n\nPONTO HUE: ZANG(ÓRGÃOS)-F13, FU(VÍSCERAS)-VC12, QI-VC17, XUE-B17, TENDÃO-VB34, VASCULAR-P9, OSSO-B11, MEDULA/CÉREBRO-VB39\n\n\nPARA USO COM O PONTO XI EM DOENÇAS INFECCIOSAS, SENDO ESTE O SUBTIPO DE TRATAMENTO PARA A DOENÇA, USO COM 2 PROBLEMAS EM MESMO ÓRGÃO (E.G. ESTAGNAÇÃO DE XUE DE FÍGADO E DEFICIÊNCIA DE QI DE FÍGADO)\nPONTO DE XUE (B17) USO SOMENTE MOXA TONIFICA SANGUE, AGULHAMENTO EM TONIFICAÇÃO REMOVE ESTAGNAÇÃO DE XUE.\n\n')
                print()
                print('Ao momento em prescrição: ')
                if len(pool3) > 0:
                    print(pool3)
                else:
                    print('Nada prescrito ainda...')
                lemb = input(
                    '\n\nAnotações para prescrição (ou enter para voltar): ').upper()
                if lemb == '':
                    print('\n\nNada foi adicionado. Retornando...\n')
                    time.sleep(1)
                else:
                    lembrete.add(lemb)
            if pipe == 11:
                print('\nSHENS\n\nPONTOS DE TRATAMENTO PSIQUIÁTRICO POR PONTOS DE RESIDÊNCIA DE MORADA (SHEN) B42 - PO (HOMEOSTASE/IMUNIDADE) (REDUZ EFEITO EMOCIONAL SOBRE ZHANG) B44 - SHEN (XIANG/ SABEDORIA/ SUPEREGO) B47 - HUN [ID/ VOLEMIA DE HUMOR - DEPRESSÃO (BAIXO HUN) E MANIA (EXCESSO DE HUN)]FF5 B49 - YI (CONCENTRAÇÃO/ MEMORIZAÇÃO) B52 - ZHI (PROJETOS/ SONHOS) B43 (GAOHUANG) - MOLÉSTIA CRÔNICA INCURÁVEL AUMENTAR PO (CURA IMPOTÊNCIA E IMUNIDADE) #VB40# RETER PO (MELHORA DE ALERGIA E COMPULSÃO SEXUAL) #F3# AUMENTAR O SHEN CONTROLA O HUN.\n\nO QUE É SHEN\n\nSHEN = ESPÍRITO (DIVIDE EM 5 SHENS) (PODE REFERIR AO XIANG EM CERTAS TRADUÇÕES MESMO SENDO ATRIBUÍDA A GRUPO MAIOR E A SUBCATEGORIA SE NOMEADA IDENTICAMENTE) HUN/ FÍGADO: ALMA ETÉRIA, F, +HUN=MANIA, -HUN=DEPRESSÃO - ID PO/ PULMÃO - CORPO: , ENTRADA/SAÍDA DE DOENÇAS, ASSOCIADO COM PELE DE FANTASMA (ALMA OU ENERGIA EXTRACORPÓREA, ENERGIA MATERIALIZADA INVISÍVEL COM ACESSO A PLANO ESPIRITUAL E ENVELOPANDO CORPO (PORÉM COM LEVE CONSCIÊNCIA PRÓPRIA INVOLUNTÁRIA), GASTA-SE COM IDADE E DOENÇAS (OCORRE COMA SE PERDA DE PO), MANTÉM POSSÍVEL PERMUTA DE CORPO A PERCEPÇÃO EXTRA-COPÓREA, SENDO ASSOCIADA A  DISTÚRBIOS DOLOROSOS, EMOCIONAIS E ALUCINANTES ASSOCIADOS A FIGURAS DE MORTOS), GERA PRURIDO AO SER ATIVADO, DOR DE INVASÃO EM TENDER POINTS DA FIBROMIALGIA COM CONTRATURAS, SE BAIXO HÁ VONTADE DE SUICÍDIO, SE BAIXO PO PESSOA É VULNERÁVEL A SENTIMENTOS EMPÁTICOS NEGATIVOS, SE HOUVER EXCESSO OCORRE PERCEPÇÃO EXTRASSENSORIAL (USANDO-SE EM TRATAMENTOS DE ESQUIZOFRENIA) YI/ BAÇO - INTELECTO: COGNIÇÃO, CONCENTRAÇÃO, MEMORIZAÇÃO ZHI/ RIM - FORÇA DE VONTADE: PERSEVERANÇA, RESILIÊNCIA XIANG/ CORAÇÃO - CÉREBRO GERAL: FUNÇÕES NÃO ASSOCIADAS A CONIÇÃO, CONTROLA O HUN - SUPEREGO, COMO TAL (CÉREBRO) ELE ALOCA FUNÇÕES COGNITIVAS (E NÃO AS CONTROLA) E ALOCA (E CONTROLA) OS SENTIMENTOS (SE BAIXO HÁ DISTIMIA, EMBOTAMENTO) VER SHU DORSAIS EM ÁREAS DE AVALIAÇÃO XIANG: CASA DA MENTE ZHI: QUARTO DA MENTE YI: SALA DE ESTAR DA MENTE HUN: PORTA DA MENTE PO: JANELA DA MENTE \n\n')
                print('Ao momento em prescrição: ')
                if len(pool3) > 0:
                    print(pool3)
                else:
                    print('Nada prescrito ainda...')
                lemb = input(
                    '\n\nAnotações para prescrição (ou enter para voltar): ').upper()
                if lemb == '':
                    print('\n\nNada foi adicionado. Retornando...\n')
                    time.sleep(1)
                else:
                    lembrete.add(lemb)
            if pipe == 12:
                print('\n\n\nPONTOS HO\n\n E(E36), IG(E37), ID(E39), VB(VB34), B(B54), TA(B39) \n\nUSADO PARA DOENÇA DE VÍSCERAS. \n\n')
                print('Ao momento em prescrição: ')
                if len(pool3) > 0:
                    print(pool3)
                else:
                    print('Nada prescrito ainda...')
                lemb = input(
                    '\n\nAnotações para prescrição (ou enter para voltar): ').upper()
                if lemb == '':
                    print('\n\nNada foi adicionado. Retornando...\n')
                    time.sleep(1)
                else:
                    lembrete.add(lemb)
            if pipe == 13:
                print('PONTOS EXTRAS DELIMITADOS NO PROGRAMA CONFORME ESTA LISTA:\n\n')
                nota1={'EX1':'SI-SHEN-TSUNG - CEFALÉIA, VERTIGEM, CONVULSÃO, DISTÚRBIO MENTAL','EX2':'JIA-SHANG-XING - RINITE, POLIPOSE NASAL','EX3':'DANG-YANG - CONJUNTIVITE, VERTIGEM, RESFRIADO, CONGESTÃO NASAL','EX4':'ER-ZHUNG - HORDÉOLO, VERTIGEM','EX5':'YIN-TANG - DOENÇAS OLHO-NARIZ: CONJUNTIVITE ALÉRGICA, DACRIOCISTITE','EX6':'SHAN-QUEN - VERTIGEM ROTACIONAL','EX7':'TOU-KUANG-MIN - PARALISIA OCULAR, ENXAQUECA, HORDÉOLO','EX8':'YU-YAO - PTERÍGIO, CONJUNTIVITE, PARALISIA OFTÁLMICA','EX9':'YU-WEI - ENXAQUECA, PROBLEMAS OCULARES DIVERSOS','EX10':'CHIU-HOU - OFTALMOPATIAS','EX11':'JIEN-MIN - CATARATA, DMRI, RINITE, ESTRABISMO, DACRIOCISTITE','EX12':'TAI-YANG - DOR OCULAR','EX13':'ER-JIAN - TRACOMA, PTERÍGIO, CEFALÉIA TENSIONAL','EX14':'LUNG-XUE - SURDEZ','EX15':'HOU-TING-HWEI - TINNITUS','EX16':'YI-MING - AMETROPIA, CATARATA, INSÔNIA','EX17':'SHANG-YING-HSIANG - TUMORES DE RINOFARINGE','EX18':'JIAN-BI - RINITE','EX19':'BI-TUNG - CONGESTÃO NASAL E PARALISIA FACIAL','EX20':'SAN-XIAO - ESPASMO FACIAL, PARALISIA FACIAL, OBSTRUÇÃO NASAL','EX21':'TI-HOU - DOR DENTAL (ARCADA INFERIOR), EDEMA DE FACE, PARALISIA FACIAL','EX22':'JINJING-YUYE - ESTOMATITE, AMIGDALITE, AFONIA','EX23':'SHAN-LIAN-CHUAN - SIALORRÉIA, AFASIA, MUDEZ','EX24':'WAI-JINJING-YUYE - SIALORRÉIA, AFASIA, MUDEZ','EX25':'LUO-JING - TORCICOLO, ESPONDILITE CERVICAL','EX26':'XING-SHI - DOR ESCAPULAR IRRADIANDO A CERVICAL, CEFALÉIA TENSIONAL','EX27':'BAI-LAO - TRAUMA DE NUCA, HIPERTERMIA PÓS-PARTO, TORCICOLO','EX28':'TSUNG-GU - RESFRIADO, MALÁRIA, BRONQUITE, EPILEPSIA, VÔMITOS','EX29':'CHIAN-CHENG - PARALISIA FACIAL, ESTOMATITE','EX30':'AN-MIN-1 - INSÔNIA, ENXAQUECA, ESQUIZOFRENIA','EX31':'AN-MIN-2 - ESQUIZOFRENIA','EX32':'XING-FENG - HIPERSSONIA, CATATONIA, NARCOLEPSIA','EX33':'CHI-XUE - ASMA, PLEURITE, NEVRALGIA INTERCOSTAL','EX34':'TAN-CHUAN - ASMA, ENFISEMA','EX35':'TSOUYI | YOUYI - MASTITE, NEVRALGIA INTERCOSTAL','EX36':'MEI-HUA - GASTRITE, DISPEPSIA, ÚLCERA PÉPTICA','EX37':'SHI-TSANG - IMPOTÊNCIA, MENORRAGIA, DISPEPSIA','EX38':'SHI-KUAN - SOLUÇO, DRGE','EX39':'WAI-SI-MAN - DISMENORRÉIA','EX40':'JUE-YUN - ESTERELIDADE E DIARRÉIA (ENDOMETRIOSE INTESTINAL)','EX41':'YI-JING - ESPERMATORRÉIA, EJACULAÇÃO PRECOCE, DERMATITE DE ESCROTO','EX42':'WEI-BAO - PROLAPSO UTERINO','EX43':'CHANG-YI - LEUCORRÉIA, DOR GENITAL, CORRIMENTO E ORQUITE','EX44':'TSI-KUNG | ZIGONG - ENDOMETRIOSE','EX45':'TI-TUO - HÉRNIA ABDOMINAL','EX46':'TSUNG-JIAN - PROLAPSO UTERINO','EX47':'HENG-WEN - SUDORESE, FRAQUEZA EM PERNAS','EX48':'CHUAN-XI - ALERGIA','EX49':'TING-CHUAN | DINGCHUAN - ASMA','EX50':'WAI-TING-CHUAN - ASMA','EX51':'BA-HUA - INSUFICIÊNCIA RESPIRATÓRIA CRÔNICA, BAIXO JING NA ASMA','EX52':'ZHU-TSE - DOR TORÁCICA E ABDOMINAL INCURÁVEL, LOMBALGIA, ASMA','EX53':'JU-JUE-SHU - CARDIOPATIA, NEURASTENIA, NEVRALGIA INTERCOSTAL','EX54':'WEI-RE-XUE - DOENÇAS GÁSTRICAS, DOR DENTAL','EX55':'ZHONG-CHUAN - DORSALGIA','EX56':'PI-RE-XUE - PANCREATITE, ESPLENOMEGALIA','EX57':'SHEN-RE-XUE - NEFROPATIAS','EX58':'CHI-CHUAN - PLEURITE, PALPITAÇÃO','EX59':'KUEI-YANG-XUE - ÚLCERA PÉPTICA','EX60':'PI-GEN - HEPATOESPLENOMEGALIA, GASTRITE COM LOMBALGIA','EX61':'XUE-CHOU - HEMOPTISE, HEMATÊMESE, MELENA','EX62':'JI-JU-PI-KUAI - CÂNCER DE OVÁRIO, ENTERITE','EX63':'WEI-XU - DOR E ESPASMO GÁSTRICO','EX64':'YAO-YI - LOMBALGIA','EX65':'YAO-YIAN - INFECÇÃO GENITAL, ISTS','EX66':'CHONG-KUNG - LOMBALGIA','EX67':'JIU-JI - MENORRAGIA','EX68':'TUN-ZHUNG - PARESIA DE MMII, PARALISIA','EX69':'HUAN-ZHUNG - DOR CIÁTICA','EX70':'HUA-TUO-JIA-JI-XUE - INFLAMAÇÃO GASTROINTESTINAL, GONADAL E UROLÓGICA','EX71':'TSOU-GU - DOR CIÁTICA','EX72':'SHI-CHI-ZUI-XIA | SHIQUIHUIXIA - DOR CIÁTICA','EX73':'SHI-XUAN - SÍNCOPE, CALOR TÓXICO, CONVULSÃO','EX74':'JIU-TIEN-FENG - VITILIGO','EX75':'SI-FUNG - VÔMITOS INFANTIS, TOSSE','EX76':'SHOU-ZHONG-PING - LESÃO OROFARINGE','EX77':'YA-TUNG - DOR DENTÁRIA','EX78':'SHANG-HOUXI - MUDEZ, SURDEZ','EX79':'TA-GU-KUNG - OFTALMOPATIAS','EX80':'ZHONG-KUEI - EPIGASTRALGIA, VITILIGO, INAPETÊNCIA, SOLUÇO','EX81':'BA-XIE - ARTRITE, PICADA DE COBRA','EX82':'LUO-JEN | LUO-ZHEN - TORCICOLO, DOR OMBRO-BRAÇO, DRGE','EX83':'WAI-LAO-KUNG - PARESIA DE MMSS, PARESTESIA MMSS','EX84':'ER-BAI - HEMORRÓIDAS, PROLAPSO RETAL, DOR ANTEBRAÇO','EX85':'TSUN-PIN - CRISE DE PÂNICO','EX86':'NEU-SHANG-XUE - TRAUMA LOMBAR E TRAUMA RAQUIMEDULAR, TORÇÃO DE QUADRIL','EX87':'BEI-ZHONG - HIPOTONIA DE MMSS','EX88':'ZE-CHIAN - HIPERTIREOIDISMO, CONTRATURA DE BRAÇO','EX89':'JIAN-SAN-JEN - DOR EM OMBRO, FRAQUEZA DE MMSS, OMBRO CONGELADO','EX90':'JIAN-SHU - DOR EM OMBRO','EX91':'ZHU-PEI - BURSITE DE OMBRO','EX92':'TAI-JIAN - ARTRITE DE OMBRO','EX93':'CHIEN-HOU-YINJU - PIODERMITE DE MMII, FASCITE PLANTAR, HAS','EX94':'TSU-XIN - MENORRAGIA, ESPASMO GASTROCNÊMIO','EX95':'SHIH-MIN - INSÔNIA, FASCITE CALCIFICADA','EX96':'BA-FENG - CEFALÉIA, MALÁRIA, EDEMA DE MMII, PICADA DE COBRA','EX97':'NUI-SHI - GENGIVITE','EX98':'NAO-CHING | NAOQING - DEMÊNCIA, SONOLÊNCIA, TONTURA, AMNÉSIA','EX99':'JIU-WAI-FAN - PÉ INVERTIDO, VARO, PARA DENTRO, PARALISIA CEREBRAL','EX100':'JIU-NEI-FAN - POLIOMIELITE','EX101':'JING-XIA - PARAPLEGIA','EX102':'WAN-LI - OFTALMOPATIAS','EX103':'LAU-WEI | LAN-WEI-XUE - APENDICITE','EX104':'CHI-YEN | XIYAN - TENDINITE JOELHO','EX105':'CHI-XIA - CANELITE, ESPASMO DE PANTURRILHA','EX106':'DAN-NANG-DIEN | DANNANGXUE - COLECISTITE, NEFROLITÍASE','EX107':'LING-HOU - PARAPLEGIA, TENDINITE JOELHO','EX108':'HER-TING | HEDING - DOR DE JELHO, PARALISIA','EX109':'LING-XIA - SURDEZ, COLECISTITE','EX110':'CHIEN-FENG-SHI - ALTERAÇÃO DE MARCHA','EX111':'SHANG-FENG-XI - DOR CIÁTICA','EX112':'SHEN-XI - DIABETES','EX113':'BAI-CHONG-WO - ALERGIA, ARTROSES','EX114':'YIN-WEI-1 - MANIA','EX115':'YIN-WEI-2 - MANIA','EX116':'YIN-WEI-3 - MANIA','EX117':'SI-LIEN - DEPRESSÃO','EX118':'WU-LING - ALTERAÇÃO DE COMPORTAMENTO','EX119':'LING-BAO - DISTÚRBIO DE PERSONALIDADE','EX120':'XIN-JIAN - DOR E PARALISIA DE PERNAS','EX121':'JING-ZHONG - DISMENORRÉIA','EX122':'QI-MEN - INFERTILIDADE','EX123':'JING-GONG - NUTRE JING DE RIM, INFERTILIDADE','EX124':'JIAN-NEI-LING - DOR OMBRO UMIDADE-FRIO, DOR EM PESO COM ENTORPECIMENTO','EX125':'NEI-MA-DIAN - DOR EM PÓS-OPERATÓRIO','EX126':'YAO-TONG-XUE - DOR LOMBAR COM TENSÃO','EX127':'QI-PANG - CA BEXIGA, CA UTERO, CA PÊNIS, CA VULVAR'}
                [print(key, ' : ', value) for key, value in nota1.items()]
                print('\n\nPOR ESPECIALIDADES DE FUNÇÕES:')
                print('ALERGOLOGIA: 48 49 50')
                print('CARDIOLOGIA: 53 58')
                print('ALERGOLOGIA: 48 49 50')
                print('CIRURGIA: 103 106 109 125')
                print('DERMATOLOGIA: 74')
                print('ENDOCRINOLOGIA: 48 88 112 123')
                print('GASTROENTEROLOGIA: 29 36 38 54 59 61 63 76 77 80 84 97')
                print('GENECOLOGIA: 35 39 40 42 44 46 67 121 122')
                print('HEMATOLOGIA: 56 60')
                print('INFECTOLOGIA 65 96')
                print('ALERGOLOGIA: 48 49 50')
                print('NEFROLOGIA: 21 57')
                print('NEUROLOGIA: 7 19 20 23 24 27 68 78 83 87 98 100 101 110')
                print('OFTALMOLOGIA: 4 5 8 9 10 11 12 13 16 79 102 ')
                print('ONCOLOGIA: 62 70 73 127')
                print('OTORRINOLARINGOLOGIA: 2 3 6 14 15 17 18 22')
                print('ORTOPEDIA: 25 26 52 55 64 66 69 71 72 82 86 89 90 91 92 93 94 95 99 104 105 107 108 111 113 120 124 126')
                print('PEDRIATRIA: 75')
                print('PNEUMOLOGIA: 28 33 34 51')
                print('PSIQUIATRIA: 1 30 31 32 37 85 114 115 116 117 118 119')
                print('REUMATOLOGIA: 81')
                print('UROLOGIA: 41 43 45')
                print('\n\nPOR LOCALIZAÇÃO DO PONTO:')
                print('CABEÇA/ PESCOÇO: 1-32')
                print('ABDOME: 33-47, 121, 122, 127')
                print('DORSAL: 48-72, 123')
                print('MEMBROS SUPERIORES: 73-92, 124, 126')
                print('MEMBROS INFERIORES: 93-120, 125\n\n')
                if len(lembrete) > 0:
                    print(lembrete)
                else:
                    print('Sem lembretes anotados...')                    
                lemb = input(
                    '\n\nAnotações para prescrição (ou enter para voltar): ').upper()
                if lemb == '':
                    print('\n\nNada foi adicionado. Retornando...\n')
                    time.sleep(1)
                else:
                    lembrete.add(lemb)
            if pipe == 14:
                print('\nVENTOSA\n\nUSO EM TORÇAO, CONTUSÃO, TENDINITE, ATROFIA MUSCULAR, PARALISIA TAMBÉM EM ASMA, BRONQUITE E INTESTINO IRRITÁVEL. \n\nTIPOS: H - TIPO SAN-KUAN APLICAÇÃO DE 1 MINUTO ATÉ TER HIPEREMIA \nA - TSUO-KUAN APLICAÇÃO COM ARRASTO SOBRE O LOCAL \nC - CHUN-HSHEI-SHIN-KUAN APLICAR ATÉ COR VERMELHA CONGESTIONADA \nE - UI-HSHEI-SHIN-KUAN CONTATO COM SANGUE POR EQUIMOSE\n\nRESFRIADO: EX12/H, IN-IAN/H, IG4/H, CHIEN-OU/H, TAY-YANG/H, DM14/E CEFALÉIA: DM14/E, TAY-YANG/H REUMATISMO: DM14/I, IG11/I, B40/I, DM4/I ASMA: B11/H, DM12/H, REN12/H, REN6 /H,MAMILOS/H, REGIÃO DORSO-ESCAPULAR/H EPIGASTRALGIA: REN12, E36, PC6, B20, B21 SOLUÇO: B11, B13, REN12 DIARRÉIA: E25 (LADO ESQUERDO), REN3 VÔMITO: E25, REN6, REN4, B20, BP6 DOR ABDOMINAL: E25, PEN12, REN6, LOCAL DE DOR/H DOR TORÁCICA: LOCAL LOMBALGIA: B23/H, DM2/H, INTERESCAPULAR/E OMBRO DOLOROSO: DM14, DM12, B11, B13 DOR QUADRIL B23, BP10 LESÃO DE OMBRO/BRAÇO: B11, IG11, IG15 DOR NA PERNA: B40, B57, BP6 DISMENORRÉIA: R6, R3, R4, E25, B23, F3 LEUCORRÉIA: R4, R6, BP6 CONJUNTIVITE: TAY-YANG DOR ARTICULAR MMSS: IG15, IG11, TA5, IG4, LOCAL DOR ARTICULAR MMII: B30, E36, VB39, LOCAL LOMBALGIA: DM14, B23, DM4, B40 ENTORSE: LOCAL \n\n')
                print('Ao momento em prescrição: ')
                if len(pool3) > 0:
                    print(pool3)
                else:
                    print('Nada prescrito ainda...')
                lemb = input(
                    '\n\nAnotações para prescrição (ou enter para voltar): ').upper()
                if lemb == '':
                    print('\n\nNada foi adicionado. Retornando...\n')
                    time.sleep(1)
                else:
                    lembrete.add(lemb)
            if pipe == 15:
                print('\nPONTOS JANELA DO CÉU\n\nPONTOS PARA QI INVASOR DE CABEÇA (LITERAMENTE QI AFETANDO CÉREBRO) DESEQUILÍBRIO ENTRE QI DE CABEÇA E CORPO (MENTAL OU FÍSICO), SINTOMAS HIPOCONDRÍCOS, PSICOGÊNICOS, NEUROLÓGICOS COMPLEXOS ATÍPICOS E9, IG18, TA16, B10, P3, VC22, ID16, ID17, VB9, VG16, PC1\n\n')
                print('Ao momento em prescrição: ')
                if len(pool3) > 0:
                    print(pool3)
                else:
                    print('Nada prescrito ainda...')
                lemb = input(
                    '\n\nAnotações para prescrição (ou enter para voltar): ').upper()
                if lemb == '':
                    print('\n\nNada foi adicionado. Retornando...\n')
                    time.sleep(1)
                else:
                    lembrete.add(lemb)
            if pipe == 16:
                print('CORRELAÇÃO PARA PATOLOGIAS DA MEDICINA OCIDENTAL\n\n=== CABEÇA/PESCOÇO\n=== TÓRAX E ABDOME\n=== OSTEOESQUELÉTICO\n=== GINECOLOGIA E OBSTETRÍCIA\n=== NEUROPSIQUIATRIA E GERIATRIA\n\n')
                CABPESC = {'AMETROPIAS: GVB42 GVB37', 'ANOSMIA: GB15 GVG4 GVC19', 'CATARATA: GVB2 GTA4 GTA17 GIG20', 'CEFALÉIA EM LEVEZA (SHAO YIN): GVB2 GB63', 'CEFALÉIA ENXAQUECA (SHAO YANG): GF3 GIG2 GE36 GIG5', 'CEFALÉIA FRONTAL (YANG MING): GR6', 'CEFALÉIA SUNA EM CAPACETE ( TAI YIN): SIG2 SIG5 GTA21 GVC24 GTA23', 'CEFALÉIA SUNCT PARIETAL (JUE YIN): SIG2 SIG5', 'CEFALÉIA TENSIONAL (TAI YANG): GVG20 GF3 GR6 GBP6 GVC22 GVC22 GIG18 GIG4 GTA2', 'CEGUEIRA: GVG20 GTA17 GVG20 GVG8 GVB40 GF3 WTA2 XB18', 'COJUNTIVITE: GTA5 GVB41 GB1 GVB14 GB62 GP7', 'COMA: GVG23 GVB20 GIG4 GE36 GF2 WF3', 'DISFONIA: GVB3 GVB5 GBP6', 'DOENÇA MACULAR: GVB20 GB2 GP7 GIG4 GE36 GE9 WBP2 GVG20 GVG23 XB23 XVG4', 'DOR DENTÁRIA: GE45 GID18 GE8 GE41 GVG23 GVG24', 'DOR NUCAL: GB2 GVB14 GID18 GTA17 WE5', 'DTM: GB10 GVB20 GVG25 GR3 GID3 GB20', 'EDEMA CEREBRAL: GE7 GTA21 GTA17 GE5 GTA5 GVB34 WTA2',
                           'EDEMA DE FACE: GB10 GVB20 GVG16 GID3 GTA2 GID2 GID7', 'EDEMA LARÍNGEO: GB1', 'EPISTAXE: GB23 GVG4', 'ESTENOSE LARÍNGEA: GB18', 'GLOSSITE: GVB2', 'HALITOSE: GVG26 GVG21 GIG4 GE44', 'LACRIMAÇÃO: GVG23', 'LARINGITE: GIG20', 'MACROGLOSSIA: GE4 GE6', 'NEURALGIA TRIGEMINAL: GPC7 GE44', 'ODINOFAGIA: GIG20', 'OFTALMOPATIA: GB47 GB19', 'PARALISIA FACIAL: GID1 GB18', 'PARESTESIA FACIAL: GVB41 GE8 GB1 GF2', 'PAROTIDITE: GB2 GIG3', 'POLIPOSE NASAL: GB2 GIG3', 'PRURIDO OCULAR: GP3 GIG4', 'PTERÍGIO: GB7', 'RINITE: GVG28', 'SINUSOPATIA: GID5 GVB43', 'SURDEZ DE CONDUÇÃO: GR7', 'SURDEZ NEUROSSENSORIAL: GVC23 GPC9', 'TINNITUS: GVC23 GPC9', 'TINNITUS COM BAIXO JING RIM: GE36 GVB42 GVB2 GVB42 GTA21 GE36', 'TIREOIDOPATIA: GB57', 'TORCICOLO: WE36 WVB42', 'TRAUMA DE FACE: GVG26', 'VERTIGEM: GE10 GIG4 GPC6', 'XEROSTOMIA: GE40', }
                print('\nMEDICINA OCIDENTAL - CABEÇA/ PESCOÇO\n')
                for i in sorted(CABPESC):
                    print(i)
                TORABD = {'CÓLICA BILIAR: GB18 GB19 GIG4 GVC5 GF14', 'DOR GENITAL: GE34 GE35 GVB34 GBP9 GF8 WF3 GIG2 GTA2 GE44WP9 WP10 GVB1 GVB30', 'CÓLICA NEFRÉTICA: GB23 GB52 GB22 GVB25 GBP6 GR3 GE25', 'NEURALGIA INTERCOSTAL : GTA5 GVB41 GVB43 GTA6 WB18 WB19', 'CONSTIPAÇÃO INTESTINAL: GE25 GTA6 GR6 XF1', 'DISFAGIA: GVC22 GPC6', 'DOR ABDOMINAL: GE25 GPC6 GVC6 GE36 GBP4', 'DOR TORÁCICA: GVC17 GPC6', 'VÔMITO: GE36 GPC6 GVG16 GVC13 GVG16 ', 'PALPITAÇÃO: GPC6 GPC4 GF3 GBP9 GB57', 'DOR TORÁCICA SEM ANSIEDADE: GVC13 GVC12 GPC8 GPC7 GVC11 GPC6', 'ABDOME AGUDO: GVC11 GVC9 GPC6', 'LINFADENITE SUPURATIVA: GB39 GPC1', 'METEORISMO: GVC10 GE43 GE43', 'HEMORRÓIDAS: GVG1 GB57',
                          'DIARRÉIA COM BAIXO QI DE BP: GE25', 'DOR GÁSTRICA: GBP5 GVC12 GE36', 'DOR AXILAR: GTA6 GF13 ', 'DOR CONDRAL: GTA6 GF13 ', 'ASCITE: GIG6 GBP6 GVC9 GE36 GBP9 GVC9', 'MASTALGIA: GP9 GP7', 'COLESTASE: GB67 GE15', 'ÍLEO PARALÍTICO: GVG1 GF1', 'VOLVO: GVG1 GF1', 'DOR MESOGÁSTRICA: GBP9 GR1', 'DISPNÉIA: GE36 GVC22 GVC17', 'DRGE: GIG10 GE36 ', 'FLATULÊNCIA: GB11 GVG1', 'SOLUÇO: GVC6', 'TUMOR ABDOMINAL: GPC6 GR6', 'ASMA: GVC22 GVC17', 'ICTERÍCIA: GVG9 GID4 GVC12', 'ICC: GC9', 'IRC: GVB26 GVC4', 'HÉRNIA INGUINAL: GF1 GF14', 'PLEURITE: GVC17 GVC14', 'CISTITE INTERSTICIAL: GBP6 GR1', 'MELENA: GVG1 GB57', 'PROLAPSO RETAL: GVG20 GVC15 GVB36', }
                print('\nMEDICINA OCIDENTAL - TÓRAX E ABDOME\n')
                for i in sorted(TORABD):
                    print(i)
                OSTE = {'ARTRALGIA DEDOS MMSS: GIG4 GID3 WR7', 'ARTRITE AGUDA DE JOELHO: GVB34 GBP9', 'ARTRITE AGUDA DE PÉ: GBP5 GE41 GVB40', 'ARTRITE AGUDA MÃO OU BRAÇO: GTA3 GTA2', 'BURSITE TROCANTÉRICA: GP5 GP9 GIG11', 'CERVICOBRAQUIALGIA: GIG4 GF3 GB23 GE3 GIG15 GTA5', 'CLAUDICAÇÃO: GVB39 GVB30 GE33 GVB31', 'COMPRESSÃO MEDULAR: GE28 GVG8', 'COXARTROSE: GE36', 'DOR ADUTORES COXA: WF1 GVC2 WF2 WF10 WF8', 'DOR BRAQUIAL (LESÃO): GVB21', 'DOR CALCÂNEA: GE42 GR2 GR3 GE41 GE7', 'DOR CERVICAL: GB30 GB54', 'DOR CRÔNICA EM BRAÇO: GVB21', 'DOR EM TODA COLUNA: GVG1 GVG16 GB10 GVB20 GR6 GID3', 'DOR ESCAPULAR: GVB27 ', 'DOR GLENOUMERAL: GVB27 ', 'DOR LATERAL COXA: GE36 GIG4 GVB34', 'DOR MIOFASCIAL: GB65 GB10 GB26 GVB34 GID3 GVG16', 'DOR MMII: GVB30 GVB34 GID3 ', 'DOR OLECRANIANA: GTA10 GIG11 WP5 GTA5 GTA7 GTA2 GTA3 GVB41 GVB43', 'DOR OMBRO (ID): WVG20 WPC1 WTA16 ', 'DOR OMBRO (IG): GB67 GID18 GIG1 GTA1 GVB13B GP11', 'DOR ONCOLÓGICA: XB43 ', 'DOR REGIONAL COMPLEXA: GB65 GB10 GVB34', 'DOR TORNOZELO: GE41 GE42 GVB39 GE44 GVB41 GB65 GB66', 'EDEMA: GVC9 GVC6 ', 'EDEMA MMII: GVB39 GBP6 GE36', 'ENTORSE: GB57 GB60', 'ENTORSE TORNOZELO: GB63 GVB40 GVB21 GE36', 'EPICONDILITE LATERAL: GIG11 GIG10 GIG12 GP5 GIG4 GP7 GR6 GIG2 GIG3 GE43',
                        'EPICONDILITE MEDIAL: GC3 GID8 GID3 GPC6 GC6 WP9', 'FASCITE PLANTAR: GVB30 GF7 ', 'FIBROMIALGIA: GB65 GB10 GP7 GB9 GB10 GVB34 GF3 GID3 GVG16', 'GOTA: GB67 XVB34 GE36 GVB39 GBP9 GBP6', 'GOTA (PODAGRA): GBP5 GE41 GVB40', 'HEMIPLEGIA: GVB30', 'HÉRNIA LOMBAR: GID3 GB62 WVG2 WVG3 WVG4 GVB30', 'LINFANGITE: GB67 XVB34 GE36 GVB39 GBP9 GBP6', 'LOMBALGIA: GVG26 GB40', 'LOMBALGIA COM BAIXO QI DE RIM: GB15 GB23', 'MANGUITO ROTADOR: GE36 GIG15', 'METATARSALGIA: GE36 GF4 GF3', 'NEUROPATIAS: GB10 GB17 GF3 GID3 GVG16', 'OA JOELHO: GB67 XVB34 GE36 GVB39 GBP9 GBP6', 'OA PÉ: GE36 GVB39 GBP9 GBP6', 'OA PUNHO: GID4', 'OMBRO CONGELADO: GIG5 GTA14 GID9 GID10 GID11 GID15 GID16 ', 'PARESIA COTOVELO: GTA10 GIG11 WPC5 WIG5 WP9 WTA3 WP7', 'PARESTESIA COMPRESSIVA: GIG11 GIG4 GF3', 'PARESTESIA MMSS: GC3 GIG10', 'SÍNDROME FACETÁRIA: GID3 GB62 GB10 GB60 WR3 WR2 GTA5 GVB41 GVG4', 'TENDINITE (QUALQUER): GB47', 'TENOSSINOVITE FLEXOR ULNAR: GC7 GID4 GID3 GPC7 GR2 GR3 WC9', 'TENOSSINOVITE RADIOCARPINA: GP7 GP8 GIG4 GBP2 GP10 GP9 WC9', 'TETRAPARESIA (SÍND. WEI): GB13 GP5 GE44 GVC12 GIG11 WR3 WB18 SIG15 GVB39', 'TORCICOLO: GIG7 GF14', 'TREMORES MMSS: GIG11 GPC6 GTA5 GIG4 WF8 GIG16', 'TÚNEL DO CARPO: GPC7 GPC6 GPC7 GF2 GF3 GP11 GTA5 WC9', }
                print('\nMEDICINA OCIDENTAL - OSTEOESQUELÉTICO\n')
                for i in sorted(OSTE):
                    print(i)
                GO = {'ACREÇÃO PLACENTÁRIA: GBP6 GTA4', 'AMENORRÉIA SECUNDÁRIA: GR8 GB55', 'DISMENORRÉIA: GBP12 GE30', 'DISTÓCIA: GE25 GR5',
                      'HEMORRAGIA: GBP6 GR18', 'INFERTILIDADE: R1', 'LEUCORRÉIA: GVC6 GVC4', 'MASTITE: GE28', 'OLIGODRAMNIA: GVG7', 'SÍNDROME HELLP: GVB21', }
                print('\nMEDICINA OCIDENTAL - GINECOLOGIA E OBSTERÍCIA\n')
                for i in sorted(GO):
                    print(i)
                NEU = {'AFASIA (QUALQUER): GC7 GPC6', 'AFONIA: GVC4 GE36 GB43', 'AGITAÇÃO PSÍQUICA: GVG26', 'ANEMIA COM POLIDIPSIA: GVG14 GIG11 GIG4', 'ANSIEDADE AO SONHAR: GC7 GBP6 GR3', 'ARTROSE SISTÊMICA: GR4 GC7', 'ASTENIA: GE25', 'BURNOUT: GR1 GVC15', 'CA BEXIGA: GVC4', 'CA COLORRETAL: GVG26 GGB40 XVC4', 'CA MAMA: GVG26 GGB40 XVC4', 'CA TIREÓIDE: GVC4 GBP6', 'CALAFRIOS: GVB30 GVB29 GB54', 'CAQUEXIA: GVG9', 'CÓLERA: GC3 GE33', 'CÓLICA INFANTIL: GC5', 'CONVULSÃO FEBRIL: GE36', 'DÉFICIT COGNITIVO: GB15 GB23', 'DEPRESSÃO: GID7 GB58', 'DISPNÉIA E BAIXO YUAN: GE6 GE4 GF3', 'DOR CERVICAL AO TOSSIR: GVG15 GTA1', 'DOR TORÁCICA POR TOSSE: GIG17 GPC5', 'EPILEPSIA: GVG15', 'ESPERMATORRÉIA: GID19 GB20', 'FEBRE: GE13 GVC20', 'FEBRE DE ORIGEM INDETERMINADA: GVB34 GIG11', 'FEBRE INCESSANTE: GIG2 GC6', 'FEBRE SEM SUDORESE: GC5 GR4', 'GRIPE: GBP6 GVC6', 'HEMIPLEGIA: GID3 GVC13 GC7 GVG12 GVB13 GPC5',
                       'HIPERSSONIA: GE45 GBP1', 'IMPOTÊNCIA SEXUAL: GVB39 GE38 GE42', 'INCONTINÊNCIA URINÁRIA: GE36', 'INSÔNIA: GB41', 'MALÁRIA: GC6 GID3', 'MANIA: GVC15 GE36', 'MEDO PATOLÓGICO: GVC16 GVB20 GIG4 GR7 GF14 GB12 GP9 GP7', 'MUTISMO: GBP11', 'NEVRALGIA HERPÉTICA: GBP11', 'PARALISIA ESPÁSTICA: GTA10 GPC8 GPC7', 'PARALISIA FACIAL: GVG12', 'PARASSONIAS: GR1 GVC4 GE40 GP1 GB48', 'PIODERMITE: GPC5 GID3 GIG1 GR3', 'PNEUMONIA: GR25 GVC21', 'PROLAPSO RETAL/INTUSCEPÇÃO: GR1 GB34', 'PROSTRAÇÃO: GR10 GE26', 'RAQUITISMO: GBP2 GP8', 'RESFRIADO: GC9 GIG11', 'RINITE: VG14 GIG11 GIG4 GP11', 'SÍNCOPE: GB42 GR11', 'SÍNDROME DO PÂNICO: GIG4 GPB6', 'SUDORESE NOTURNA INFECCIOSA: GID1 GVB1', 'TEPT: GBP6 GR1 GE36', 'TOSSE PÓS-INFECCIOSA: GBP6 GR1', 'TREMOR E FRIO (IDOSO): GP11 GPC3', 'TUBERCULOSE: GE40', 'URETRITE: GVG20 XVC15', 'URETRITE DE REPETIÇÃO: SR2', 'VERTIGEM: GTA1 GBP15', }
                print('\nMEDICINA OCIDENTAL - NEUROPSIQUIATRIA E GERIATRIA\n')
                for i in sorted(NEU):
                    print(i)
                lemb = input(
                    '\n\nAnotações para prescrição (ou enter para voltar): ').upper()
                if lemb == '':
                    print('\n\nNada foi adicionado. Retornando...\n')
                    time.sleep(1)
                else:
                    lembrete.add(lemb)
            only()
        except:
            only()

# -------------------------------------- MÓDULO DE INICIALIZAÇÃO DE PROGRAMA E DICTS
global warn_pun
warn_pun = set()
# datação
ger_hor_atu = datetime.datetime.now()
global horadia
horadia = ger_hor_atu.strftime("%d-%m-%Y %H:%M:%S")
global data_limpa_hoje
data_limpa_hoje = ger_hor_atu.strftime("%d/%m/%y")
onlyday = ger_hor_atu.strftime("%d")
onlyday = int(onlyday)
onlymonth = ger_hor_atu.strftime("%m")
onlymonth = int(onlymonth)
global anoge
anogen=ger_hor_atu.strftime("%y")
anoge=int(anogen,10)

def estacionador(d, m):
    v = 'verão'.upper()
    p = 'primavera'.upper()
    o = 'outono'.upper()
    i = 'inverno'.upper()
    if m == 1 or m == 2:
        return v
    if m == 12:
        if m > 20:
            return v
        else:
            return p
    if m == 3:
        if d > 20:
            return o
        else:
            return v
    if m == 4 or m == 5:
        return o
    if m == 6:
        if d > 21:
            return i
        else:
            return o
    if m == 7 or m == 8:
        return i
    if m == 9:
        if d > 22:
            return p
        else:
            return i
    if m == 10 or m == 11:
        return p

global moradia
moradia = set()
global estação
estação = estacionador(onlyday, onlymonth)
if estação == 'PRIMAVERA':
    warn_pun.add('Picar colaterais de canal e atingir porfundamente entre músculos, se gravidade picar profundamente - estação de primavera, fonte: si shi qi de ling shu'.upper())
    warn_pun.add('Tratar colateral engurgitado'.upper())
    moradia.add('L')
if estação == 'VERÃO':
    warn_pun.add('Picar canais yang (dan, dachang, wei, xiaoxang, panguan, sanjiao) e colaterais do ponto shu, sendo picado somente superficialmente - estação de verão, fonte: si shi qi de ling shu'.upper())
if estação == 'OUTONO':
    warn_pun.add('Picar pontos shus de doenças yin ou pontos he de doenças yang, esfregar pele antes de aplicar e aplicar superficialmente - estação de outono, fonte: si shi qi de ling shu'.upper())
if estação == 'INVERNO':
    warn_pun.add('Picar canas afetados usar pontos poço e xing, picar profundamente em todas punturas e permanecer tempo longo de agulha - estação de inverno, fonte: si shi qi de ling shu'.upper())
global horashu
horashu = ger_hor_atu.strftime("%H")
shu_h = int(horashu)

def now_shu(x):
    if x == 23:
        y = 'DAN - VESÍCULA BILIAR'
    if x == 0:
        y = 'DAN - VESÍCULA BILIAR'
    if x == 1:
        y = 'GAN - FÍGADO'
    if x == 2:
        y = 'GAN - FÍGADO'
    if x == 3:
        y = 'FEI - PULMÃO'
    if x == 4:
        y = 'FEI - PULMÃO'
    if x == 5:
        y = 'DACHANG - INTESTINO GROSSO'
    if x == 6:
        y = 'DACHANG - INTESTINO GROSSO'
    if x == 7:
        y = 'WEI - ESTÔMAGO'
    if x == 8:
        y = 'WEI - ESTÔMAGO'
    if x == 9:
        y = 'PI - BAÇO'
    if x == 10:
        y = 'PI - BAÇO'
    if x == 11:
        y = 'XIN - CORAÇÃO'
    if x == 12:
        y = 'XIN - CORAÇÃO'
    if x == 13:
        y = 'XIAOXANG - INTESTINO DELGADO'
    if x == 14:
        y = 'XIAOXANG - INTESTINO DELGADO'
    if x == 15:
        y = 'PANGGUAN - BEXIGA'
    if x == 16:
        y = 'PANGGUAN - BEXIGA'
    if x == 17:
        y = 'SHEN - RIM'
    if x == 18:
        y = 'SHEN - RIM'
    if x == 19:
        y = 'XINBAO - PERICÁRDIO'
    if x == 20:
        y = 'XINBAO - PERICÁRDIO'
    if x == 21:
        y = 'SANJIAO - TRIPLO AQUECEDOR'
    if x == 22:
        y = 'SANJIAO - TRIPLO AQUECEDOR'
    return y

def next_shu(x):
    if x == 21:
        y = 'DAN - VESÍCULA BILIAR'
    if x == 22:
        y = 'DAN - VESÍCULA BILIAR'
    if x == 23:
        y = 'GAN - FÍGADO'
    if x == 0:
        y = 'GAN - FÍGADO'
    if x == 1:
        y = 'FEI - PULMÃO'
    if x == 2:
        y = 'FEI - PULMÃO'
    if x == 3:
        y = 'DACHANG - INTESTINO GROSSO'
    if x == 4:
        y = 'DACHANG - INTESTINO GROSSO'
    if x == 5:
        y = 'WEI - ESTÔMAGO'
    if x == 6:
        y = 'WEI - ESTÔMAGO'
    if x == 7:
        y = 'PI - BAÇO'
    if x == 8:
        y = 'PI - BAÇO'
    if x == 9:
        y = 'XIN - CORAÇÃO'
    if x == 10:
        y = 'XIN - CORAÇÃO'
    if x == 11:
        y = 'XIAOXANG - INTESTINO DELGADO'
    if x == 12:
        y = 'XIAOXANG - INTESTINO DELGADO'
    if x == 13:
        y = 'PANGGUAN - BEXIGA'
    if x == 14:
        y = 'PANGGUAN - BEXIGA'
    if x == 15:
        y = 'SHEN - RIM'
    if x == 16:
        y = 'SHEN - RIM'
    if x == 17:
        y = 'XINBAO - PERICÁRDIO'
    if x == 18:
        y = 'XINBAO - PERICÁRDIO'
    if x == 19:
        y = 'SANJIAO - TRIPLO AQUECEDOR'
    if x == 20:
        y = 'SANJIAO - TRIPLO AQUECEDOR'
    return y


global shu_agora
shu_agora = now_shu(shu_h)
global shu_proximo
shu_proximo = next_shu(shu_h)
global dx  # lista de diagnósticos (truple)
dx = ('Deficiência de Xue em Canal de Coração e Intestino Delgado', 'Deficiência de Xue em Canal de Baço/Pâncreas e Estômago', 'Deficiência de Xue em Canal de Pericárdio e Triplo Aquecedor', 'Deficiência de Xue em Canal de Pulmão e Intestino Grosso', 'Deficiência de Xue em Canal de Rim e Bexiga', 'Deficiência de Xue em Canal de Fígado e Vesícula Biliar', 'Deficiência de Yin em Canal de Coração e Intestino Delgado', 'Deficiência de Yin em Canal de Baço/Pâncreas e Estômago', 'Deficiência de Yin em Canal de Pericárdio e Triplo Aquecedor', 'Deficiência de Yin em Canal de Pulmão e Intestino Grosso', 'Deficiência de Yin em Canal de Rim e Bexiga', 'Deficiência de Yin em Canal de Fígado e Vesícula Biliar', 'Deficiência de Yang em Canal de Coração e Intestino Delgado', 'Deficiência de Yang em Canal de Baço/Pâncreas e Estômago', 'Deficiência de Yang em Canal de Pericárdio e Triplo Aquecedor', 'Deficiência de Yang em Canal de Pulmão e Intestino Grosso', 'Deficiência de Yang em Canal de Rim e Bexiga', 'Deficiência de Yang em Canal de Fígado e Vesícula Biliar', 'Deficiência de Qi em Canal de Coração e Intestino Delgado', 'Deficiência de Qi em Canal de Baço/Pâncreas e Estômago', 'Deficiência de Qi em Canal de Pericárdio e Triplo Aquecedor', 'Deficiência de Qi em Canal de Pulmão e Intestino Grosso', 'Deficiência de Qi em Canal de Rim e Bexiga', 'Deficiência de Qi em Canal de Fígado e Vesícula Biliar', 'Deficiência de Yuan em Canal de Coração e Intestino Delgado', 'Deficiência de Yuan em Canal de Baço/Pâncreas e Estômago', 'Deficiência de Yuan em Canal de Pericárdio e Triplo Aquecedor', 'Deficiência de Yuan em Canal de Pulmão e Intestino Grosso', 'Deficiência de Yuan em Canal de Rim e Bexiga', 'Deficiência de Yuan em Canal de Fígado e Vesícula Biliar', 'Deficiência de mar de Qi em Canal de Coração e Intestino Delgado', 'Deficiência de mar de Qi em Canal de Baço/Pâncreas e Estômago', 'Deficiência de mar de Qi em Canal de Pericárdio e Triplo Aquecedor', 'Deficiência de mar de Qi em Canal de Pulmão e Intestino Grosso', 'Deficiência de mar de Qi em Canal de Rim e Bexiga', 'Deficiência de mar de Qi em Canal de Fígado e Vesícula Biliar', 'Deficiência de mar de Xue em Canal de Coração e Intestino Delgado', 'Deficiência de mar de Xue em Canal de Baço/Pâncreas e Estômago', 'Deficiência de mar de Xue em Canal de Pericárdio e Triplo Aquecedor', 'Deficiência de mar de Xue em Canal de Pulmão e Intestino Grosso', 'Deficiência de mar de Xue em Canal de Rim e Bexiga', 'Deficiência de mar de Xue em Canal de Fígado e Vesícula Biliar', 'Deficiência de mar de Gu em Canal de Coração e Intestino Delgado', 'Deficiência de mar de Gu em Canal de Baço/Pâncreas e Estômago', 'Deficiência de mar de Gu em Canal de Pericárdio e Triplo Aquecedor', 'Deficiência de mar de Gu em Canal de Pulmão e Intestino Grosso', 'Deficiência de mar de Gu em Canal de Rim e Bexiga', 'Deficiência de mar de Gu em Canal de Fígado e Vesícula Biliar', 'Deficiência de mar de Xiang em Canal de Coração e Intestino Delgado', 'Deficiência de mar de Xiang em Canal de Baço/Pâncreas e Estômago', 'Deficiência de mar de Xiang em Canal de Pericárdio e Triplo Aquecedor', 'Deficiência de mar de Xiang em Canal de Pulmão e Intestino Grosso', 'Deficiência de mar de Xiang em Canal de Rim e Bexiga', 'Deficiência de mar de Xiang em Canal de Fígado e Vesícula Biliar', 'Estagnação de Xue em Canal de Coração e Intestino Delgado', 'Estagnação de Xue em Canal de Baço/Pâncreas e Estômago', 'Estagnação de Xue em Canal de Pericárdio e Triplo Aquecedor', 'Estagnação de Xue em Canal de Pulmão e Intestino Grosso', 'Estagnação de Xue em Canal de Rim e Bexiga', 'Estagnação de Xue em Canal de Fígado e Vesícula Biliar', 'Estagnação de Qi em Canal de Coração e Intestino Delgado', 'Estagnação de Qi em Canal de Baço/Pâncreas e Estômago', 'Estagnação de Qi em Canal de Pericárdio e Triplo Aquecedor', 'Estagnação de Qi em Canal de Pulmão e Intestino Grosso', 'Estagnação de Qi em Canal de Rim e Bexiga', 'Estagnação de Qi em Canal de Fígado e Vesícula Biliar', 'Excesso de mar de Qi em Canal de Coração e Intestino Delgado', 'Excesso de mar de Qi em Canal de Baço/Pâncreas e Estômago', 'Excesso de mar de Qi em Canal de Pericárdio e Triplo Aquecedor', 'Excesso de mar de Qi em Canal de Pulmão e Intestino Grosso', 'Excesso de mar de Qi em Canal de Rim e Bexiga', 'Excesso de mar de Qi em Canal de Fígado e Vesícula Biliar', 'Excesso de mar de Xue em Canal de Coração e Intestino Delgado', 'Excesso de mar de Xue em Canal de Baço/Pâncreas e Estômago', 'Excesso de mar de Xue em Canal de Pericárdio e Triplo Aquecedor', 'Excesso de mar de Xue em Canal de Pulmão e Intestino Grosso', 'Excesso de mar de Xue em Canal de Rim e Bexiga', 'Excesso de mar de Xue em Canal de Fígado e Vesícula Biliar', 'Excesso de mar de Gu em Canal de Coração e Intestino Delgado', 'Excesso de mar de Gu em Canal de Baço/Pâncreas e Estômago', 'Excesso de mar de Gu em Canal de Pericárdio e Triplo Aquecedor', 'Excesso de mar de Gu em Canal de Pulmão e Intestino Grosso', 'Excesso de mar de Gu em Canal de Rim e Bexiga', 'Excesso de mar de Gu em Canal de Fígado e Vesícula Biliar', 'Excesso de mar de Xiang em Canal de Coração e Intestino Delgado', 'Excesso de mar de Xiang em Canal de Baço/Pâncreas e Estômago', 'Excesso de mar de Xiang em Canal de Pericárdio e Triplo Aquecedor', 'Excesso de mar de Xiang em Canal de Pulmão e Intestino Grosso', 'Excesso de mar de Xiang em Canal de Rim e Bexiga', 'Excesso de mar de Xiang em Canal de Fígado e Vesícula Biliar', 'Frio Interno em Canal de Coração e Intestino Delgado', 'Frio Interno em Canal de Baço/Pâncreas e Estômago', 'Frio Interno em Canal de Pericárdio e Triplo Aquecedor', 'Frio Interno em Canal de Pulmão e Intestino Grosso', 'Frio Interno em Canal de Rim e Bexiga', 'Frio Interno em Canal de Fígado e Vesícula Biliar', 'Frio Externo em Canal de Coração e Intestino Delgado', 'Frio Externo em Canal de Baço/Pâncreas e Estômago', 'Frio Externo em Canal de Pericárdio e Triplo Aquecedor', 'Frio Externo em Canal de Pulmão e Intestino Grosso', 'Frio Externo em Canal de Rim e Bexiga', 'Frio Externo em Canal de Fígado e Vesícula Biliar', 'Calor Interno em Canal de Coração e Intestino Delgado', 'Calor Interno em Canal de Baço/Pâncreas e Estômago', 'Calor Interno em Canal de Pericárdio e Triplo Aquecedor', 'Calor Interno em Canal de Pulmão e Intestino Grosso', 'Calor Interno em Canal de Rim e Bexiga', 'Calor Interno em Canal de Fígado e Vesícula Biliar', 'Calor Externo em Canal de Coração e Intestino Delgado', 'Calor Externo em Canal de Baço/Pâncreas e Estômago', 'Calor Externo em Canal de Pericárdio e Triplo Aquecedor', 'Calor Externo em Canal de Pulmão e Intestino Grosso', 'Calor Externo em Canal de Rim e Bexiga', 'Calor Externo em Canal de Fígado e Vesícula Biliar', 'Fleuma/umidade em Canal de Coração e Intestino Delgado', 'Fleuma/umidade em Canal de Baço/Pâncreas e Estômago', 'Fleuma/umidade em Canal de Pericárdio e Triplo Aquecedor', 'Fleuma/umidade em Canal de Pulmão e Intestino Grosso',
      'Fleuma/umidade em Canal de Rim e Bexiga', 'Fleuma/umidade em Canal de Fígado e Vesícula Biliar', 'Secura em Canal de Coração e Intestino Delgado', 'Secura em Canal de Baço/Pâncreas e Estômago', 'Secura em Canal de Pericárdio e Triplo Aquecedor', 'Secura em Canal de Pulmão e Intestino Grosso', 'Secura em Canal de Rim e Bexiga', 'Secura em Canal de Fígado e Vesícula Biliar', 'Vento Interno em Canal de Coração e Intestino Delgado', 'Vento Interno em Canal de Baço/Pâncreas e Estômago', 'Vento Interno em Canal de Pericárdio e Triplo Aquecedor', 'Vento Interno em Canal de Pulmão e Intestino Grosso', 'Vento Interno em Canal de Rim e Bexiga', 'Vento Interno em Canal de Fígado e Vesícula Biliar', 'Vento Externo em Canal de Coração e Intestino Delgado', 'Vento Externo em Canal de Baço/Pâncreas e Estômago', 'Vento Externo em Canal de Pericárdio e Triplo Aquecedor', 'Vento Externo em Canal de Pulmão e Intestino Grosso', 'Vento Externo em Canal de Rim e Bexiga', 'Vento Externo em Canal de Fígado e Vesícula Biliar', 'Canícula em Canal de Coração e Intestino Delgado', 'Canícula em Canal de Baço/Pâncreas e Estômago', 'Canícula em Canal de Pericárdio e Triplo Aquecedor', 'Canícula em Canal de Pulmão e Intestino Grosso', 'Canícula em Canal de Rim e Bexiga', 'Canícula em Canal de Fígado e Vesícula Biliar', 'Colapso em Canal de Coração e Intestino Delgado', 'Colapso em Canal de Baço/Pâncreas e Estômago', 'Colapso em Canal de Pericárdio e Triplo Aquecedor', 'Colapso em Canal de Pulmão e Intestino Grosso', 'Colapso em Canal de Rim e Bexiga', 'Colapso em Canal de Fígado e Vesícula Biliar', 'Rebeldia Ascendente em Canal de Coração e Intestino Delgado', 'Rebeldia Ascendente em Canal de Baço/Pâncreas e Estômago', 'Rebeldia Ascendente em Canal de Pericárdio e Triplo Aquecedor', 'Rebeldia Ascendente em Canal de Pulmão e Intestino Grosso', 'Rebeldia Ascendente em Canal de Rim e Bexiga', 'Rebeldia Ascendente em Canal de Fígado e Vesícula Biliar', 'Rebeldia Descendente em Canal de Coração e Intestino Delgado', 'Rebeldia Descendente em Canal de Baço/Pâncreas e Estômago', 'Rebeldia Descendente em Canal de Pericárdio e Triplo Aquecedor', 'Rebeldia Descendente em Canal de Pulmão e Intestino Grosso', 'Rebeldia Descendente em Canal de Rim e Bexiga', 'Rebeldia Descendente em Canal de Fígado e Vesícula Biliar', 'Rebeldia Horizontal em Canal de Coração e Intestino Delgado', 'Rebeldia Horizontal em Canal de Baço/Pâncreas e Estômago', 'Rebeldia Horizontal em Canal de Pericárdio e Triplo Aquecedor', 'Rebeldia Horizontal em Canal de Pulmão e Intestino Grosso', 'Rebeldia Horizontal em Canal de Rim e Bexiga', 'Rebeldia Horizontal em Canal de Fígado e Vesícula Biliar', 'Calor Cheio em Canal de Coração e Intestino Delgado', 'Calor Cheio em Canal de Baço/Pâncreas e Estômago', 'Calor Cheio em Canal de Pericárdio e Triplo Aquecedor', 'Calor Cheio em Canal de Pulmão e Intestino Grosso', 'Calor Cheio em Canal de Rim e Bexiga', 'Calor Cheio em Canal de Fígado e Vesícula Biliar', 'Calor Vazio em Canal de Coração e Intestino Delgado', 'Calor Vazio em Canal de Baço/Pâncreas e Estômago', 'Calor Vazio em Canal de Pericárdio e Triplo Aquecedor', 'Calor Vazio em Canal de Pulmão e Intestino Grosso', 'Calor Vazio em Canal de Rim e Bexiga', 'Calor Vazio em Canal de Fígado e Vesícula Biliar', 'Frio Cheio em Canal de Coração e Intestino Delgado', 'Frio Cheio em Canal de Baço/Pâncreas e Estômago', 'Frio Cheio em Canal de Pericárdio e Triplo Aquecedor', 'Frio Cheio em Canal de Pulmão e Intestino Grosso', 'Frio Cheio em Canal de Rim e Bexiga', 'Frio Cheio em Canal de Fígado e Vesícula Biliar', 'Frio Vazio em Canal de Coração e Intestino Delgado', 'Frio Vazio em Canal de Baço/Pâncreas e Estômago', 'Frio Vazio em Canal de Pericárdio e Triplo Aquecedor', 'Frio Vazio em Canal de Pulmão e Intestino Grosso', 'Frio Vazio em Canal de Rim e Bexiga', 'Frio Vazio em Canal de Fígado e Vesícula Biliar', 'Deficiência de Triplo Aquecedor Superior', 'Deficiência de Triplo Aquecedor Médio', 'Deficiência de Triplo Aquecedor Inferior', 'Excesso de Triplo Aquecedor Superior', 'Excesso de Triplo Aquecedor Médio', 'Excesso de Triplo Aquecedor Inferior', 'Xie-Calor em Nível Wei (1/4)', 'Xie-Calor em Nível Qi (2/4)', 'Xie-Calor em Nível Ying Qi (3/4)', 'Xie-Calor em Nível Xue (4/4)', 'Xie-Frio em Yang Maior (1/6)', 'Xie-Frio em Yang Brilhante (2/6)', 'Xie-Frio em Yang Menor (3/6)', 'Xie-Frio em Yin Maior (4/6)', 'Xie-Frio em Yin Menor (5/6)', 'Xie-Frio em Yin Terminal (6/6)', 'Fleuma-fogo em Canal de Coração e Intestino Delgado', 'Fleuma-fogo em Canal de Baço/Pâncreas e Estômago', 'Fleuma-fogo em Canal de Pericárdio e Triplo Aquecedor', 'Fleuma-fogo em Canal de Pulmão e Intestino Grosso', 'Fleuma-fogo em Canal de Rim e Bexiga', 'Fleuma-fogo em Canal de Fígado e Vesícula Biliar', 'Fogo interno causado por Estagnação em Canal de Coração e Intestino Delgado', 'Fogo interno causado por Estagnação em Canal de Baço/Pâncreas e Estômago', 'Fogo interno causado por Estagnação em Canal de Pericárdio e Triplo Aquecedor', 'Fogo interno causado por Estagnação em Canal de Pulmão e Intestino Grosso', 'Fogo interno causado por Estagnação em Canal de Rim e Bexiga', 'Fogo interno causado por Estagnação em Canal de Fígado e Vesícula Biliar', 'Padrão Patológico de Dai Mai (vaso de cintura)', 'Padrão Patológico de Chong Mai (VP)', 'Padrão Patológico de Du Mai (VG)', 'Padrão Patológico de Ren Mai(VC)', 'Padrão Patológico de Yang Qiao Mai', 'Padrão Patológico de Yin Qiao Mai', 'Padrão Patológico de Yang Wei Mai', 'Padrão Patológico de Yin Wei Mai', 'Fleuma afetando Mente/Pensamentos (Shen)', 'Vento-Calor Padrão tipo Vento-Calor', 'Vento-Calor Padrão tipo Canícula', 'Vento-Calor Padrão tipo Umidade-Calor', 'Vento-Calor Padrão tipo Calor-Secura', 'Vento-Calor Padrão tipo Calor em Pulmões - tórax/diafragma', 'Vento-Calor Padrão tipo Calor de Estômago', 'Vento-Calor Padrão tipo Calor-Secura em Intestinos', 'Vento-Calor Padrão tipo Calor em Vesícula Biliar', 'Vento-Calor Padrão tipo Umidade-calor em Estômago/Baço', 'Vento-Calor Padrão tipo Calor no nível Qi Nutritivo', 'Vento-Calor Padrão tipo Calor de Pericárdio', 'Vento-Calor Padrão tipo Calor agitando Sangue', 'Vento-Calor Padrão tipo Fogo provocando Vento', 'Vento-Calor Padrão tipo Vento-vazio agitando interior', 'Vento-Calor Padrão tipo Colapso de Yin', 'Vento-Calor Padrão tipo Colapso de Yang', 'Vento-Calor Padrão tipo Vento-Calor em Qi defensivo (wei) de Pulmão', 'Vento-Calor Padrão tipo Calor nos pulmões - nível de qi', 'Vento-Calor Padrão tipo Calor de Pericárdio nível de Qi nutritivo', 'Vento-Calor Padrão tipo Calor no Yang Brilhante', 'Vento-Calor Padrão tipo Umidade-calor em Baço', 'Vento-Calor Padrão tipo Calor nos Rins', 'Vento-Calor Padrão tipo Calor no Fígado provocando Ventos', 'Vento-Calor Padrão tipo Vento-vazio de Fígado', 'Distúrbio de Shen-Coração - Xiang', 'Distúrbio de Shen-Baço - Yi', 'Distúrbio de Shen-Pulmão - Po', 'Distúrbio de Shen-Rim - Zhi', 'Distúrbio de Shen-Fígado - Hun', 'Calor de Xue')
global tipo_p
tipo_p = ('', 'Pulso patológico - Fu (flutuante)', 'Pulso patológico - Chen (profundo)', 'Pulso patológico - Chi (lento)', 'Pulso patológico - Shu (rápido)', 'Pulso patológico - Xu (vazio)', 'Pulso patológico - Shi (cheio)', 'Pulso patológico - Hua (deslizante)', 'Pulso patológico - Se (áspero)', 'Pulso patológico - Chang (longo)', 'Pulso patológico - Duan (curto)', 'Pulso patológico - Hong (transbordante)', 'Pulso patológico - Xi (fino)', 'Pulso patológico - Wei (mínimo)', 'Pulso patológico - Jin (tenso)',
          'Pulso patológico - Xian (corda)', 'Pulso patológico - Huan (retardadodo)', 'Pulso patológico - Kou (oco)', 'Pulso patológico - Ge (couro)', 'Pulso patológico - Lao (firme)', 'Pulso patológico - Ru (encharcado)', 'Pulso patológico - Ruo (fraco)', 'Pulso patológico - San (disperso)', 'Pulso patológico - Fua (escorregadio)', 'Pulso patológico - Dong (móvel)', 'Pulso patológico - Cu (precipitado)', 'Pulso patológico - Jie (nodoso)', 'Pulso patológico - Dai (intermitente)', 'Pulso patológico - Ji (acelerado)')
global ext
ext={'EX1' :  'SI-SHEN-TSUNG','EX2' :  'JIA-SHANG-XING','EX3' :  'DANG-YANG','EX4' :  'ER-ZHUNG','EX5' :  'YIN-TANG','EX6' :  'SHAN-QUEN','EX7' :  'TOU-KUANG-MIN','EX8' :  'YU-YAO','EX9' :  'YU-WEI','EX10' :  'CHIU-HOU','EX11' :  'JIEN-MIN','EX12' :  'TAI-YANG','EX13' :  'ER-JIAN','EX14' :  'LUNG-XUE','EX15' :  'HOU-TING-HWEI','EX16' :  'YI-MING','EX17' :  'SHANG-YING-HSIANG','EX18' :  'JIAN-BI','EX19' :  'BI-TUNG','EX20' :  'SAN-XIAO','EX21' :  'TI-HOU','EX22' :  'JINJING-YUYE','EX23' :  'SHAN-LIAN-CHUAN','EX24' :  'WAI-JINJING-YUYE','EX25' :  'LUO-JING','EX26' :  'XING-SHI','EX27' :  'BAI-LAO','EX28' :  'TSUNG-GU','EX29' :  'CHIAN-CHENG','EX30' :  'AN-MIN-1','EX31' :  'AN-MIN-2','EX32' :  'XING-FENG','EX33' :  'CHI-XUE','EX34' :  'TAN-CHUAN','EX35' :  'TSOUYI | YOUYI','EX36' :  'MEI-HUA','EX37' :  'SHI-TSANG','EX38' :  'SHI-KUAN','EX39' :  'WAI-SI-MAN','EX40' :  'JUE-YUN','EX41' :  'YI-JING','EX42' :  'WEI-BAO','EX43' :  'CHANG-YI','EX44' :  'TSI-KUNG | ZIGONG','EX45' :  'TI-TUO','EX46' :  'TSUNG-JIAN','EX47' :  'HENG-WEN','EX48' :  'CHUAN-XI','EX49' :  'TING-CHUAN | DINGCHUAN','EX50' :  'WAI-TING-CHUAN','EX51' :  'BA-HUA','EX52' :  'ZHU-TSE','EX53' :  'JU-JUE-SHU','EX54' :  'WEI-RE-XUE','EX55' :  'ZHONG-CHUAN','EX56' :  'PI-RE-XUE','EX57' :  'SHEN-RE-XUE','EX58' :  'CHI-CHUAN','EX59' :  'KUEI-YANG-XUE','EX60' :  'PI-GEN','EX61' :  'XUE-CHOU','EX62' :  'JI-JU-PI-KUAI','EX63' :  'WEI-XU','EX64' :  'YAO-YI','EX65' :  'YAO-YIAN','EX66' :  'CHONG-KUNG','EX67' :  'JIU-JI','EX68' :  'TUN-ZHUNG','EX69' :  'HUAN-ZHUNG','EX70' :  'HUA-TUO-JIA-JI-XUE','EX71' :  'TSOU-GU','EX72' :  'SHI-CHI-ZUI-XIA | SHIQUIHUIXIA','EX73' :  'SHI-XUAN','EX74' :  'JIU-TIEN-FENG','EX75' :  'SI-FUNG','EX76' :  'SHOU-ZHONG-PING','EX77' :  'YA-TUNG','EX78' :  'SHANG-HOUXI','EX79' :  'TA-GU-KUNG','EX80' :  'ZHONG-KUEI','EX81' :  'BA-XIE','EX82' :  'LUO-JEN | LUO-ZHEN','EX83' :  'WAI-LAO-KUNG','EX84' :  'ER-BAI','EX85' :  'TSUN-PIN','EX86' :  'NEU-SHANG-XUE','EX87' :  'BEI-ZHONG','EX88' :  'ZE-CHIAN','EX89' :  'JIAN-SAN-JEN','EX90' :  'JIAN-SHU','EX91' :  'ZHU-PEI','EX92' :  'TAI-JIAN','EX93' :  'CHIEN-HOU-YINJU','EX94' :  'TSU-XIN','EX95' :  'SHIH-MIN','EX96' :  'BA-FENG','EX97' :  'NUI-SHI','EX98' :  'NAO-CHING | NAOQING','EX99' :  'JIU-WAI-FAN','EX100' :  'JIU-NEI-FAN','EX101' :  'JING-XIA','EX102' :  'WAN-LI','EX103' :  'LAU-WEI | LAN-WEI-XUE','EX104' :  'CHI-YEN | XIYAN','EX105' :  'CHI-XIA','EX106' :  'DAN-NANG-DIEN | DANNANGXUE','EX107' :  'LING-HOU','EX108' :  'HER-TING | HEDING','EX109' :  'LING-XIA','EX110' :  'CHIEN-FENG-SHI','EX111' :  'SHANG-FENG-XI','EX112' :  'SHEN-XI','EX113' :  'BAI-CHONG-WO','EX114' :  'YIN-WEI-1','EX115' :  'YIN-WEI-2','EX116' :  'YIN-WEI-3','EX117' :  'SI-LIEN','EX118' :  'WU-LING','EX119' :  'LING-BAO','EX120' :  'XIN-JIAN','EX121' :  'JING-ZHONG','EX122' :  'QI-MEN','EX123' :  'JING-GONG','EX124' :  'JIAN-NEI-LING','EX125' :  'NEI-MA-DIAN','EX126' :  'YAO-TONG-XUE','EX127' :  'QI-PANG'}
global cid11
# cid11 é somente expositivo sem interferência em programa, porém traduzido
cid11 = ['SE72 Calor ',  'SE73 Frio ',  'SE74 Excesso ',  'SE75 Deficiência ',  'SE76 Externo ',  'SE77 Interno ',  'SE80 Vento ',  'SE81 Xié/Frio ',  'SE82 Humidade ',  'SE83 Secura ',  'SE84 Fogo ',  'SE85 Canícula ',  'SG60 6 estágios - Liu Xie/Frio - Yang Maior (1/6) ',  'SG61 6 estágios - Liu Xie/Frio - Yang Brilhante (2/6) ',  'SG62 6 estágios - Liu Xie/Frio - Yang Menor (3/6) ',  'SG63 6 estágios - Liu Xie/Frio - Yin Maior (4/6) ',  'SG64 6 estágios - Liu Xie/Frio - Yin Menor (5/6) ',  'SG65 6 estágios - Liu Xie/Frio - Yin Terminal (6/6) ',  'SG6Z 6 estágios - Liu Xie/Frio - indefinido ',  'SG80 4 fases - Liu Xie/Calor - Padrão Wei ',  'SG9Z 4 fases - Liu Xie/Calor - Padrão Qi ',  'SH0Z 4 fases - Liu Xie/Calor - Padrão Ying ',  'SH1Z 4 fases - Liu Xie/Calor - Padrão Xue ',  'SH3Z 4 fases - Liu Xie/Calor - indefinido ',  'SE90 Deficiência de Qi ',  'SE91 Estase de Qi ',  'SE92 Qi Ascendente ',  'SE93 Qi Descendente ',  'SE94 Qi Horizontal ',  'SE9Z Patologia de Qi ',  'SF00 Deficiência de Xue ',  'SF01 Estase de Xue ',  'SF02 Calor no Xue ',  'SF03 Frio de Xue ',  'SF04 Secura de Xue ',  'SF10 Deficiência de Jin Yé ',  'SF11 Distúrbio do Jin Yé ',  'SF12 Fleuma-Secura ',  'SF13 Fleuma-Humidade ',  'SF14 Fleuma-Fogo ',  'SF15 Fleuma-Vento ',  'SF20 Deficiência de Yuan ',  'SF50 Deficiência de Yin de Fígado ',  'SF51 Deficiência de Yang de Fígado ',  'SF52 Ascensão de Yang de Fígado ',  'SF53 Deficiência de Qi de Fígado ',  'SF54 Deficiência de Xue de Fígado ',  'SF55 Estase de Fígado ',  'SF56 Fígado-Vento ',  'SF58 Ascensão de Fogo de Fígado ',  'SF59 Fígado produzindo Vento ',  'SF5A Fleuma-Calor de Fígado ',  'SF5C Frio de Fígado ',  'SF5D Deficiência de Qi de Fígado ',  'SF5E Fleuma por depleção de Vesícula Biliar ',  'SF5F Calor de Vesícula Biliar ',  'SF5G Frio de Vesícula ',  'SF5H Deficiência Yin de Fígado e Rim ',  'SF5J Distúrbio Fígado/Baço ',  'SF5K Distúrbio Fígado/Estômago ',  'SF5L Fogo de Fígado invadindo Estômago ',  'SF5M Fogo de Fígado invadindo Pulmão ',  'SF5Z Padrão patológico em Fígado ',  'SF60 Deficiência de Qi de Coração ',  'SF61 Deficiência de Xue de Coração ',  'SF62 Deficiência de Qi e Xue de Coração ',  'SF63 Obstrução de Coração ',  'SF64 Deficiência Yin de Coração ',  'SF65 Deficiência de Qi de Coração em Padrão Yin ',  'SF66 Deficiência Yang de Coração ',  'SF67 Colapso de Coração ',  'SF68 Fogo de Coração Ascendendo ',  'SF69 Fogo de Coração Afetando Shen ',  'SF6A Qi de água afetando Coração ',  'SF6B Shen agitado ',  'SF6C Ansiedade afetando Shen ',  'SF6D Estase de Qi de Intestino Delgado ',  'SF6E Calor de Intestino Delgado ',  'SF6F Frio de Intestino Delgado ',  'SF6G Deficiência de Xue de Coração e Fígado ',  'SF6H Deficiência de Qi Vesícula Biliar e Coração ',  'SF6J Deficiência Coração/Baço ',  'SF6K Deficiência Coração/Pulmão ',  'SF6L Disarmonia Coração/Rim ',  'SF6M Deficiência Coração/Bexiga ',  'SA6Z Padrão patológico em Coração ',  'SF70 Deficiência de Qi de Baço ',  'SF71 Rebelião de Qi de Baço Descendente ',  'SF72 Estase de Qi de Baço ',  'SF73 Baço em deficiência com retenção alimentar ',  'SF74 Baço não gerando Xue ',  'SF75 Deficiência de Baço e Xue ',  'SF76 Deficiência Yin de Baço ',
         'SF77 Deficiência Yang de Baço ',  'SF78 Fleuma-fogo-Calor de Baço ',  'SF79 Deficiência de Baço em padrão de Fleuma ',  'SF7A Edema/humidade por deficiência de Baço ',  'SF7B Frio/fleuma de Baço ',  'SF7C Deficiência de Qi de Estômago ',  'SF7D Rebelião ascendente de estômago ',  'SF7E Deficiência Yin de Estômago ',  'SF7F Calor de Estômago ',  'SF7G Padrão umidade/intestinos ',  'SF7H Frio de Estômago   ',  'SF7J Estase por frio de intestino ',  'SF7K Ansiedade afetando Baço ',  'SF7L Deficiência Pulmão/Baço ',  'SF7M Deficiência Yang de Baço/Rim ',  'SF7Z Padrão patológico em Baço ',  'SF80 Deficiência de Qi de Pulmão ',  'SF81 Deficiência de yin de Pulmão ',  'SF82 Deficiência de yin de Pulmão e Rim ',  'SF83 Deficiência de yin e de qi de Pulmão ',  'SF84 Deficiência de yang de Pulmão ',  'SF85 Fleuma-Frio Obstruindo Pulmão ',  'SF86 Fleuma de Pulmão ',  'SF87 Frio externo com calor de pulmão ',  'SF88 Congestão por calor de pulmão ',  'SF89 Fleuma-fogo de pulmão ',  'SF8A Vento-Calor invadindo Pulmão ',  'SF8B Calor de pulmão afetando instestinos ',  'SF8C Vento-Frio de Pulmão ',  'SF8D Secura de Pulmão ',  'SF8E Secura de Pulmão afetando Intestinos ',  'SF8F Calor de Intestino Grosso ',  'SF8G Umidade-Calor de Intestino Grosso ',  'SF8H Deficiência de Fluidos de Intestino Grosso ',  'SF8J Frio de Intestino Grosso ',  'SF8Z Outros padrões patológicos de Pulmão ',  'SF90 Deficiência de qi de Rim ',  'SF91 Falha de receber qi de Rim ',  'SF92 Deficiência de qi de Rim gerando umidade ',  'SF93 Deficiência de Yin de Rim ',  'SF94 Deficiência de Yin e Yang de Rim ',  'SF95 Deficiência de Rim afetando Medula Óssea ',  'SF96 Deficiência de Yuan ',  'SF98 Medo afetando Rim ',  'SF99 Calor de Xue em Útero ',  'SF9A Fleuma de Útero ',  'SF9B Humidade-calor de útero ',  'SF9C Frio de Útero ',  'SF9D Frio por deficiência de útero ',  'SF9E Estase de Xue de Bexiga ',  'SF9F Calor de Bexiga ',  'SF9G Calor-umidade de Bexiga ',  'SF9H Umidade de Bexiga ',  'SF9J Frio vazio de Bexiga ',  'SF9Z Padrão patológico em Rim ',  'SG20 Padrão patológico de pulmão (meridiano) ',  'SG21 Padrão patológico de intestino grosso (meridiano) ',  'SG22 Padrão patológico de estômago (meridiano) ',  'SG23 Padrão patológico de baço (meridiano) ',  'SG24 Padrão patológico de coração (meridiano) ',  'SG25 Padrão patológico de intestino delgado (meridiano) ',  'SG26 Padrão patológico de bexiga (meridiano) ',  'SG27 Padrão patológico de rim (meridiano) ',  'SG28 Padrão patológico de pericárdio (meridiano) ',  'SG29 Padrão patológico de triplo aquecedor (meridiano) ',  'SG2A Padrão patológico de vesícula (meridiano) ',  'SG2B Padrão patológico de fígado (meridiano) ',  'SG30 Padrão patológico de Du Mai/vasogovernador ',  'SG31 Padrão patológico de Ren Mai/vasoconcepção ',  'SG32 Padrão patológico de Yin Qiao ',  'SG33 Padrão patológico de Yang Qiao ',  'SG34 Padrão patológico de Yin Wei ',  'SG35 Padrão patológico de Yang Wei ',  'SG36 Padrão patológico de Chong/vasopenetrador ',  'SG37 Padrão patológico de Dai Mai/Cintura ',  'SG70 Padrão patológico de Triplo Aquecedor Superior ',  'SG71 Padrão patológico de Triplo Aquecedor Médio ',  'SG72 Padrão patológico de Triplo Aquecedor Inferior']
new = [i[:5] for i in cid11]
new2 = [i.replace(' ', '') for i in new]
ape = [i.split(' ', 1) for i in cid11]
ape2 = [i[1].upper() for i in ape]
global ape3
ape3 = [i for i in ape2]
global ciddict
ciddict = {}
for i, j in zip(new2, ape3):
    ciddict[i] = j
global toic
toic = ['SF61', 'SF75', 'SG7Z&SF00', 'SF81&SF00', 'SF9Y&SF00', 'SF54', 'SF64', 'SF76', 'SE75&SG7Y', 'SF81', 'SF93', 'SF50', 'SF66', 'SF77', 'SG7Z&SE70', 'SF84', 'SF97', 'SF51', 'SF60', 'SF70', 'SG7Y&SE75', 'SF80', 'SF90', 'SF53', 'SF20&SF6Z', 'SF20&SF7Z', 'SF20&SG7Z', 'SF20&SF8Z', 'SF20&SF9Z', 'SF20&SF5Z', 'SF2Y&SF6Z', 'SF2Y&SF7Z', 'SF2Y&SG7Z', 'SF2Y&SF8Z', 'SF2Y&SF9Z', 'SF2Y&SF5Z', 'SF2Y&SF6Z', 'SF2Y&SF7Z', 'SF2Y&SG7Z', 'SF2Y&SF8Z', 'SF2Y&SF9Z', 'SF2Y&SF5Z', 'SF2Y&SF6Z', 'SF2Y&SF7Z', 'SF2Y&SG7Z', 'SF2Y&SF8Z', 'SF2Y&SF9Z', 'SF2Y&SF5Z', 'SF2Y&SF6Z', 'SF2Y&SF7Z', 'SF2Y&SG7Z', 'SF2Y&SF8Z', 'SF2Y&SF9Z', 'SF2Y&SF5Z', 'SF63', 'SF72', 'SG80', 'SF88', 'SF9E', 'SF5J', 'SE91&SF6Z', 'SE91&SF7Z', 'SE91&SG7Z', 'SE91&SF8Z', 'SE91&SF9Z', 'SE91&SF5Z', 'SF2Y&SF6Z', 'SF2Y&SF7Z', 'SF2Y&SG7Z', 'SF2Y&SF8Z', 'SF2Y&SF9Z', 'SF2Y&SF5Z', 'SF2Y&SF6Z', 'SF2Y&SF7Z', 'SF2Y&SG7Z', 'SF2Y&SF8Z', 'SF2Y&SF9Z', 'SF2Y&SF5Z', 'SF2Y&SF6Z', 'SF2Y&SF7Z', 'SF2Y&SG7Z', 'SF2Y&SF8Z', 'SF2Y&SF9Z', 'SF2Y&SF5Z', 'SF2Y&SF6Z', 'SF2Y&SF7Z', 'SF2Y&SG7Z', 'SF2Y&SF8Z', 'SF2Y&SF9Z', 'SF2Y&SF5Z', 'SE81&SF6Z', 'SE81&SF7Z', 'SE81&SG7Z', 'SE81&SF8Z', 'SE81&SF9Z', 'SE81&SF5Z', 'SE81&SF6Z&SE76', 'SE81&SF7Z&SE76', 'SE81&SG7Z&SE76', 'SE81&SF8Z&SE76', 'SE81&SF9Z&SE76', 'SE81&SF5Z&SE76', 'SE72&SF6Z', 'SE72&SF7Z', 'SE72&SG7Z', 'SE72&SF8Z', 'SE72&SF9Z', 'SE72&SF5Z', 'SE72&SF6Z&SE76', 'SE72&SF7Z&SE76', 'SE72&SG7Z&SE76', 'SE72&SF8Z&SE76', 'SE72&SF9Z&SE76', 'SE72&SF5Z&SE76', 'SF13&SF6Z', 'SF13&SF7Z', 'SF13&SG7Z', 'SF13&SF8Z', 'SF13&SF9Z', 'SF13&SF5Z', 'SF12&SF6Z', 'SF12&SF7Z', 'SF12&SG7Z', 'SF12&SF8Z', 'SF12&SF9Z', 'SF12&SF5Z', 'SE80&SE77&SF6Z', 'SE80&SE77&SF7Z', 'SE80&SE77&SG7Z',
        'SE80&SE77&SF8Z', 'SE80&SE77&SF9Z', 'SE80&SE77&SF5Z', 'SE80&SE76&SF6Z', 'SE80&SE76&SF7Z', 'SE80&SE76&SG7Z', 'SE80&SE76&SF8Z', 'SE80&SE76&SF9Z', 'SE80&SE76&SF5Z', 'SE85&SF6Z', 'SE85&SF7Z', 'SE85&SG7Z', 'SE85&SF8Z', 'SE85&SF9Z', 'SE85&SF5Z', 'SE94&SF6Z', 'SE94&SF7Z', 'SE94&SG7Z', 'SE94&SF8Z', 'SE94&SF9Z', 'SE94&SF5Z', 'SE92&SF6Z', 'SE92&SF7Z', 'SE92&SG7Z', 'SE92&SF8Z', 'SE92&SF9Z', 'SE92&SF5Z', 'SE93&SF6Z', 'SE93&SF7Z', 'SE93&SG7Z', 'SE93&SF8Z', 'SE93&SF9Z', 'SE93&SF5Z', 'SF68', 'SF7D', 'SE84', 'SF8B', 'SF9F', 'SF58', 'SE72&SE74&SF6Z', 'SE72&SE74&SF7Z', 'SE72&SE74&SG7Z', 'SE72&SE74&SF8Z', 'SE72&SE74&SF9Z', 'SE72&SE74&SF5Z', 'SE72&SE75&SF6Z', 'SE72&SE75&SF7Z', 'SE72&SE75&SG7Z', 'SE72&SE75&SF8Z', 'SE72&SE75&SF9Z', 'SE72&SE75&SF5Z', 'SE73&SE74&SF6Z', 'SE73&SE74&SF7Z', 'SE73&SE74&SG7Z', 'SE73&SE74&SF8Z', 'SE73&SE74&SF9Z', 'SE73&SE74&SF5Z', 'SE73&SE75&SF6Z', 'SE73&SE75&SF7Z', 'SE73&SE75&SG7Z', 'SE73&SE75&SF8Z', 'SE73&SE75&SF9Z', 'SE73&SE75&SF5Z', 'SE75&SG70', 'SE75&SG71', 'SE75&SG72', 'SE74&SG70', 'SE74&SG71', 'SE74&SG72', 'SG80', 'SG90', 'SH01', 'SH10', 'SG60', 'SG61', 'SG62', 'SG63', 'SG64', 'SG65', 'SF14&SF6Z', 'SF14&SF7Z', 'SF14&SG7Z', 'SF14&SF8Z', 'SF14&SF9Z', 'SF14&SF5Z', 'SE72&SE91&SF6Z', 'SE72&SE91&SF7Z', 'SE72&SE91&SG7Z', 'SE72&SE91&SF8Z', 'SE72&SE91&SF9Z', 'SE72&SE91&SF5Z', 'SG37', 'SG36', 'SG30', 'SG31', 'SG33', 'SG32', 'SG35', 'SG34', '6F6B', 'SH3Z', 'SG80', 'SG80', 'SG80', 'SG9Z', 'SG9Z', 'SG9Z', 'SG9Z', 'SG9Z', 'SH0Z', 'SH0Z', 'SH1Z', 'SH1Z', 'SH1Z', 'SH1Z', 'SH1Z', 'SG70&SE74', 'SG70&SE74', 'SG70&SE74', 'SG71&SE74', 'SG71&SE74', 'SG72&SE74', 'SG72&SE74', 'SG72&SE74', '6F6B', '6F6B', '6F6B', '6F6B', '6F6B', 'SF02']
global met
met = {'G': 'SEDAÇÃO FRIA', 'H': 'SEDAÇÃO COM MOXA', 'W': 'TONIFICAÇÃO FRIA', 'X': 'TONIFICAÇÃO COM MOXA', 'Z': 'NEUTRO', 'Y': 'VENTOSA', 'K': 'SANGRIA',
       'M': 'UNILATERAL DIREITA - SEDADO', 'N': 'UNILATERAL ESQUERDA - SEDADO', 'A': 'UNILATERAL DIREITA - TONIFICADO', 'D': 'UNILATERAL ESQUERDA - TONIFICADO'}
global locex
locex={'EX1' :  '1 CUN FORMANDO CRUZ (FRENTE-TRÁS-LADOS) EM LINHA DE ORELHA (VG20)','EX2' :  '3 CUN LATERAIS A VG23 (INSERÇÃO CABELO EM LINHA DE NARIZ)','EX3' :  'EM LINHA VERTICAL DE PUPILA, 1 CUN APÓS INSERÇÃO CAPILAR','EX4' :  '1 CUN ACIMA DE YIN-TANG (ENTRE SOMBRANCELHAS)','EX5' :  'MEIO DE LINHA DE SOMBRANCELHAS','EX6' :  'MEIO DE LINHA ENTRE COMISSURAS INTERNAS DE OLHO','EX7' :  'LINHA VERTICAL DE PUPILAS EM BORDA SUPERIOR DE SOMBRANCELHAS','EX8' :  'LINHA VERTICAL DE PUPILA, MEDIANA NA SOMBRANCELHA','EX9' :  '0,1 CUN DE COMISSURAS LATERAIS DE OLHOS','EX10' :  'BORDA INFRA-ORBITAL EXTERNA A UM QUARTO DA DISTÂNCIA ENTRE COMISSURAS, INSERÇÃO POUCO PROFUNDA','EX11' :  '0,4 CUN ABAIXO DE B1 (NA COMISSURA MEDIAL), DIRECIONAR PARA BAIXO, INSERÇÃO POUCO PROFUNDA','EX12' :  'LATERALMENTE A COMISSURA LATERAL DAS SOMBRANCELHAS, ONDE HÁ DEPRESSÃO ÓSSEA','EX13' :  'AO DOBRAR ORELHA PARA FRENTE, PONTO SUPERIOR DE PAVILHÃO EXTERNO','EX14' :  'MEIO DE LINHA ENTRE ID9 (TRAGUS) E TA21 (MASTÓIDE)','EX15' :  'DEPRESSÃO POSTEROINFERIOR DE ORELHA EXTERNA, INSERÇÃO PROFUNDA','EX16' :  'BORDA POSTERIOR DE PROCESSO MASTÓIDE','EX17' :  '0,5 CUN INFERIOR A COMISSURAS MEDIAIS DE OLHOS','EX18' :  'TRANSIÇÃO OSSO-CARTILAGEM EM NARINA PARALELO A COMISSURA MEDIAL DOS OLHOS','EX19' :  'LATERAL A ASA DE NARIZ EXTERNAMENTE','EX20' :  'MEDIANA DE LINHA ENTRE ASA NASAL E COMISSURA LABIAL','EX21' :  'ÂNGULO DE MANDÍBULA','EX22' :  'AO DOBRAR LÍNGUA PARA CIMA EM VEIAS LATERAIS DA LÍNGUA, BILATERALMENTE','EX23' :  'EM CENTRO SUPERIOR ACIMA DE OSSO HIÓIDE NA TIREÓIDE, INSERÇÃO POUCO PROFUNDA','EX24' :  '1 CUN SUPERIOR A CRICÓIDE, 0,3 CUN DE LINHA MÉDIA (SOBRE CARTILAGEM TIREÓIDE), INSERÇÃO POUCO PROFUNDA','EX25' :  'SOBRE BORDA LATERAL DE ECM, EM 1/3 SUPERIOR DE PESCOÇO','EX26' :  '1,5 CUN DE LINHA MEDIANA DA COLUNA, ALTURA DA C3 (ENTRE B10-B11) ','EX27' :  '2 CUN SUPERIOR A BORDA INFERIOR DA C7, 1 CUN BILATERAL DE LINHA MÉDIA','EX28' :  'ABAIXO DA C6','EX29' :  '0,5 CUN INFERIOR E 1 CUN ANTERIOR A LÓBULO DE ORELHA','EX30' :  'ENTRE BORDA DE MASTÓIDE E DEPRESSÃO INFERIOR ATRÁS DE LÓBULO DE ORELHA (TA17)','EX31' :  'ENTRE BORDA DE MASTÓIDE E VB20 (SULCO DE PROTUBERÂNCIA OCCIPTAL EM LINHA PUPILAR)','EX32' :  'ANTEROPOSTERIOR DE MASTÓIDE, A 0,5CUN ACIMA DE ANMIN1 ','EX33' :  '1 CUN BILATERALMENTE LATERAL A SULCO DE FÚRCULA ESTERNAL','EX34' :  '1,8C UN LATERAL A INTERSEÇÃO DE TERCEIRO EIC SOB LINHA DE MAMILO (E16)','EX35' :  '1 CUN LATERAL A CADA BORDA INFERIOR MAMILAR','EX36' :  '4 CUN ACIMA DO UMBIGO (VC12) E 0,5 CUN ACIMA E ABAIXO DE R19 (0,5CUN LATERAIS A 4 CUN ACIMA DE UMBIGO)','EX37' :  '3 CUN LATERAIS A PONTO 4 CUN ACIMA DO UMBIGO (VC12),INSERÇÃO POUCO PROFUNDA','EX38' :  '1 CUN LATERAL A PONTO 3 CUN ACIMA DO UMBIGO (VC11), INSERÇÃO POUCO PROFUNDA','EX39' :  '1 CUN ABAIXO DE PONTOS R14 (0,5 CUN LATERALMENTE EM 2 CUN ABAIXO DE UMBIGO)','EX40' :  '0,3 CUN ABAIXO DE PONTO 2 CUN ABAIXO DO UMBIGO (VC5)','EX41' :  '1 CUN LATERAIS A PONTO 3 CUN ABAIXO DO UMBIGO (VC4)','EX42' :  'INFERO-MEDIAL A ESPINHA ILÍACA ANTEROSUPERIOR, INSERÇÃO PROFUNDA','EX43' :  '2,5 CUN BILATERALMENTE LATERAL A VC3 (4 CUN INFERIOR A UMBIGO)','EX44' :  '3 CUN BILATERALMENTE LATERAL A VC3 (4 CUN INFERIOR A UMBIGO), INSERÇÃO POUCO PROFUNDA','EX45' :  '4 CUN LATERAIS A PONTO 3 CUN ABAIXO DO UMBIGO (VC4)','EX46' :  '3 CUN BILATERALMENTE LATERAL A VC2 (MARGEM SUPERIOR DE SÍNFISE PÚBICA)','EX47' :  '0,5 CUN MEDIALMENTE A BP15 (4 CUN LATERAIS A UMBIGO)','EX48' :  '1 CUN BILATERALMENTE LATERAL A VG14 (INFERIOR A C7)','EX49' :  '0,5 CUN BILATERALMENTE LATERAL A VG14 (INFERIOR A C7)','EX50' :  '1,5 CUN BILATERALMENTE LATERAL A VG14 (INFERIOR A C7)','EX51' :  '8 PONTOS DE BASES DE TRIÂNGULO MEDIDO EM QUARTO INTERMAMILAR COM ÁPICE EM C7, C8, C9 E C10','EX52' :  '0,5 CUN BILATERALMENTE LATERAL A BORDA INFERIOR DE T3','EX53' :  'BORDA INFERIOR DE T4','EX54' :  '0,5 CUN BILATERALMENTE LATERAL A BORDA INFERIOR DE T4','EX55' :  '0,5 CUN BILATERALMENTE LATERAL A BORDA INFERIOR DE T5','EX56' :  '0,5 CUN BILATERALMENTE LATERAL A BORDA INFERIOR DE T6','EX57' :  '0,5 CUN BILATERALMENTE LATERAL A BORDA INFERIOR DE T7','EX58' :  '2 CUN BILATERALMENTE LATERAL A BORDA INFERIOR DE T7','EX59' :  '6 CUN BILATERALMENTE LATERAL A BORDA INFERIOR DE T12','EX60' :  '3,5 CUN BILATERALMENTE LATERAL A BORDA INFERIOR DE L1, INSERÇÃO POUCO PROFUNDA','EX61' :  'EM CENTRO DO PROCESSO ESPINHOSO DE L2 (ENTRE VG4-VG5)','EX62' :  '4 CUN BILATERALMENTE LATERAL A BORDA INFERIOR DE L2','EX63' :  'LATERALMENTE A MÚSCULOS ILIOCOSTAIS EM ALTURA DE L2, INSERÇÃO PROFUNDA','EX64' :  '3 CUN LATERAL A COLUNA NA ALTURA DE BORDA INFERIOR L4, INSERÇÃO PROFUNDA','EX65' :  '3,8 CUN LATERAL A COLUNA NA ALTURA DE BORDA INFERIOR L4, INSERÇÃO PROFUNDA','EX66' :  '3,5 CUN LATERAL A COLUNA NA ALTURA DE BORDA INFERIOR L5, INSERÇÃO PROFUNDA','EX67' :  'DEPRESSÃO ABAIXO DE S1','EX68' :  'LINHA TROCÂNTER MAIOR-TUBÉRCULO ISQUIÁTICO  COMO BASE DE TRIÂNG. EQUIL. PONTO É ÁPICE,  MUITO PROFUNDA','EX69' :  'PONTO MÉDIO VB30-VG2 (HIATO SACRAL E 2/3 DE CÓCCIX-TROCANTER MAIOR), INSERÇÃO MUITO PROFUNDA','EX70' :  '0,5 CUN LATERAL A COLUNA NA ALTURA DE BORDAS INFERIORE DE: T1-T12 E L1-L5 (2 PARES DE 17 PONTOS)','EX71' :  '1 CUN ABAIXO DE PONTO MÉDIO TROCÂNTER MAIOR E CÓCCIX, INSERÇÃO MUITO PROFUNDA','EX72' :  'LINHA MÉDIA ENTRE A L5 E S1','EX73' :  'PONTAS DE DEDOS DE MÃOS, 0,1 CUN DE UNHAS','EX74' :  'PONTO MÉDIO DE PREGA DE 3IFD','EX75' :  'PONTO MÉDIO DE PREGAS 2IFP, 3IFP, 4IFP E 5IFP BILATERAIS (MANIPULAR ATÉ SAIR LÍQUIDO AMARELO)','EX76' :  'PONTO MÉDIO DE PREGA DE 3MCF, , INSERÇÃO POUCO PROFUNDA','EX77' :  '1 CUN PROXIMAL DE 2MCF E 3MCF','EX78' :  'MEDIANA ENTRE ID3-ID4 (LADO ULNAR ENTRE DE 5MCF-PSIFORME)','EX79' :  'MEIO DE LADO POSTERIOR DA 1IF','EX80' :  'MEIO DA 3IFD POSTERIORMENTE','EX81' :  'PREGA INTERDIGITAL DORSAL DE MÃOS','EX82' :  '0,5 CUN PROXIMAL EM DORSO DE 2MCF E 3MCF','EX83' :  'EM LINHA MÉDIA ENTRE PREGA DORSAL ULNAR DE 3MCF E LINHA DORSAL DO PUNHO (AO CENTRO DA MÃO)','EX84' :  '4 CUN PROXIMAL DE PUNHO ANTERIOR ENTRE TENDÕES E OUTRO LADO RADIAL APÓS TENDÃO','EX85' :  '1 CUN PROXIMAL E RADIAL DE MEIO DO PUNHO ANTERIOR','EX86' :  'COTOVELO FLEXIONADO E PALMA EM ABDOME, 2 PONTOS EM 1/4 E 3/4 DE IG11-TA4 (PREGA MEDIAL COTOVELO E PUNHO)','EX87' :  'PONTO MÉDIO ENTRE PREGAS PUNHO E COTOVELO, ENTRE RÁDIO E ULNA','EX88' :  '1 CUN EM DIREÇÃO AO DEDO 3 EM P5 (LATERAL DE TENDÃO BICEPTAL EM PREGA DE COTOVELO)','EX89' :  'EM LINHA DE IG15 (DELTÓIDE-ACRÔMIO), 1,5 POSTERIOR ACIMA DE PREGA AXILAR E OUTRO 1 CUN ANTERIOR, 3 PONTOS','EX90' :  'PONTO MÉDIO P2 (LINHA MEDIANA DA CURVA CLAVICULAR) E IG 15 (DELTÓIDE-ACRÔMIO)','EX91' :  '3,5 CUN ANTEROLATERAIS A ACRÔMIO (EM DELTÓIDE)','EX92' :  '1,5 CUN ANTEROLATERAIS A ACRÔMIO (EM DELTÓIDE)','EX93' :  '0,5 CUN PROXIMAIS E DISTAIS A R1 (1/3 DISTAL EM PLANTA DO PÉ ENTRE 2MTF E 3MTF)','EX94' :  '1 CUN PROXIMAL A R1 (1/3 DISTAL EM PLANTA DO PÉ ENTRE 2MTF E 3MTF)','EX95' :  'BARICENTRO DE CALCÂNEO EM DORSO DE PÉ','EX96' :  'ENTRE CABEÇAS DE METATARSOS EM DORSO DE PÉ (4 EM CADA LADO)','EX97' :  'MEIO DE TENDÃO DO CALCÂNEO','EX98' :  '2 CUN SUPERIORES A E41 (LINHA ANTERIOR DE TORNOZELO, ENTRE OS 2 TENDÕES EM DORSO DE PÉ)','EX99' :  '1 CUN MEDIAL A B57 (MEDIANA FOSSA POPLÍTEA-LINHA DE CALCÂNEOS, EM PANTURRILHA), INSERÇÃO PROFUNDA','EX100' :  '1 CUN LATERAL A B57 (MEDIANA FOSSA POPLÍTEA-LINHA DE CALCÂNEOS, EM PANTURRILHA)','EX101' :  '3 CUN SUPERIORES A E41 (LINHA ANTERIOR DE TORNOZELO, ENTRE OS 2 TENDÕES EM DORSO DE PÉ) E 1 LATERAL A TÍBIA','EX102' :  '0,5 CUN INFERIOR A E36 (3 CUN ABAIXO DE PATELA, LATERALMENTE A TÍBIA)','EX103' :  '2 CUN INFERIOR A E36 (3 CUN ABAIXO DE PATELA, LATERALMENTE A TÍBIA)','EX104' :  'BORDA LATERAL AO LIMITE INFERIOR DE PATELA','EX105' :  'PONTO MÉDIO AO LIMITE INFERIOR DE PATELA','EX106' :  '1 CUN ABAIXO DE VB34 (DEPRESSÃO ANTEROINFERIOR DE CABEÇA DE FÍBULA)','EX107' :  'DEPRESSÃO POSTERIOR A CABEÇA DE FÍBULA','EX108' :  'COM JOELHO FLETIDO, DEPRESSÃO DE BORDA SUPERIOR PATELAR','EX109' :  '2 CUN ABAIXO DE VB34 (DEPRESSÃO ANTEROINFERIOR DE CABEÇA DE FÍBULA)','EX110' :  '2 CUN ANTERIOR A VB31 (EM PÉ ONDE BATE PONTA DE DEDO 3 DE MÃOS)','EX111' :  '2 CUN SUPERIOR A VB31 (EM PÉ ONDE BATE PONTA DE DEDO 3 DE MÃOS)','EX112' :  '7 CUN ACIMA DE PATELA, PARALELO A LINHA PATELAR LATERAL','EX113' :  '3 CUN ACIMA DE PATELA, PARALELO A LINHA PATELAR MEDIAL','EX114' :  '1 CUN LATERAL A PREGA POPLÍTEA LATERAL','EX115' :  '2 CUN SUPERIOR A PREGA POPLÍTEA LATERAL','EX116' :  '3 CUN SUPERIOR A PREGA POPLÍTEA LATERAL','EX117' :  '4 CUN SUPERIOR A PREGA POPLÍTEA LATERAL, INSERÇÃO MUITO PROFUNDA, TODA AGULHA','EX118' :  '5 CUN SUPERIOR A PREGA POPLÍTEA LATERAL, INSERÇÃO MUITO PROFUNDA, TODA A AGULHA','EX119' :  '6 CUN SUPERIOR A PREGA POPLÍTEA LATERAL, INSERÇÃO MUITO PROFUNDA, TODA A AGULHA','EX120' :  'MEIO DE LINHA TROCANTE MAIOR E ESPINHA ILÍACA ANTERO-SUPERIOR','EX121' :  '3 CUN BILATERALMENTE LATERAL A VC6 (1,5 CUN INFERIOR A UMBIGO)','EX122' :  '3 CUN BILATERALMENTE LATERAL A VC4 (3 CUN INFERIOR A UMBIGO)','EX123' :  '1,5 CUN LATRAL A B52 (L2 INFERIOR A 3 CUN DE LINHA MEDIANA)','EX124' :  'PONTO MÉDIO AXILA E IG15 (ANTERIOR DE ACRÔMIO)','EX125' :  '7 CUN SUPERIOR A MALÉOLO MEDIAL, 0,5 CUN POSTERIOR A TÍBIA','EX126' :  '2 PONTOS EM DORSO DE MÃOS, ENTRE 2MCF-3MCF E 4MCF-5MCF, AO CENTRO DA MÃO (USAR EM LADO DE DOR)','EX127' :  'TRIÂNGULO EQUILÁTERO COM ÁPICE EM UMBIGO (SEM AGULHA) E LADOS NO TAMANHO HORIZONTAL DA BOCA '}
global cls
def cls(): return print("\x1b[2J\x1b[1;1H", end="")
global tipo_shi  # estado shi (escrito oculto como bp, p, f, pc...)
tipo_shi = set()
global smt
smt = set()
# print(dx[10]) ou pct.add() ou pct[2]
# lista de resultados do paciente e coleta de dados (banco volátil de dados)
global pct
pct = set()
# pct.add(dx[10]) >>>>> ADICIONAR DX AO PACIENTE
global pool
pool = set()  # PULSOS PATOLÓGICOS
global pool2
pool2 = set()
global pool3
pool3 = set()  # PONTOS DE ACUPUNTURA
global path
path = set()
global vector1
vector1 = [0, 0, 0, 0, 0, 0]
global vector2
vector2 = [0, 0, 0, 0, 0, 0]
global perfil
perfil = [0, 0, 0, 0, 0]
global ver
ver = '2.5'
global seta
seta = set()
global pipe
pipe = 999
global dxcid
dxcid = set()
global tensor
tensor = set()
global coid
coid = set()
global warn
warn = set()
global dxconf
dxconf = set()
global exame_x
exame_x = set()
global oneway
oneway = set()
global homm
homm = ''
global lembrete
lembrete = set()
class limpar(set):
    def __str__(self):
        return ', '.join([str(i) for i in self])
home()