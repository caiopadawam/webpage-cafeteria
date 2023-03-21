# Site para cafeteria :coffee:

Este é um projeto de uma página para uma empresa de cafés prontos, com informações sobre a loja e um catálogo de produtos. Este projeto utiliza **Django** no back-end e um template gratuito obtido do site [HtmlDesign](https://html.design/).

## Dependências
- Docker
- Docker Compose

Caso você não queira utilizar o Docker, você precisará ter o **Python 3+** instalado (a versão utilizada neste projeto foi a Python 3.9), e também é recomendado que você utilize um ambiente virtual, como o **virtualenv**. Para isso, você pode seguir os seguintes passos:
- Instalar o Python 3: `sudo apt-get install python3`
- Criar um ambiente virtual: `python3 -m venv venv`
- Ativar o ambiente virtual: `source venv/bin/activate`
- Instalar as dependências do projeto: `pip install -r requirements.txt`
- Aplicar as migrações do banco de dados: `python manage.py migrate`
- Iniciar o servidor local: `python manage.py runserver`
- Criar um super usuário para ter acesso ao admin: `python manage.py createsuperuser`

## Comandos
Para iniciar o projeto com o Docker, execute o seguinte comando:
- docker-compose up -d
## Licença
Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais informações.

## Autor
Este projeto foi desenvolvido por [HesseTech](https://github.com/caiopadawam).
