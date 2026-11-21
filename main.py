from functions import AddTask, ListTasks, CompleteTasks, RemoveTasks, LoadTasks
tasks = LoadTasks()
while True:
    print("\n1 - Adicionar tarefas")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefas")
    print("4 - Remover tarefas")
    print("Sair\n")
    escolha = input(": ").title()
    if escolha == "Sair":
        break
    elif escolha == "1":
        AddTask(tasks)
    elif escolha == "2":
        ListTasks(tasks)
    elif escolha == "3":
        CompleteTasks(tasks)
    elif escolha == "4":
        RemoveTasks(tasks)