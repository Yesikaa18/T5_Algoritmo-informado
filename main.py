import networkx as nx
from matplotlib import pyplot as plt

from graph import Graph, Node
from a_star import AStar
import time

inicio = time.time()

# Código a medir
time.sleep(1)

def run():
    # Create graph
    graph = Graph()

    # Add vertices
    graph.add_node(Node('a', (1, 1)))
    graph.add_node(Node('b', (1, 2)))
    graph.add_node(Node('c', (1, 4)))
    graph.add_node(Node('d', (2, 1)))
    graph.add_node(Node('e', (2, 2)))
    graph.add_node(Node('f', (2, 3)))
    graph.add_node(Node('g', (2, 4)))
    graph.add_node(Node('h', (3, 1)))
    graph.add_node(Node('i', (3, 4)))
    graph.add_node(Node('j', (4, 1)))
    graph.add_node(Node('k', (4, 2)))
    graph.add_node(Node('l', (4, 3)))
    graph.add_node(Node('m', (4, 4)))
    graph.add_node(Node('n', (1, 1)))
    graph.add_node(Node('o', (1, 2)))
    graph.add_node(Node('p', (1, 4)))
    graph.add_node(Node('q', (2, 1)))
    graph.add_node(Node('r', (2, 2)))
    graph.add_node(Node('s', (2, 3)))
    graph.add_node(Node('t', (2, 4)))
    graph.add_node(Node('u', (3, 1)))
    graph.add_node(Node('v', (3, 4)))
    graph.add_node(Node('w', (4, 1)))
    graph.add_node(Node('x', (4, 2)))
    graph.add_node(Node('y', (4, 3)))
    graph.add_node(Node('z', (4, 4)))

    graph.add_node(Node('A', (1, 1)))
    graph.add_node(Node('B', (1, 2)))
    graph.add_node(Node('C', (1, 4)))
    graph.add_node(Node('D', (2, 1)))
    graph.add_node(Node('E', (2, 2)))
    graph.add_node(Node('F', (2, 3)))
    graph.add_node(Node('G', (2, 4)))
    graph.add_node(Node('H', (3, 1)))
    graph.add_node(Node('I', (3, 4)))
    graph.add_node(Node('J', (4, 1)))
    graph.add_node(Node('K', (4, 2)))
    graph.add_node(Node('L', (4, 3)))
    graph.add_node(Node('M', (4, 4)))
    graph.add_node(Node('N', (1, 1)))
    graph.add_node(Node('O', (1, 2)))
    graph.add_node(Node('P', (1, 4)))
    graph.add_node(Node('Q', (2, 1)))
    graph.add_node(Node('R', (2, 2)))
    graph.add_node(Node('S', (2, 3)))
    graph.add_node(Node('T', (2, 4)))
    graph.add_node(Node('U', (3, 1)))
    graph.add_node(Node('V', (3, 4)))
    graph.add_node(Node('W', (4, 1)))
    graph.add_node(Node('X', (4, 2)))
    graph.add_node(Node('Y', (4, 3)))
    graph.add_node(Node('Z', (4, 4)))

    graph.add_node(Node('1', (1, 1)))
    graph.add_node(Node('2', (1, 2)))
    graph.add_node(Node('3', (1, 4)))
    graph.add_node(Node('4', (2, 1)))
    graph.add_node(Node('5', (2, 2)))
    graph.add_node(Node('6', (2, 3)))
    graph.add_node(Node('7', (2, 4)))
    graph.add_node(Node('8', (3, 1)))
    graph.add_node(Node('9', (3, 4)))
    graph.add_node(Node('10', (4, 1)))

    # Definir las aristas
    graph.add_edge('a', 'c', 14)
    graph.add_edge('a', 'e', 7)
    graph.add_edge('a', 'b', 9)
    graph.add_edge('a', 'B', 28)
    graph.add_edge('a', 'C', 31)

    graph.add_edge('b', 'f', 9)
    graph.add_edge('b', 'd',6)
    graph.add_edge('b', 'K', 17)
    graph.add_edge('c', 'b', 14)
    graph.add_edge('c', 'a', 9)
    graph.add_edge('c', 'd', 2)
    graph.add_edge('c', 'G', 12)
    graph.add_edge('c', 'F', 29)

    graph.add_edge('d', 'c', 7)
    graph.add_edge('d', 'e', 10)
    graph.add_edge('d', 'f', 15)
    graph.add_edge('d', 'O', 15)

    graph.add_edge('e', 'a', 9)
    graph.add_edge('e', 'd', 2)
    graph.add_edge('e', 'q', 10)
    graph.add_edge('e', 'c', 11)
    graph.add_edge('e', 'F', 8)

    graph.add_edge('f', 'h', 6)
    graph.add_edge('f', 'j', 15)
    graph.add_edge('f', 'e', 11)
    graph.add_edge('f', 'E', 11)

    graph.add_edge('g', 'b', 3)
    graph.add_edge('g', 'j', 6)
    graph.add_edge('g', 'U', 18)

    graph.add_edge('h', 'a', 14)
    graph.add_edge('h', 'i', 19)
    graph.add_edge('h', 'f', 2)
    graph.add_edge('h', 'L', 18)

    graph.add_edge('i', 'c', 7)
    graph.add_edge('i', 'q', 10)
    graph.add_edge('i', 'f', 15)
    graph.add_edge('i', 'P', 26)

    graph.add_edge('j', 'e', 9)
    graph.add_edge('j', 'h', 2)
    graph.add_edge('j', 'k', 11)
    graph.add_edge('j', 'K', 10)

    graph.add_edge('k', 'l', 9)
    graph.add_edge('k', 'P', 19)

    graph.add_edge('l', 'b', 14)
    graph.add_edge('l', 'u', 9)
    graph.add_edge('l', 'x', 2)
    graph.add_edge('l', 'a', 12)

    graph.add_edge('m', 'c', 7)
    graph.add_edge('m', 's', 10)
    graph.add_edge('m', 't', 15)
    graph.add_edge('m', 'C', 19)

    graph.add_edge('n', 'g', 9)
    graph.add_edge('n', 'm', 2)
    graph.add_edge('n', 'c', 11)
    graph.add_edge('n', 'C', 12)
    graph.add_edge('n', 'B', 20)
    graph.add_edge('n', 'I', 15)

    graph.add_edge('o', 'e', 9)
    graph.add_edge('o', 's', 6)
    graph.add_edge('o', 'D', 3)
    graph.add_edge('o', 'H', 7)

    graph.add_edge('p', 'u', 14)
    graph.add_edge('p', 'a', 9)
    graph.add_edge('p', 'w', 2)

    graph.add_edge('q', 'o', 7)
    graph.add_edge('q', 'e', 10)
    graph.add_edge('q', 'k', 15)

    graph.add_edge('r', 'w', 9)
    graph.add_edge('r', 'x', 10)

    graph.add_edge('s', 'c', 9)
    graph.add_edge('s', 'i', 6)

    graph.add_edge('t', 'c', 14)
    graph.add_edge('t', 'a', 9)

    graph.add_edge('u', 'z', 7)
    graph.add_edge('u', 'q', 10)
    graph.add_edge('u', 'v', 0)

    graph.add_edge('v', 'e', 9)
    graph.add_edge('v', 'b', 2)
    graph.add_edge('v', 'x', 10)
    graph.add_edge('v', 'c', 11)

    graph.add_edge('w', 'a', 9)
    graph.add_edge('w', 'd', 6)

    graph.add_edge('x', 'g', 14)
    graph.add_edge('x', 'r', 9)
    graph.add_edge('x', 's', 2)

    graph.add_edge('y', 'e', 7)
    graph.add_edge('y', 'm', 10)
    graph.add_edge('y', 'l', 15)

    graph.add_edge('z', 'a', 9)
    graph.add_edge('z', 'd', 2)
    graph.add_edge('z', 'f', 10)
    graph.add_edge('z', 'B', 11)

    #Nodos del A-Z
    graph.add_edge('A', 'a', 12)
    graph.add_edge('A', 'x', 2)
    graph.add_edge('A', 'g', 10)

    graph.add_edge('B', 'c', 2)
    graph.add_edge('B', 'u', 6)
    graph.add_edge('B', 'h', 1)
    graph.add_edge('B', 'J', 23)

    graph.add_edge('C', 'a', 7)
    graph.add_edge('C', 'z', 11)

    graph.add_edge('D', 'C', 3)
    graph.add_edge('D', 'e', 9)
    graph.add_edge('D', 'r', 4)

    graph.add_edge('E', 'A', 1)
    graph.add_edge('E', 'C', 4)
    graph.add_edge('E', 'h', 12)
    graph.add_edge('E', '5', 79)

    graph.add_edge('F', 'D', 6)
    graph.add_edge('F', 'a', 13)

    graph.add_edge('G', 'y', 4)
    graph.add_edge('G', 'w', 8)
    graph.add_edge('G', 's', 5)
    graph.add_edge('G', 'C', 7)
    graph.add_edge('G', 'L', 29)

    graph.add_edge('H', 'A', 1)
    graph.add_edge('H', 'a', 14)
    graph.add_edge('H', 'G', 12)

    graph.add_edge('I', 'E', 12)
    graph.add_edge('I', 'u', 7)
    graph.add_edge('I', 'W', 12)

    graph.add_edge('J', 'I', 2)
    graph.add_edge('J', 'H', 6)
    graph.add_edge('J', 'b', 15)

    graph.add_edge('K', 'J', 4)
    graph.add_edge('K', 'c', 10)
    graph.add_edge('K', 'z', 4)
    graph.add_edge('K', 'F', 10)
    graph.add_edge('K', '1', 45)

    graph.add_edge('L', 'K', 12)
    graph.add_edge('L', 'B', 3)
    graph.add_edge('L', 'c', 6)
    graph.add_edge('L', 'M', 13)

    graph.add_edge('M', 'J', 1)
    graph.add_edge('M', 'j', 5)

    graph.add_edge('N', 'K', 3)
    graph.add_edge('N', 'u', 13)
    graph.add_edge('N', 'D', 45)

    graph.add_edge('O', 't', 3)
    graph.add_edge('O', 'u', 12)

    graph.add_edge('P', 'K', 4)
    graph.add_edge('P', 'G', 8)

    graph.add_edge('Q', 'P', 12)
    graph.add_edge('Q', 'O', 5)
    graph.add_edge('Q', 'L', 9)

    graph.add_edge('R', 'Q', 1)
    graph.add_edge('R', 'h', 3)
    graph.add_edge('R', 'x', 8)

    graph.add_edge('S', 'B', 5)
    graph.add_edge('S', 'D', 4)

    graph.add_edge('T', 'R', 12)
    graph.add_edge('T', 'o', 11)

    graph.add_edge('U', 'T', 10)
    graph.add_edge('U', 'a', 2)

    graph.add_edge('V', 'U', 9)
    graph.add_edge('V', 'S', 12)
    graph.add_edge('W', 'U', 10)
    graph.add_edge('W', 'i', 3)
    graph.add_edge('X', 'D', 3)
    graph.add_edge('X', 'a', 9)
    graph.add_edge('X', 'A', 19)
    graph.add_edge('Y', 'W', 6)
    graph.add_edge('Y', 'V', 7)
    graph.add_edge('Z', 'X', 11)
    graph.add_edge('Z', 'H', 2)
    graph.add_edge('Z', 'X', 7)

    graph.add_edge('1', 'a', 14)
    graph.add_edge('1', '5', 7)
    graph.add_edge('1', '2', 9)
    graph.add_edge('1', '4', 28)
    graph.add_edge('2', '6', 9)
    graph.add_edge('2', '4', 6)
    graph.add_edge('2', 'K', 17)
    graph.add_edge('3', '2', 14)
    graph.add_edge('3', '1', 9)
    graph.add_edge('3', '4', 2)
    graph.add_edge('3', '7', 12)
    graph.add_edge('4', '3', 7)
    graph.add_edge('4', '5', 10)
    graph.add_edge('4', '6', 15)
    graph.add_edge('4', 'O', 15)
    graph.add_edge('5', '1', 9)
    graph.add_edge('5', '4', 2)
    graph.add_edge('5', '7', 10)
    graph.add_edge('5', '3', 11)
    graph.add_edge('5', '6', 8)
    graph.add_edge('6', '8', 6)
    graph.add_edge('6', '10', 15)
    graph.add_edge('6', '5', 11)
    graph.add_edge('6', 'R', 11)
    graph.add_edge('7', '2', 3)
    graph.add_edge('7', '10', 6)
    graph.add_edge('7', 'U', 18)
    graph.add_edge('8', '1', 14)
    graph.add_edge('8', '9', 9)
    graph.add_edge('8', '6', 2)
    graph.add_edge('8', 'L', 18)
    graph.add_edge('9', '3', 7)
    graph.add_edge('9', 'q', 10)
    graph.add_edge('9', '6', 15)
    graph.add_edge('9', 'P', 26)
    graph.add_edge('10', '5', 9)
    graph.add_edge('10', '8', 2)
    graph.add_edge('10', 'k', 11)
    graph.add_edge('10', 'K', 10)


#En este caso, podemos reemplazar el grafo con estos valores nuevos


    alg = AStar(graph, "e", "z")
    path, path_length = alg.search()
    print("Recorrido: ")
    print(" -> ".join(path))
    print(f"Costo total: {path_length}")

fin = time.time()
print("Tiempo de ejecución del programa: ", fin-inicio)

dato = fin-inicio
if __name__ == '__main__':
    run()
