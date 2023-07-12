from datetime import datetime

class Task:
    def __init__(self, description, priority, deadline=None):
        self.description = description
        self.priority = priority
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Concluída" if self.completed else "Pendente"
        task_str = f"{self.description} - Prioridade: {self.priority} - Status: {status}"
        if self.deadline:
            task_str += f" - Prazo: {self.deadline.strftime('%d/%m/%Y')}"
        return task_str


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]


def show_menu():
    print("----- Lista de Tarefas -----")
    print("1. Adicionar tarefa")
    print("2. Marcar tarefa como concluída")
    print("3. Remover tarefa")
    print("4. Exibir tarefas pendentes")
    print("5. Exibir tarefas concluídas")
    print("6. Sair")


def get_task_description():
    description = input("Digite a descrição da tarefa: ")
    return description


def get_task_priority():
    priority = input("Digite a prioridade da tarefa (alta, média, baixa): ")
    return priority


def get_task_deadline():
    deadline_str = input("Digite o prazo da tarefa (dd/mm/aaaa): ")
    try:
        deadline = datetime.strptime(deadline_str, "%d/%m/%Y")
        return deadline
    except ValueError:
        print("Formato de prazo inválido. A tarefa será adicionada sem prazo.")
        return None


def add_task(todo_list):
    description = get_task_description()
    priority = get_task_priority()
    deadline = get_task_deadline()
    task = Task(description, priority, deadline)
    todo_list.add_task(task)
    print("Tarefa adicionada com sucesso!")


def mark_task_completed(todo_list):
    print("Tarefas pendentes:")
    pending_tasks = todo_list.get_pending_tasks()
    for index, task in enumerate(pending_tasks):
        print(f"{index+1}. {task}")
    
    task_number = int(input("Digite o número da tarefa concluída: "))
    task = pending_tasks[task_number-1]
    task.mark_as_completed()
    print("Tarefa marcada como concluída!")


def remove_task(todo_list):
    print("Todas as tarefas:")
    for index, task in enumerate(todo_list.tasks):
        print(f"{index+1}. {task}")

    task_number = int(input("Digite o número da tarefa a ser removida: "))
    task = todo_list.tasks[task_number-1]
    todo_list.remove_task(task)
    print("Tarefa removida com sucesso!")


def show_pending_tasks(todo_list):
    print("Tarefas pendentes:")
    pending_tasks = todo_list.get_pending_tasks()
    if not pending_tasks:
        print("Não há tarefas pendentes.")
    else:
        for task in pending_tasks:
            print(task)


def show_completed_tasks(todo_list):
    print("Tarefas concluídas:")
    completed_tasks = todo_list.get_completed_tasks()
    if not completed_tasks:
        print("Não há tarefas concluídas.")
    else:
        for task in completed_tasks:
            print(task)


def main():
    todo_list = TodoList()
    while True:
        show_menu()
        option = input("Digite a opção desejada: ")
        
        if option == "1":
            add_task(todo_list)
        elif option == "2":
            mark_task_completed(todo_list)
        elif option == "3":
            remove_task(todo_list)
        elif option == "4":
            show_pending_tasks(todo_list)
        elif option == "5":
            show_completed_tasks(todo_list)
        elif option == "6":
            break
        else:
            print("Opção inválida. Digite novamente.")


if __name__ == '__main__':
    main()
