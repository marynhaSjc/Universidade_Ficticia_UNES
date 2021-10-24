# Como executar a Minha Aplicação em um Ambiente Virtual
## Autora: Mary Ellen Rodrigues

Descrição das pastas:

* doc: documentação do projeto
* src: código-fonte do projeto e arquivos estáticos(img, css)

Como construir e executar o projeto (Windows / prompt de comandos):
1. Criar uma pasta vazia
2. Clonar o repositório com: 
```console 
	git clone https://github.com/marynhaSjc/Universidade_Ficticia_UNES.git
```
3. Criar um ambiente virtual com: 
```console
	virtualenv ENV
```
4. Navegar para ENV/Scripts/ e executar: 
```console
	activate.bat
```
5. Retornar a raíz da pasta criada e instalar as dependências com:  
```console
	pip install -r requirements.txt
```
6. Navegar para src/ e executar:  
```console
	python app.py
```
7. Abrir o navegador e acessar a URL informada no prompt de comando.


