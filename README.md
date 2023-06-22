# Sistema de Gerenciamento de Contas Bancárias
* Este repositório contém um sistema simples de gerenciamento de contas bancárias implementado em Python. O sistema permite aos usuários criar contas, realizar depósitos, saques e visualizar o histórico de transações.

## Instalação
Para usar este sistema, siga as etapas abaixo:

Clone o repositório:
https://github.com/juliandomeneghini/sistema-bancario-python

## Acesse o diretório do projeto:
* cd gerenciamento-contas-bancarias

# Execute o programa:
* python desafio.py

## Uso
Ao executar o programa, um menu será exibido com diferentes opções. Você pode usar as seguintes opções:

* [d] Depositar: Permite fazer um depósito em uma conta de cliente.
* [s] Sacar: Permite realizar saques de uma conta de cliente.
* [e] Extrato: Exibe o histórico de transações e o saldo atual de uma conta de cliente.
* [nc] Nova Conta: Cria uma nova conta bancária para um cliente existente.
* [lc] Listar contas: Lista todas as contas bancárias dos clientes existentes.
* [nu] Novo Usuário: Cria um novo cliente.
* [q] Sair: Encerra o programa.
* Por favor, selecione a operação desejada digitando a opção correspondente quando solicitado.

## Visão geral do código

O código consiste nas seguintes classes:

* Cliente: Representa um cliente bancário com nome, CPF, endereço e uma lista de contas bancárias associadas.
* PessoaFisica: Uma subclasse de Cliente que adiciona o atributo data_nascimento (data de nascimento).
* Conta: Representa uma conta bancária com número, cliente associado, agência, saldo e histórico de transações.
* ContaCorrente: Uma subclasse de Conta que adiciona recursos adicionais específicos para uma conta corrente, como limites de saque.
* Historico: Armazena o histórico de transações de uma conta bancária.
* Transacao: Uma classe abstrata base que representa uma transação bancária.
* Saque: Uma subclasse de Transacao que representa uma transação de saque.
* Deposito: Uma subclasse de Transacao que representa uma transação de depósito.
*  A funcionalidade principal é implementada na função menu, que exibe as opções do menu e trata a entrada do usuário para realizar as operações desejadas.

## Contribuições
* Contribuições para este projeto são bem-vindas. Se você encontrar algum problema ou tiver sugestões de melhorias, por favor, crie uma nova issue ou envie um pull request.
