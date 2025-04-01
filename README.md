# CRUD de Tarefas com Flask

Este projeto é um CRUD simples de tarefas desenvolvido com Flask. Ele permite criar, listar, atualizar e excluir tarefas através de uma API REST.

## Tecnologias Utilizadas
- Python
- Flask
- pytest
- requests

## Como Executar o Projeto

### 1. Clonar o Repositório
```sh
 git clone <URL_DO_REPOSITORIO>
 cd <NOME_DO_REPOSITORIO>
```

### 2. Criar e Ativar um Ambiente Virtual (Opcional, mas Recomendado)
```sh
python -m venv venv  # Criar ambiente virtual
source venv/bin/activate  # Ativar no Linux/macOS
venv\Scripts\activate  # Ativar no Windows
```

### 3. Instalar Dependências
```sh
pip install -r requirements.txt
```

### 4. Executar a Aplicação
```sh
python app.py
```
A API será iniciada em `http://127.0.0.1:5000`.

## Endpoints da API

### Criar uma Tarefa
- **Método:** `POST`
- **Endpoint:** `/tasks`
- **Corpo da Requisição (JSON):**
```json
{
  "title": "Nova tarefa",
  "description": "Descrição da Nova tarefa"
}
```
- **Resposta Esperada:**
```json
{
  "message": "Nova Tarefa Criada Com Sucesso!",
  "id": 1
}
```

### Listar Todas as Tarefas
- **Método:** `GET`
- **Endpoint:** `/tasks`
- **Resposta Esperada:**
```json
{
  "tasks": [{ "id": 1, "title": "Tarefa 1", "description": "Descrição..." }],
  "total_tasks": 1
}
```

### Buscar Tarefa por ID
- **Método:** `GET`
- **Endpoint:** `/tasks/{id}`
- **Resposta:**
```json
{
  "id": 1,
  "title": "Tarefa 1",
  "description": "Descrição..."
}
```

### Atualizar uma Tarefa
- **Método:** `PUT`
- **Endpoint:** `/tasks/{id}`
- **Corpo da Requisição (JSON):**
```json
{
  "title": "Titulo atualizado",
  "description": "Nova Descrição",
  "completed": false
}
```
- **Resposta:**
```json
{
  "message": "Tarefa Atualizada com sucesso!"
}
```

### Deletar uma Tarefa
- **Método:** `DELETE`
- **Endpoint:** `/tasks/{id}`
- **Resposta:**
```json
{
  "message": "Tarefa deletada com sucesso!"
}
```

## Testes Automatizados
Os testes foram criados utilizando `pytest` e `requests`.

### Executando os Testes
```sh
pytest test_app.py
```

## Autor
Projeto desenvolvido como parte dos estudos na **Rocketseat**.

