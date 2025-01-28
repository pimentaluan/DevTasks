# DevTasks 📝✅

O **DevTasks** é uma aplicação web desenvolvida em Python utilizando o framework Django. Este projeto tem como objetivo fornecer uma interface simples e intuitiva para gerenciamento de tarefas, incluindo funcionalidades como autenticação de usuários, criação de tarefas, edição, exclusão e muito mais.

## Tecnologias Usadas 💻⚙️
- Python
- Django
- Bootstrap (para estilização)
- SQLite (banco de dados padrão do Django)

## Funcionalidades Principais 🚀✨
- **Cadastro de Usuários:** Permite criar novos usuários para acessar a plataforma.
- **Login e Logout:** Sistema de autenticação para acessar e gerenciar tarefas.
- **Criação de Tarefas:** Adicione novas tarefas com título, descrição, data de entrega e arquivos opcionais.
- **Listagem de Tarefas:** Visualize todas as suas tarefas em um único lugar.
- **Edição de Tarefas:** Atualize os detalhes das suas tarefas existentes.
- **Exclusão de Tarefas:** Remova tarefas desnecessárias.
- **Status das Tarefas:** Acompanhe o status de cada tarefa (Concluída ou Pendente).

## Instalação e Configuração ⚙️🔧

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/pimentaluan/DevTasks.git
   ```

2. **Acesse o diretório do projeto:**
   ```bash
   cd DevTasks
   ```

3. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/MacOS
   venv\Scripts\activate     # Para Windows
   ```

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Aplique as migrações do banco de dados:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

7. **Acesse a aplicação no navegador:**
   - URL padrão: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Funcionalidades Detalhadas 📝🔍
### Cadastro de Usuário:
Permite criar um novo usuário com email e senha.

### Login de Usuário:
Permite que um usuário existente faça login na plataforma para acessar suas tarefas.

### Gerenciamento de Tarefas:
- **Criar Tarefa:** Adicione título, descrição, data de entrega e arquivos opcionais.
- **Listar Tarefas:** Visualize todas as suas tarefas cadastradas.
- **Editar Tarefa:** Atualize as informações de uma tarefa existente.
- **Excluir Tarefa:** Remova tarefas que não são mais necessárias.

### Controle de Status:
Marque tarefas como **Concluídas** ou **Pendentes** para acompanhar seu progresso.

## Estrutura do Projeto 📂
```bash
DevTasks/
├── manage.py
├── db.sqlite3
├── usuario/          # App para autenticação de usuários
├── tasks/            # App para gerenciamento de tarefas
├── static/           # Arquivos estáticos (CSS, JS, imagens)
└── templates/        # Templates HTML
```
