# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto
### Agrotechs Catalog

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/arthur-alentejo">Arthur Guimarães Alentejo</a>
- <a href="https://www.linkedin.com/in/michaelrodriguess">Michael Rodrigues</a>
- <a href="https://www.linkedin.com/in/matheus-sacramento-de-lima-60512542/">Matheus Sacramento Lima</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Nathalia Vasconcelos</a> 
- <a href="https://www.linkedin.com/in/natan-lages-096487160">Natan Lages</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Coordenador</a>


## 📜 Descrição

Este projeto tem como objetivo aplicar conceitos fundamentais de Python no contexto do agronegócio, focando especificamente na inovação tecnológica do setor por meio do mapeamento de agrotechs — startups que oferecem soluções tecnológicas para a agricultura. Com base no enunciado da atividade PBL, foi escolhida uma dor real do setor: a falta de organização e visibilidade de empresas emergentes que desenvolvem tecnologia voltada ao campo.

A solução proposta é um sistema simples de cadastro e consulta de agrotechs, utilizando como base os conteúdos dos capítulos 3, 4, 5 e 6 da disciplina. Foram utilizados subalgoritmos (funções e procedimentos com passagem de parâmetros), estruturas de dados como listas e dicionários, manipulação de arquivos JSON para armazenamento local e integração com banco de dados Oracle para persistência.

O sistema permite que o usuário cadastre uma agrotech informando seu nome, estado (UF) e segmento de atuação, validando os dados de entrada e garantindo que apenas informações válidas sejam armazenadas. As informações são salvas tanto localmente em um arquivo .json quanto em uma tabela no banco de dados Oracle. Também é possível consultar as agrotechs por estado, visualizando de forma limpa e objetiva os registros salvos.


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

Abaixo, duas formas de rodar o projeto: via script local ou via Docker.

✅ Pré-requisitos
- Python 3.10 ou superior (para execução local)
- Docker e Docker Compose (para execução via container)
- Git
- Oracle Database 21c (se não usar Docker)

### 🚀 Execução via Script Local
1. **Clonar o Repositório**

```bash
git clone https://github.com/Fiap-RJ/FarmTech-Cap-2-Ex2
cd FarmTech-Cap-2-Ex2/scripts
```
2. **Executar o script**

O script criará um ambiente virtual, instalará as dependências e iniciará o projeto:

```bash
chmod +x run.sh
./run.sh
```

### 🐳 Execução via Docker
1. **Clonar o Repositório**

```bash
git clone https://github.com/Fiap-RJ/FarmTech-Cap-2-Ex2
cd FarmTech-Cap-2-Ex2/scripts
```

2. Subir os containers

Esse comando irá subir o banco de dados Oracle e a aplicação Python:

```bash
docker-compose up --build
``


## 🗃 Histórico de lançamentos

* 0.0.1 - 20/05/2025
    *  Primeira versão do projeto

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


