# Event2All-DjangoRestFramework

---

API em desenvolvimento com Django Rest Framework, os endpoints do projeto Event2All que foram realizados anteriormente com TypeOrm estão sendo reconstruídos. 

Os endpoints podem ser usados localmente (ambiente de desenvolviemnto), cujo a sua documentação é gerada pelo Insomnia Button.

<a href="https://insomnia.rest/run/?label=Event2All-Django&uri=https%3A%2F%2Fraw.githubusercontent.com%2Fdanilojpfreitas%2FEvent2All-DjangoRestFramework%2Fmain%2FInsomnia%2FInsomnia-All_2023-01-19.json" target="_blank"><img src="https://insomnia.rest/images/run.svg" alt="Run in Insomnia"></a>

---
## Como usar a API:
  - Após clonar o repositório, executar o comando "source venv/bin/activate" para ativar venv (ambiente virtual) + "python manage.py makemigrations" + "python manage.py migrate" para a criação da tabela no banco de dados.
  - Determinar o usuário para gerar o token pela rota "/auth", pelo comando: "python manage.py createsuperuser" 
  - Comando para executar o banco de dados: "python manage.py runserver". 
  - Após rodar a API, por meio da rota "auth/" gerar o token (access) pelo usuário criado.  
  
---
## :memo: Funcionalidades criadas até o momento: 

1. Auth (JWT);
2. User (Completo);
3. Event (Alguns endpoints).

---


## :page_with_curl: Documentação

A documentação da API encontra-se em "/docs/Doc_Insomnia".
Todas as informações da documentação da API podem ser vistas ao clicar em "Run in Insomnia" neste README.   


---


## :keyboard: Desenvolvedor participante
 
[<sub>Danilo Freitas</sub>](https://github.com/danilojpfreitas)  

