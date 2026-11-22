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