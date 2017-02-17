class CadenasTp1:
    algo=[]
    cad=raw_input('Escribe un nombre: ')
    print cad, ' tiene ',len(cad), ' caracteres '
    print 'La cadena ',cad,' escrita al reves es ', cad[::-1]
    # Creando array de Strings
    algo=["clases","python","pelo","aula",cad,"cielo"]
    for var in algo:
        print var