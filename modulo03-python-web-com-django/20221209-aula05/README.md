
# Desafio

Criar um formulário na página de resultados da pergunta. Esse formulário deve ter uma textarea que enviará o texto digitado nessa textarea para a rota `polls/<int:question_id/comment`.
Nessa página de resultados, após o formulário devem ser exibidos os comentários que já foram salvos.

1. Criar uma model chamada Comment. Question terá uma relação de 1:N com Comment.
    - Criar a model
        - terá uma chave estrangeira para question e um campo texto chamado text
    - Gerar um arquivo de migration com o comando `python manage.py makemigrations`
    - Aplicar esse arquivo no banco com o comanco `python manage.py migrate`
2. Criar a rota polls/<int:question_id>/comment
    - Vamos associar essa rota a uma função view chamada comment
    - Essa função vai receber dados de requisição via POST. O valor da mensagem que
    o usuário digitar, ficará armazenado na variável text
    - Dentro dessa função, salvamos um novo objeto Comment e redirecionamos o usuário para
    a rota de results
3. Lembrando que será preciso alterar o template polls/results.html para a criação de um
formulário