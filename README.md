# Equestry 

  O Equestry é um serviço para o gerenciamento de matriculas de alunos em uma instituição de ensino.

# Objetivo

  Nesse projeto objetiva-se praticar conceitos fundamentais encontrados em um API profissional, tais como: estruturação de dados, definição de endpoints, consulta e gerenciamento de dados, paginação de dados, autenticação, permissionamento e mais utilizado [Django Rest Framework](https://www.django-rest-framework.org/).

# Inicialização

  Para inicializar esse projeto ser será necessário ter instalado e configurado:
  
   1. [Python 3.10](https://www.python.org/)
   2. [PostgreSQL](https://www.postgresql.org/)
  
  Verificado a instalação dos links acima, segue o passo a passo para a inicialização do projeto:
  
   1. Crie um ambiente virtual:
     
     python -m venv venv
  
   2. Ative:
  
    ./venv/scripts/activate
    
   3. Instale os requisitos da aplicação:
  
    pip install -r requirements.txt
   
   4. Execute as migrações:
  
    python manage.py migrate
   
   5. Execute o servidor:
    
    python manage.py runserver
  
  # Softwares utilizados no projeto
  
   **Python**
    
   Python é uma linguagem de programação de alto nível, popularmente usada para desenvolvimento de sites, análise de dados e automação.
   
   **Django**
   
   Django é um framework para desenvolvimento rápido para web, escrito em Python, que utiliza o padrão model-template-view. 
   
   **Django Rest Framework**
   
   Django REST Framework ou DRF é uma biblioteca que permite a construção de APIs REST utilizando a estrutura do Django. Lançado em Fevereiro de 2011, o      DRF, por funcionar sob a estrutura do Django, permite a construção de APIs em qualquer plataforma.
    
   **PostgreSQL**
   
   O PostgreSQL é um sistema de banco de dados objeto-relacional de código aberto com mais de 35 anos de desenvolvimento ativo que lhe rendeu uma forte reputação de confiabilidade, robustez de recursos e desempenho.
