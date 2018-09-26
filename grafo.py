#!/usr/bin/env python
# coding=utf-8

import pandas as pd
import networkx as nx
import random
import matplotlib.pyplot as plt
#Diccionario de nodos y arcos

def leerInformacion(Grafo):
    file = 'CPS.xlsx'
    #x = pd.ExcelFile(file)
    line1 = pd.read_excel(file) #DataFrame
    #print(line1)
    #Grafo.add_node(nombre)7

    #DataFrame por codPueblo

    #DataFrame a diccionario
    dicc_nodos = line1.set_index('CODCP').T.to_dict('list')

    line1.set_index(['CODCP'], inplace=True)
    #print(dicc_nodos)
    GenerarGrafoDiccionario(dicc_nodos,line1,Grafo)

def GenerarGrafoDiccionario(dicc_nodos,dataXCodigo,Grafo):
    #print(dataXCodigo)
    #print('--------')
    #print(dataXCodigo.loc[683896].Y_X_COORD)
    print(dicc_nodos)
    print('----------')
    print(dataXCodigo)
    print('----------')
    grafo = {}
    a = 1
    
   
    
    for x in dicc_nodos:
        arreglo_grafo = Grafo.nodes().data()
        if len(Grafo.nodes()) == 0: 
            Grafo.add_node(x)
            #plt.show()
            
            print(Grafo.nodes())
            #Nodo con codigo de la ciudad
        elif len(Grafo.nodes()) >= 1: 
            #coordenadas
            #print(grafo)
            listKeys = list(Grafo.nodes())
            valor = random.randint(0,len(listKeys)-1)
            #a = Grafo.nodes[listKeys[valor]]
            #b = dicc_nodos[listKeys[valor]]
            
            Grafo.add_edge(x,listKeys[valor])
            #grafo[grafo.keys()[0]] = [(x,'DISTANCIA')]
            #y,x = extraerCoordenadas(dicc_nodos[grafo.keys()[0]][1])
            
            
            #y2,x2 = extraerCoordenadas(grafo[grafo.keys()[0]][1][0])
            #print(y + " : " + x)
            #print(y2 + " : " + x2)

            #print(distance((x,y),(x2,y2)))
            
            #grafo[x] = []
            #print(grafo.keys())
            #grafo[grafo.keys()[1]] = [(grafo.keys()[0],'DISTANCIA')]
        
        a+=1;
        #print('Grafo---')
    nx.draw_networkx(Grafo)
    plt.show()

def GenerarGrafoDicci(dicc_nodos,dataXCodigo):
    #print(dataXCodigo)
    #print('--------')
    #print(dataXCodigo.loc[683896].Y_X_COORD)
    grafo = []
    listKeys = dicc_nodos.keys()
    
    for x in dicc_nodos:
        nodo = {}
        
        if len(grafo) == 0: 
            nodo = {}
            nodo[x] 
            grafo.append(nodo)
             #Nodo con codigo de la ciudad
        elif len(grafo) == 1: 
            #coordenadas
            #print(grafo)
            grafo.append()
            grafo[grafo.keys()[0]] = [(x,'DISTANCIA')]
            y,x = extraerCoordenadas(dicc_nodos[grafo.keys()[0]][1])
            
            
            #y2,x2 = extraerCoordenadas(grafo[grafo.keys()[0]][1][0])
            #print(y + " : " + x)
            #print(y2 + " : " + x2)

            #print(distance((x,y),(x2,y2)))
            
            grafo[x] = []
            print(grafo.keys())
            grafo[grafo.keys()[1]] = [(grafo.keys()[0],'DISTANCIA')]
        
        a+=1;
        print(grafo)


def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5


def agregarDatosGrafo(nombre,dataFrame,Grafo):
    print(dataFrame.columns[1])
    print(nombre)
    #Grafo.add_edge('X',nombre,label='10')
    Grafo.add_edge('a','b',label='8')
    Grafo.add_edge('a','c',label='2')
    Grafo.add_edge('a','e',label='6')
    Grafo.add_edge('a','d',label='4')
    Grafo.add_edge('b','c',label='6')
    Grafo.add_edge('b','e',label='9')
    Grafo.add_edge('b','d',label='12')
    Grafo.add_edge('c','e',lebel='5')
    Grafo.add_edge('c','d',label='3')
    Grafo.add_edge('d','e',label='4')

def extraerCoordenadas(dato):
    xy = dato.split('-')
    y = xy[1]
    x = xy[2]
    
    return y,x



G = nx.Graph()

leerInformacion(G)



#extraerCoordenadas('-13.992029757-72.5312662119999')