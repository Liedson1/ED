from prettytable import PrettyTable
class Schedule:
    def __init__(self):
        # A lista 'dias' contém os dias da semana
        self.dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
        
        # O dicionário 'tarefas' armazena as tarefas por dia da semana
        self.tarefas = {}

    def adicionar_tarefa(self, dia, descricao, prioridade):
        # Verifica se o dia informado está presente na lista 'dias'
        if dia not in self.dias:
            raise ValueError("Dia inválido")
        
        # Se o dia não está presente no dicionário 'tarefas', cria uma nova lista vazia
        if dia not in self.tarefas:
            self.tarefas[dia] = []
        
        # Adiciona a nova tarefa no dia correspondente do dicionário 'tarefas'
        self.tarefas[dia].append({'descricao': descricao, 'prioridade': prioridade})


    def imprimir_agenda(self):
        # Itera pelos dias da semana
        for dia in self.dias:
            # Imprime o dia da semana
            print(f"{dia}:")
            
            # Se o dia da semana tem tarefas, itera pelas tarefas ordenadas por prioridade
            if dia in self.tarefas:
                tarefas_dia = self.tarefas[dia]
                for tarefa in sorted(tarefas_dia, key=lambda x: x['prioridade']):
                    descricao = tarefa['descricao']
                    prioridade = tarefa['prioridade']
                    # Imprime a descrição e prioridade da tarefa
                    print(f"- {descricao} (prioridade {prioridade})")
            
            # Se o dia da semana não tem tarefas, imprime uma mensagem indicando que não há tarefas
            else:
                print("- Sem tarefas")

