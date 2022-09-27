import re

def re_strip(string: str, remove: str = '') -> str:
    if remove == '':
        regex = re.compile(r'(\S+)')
    else:
        regex = re.compile(fr'([^{remove}]+)')
    regex_fa = regex.findall(string)
    txt = ' '.join(regex_fa)
    return txt

texto = '    ola   oiii. ´ ^; '

texto_strip = re_strip(texto)

print(texto_strip)
