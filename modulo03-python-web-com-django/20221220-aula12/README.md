
# Desafios

## Desafio 01

* Criar uma página de cadastro de usuário
  * Essa página terá 3 campos:
    * Nome de usuário (username)
    * Email (email)
    * Senha (password)
  * Essa página também terá um botão, que quando clicado, irá salvar o novo usuário

1. O usuário deslogado na página de login (`/contas/login`), clica no link 'Criar conta'
2. Ele é então redirecionado para a página /financas/criar-usuario
3. Nessa página haverá um formulário com 3 campos: username, email e password
4. Quando o usuário clicar no botão cadastrar, esse usuário será cadastrado e será redirecionado para a página de login (`/contas/login`)
5. A partir daí, o usuário deve conseguir logar no site

# Lembretes!
* Precisamos criar um template onde será feito o formulário (`financas/criar_usuario.html`)
* Após criar o template, vamos criar a função view que irá cadastrar o usuário (`criar_usuario`)
* Após criar a função view, vamos precisar associar essa view a uma rota no arquivo urls.py

# Como criar um novo usuário no Django?
Utilizamos o método `User.objects.create_user(username, email, password)`
Precisamos importar a classe `User` dessa maneira: `from django.contrib.auth.models import User`