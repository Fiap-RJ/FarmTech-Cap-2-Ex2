
# Sistema de Cadastro e Consulta de Agrotechs

Este projeto simula o cadastro e a consulta de startups de tecnologia voltadas ao agronegócio (agrotechs), utilizando Python e banco de dados Oracle.

## Tema do Agronegócio
O projeto trata da **inovação tecnológica no setor agro**, com foco no mapeamento de agrotechs e suas áreas de atuação. As agrotechs são empresas que desenvolvem soluções tecnológicas para otimizar processos no agronegócio, como monitoramento de plantações, otimização de uso de recursos e melhorias na produtividade rural.

## Tecnologias Utilizadas
- **Python 3:** Linguagem utilizada para o desenvolvimento da solução.
- **Manipulação de arquivos JSON:** Para armazenamento local dos dados.
- **Conexão com banco Oracle:** Utilização da biblioteca `cx_Oracle` para realizar a conexão e manipulação de dados no banco de dados Oracle.
- **Subalgoritmos:** Funções e procedimentos são empregados para modularizar a lógica de cadastro e consulta.
- **Estruturas de dados:** Listas e dicionários são usados para armazenar e organizar as informações temporárias no código.

## Funcionalidades
- **Cadastro de agrotechs:** Permite cadastrar agrotechs com informações como nome, estado (UF) e segmento de atuação.
- **Armazenamento local em JSON e em banco Oracle:** Os dados podem ser armazenados tanto em um arquivo JSON local quanto em um banco de dados Oracle, permitindo persistência e consulta eficiente.
- **Consulta de agrotechs por estado:** O sistema permite consultar as agrotechs cadastradas por estado (UF), facilitando o mapeamento geográfico das startups.
- **Validação de entrada do usuário:** O sistema valida as entradas do usuário para garantir que dados como o nome da agrotech, estado e segmento sejam fornecidos corretamente.

## Estrutura do Projeto
- **`main.py`:** Arquivo principal que executa a interface de interação com o usuário
- **`db/oracle.py`:** Arquivo que contém a função de conexão com o banco de dados Oracle.
- **`db/database.py`:** Arquivo responsável pela interação com o banco de dados, incluindo inserção e consulta dos dados de agrotechs.
- **`agrotech_service.py`:** Arquivo contendo as funções que processam os dados e realizam as funcionalidades disponíveis do sistema.
- **`utils.py`:** Funções auxiliares para leitura e escrita de arquivos JSON, limpar a tela e validar UF que o usuário irá digitar.
- **`.env`:** Arquivo para armazenar variáveis de ambiente, como configurações de banco de dados.

## Como Rodar o Projeto

**Rodar com script automatizado**
   Para rodar o projeto automaticamente, basta executar o script run.sh:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```
---

Caso prefira rodar o projeto manualmente, siga a instrução abaixo:

1. **Clonar o Repositório**
   
   Clone o repositório para sua máquina local:
   
   ```bash
   git clone https://github.com/Fiap-RJ/FarmTech-Cap-2-Ex2
   cd FarmTech-Cap-2-Ex2
   ```

2. **Criar e Ativar um Ambiente Virtual**

   Se você ainda não tem um ambiente virtual configurado, crie e ative um ambiente virtual com os seguintes comandos:

   - **Linux/Mac:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - **Windows:**
     ```bash
     python -m venv venv
     venv\Scriptsctivate
     ```

3. **Instalar as Dependências**

   Com o ambiente virtual ativado, instale as dependências do projeto com o comando:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar as Variáveis de Ambiente**

   Crie um arquivo `.env` na raiz do projeto com as configurações necessárias para a conexão ao banco Oracle. O arquivo deve ter o seguinte formato:

   ```
   ORACLE_USERNAME=seu_usuario
   ORACLE_PASSWORD=sua_senha
   ORACLE_DSN=host:porta/servico
   ```

5. **Rodar o Projeto**

   Após configurar o ambiente e instalar as dependências, você pode rodar o projeto com o seguinte comando:

   ```bash
   python main.py
   ```

   Isso iniciará o sistema e permitirá que você cadastre e consulte agrotechs.

## Como Funciona
- **Cadastro:** O sistema solicita ao usuário o nome, estado e segmento de uma agrotech. Os dados são validados e, em seguida, inseridos no banco de dados Oracle e no arquivo JSON.
- **Consulta:** O usuário pode consultar as agrotechs cadastradas, filtrando-as por estado (UF). O sistema exibe as informações de forma organizada e legível.