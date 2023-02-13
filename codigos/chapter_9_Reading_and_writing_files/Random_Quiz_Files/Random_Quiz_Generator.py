if __name__ == '__main__':
    from Random_Quiz_Generator_data import paises, capitais, dados
    from random import choices, shuffle

    todas_capitais = capitais.copy()
    todos_paises = paises.copy()

    for i in range(1,36): # Criar arquivos txt
        capitais = todas_capitais.copy()
        paises = todos_paises.copy()
        
        path_p = fr'''C:\Users\grusi\Gabriel\Programacao\MeusProjetos\Automate-the-Boring-Stuff-with-Python\codigos\chapter_9_Reading_and_writing_files\Random_Quiz_Files\Perguntas_Respostas\teste{i}.txt'''
        path_r = fr'''C:\Users\grusi\Gabriel\Programacao\MeusProjetos\Automate-the-Boring-Stuff-with-Python\codigos\chapter_9_Reading_and_writing_files\Random_Quiz_Files\Perguntas_Respostas\resposta{i}.txt'''
        pergunta = open(path_p,'w')
        resposta = open(path_r,'w')
        for x in range(1,51): # Preencher arquivos txt
            
            pais = choices(paises,k=1)[0]
            paises.remove(pais)
            capitais.remove(dados[pais])

            capital_correta = dados[pais]
            capitais_questao = choices(capitais,k=3)
            capitais_questao.append(capital_correta)
            shuffle(capitais_questao)

            cap1,cap2,cap3,cap4 = capitais_questao

            txtp = f'''{x}. Capital de {pais}:
            1. {cap1}
            2. {cap2}
            3. {cap3}
            4. {cap4}
            
            '''
            txtc = f'Resposta da questão {x}: {capital_correta}\n'
            resposta.write(txtc)
            pergunta.write(txtp)
        resposta.close()
        pergunta.close()

