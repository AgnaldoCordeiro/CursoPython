import ctypes

atributo_ocultar = 0x02


retorno = ctypes.windll.kernel32.SetFileAttributesW('C:/Wordspace/CursoPython/ocultador/ocultador.txt', atributo_ocultar)


if retorno:
    print('Arquivo foi ocultado')
else:
    print('Erro ao ocultar arquivo')