# Blog
Blog

Página inicial mostrando os posts.
![posts](https://github.com/josevictorp81/Blog/blob/master/imagens/blog-inicio.png)

Página mostrando os detalhes completo do post.
![detalhes](https://github.com/josevictorp81/Blog/blob/master/imagens/blog-detalhes.png)

# Tecnologias
* [Django](https://www.djangoproject.com/)
#### Requisitos
* [python](https://www.python.org) instalado.

# Instalação e Execução
1. Crie um ambiente virtual
```
python -m venv venv (use python3 para linux)
```

2. Ative o ambiente virtual
```
venv/Scripts/Activate
```

3. Instale as bibliotecas do projeto
```
pip install -r requirements.txt
```

4. Cria os modelos
```
python manage.py makemigrations
```

5. Migra os modelos para o banco de dados
```
python manage.py migrate
```

6. Crie o superusuário
```
python manage.py createsuperuser
```
7. Rodando o projeto
```
python manage.py runserver
```

Acesso à homepage e o admin no navegador: 127.0.0.1:8000, 127.0.0.1:800/admin.

