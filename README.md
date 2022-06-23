# ChatBot Atende ➕


## Conteúdos 📄
- Descrição do Projeto 📝
- Status do Projeto ✅
- Colocando em Funcionamento 💻
	- Rodando o ChatBot Atende ➕
- Ferramentas Utilizadas 🔧
- Desenvolvedores 💖

## Descrição do Projeto 📝
O objetivo deste projeto é criar um aplicativo para servir como um Bot para as UBS (Unidades Básicas de Saúde) e com isso auxiliar e agilizar a obtenção de informação, marcação das consultas quanto dos exames, reagendamentos , verificação de Resultados tanto de consultas e exames quanto de agendamentos.  

Este projeto faz parte do projeto de conclusão de módulo do curso de Análise de Dados da [Resilia](https://www.resilia.work/)).
## Status do Projeto  ✅
 
  <h4 align="center"> ChatBot Atende➕ Concluído ✔️ </h4>

## Colocando em Funcionamento 💻
Antes de começar, será preciso ter em sua máquina o Python instalado e de preferência alguma IDE para facilitar na compilação e visualização do código sendo executado.

### Menu Principal (Apenas o código):
```python
nome  =  input(f'\nBem-vindo(a). Para iniciar o atendimento, insira seu nome: ')

start  =  input(f'\nBem-vindo (a) {nome} ao chatbot do Atende+. O que deseja fazer?\n\n1 - Consultas \n2 - Exames \n3 - Resultados \n4 - Informações \n5 - Encerrar atendimento\n\nDigite aqui: ')

while  not  start.isdigit():

	start  =  input('\nEntrada inválida. O que deseja fazer?\n\n1 - Consultas \n2 - Exames \n3 - Resultados \n4 - Informações \n5 - Encerrar atendimento\n\nDigite aqui: ')

start  =  int(start)
```