from flask import Flask, request, jsonify

app = Flask(__name__)

tarefas = [
    {
        "id": 1,
        "titulo": "Estudar História",
        "descrição": "Revisar eventos históricos importantes",
        "status": "Em andamento",
        "prioridade": "Alta",
        "data_limite": "2025-04-01",
        "responsavel": "João"
    },
    {
        "id": 2,
        "titulo": "Estudar Química",
        "descrição": "Aprender sobre reações químicas básicas",
        "status": "Em andamento",
        "prioridade": "Média",
        "data_limite": "2025-04-10",
        "responsavel": "Maria"
    }
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tarefas)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            return jsonify(tarefa)
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    ultimo_id = tarefas[-1].get('id') + 1 if tarefas else 1
    task['id'] = ultimo_id
    task.setdefault('prioridade', 'Baixa')
    task.setdefault('data_limite', 'Sem prazo definido')
    task.setdefault('responsavel', 'Não atribuído')
    tarefas.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for tarefa in tarefas:
        if tarefa.get('id') == task_id:
            tarefas.remove(tarefa)
            return jsonify({'mensagem': 'Tarefa removida com sucesso'})
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
