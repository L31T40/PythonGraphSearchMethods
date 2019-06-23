Grafo = {
    'Aveiro': [('Porto'), ('Viseu'), ('Coimbra'), ('Leiria')],
    'Braga': [('Viana do Castelo'), ('Vila Real'), ('Porto')],
    'Bragança': [('Vila Real'), ('Guarda')],
    'Beja': [('Évora'), ('Faro'), ('Setúbal')],
    'Castelo Branco': [('Coimbra'), ('Guarda'), ('Portalegre'), ('Évora')],
    'Coimbra': [('Viseu'), ('Leiria'), ('Aveiro'), ('Castelo Branco')],
    'Évora': [('Lisboa'), ('Santarém'), ('Portalegre'), ('Setúbal'), ('Beja'), ('Castelo Branco')],
    'Faro': [('Setúbal'), ('Lisboa'), ('Beja')],
    'Guarda': [('Vila Real'), ('Viseu'), ('Bragança'), ('Castelo Branco')],
    'Leiria': [('Lisboa'), ('Santarém'), ('Aveiro'), ('Coimbra')],
    'Lisboa': [('Santarém'), ('Setúbal'), ('Faro'), ('Leiria'), ('Évora')],
    'Portalegre': [('Castelo Branco'), ('Évora')],
    'Porto': [('Aveiro'), ('Viana do Castelo'), ('Vila Real'), ('Viseu'), ('Braga')],
    'Santarém': [('Évora'), ('Lisboa'), ('Leiria')],
    'Setúbal': [('Lisboa'), ('Évora'), ('Beja'), ('Faro')],
    'Viana do Castelo': [('Braga'), ('Porto')],
    'Vila Real': [('Viseu'), ('Braga'), ('Bragança'), ('Guarda'), ('Porto')],
    'Viseu': [('Aveiro'), ('Coimbra'), ('Porto'), ('Vila Real'), ('Guarda')]
}

GrafocomCustos = {
    'Aveiro': [('Porto',68), ('Viseu',95), ('Coimbra',68), ('Leiria',115)],
    'Braga': [('Viana do Castelo',48), ('Vila Real',106), ('Porto',53)],
    'Bragança': [('Vila Real',137), ('Guarda',202)],
    'Beja': [('Évora',78), ('Faro',152), ('Setúbal',142)],
    'Castelo Branco': [('Coimbra',159), ('Guarda',106), ('Portalegre',80), ('Évora',203)],
    'Coimbra': [('Viseu',96), ('Leiria',67), ('Aveiro',68), ('Castelo Branco',159)],
    'Évora': [('Lisboa',150), ('Santarém',117), ('Portalegre',131), ('Setúbal',103), ('Beja',78), ('Castelo Branco',203)],
    'Faro': [('Setúbal',249), ('Lisboa',299), ('Beja',152)],
    'Guarda': [('Vila Real',157), ('Viseu',85), ('Bragança',202), ('Castelo Branco',106)],
    'Leiria': [('Lisboa',129), ('Santarém',70), ('Aveiro',115), ('Coimbra',67)],
    'Lisboa': [('Santarém',78), ('Setúbal',50), ('Faro',299), ('Leiria',129), ('Évora',150)],
    'Portalegre': [('Castelo Branco',80), ('Évora',131)],
    'Porto': [('Aveiro',68), ('Viana do Castelo',71), ('Vila Real',116), ('Viseu',133), ('Braga',53)],
    'Santarém': [('Évora',117), ('Lisboa',78), ('Leiria',70)],
    'Setúbal': [('Lisboa',50), ('Évora',103), ('Beja',142), ('Faro',249)],
    'Viana do Castelo': [('Braga',48), ('Porto',71)],
    'Vila Real': [('Viseu',110), ('Braga',106), ('Bragança',137), ('Guarda',157), ('Porto',116)],
    'Viseu': [('Aveiro',95), ('Coimbra',96), ('Porto',133), ('Vila Real',110), ('Guarda',85)]
}




def profundidadePrimeiro(grafo, inicio, fim, debug):

    
    fronteiras = [inicio, ]
    visitados = []
    contador = 0

    while 1:
        # atribui a variavel no_atual o 1 elemento do nodo -> inicio

        no_atual = fronteiras.pop()

        # atribui ao aray visitados o 1 elemento do nodo -> inicio
        visitados.append(no_atual)

        if debug == 1:
            print(100 * '-')
            print('Iteração ' + str(contador))
            print('Nó selecionado: '+ no_atual)  
        # Verifica se o nodo atual é o objetivo var end
        if no_atual == fim:
            if debug == 1:
                print('Trajeto ->' + str(visitados))
                print('Chegou a %s' % str(fim))

            print(*visitados)
            return
       
        # Percorre nodos adjacentes
        for node in reversed(grafo[no_atual]): 
            if node not in visitados:
                fronteiras.append(node)

        if debug == 1:
            print('Nós ->' + str(fronteiras))        
            print('Trajeto ->' + str(visitados))
            print(100 * '-')
        
        contador += 1

def profundidadePrimeiroRecursiva(Grafo,no,visitado):
    if no not in visitado:
        visitado.append(no)
        for n in Grafo(no):
            profundidadePrimeiroRecursiva(Grafo,n,visitado)
    return visitado
    
    





profundidadePrimeiro(Grafo,'Aveiro','Leiria',1)


