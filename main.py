import os, time

def remove_acento(char):
    mapa_acento = {
        'ã': 'a', 'â': 'a', 'á': 'a', 'à': 'a',
        'ç': 'c', 'é': 'e', 'è': 'e', 'ê': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i',
        'õ': 'o', 'ô': 'o', 'ò': 'o', 'ó': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u'
    }
    
    return mapa_acento.get(char, char)  # Retorna o caractere original se não houver mapeamento.

def cript(s):
    abc = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
           'x', 'y', 'z']
    
    arr_criptado = []
    s = s.lower()  # Converte toda a string para minúscula.

    for char in s:
        char_sem_acento = remove_acento(char)  # Remove o acento, se houver.
        if char_sem_acento in abc:
            arr_criptado.append(abc.index(char_sem_acento))
            
            
    os.system('cls')  # Limpa a tela do terminal.
    time.sleep(3)

    return arr_criptado

s = 'Ciclano roubou pão na casa do João'
print(cript(s)) 