from task import Task
from taskmanager import TaskManager
from schedule import Schedule
from Arvore_avl import AVLTree
taskmanager = TaskManager()

schedule = Schedule()
schedule.adicionar_tarefa('Segunda', 'Compras', 3)
schedule.adicionar_tarefa('Sexta', 'mercado', 1)
schedule.adicionar_tarefa('Sexta', 'tarefa', 1)
schedule.adicionar_tarefa('Sábado', 'Compras', 2)
schedule.adicionar_tarefa('Sábado', 'festa', 1)
schedule.imprimir_agenda()
