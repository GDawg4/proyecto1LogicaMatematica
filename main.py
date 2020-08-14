# Luis Pedro Cuéllar 18220
# Rodrigo Garoz 18102
# Gerardo Méndez 18239

# Proyecto 1 - Cierre Transitivo

# Las funciones son aplicaciones de la teoría extraída de: Rosen, K. H. (2011). Discrete Mathematics and Its Applications (7.a ed.)

import numpy as np

# definimos la clase grafo
class Grafo:

  # inicialización del objeto
  def __init__(self, v):
    self.size = v

  # función para imprimir la matriz 
  def printSolution(self, solutionMatrix, mode): 
    (
      print ("El cierre transitivo por matrices para el grafo es: ") if mode == 1 else 
      print ("El cierre transitivo por Warshall para el grafo es: ") 
    )
    for i in range(self.size): 
      for j in range(self.size): 
        print (solutionMatrix[i][j], end =' ')
      print(' ')

  # operación V para matrices 
  def logicOr(self, m1, m2):
    res = [[0 for x in i] for i in m1]

    for x in range(self.size):
      for y in range(self.size):
        res[x][y] = 0 if m1[x][y] == 0 and m2[x][y] == 0 else 1
    
    return res

  # se calcula el cierre transitivo del grafo usando matrices
  # se calculan las matrices booleanas para R2, R3, ..., Rn
  # luego se hace la operación V entre cada una de ellas para obtener la matriz de cierre transitivo
  # ref. 
  def matricesBooleanas(self, grafo):
    mx_1 = grafo
    mx = mx_1

    for x in range(self.size):
      mx_1 = np.matmul(mx_1, grafo)
      mx_1 = [[1 if x >= 1 else 0 for x in i] for i in mx_1]

      mx = self.logicOr(mx_1, mx)
    
    self.printSolution(mx, 1)
  
  # se calcula el cierre transitivo del grafo con el algoritmo de Warshall
  def warshall(self, grafo):
    reach =[i[:] for i in grafo]

    for k in range(self.size):
      for i in range(self.size):
          for j in range(self.size):
              reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    
    self.printSolution(reach, 2)

# grafo representado en la matriz booleana R
R = [
  	[1, 1, 0, 1],
	[0, 1, 1, 0],
	[0, 0, 1, 1],
	[0, 0, 0, 1]
]

# inicialización del objeto Grafo
grafo = Grafo(len(R))

# se llama a los dos métodos para calcular el cierre transitivo
grafo.matricesBooleanas(R)
grafo.warshall(R)

