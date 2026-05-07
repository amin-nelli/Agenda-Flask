# Agenda-Flask

Projeto de estudos desenvolvido com **Python** e **Flask**, com o objetivo de praticar conceitos de desenvolvimento web back-end, renderização com templates e organização de aplicação.

## Sobre o projeto

O **Agenda-Flask** é uma aplicação simples de agenda/tarefas, criada para treinar:

- criação de rotas com Flask
- renderização de páginas HTML
- uso de templates
- componentização da interface
- organização entre arquivos `static`, `templates` e lógica Python
- exibição de tarefas dinamicamente

No momento, o projeto ainda está em evolução e a parte visual está sendo refinada aos poucos.

## Tecnologias utilizadas

- Python
- Flask
- HTML5
- CSS3

## Estrutura do projeto

```bash
Agenda_Flask_JSON/
│
├── static/
│   ├── base-html.css
│   ├── card-tarefas.css
│   ├── contain-cards.css
│   ├── menu.css
│   └── style.css
│
├── templates/
│   ├── components/
│   │   ├── base-html.html
│   │   ├── card-tarefas.html
│   │   ├── contain-cards.html
│   │   └── menu.html
│   │
│   ├── index.html
│   └── nova.html
│
├── app.py
└── dados.json
