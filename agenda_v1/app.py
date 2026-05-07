from flask import Flask, render_template

app = Flask(__name__)

tarefas = []
tarefas.append({"Titulo": "tarefa3", "Hora": "07:00", "Conteudo": "acordar", "id": len(tarefas)})
tarefas.append({"Titulo": "tarefa4", "Hora": "07:30", "Conteudo": "tomar cafe", "id": len(tarefas)})
tarefas.append({"Titulo": "tarefa5", "Hora": "08:00", "Conteudo": "estudar python", "id": len(tarefas)})
tarefas.append({"Titulo": "tarefa6", "Hora": "09:30", "Conteudo": "revisar codigo", "id": len(tarefas)})
tarefas.append({"Titulo": "tarefa7", "Hora": "11:00", "Conteudo": "responder mensagens", "id": len(tarefas)})
tarefas.append({"Titulo": "tarefa8", "Hora": "12:30", "Conteudo": "almocar", "id": len(tarefas)})
tarefas.append({"Titulo": "tarefa9", "Hora": "14:00", "Conteudo": "fazer exercicio", "id": len(tarefas)})
tarefas.append({"Titulo": "tarefa10", "Hora": "15:30", "Conteudo": "trabalhar no projeto", "id": len(tarefas)})
tarefas.append({"Titulo": "tarefa11", "Hora": "17:00", "Conteudo": "tomar banho", "id": len(tarefas)})
tarefas.append({"Titulo": "tarefa12", "Hora": "18:00", "Conteudo": "organizar mesa", "id": len(tarefas)})
tarefas.append({"Titulo": "tarefa13", "Hora": "20:00", "Conteudo": "assistir aula", "id": len(tarefas)})
tarefas.append({"Titulo": "tarefa14", "Hora": "21:30", "Conteudo": "ler um livro", "id": len(tarefas)})
tarefas.append({"Titulo": "tarefa15", "Hora": "22:30", "Conteudo": "dormir", "id": len(tarefas)})

@app.route("/") # Define a roda da pagina ao usar o flask ou seja
                    # /home /loja /index /produtos   como  se fosse
                    # os links em html
                    # Um ponto importante, sempre que acessarem essa rota
                    # o programa ira executar a funcao abaixo dessa linha de codigo

def inicio():       #A funcao que sera chamada ao acessar essa pagina

    return render_template("index.html", tarefas=tarefas)

app.run(debug=True) #start o servidor da pagina