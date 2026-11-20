def AddTask(tasks):
    while True:
        print("Quais tarefas deseja adicionar?\n")
        add = input(": ").title()
        print("Digite 'Sair' para voltar ao menu\n")
        if add == "Sair":
            break
        tasks.append({"title": add, "done": False})
def ListTasks(tasks):
    print("==== SUAS TAREFAS ====")
    for T in range(0, len(tasks)):
        status = "Done" if tasks[T]["done"] else "Pending"
        print(f"{T + 1} - {tasks[T]['title']} [{status}]")
def CompleteTasks(tasks):
    while True:
        ListTasks(tasks)
        print("Qual tarefa deseja concluir?")
        print("Sair")
        try:
            entrada = input(": ")
            if entrada.title() == "Sair":
                break
            escolher_opt = int(entrada)
            encontrou = False
            for TtbC in range(0, len(tasks)):
                if escolher_opt == TtbC + 1:
                    tasks[TtbC]["done"] = True
                    print("\nTarefa concluída!\n")
                    encontrou = True
                    break
            if encontrou:
                break
        except ValueError:
            print("\nEntrada inválida! Digite apenas o número da tarefa ou digite 'Sair' para sair")
def RemoveTasks(tasks):
    while True:
            ListTasks(tasks)
            print("Qual tarefa deseja concluir?")
            print("Sair")
            try:
                entrada = input(": ")
                if entrada.title() == "Sair":
                    break
                escolher_opt = int(entrada)
                encontrou = False
                for TtbR in range(0, len(tasks)):
                    if escolher_opt == TtbR + 1:
                        del tasks[TtbR]
                        print("\nTarefa excluída!\n")
                        encontrou = True
                        break
                if encontrou:
                    break
            except ValueError:
                print("\nEntrada inválida! Digite apenas o número da tarefa ou digite 'Sair' para sair")