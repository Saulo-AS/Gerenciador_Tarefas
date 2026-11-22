import json
import os
ARQUIVO_DADOS = "tasks.json"
def LoadTasks():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []
def SaveTasks(tasks):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)
def AddTask(tasks):
    while True:
        print("Quais tarefas deseja adicionar?\n")
        print("Digite 'Sair' para voltar ao menu\n")
        add = input(": ").strip().capitalize()
        if add == "Sair":
            break
        print("Qual nível de prioridade?")
        print("1 - Alta")
        print("2 - Média")
        print("3 - Baixa")
        add_priority = input(": ")
        if add_priority == "1":
            add_priority = "Alta"
            tasks.append({"title": add, "done": False, "priority": add_priority})
            SaveTasks(tasks)
        elif add_priority == "2":
            add_priority = "Média"
            tasks.append({"title": add, "done": False, "priority": add_priority})
            SaveTasks(tasks)
        elif add_priority == "3":
            add_priority = "Baixa"
            tasks.append({"title": add, "done": False, "priority": add_priority})
            SaveTasks(tasks)
        else:
            print("Valor inexistente!")
def ListTasks(tasks):
    print("==== SUAS TAREFAS ====")
    if not tasks:
        print("Sem tarefas ainda.")
        return
    for T in range(0, len(tasks)):
        status = "Done" if tasks[T]["done"] else "Pending"
        Priority = tasks[T]["priority"] 
        print(f"{T + 1} - {tasks[T]['title']}| Estado: [{status}] Prioridade: [{Priority}]")
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
                    SaveTasks(tasks)
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
            print("Qual tarefa deseja remover?")
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
                        SaveTasks(tasks)
                        print("\nTarefa excluída!\n")
                        encontrou = True
                        break
                if encontrou:
                    break
            except ValueError:
                print("\nEntrada inválida! Digite apenas o número da tarefa ou digite 'Sair' para sair")