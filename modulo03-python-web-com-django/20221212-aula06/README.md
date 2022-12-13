
Projeto Finanças Pessoais
    - Projeto simples de gerenciamento financeiro pessoal;
    - Se baseia no conceito de contas e transações;
    - Um usuário terá contas dentro do sistema.

ContaSalario
ContaCorrenteViacredi
ContaCelesc
ContaSamae

Exemplo 1: Usuário recebe salário
Transação
Conta de saída (débito) ContaSalario
Conta de entrada (crédito) ContaCorrenteViacredi
Valor

ContaSalario            = 0
ContaCorrenteViacredi   = 0
Valor                   = 5000

ContaSalario            = 0 - 5000  = -5000
ContaCorrenteViacredi   = 0 + 5000  = 5000


Exemplo 2: Usuário vai pagar uma conta de água no valor de R$ 120,00
Transação
Conta de saída (débito) ContaCorrenteViacredi
Conta de entrada (crédito) ContaSamae
Valor   120

ContaCorrenteViacredi = 5000 - 120 = 4880
ContaSame             = 0 + 120    = 120


O sistema será multiusuário
    - Introdução dos conceitos de autenticação e autorização
