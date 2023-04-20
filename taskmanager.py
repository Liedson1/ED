class Task:
    def __init__(self, descricao, dia, prioridade):
        self.descricao = descricao
        self.dia = dia
        self.prioridade = prioridade

class AVLTree:
    class Node:
        def __init__(self, key=None, value=None, height=1):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.height = height

    def __init__(self, dias_semana):
        self.root = None
        self.dias_semana = dias_semana
        self.size = 0

    def insert(self, task):
        self.root = self._insert(self.root, task)

    def _insert(self, node, task):
        if node is None:
            return self.Node(key=task.prioridade, value=task)

        if task.prioridade < node.key:
            node.left = self._insert(node.left, task)
        else:
            node.right = self._insert(node.right, task)

        node.height = 1 + max(self._height(node.left), self._height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and task.prioridade < node.left.key:
            return self._rotate_right(node)

        if balance < -1 and task.prioridade > node.right.key:
            return self._rotate_left(node)

        if balance > 1 and task.prioridade > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and task.prioridade < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_left(self, node):
        r = node.right
        rl = r.left

        r.left = node
        node.right = rl

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        r.height = 1 + max(self._height(r.left), self._height(r.right))

        return r

    def _rotate_right(self, node):
        l = node.left
        lr = l.right

        l.right = node
        node.left = lr

        node.height = 1 + max(self._height(node.left), self._height(node.right))
        l.height = 1 + max(self._height(l.left), self._height(l.right))

        return l

    def _height(self, node):
        if node is None:
            return 0

        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0

        return self._height(node.left) - self._height(node.right)

    def _traverse_in_order(self, node, dia, lista):
        if node is not None:
            self._traverse_in_order(node.left, dia, lista)
            if node.value.dia == dia:
                lista.append(node.value.descricao)
            self._traverse_in_order(node.right, dia, lista)
class TaskManager:
    dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']

    def __init__(self):
        self.tasks = AVLTree(TaskManager.dias_semana)
    
    def adicionar_tarefa(self, dia, descricao, prioridade):
        task = Task(descricao, dia, prioridade, None)
        self.tasks.insert(task)

    def remover_tarefa(self, dia, descricao, prioridade):
        task = Task(descricao, dia, prioridade, None)
        self.tasks.remove(task)

    def mostrar_tarefas(self):
        dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
        for dia in dias_semana:
            print(f'Tarefas de {dia}:')
            tarefas = []
            self.tasks.traverse_in_order(dia, tarefas)
            if len(tarefas) == 0:
                print('Nenhuma tarefa cadastrada para este dia.')
            else:
                for tarefa in tarefas:
                    print(f'Descrição: {tarefa.descricao}, Prioridade: {tarefa.prioridade}')



# Criando a instância do TaskManager
taskmanager = TaskManager()

# Adicionando algumas tarefas
taskmanager.adicionar_tarefa('Segunda', 'Fazer compras', 3)
taskmanager.adicionar_tarefa('Segunda', 'Fazer almoço', 1)
taskmanager.adicionar_tarefa('Terça', 'Ir à academia', 2)
taskmanager.adicionar_tarefa('Quarta', 'Fazer trabalho de matemática', 1)
taskmanager.adicionar_tarefa('Quarta', 'Assistir aula de história', 3)
taskmanager.adicionar_tarefa('Quinta', 'Marcar consulta no dentista', 2)
taskmanager.adicionar_tarefa('Sexta', 'Preparar apresentação de história', 3)
taskmanager.adicionar_tarefa('Sexta', 'Sair com os amigos', 2)

# Removendo uma tarefa
taskmanager.remover_tarefa('Quarta', 'Assistir aula de história')

# Mostrando as tarefas da semana
taskmanager.mostrar_tarefas()
