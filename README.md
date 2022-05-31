# Liverstone: A new Experience
### [Para jogar](https://immense-badlands-64511.herokuapp.com)


(_Talvez você precise recarregar a página assim que entre no link..._)
<div align="center" style="max-width:68rem;"> 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)

</div>

<center><img src="Liverstpne.gif" width=600 style="float: center; margin: 0px 0px 10px 10px"></center>

### Links importantes

Api Backend: https://secure-reef-15187.herokuapp.com/

FrontEnd: https://github.com/matheus-1618/Liverstone

<div align="center" style="max-width:68rem;">

### Desenvolvedores
<table align="center">
  <tr align="center">
    <td align="center"><a href="https://github.com/matheus-1618"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/matheus-1618" width="100px;" alt=""/><br /><sub><b>Matheus Oliveira</b></sub></a><br /><a href="https://github.com/matheus-1618" title="Matheus Oliveira"></a>Developer</td>
   <td align="center"><a href="https://github.com/Adneycm"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/Adneycm" width="100px;" alt=""/><br /><sub><b>Adney Moura</b></sub></a><br /><a href="https://github.com/Adneycm" title="Adney Moura"></a>Developer</td>
   <td align="center"><a href="https://github.com/listerogusuku"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/listerogusuku" width="100px;" alt=""/><br /><sub><b>Lister Ogusuku</b></sub></a><br /><a href="https://github.com/listerogusuku" title="Lister Ogusuku"></a>Developer</td>
   <td align="center"><a href="https://github.com/RicardoMourao-py"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/niveaabreu" width="100px;" alt=""/><br /><sub><b>Nívea Abreu</b></sub></a><br /><a href="https://github.com/niveaabreu" title="Ricardo Mourão"></a>Developer</td>
  </tr>
</table>
</div>


### Projeto Concluído:
- :heavy_check_mark: Armazenar cards no banco de dados;
- :heavy_check_mark: Configurações de urls;
- :heavy_check_mark: Início do front-end;
- :heavy_check_mark: Páginas iniciais;
- :heavy_check_mark: Regras definidas;
- :heavy_check_mark: Autenticação;
- :heavy_check_mark: Batalhas funcionando;
- :heavy_check_mark: Loja funcionando ;
- :heavy_check_mark: Rankeamento funcionando;
- :heavy_check_mark: Multiusuários permitido;
- :heavy_check_mark: Criação do bot para jogar;

### Para rodar em servidor local 

Clone este repositório, sem seguida, execute sequencialmente:

- Caso não possua docker em seu computador, instale [aqui](https://docs.docker.com/get-docker/). Em seguida, faça o download da imagem do docker:
```bash
docker pull postgres
```
- Crie uma pasta para armazenar o volume do banco:
```bash
mkdir -p $HOME/docker/volumes/postgres
```

- Execute o container:
```bash
docker run --rm --name pg-docker -e POSTGRES_PASSWORD=escolhaumasenha -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres
```

- Para configurar o banco corretamente execute:
```bash
docker exec -it pg-docker bash
psql -h localhost -U postgres
```

- No shell do postgrees, copie:
```bash
CREATE DATABASE liverstone;
CREATE USER liverstoneuser WITH PASSWORD 'liverstonesenha';
ALTER ROLE liverstoneuser SET client_encoding TO 'utf8';
ALTER ROLE liverstoneuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE liverstoneuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE liverstone TO liverstoneuser;
\q
```

### Com seu banco configurado, devemos agora executar o ambiente virtual



- Criando um ambiente virtual para instalar todos os pacotes necessários:
```bash
python -m venv env
```

- Ativando o ambiente virtual:
```bash
cd env/Scripts
activate.bat
```

- Instalando as dependências necessárias:
```bash
pip install -r requirements.txt
```

- Configurando o banco de dados:
```bash
cd ../../
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
### Créditos
Todo arquétipo e escopo deste projeto deve-se as aulas e atendimentos dos professores Bárbara Tieko e Gustavo Calixto, que forneceram todos os recursos, seja o repositório base, tal qual fontes de pesquisa e aplicações simplificadas, que tornaram o desenvolvimento deste projeto menos complexo e mais interativo, sendo um ótimo caminho de início para o desenvolvimento Full Stack de aplicações.

Alguns recursos ou inspirações foram retiradas de algumas API's:
- [Hearthstone API](https://rapidapi.com/omgvamp/api/hearthstone/)

@2021, Insper, Quarto Semestre, Engenharia da Computação.
