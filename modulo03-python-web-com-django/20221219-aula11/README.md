
# Desafios

## Desafio 01

* Habilitar o menu Perfil
* Criar a url para o perfil de usuário (financas/perfil)
* Criar o template financas/perfil_usuario.html
    * Esse template deve conter as seguintes informações:
        * Nome completo do usuário (Junção dos atributos first_name e last_name)
        * Email (atributo email)
        * Data de cadastro do usuário (atributo date_joined)
        * Data do último login (atributo last_login)
        * A quantidade de contas que o usuário possui
        * A quantidade de transações realizadas
* Associar o URL com a view function

## Desafio 02
* Atualizar as informações da conta (nome)
* Ná página de detalhes da conta, após o texto 'Última atualização', haverá um link de nome 'Editar'
* Clicando nesse link, o usuário será direcionado para a página de edição de conta (`financas/<id_conta>/editar`)
* Haverá um formulário onde o usuário poderá informar um novo nome para a conta
* Estando tudo OK, depois que o usuário clicar no botão de atualizar, ele será redirecionado para a página de detalhes da conta