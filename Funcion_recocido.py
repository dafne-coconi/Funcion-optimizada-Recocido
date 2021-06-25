import numpy as np
from numpy.random import randint, uniform

class Funcionx2():

    def __init__(self, max_iter, intervalo, numero_x):
        self.max_iter = max_iter
        self.intervalo = intervalo
        self.numero_x = numero_x

    def initial_solution(self):
        res = [np.round(uniform(low=self.intervalo[0], high=self.intervalo[1]),5) for _ in range(self.numero_x)]
        print(res)
        return res

    def random_neighbour(self, solution):
        random_index = randint(len(solution), size=1)[0]
        solution[random_index] = np.round(uniform(low=self.intervalo[0], high=self.intervalo[1]),5)
        return solution

    def eval(self, solution):
        res = sum(map(lambda x: x**2, solution))
        return res

    def solve(self, *args, **kwargs):
        solution = self.initial_solution()
        solution_eval = self.eval(solution)
        temperatura = solution_eval*0.4
        while temperatura >= 0.1:            
            for i in range(self.max_iter):
                neighbour = self.random_neighbour(solution.copy())
                neighbour_eval = self.eval(neighbour)
                delta = neighbour_eval - solution_eval
                message = str(i+1)+'.- Candidato x: '+str(neighbour)+ ' con f(x)={:.5f}'.format(neighbour_eval)+ ' < a solucion actual x: '+str(solution)+ ' con f(x)={:.5f}'.format(solution_eval)
                if delta <= 0 or np.random.uniform(low=0.0, high=1.0, size=None) < np.power(np.e,(-delta/(20*temperatura))):
                    solution, solution_eval = neighbour, neighbour_eval
                    if delta <= 0:
                        message += ' --> El candidato es mejor solucion'
                        print(message,'\n')
                    else:
                        message += ' --> El candidato es peor solución, pero se acepta'
                        print(message,'\n')
                else:
                    print(message,'\n')
            temperatura = temperatura * np.random.uniform(low=0.8, high=0.99, size=None)  
            print('Temperatura: ',temperatura)                  
        return [solution, solution_eval]

h = Funcionx2(1, [-10,10],3)
print(h.solve())
