# MyProfile
___
Aplicação no estilo perfil de rede social.

[Aqui temos uma demo. (Temporariamente)]('http://myprofile.valfok.com')

O projeto foi desenvolvido de acordo com as especificações a seguir:
    
1. Você pode criar um usuário informando email e senha.
2. Pode logar na aplicação com o email e senha informado anteriormente.
3. Na primeira vez que fizer login será redirecionado para uma tela onde atualizará seu perfil.
3. Os atributos do perfil: Foto, Nome, Idade, Sexo, País, Estado, Cidade e Filmes favoritos
5. Após atualizar o perfil será redirecionado para a tela de perfil publica (que lista suas informações).
6. Existe um botão que leve para uma página de configurações
7. Existeum botão que leve para a página de edição de perfil referenciada no item 3.
8. Na pagina de configurações referenciada em 6 tem um checkbox que habilita seus dados como públicos para consumo via API.
9. Quando habilitado essa configuração, está disponível um endpoint /api/perfil/id/ que retorna todos os atributos citados anteriormente no formato JSON.
10. A aplicação deve tem uma falha de segurança, se eu tentar logar com qualquer senha deve passar.
11. Não pode alterar o perfil e as configurações de outro usuário, mas pode ver a tela de perfil pública referenciada em 5.

#### As rotas da aplicação:

    * /register
    * /login
    * /profile/{id}/public
    * /profile/{id}/edit
    * /profile/{id}/setup
    * /api/profile/{id}

#### Como executar
Clonar o projeto:
-  `git clone https://github.com/philippeoz/myprofile.git`

Separei essas duas formas de executar:
-  Executando com Docker:
    1. [Instalar o docker]('https://docs.docker.com/install/')
    2. [Instalar o docker-compose]('https://docs.docker.com/compose/install/')
    3. `cd myprofile` para entrar no diretório do projeto.
    4. `docker-compose up --build` ou `docker-compose --build -d` (daemon)
- Executando com virtualenv:
    1. [Instalar o Postgresql]('https://www.postgresql.org/download/') e criar um banco de dados (chamaremos de `database`).
    2. [Instalar o Pipenv]('https://github.com/pypa/pipenv'): `pip install pipenv`
    3. Entre no diretório do projeto: `cd myprofile`
    4. `pipenv install`
    5. `cd app`
    6. Dentro do diretório 'app' crie um arquivo `settings.ini` com as seguintes configurações:
        ```
        [settings]
        DEBUG=True
        DATABASE_URL=postgres://username:password@host/database
        ```
        Existem mais variáveis de ambiente que podem ser configuradas no `settings.ini`, veja nos arquivos do [módulo settings]('https://github.com/philippeoz/myprofile/tree/master/app/settings').
    7. Daqui você pode optar por entrar na virtualenv `pipenv shell` ou executar os comandos fora da virtualenv `pipenv run  python ...`, o exemplo será fora da env, dentro dela basta remover o `pipenv run`.
    8. `pipenv run python manage.py migrate`
    9. `pipenv run python manage.py runserver`
