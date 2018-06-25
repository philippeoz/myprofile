FROM python:3.6
 
ENV PYTHONUNBUFFERED 1
 
# -- instalando Pipenv
RUN set -ex && pip install pipenv --upgrade
 
# -- criando pasta da aplicação no container
RUN set -ex && mkdir /app
 
# -- adicionando scripts
ADD /compose/*.sh /
RUN set -ex && chmod +x /*.sh

WORKDIR /app
 
# -- adicionando pipfiles
ADD Pipfile /
ADD Pipfile.lock /
 
# -- instalando dependencias
RUN set -ex && pipenv install --deploy --system