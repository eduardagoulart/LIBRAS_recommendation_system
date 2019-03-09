import re


def parser(html, token_search, token_stop, regex_numeral):
    p_start = [(a.end()) for a in list(re.finditer(token_search, html))]
    p_break = [(a.start()) for a in list(re.finditer(token_stop, html))]

    i = 0
    if regex_numeral:
        while i < len(p_start):
            if not re.match("[0-9]", html[p_start[i]].lower()):
                p_start.pop(i)
                i -= 1
            i += 1

    if len(p_start) == 0 or len(p_break) == 0:
        return None
    else:
        p_start = p_start[0]
        for i in p_break:
            if i > p_start:  # no primeiro ponto que a posição de pBreak for maior que p eu assumo aquele valor como valor de break do while que vai estar lá em baixo
                p_break = i
                break
    info = ''
    while p_start < p_break:
        info += html[p_start]
        p_start += 1

    return info


'''
    Função para salvar todas as informações encontradas dentro do intervalor definido de tokens
'''


def list_datas(html, token_search, token_stop):
    p_start = [(a.end()) for a in list(re.finditer(token_search, html))]
    p_break = [(a.start()) for a in list(re.finditer(token_stop, html))]

    end = []

    for a in range(len(list(re.finditer(token_search, html)))):
        for j in p_break:
            if j > p_start[a]:
                p_break[a] = j
                end.append(j)
                break

    lista_info = []
    for i in range(len(p_start)):
        info = ''
        while True:
            info += html[p_start[i]]
            p_start[i] += 1
            if p_start[i] > end[i]:
                lista_info.append(info)
                break

    return lista_info
