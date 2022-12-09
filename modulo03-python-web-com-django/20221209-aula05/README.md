
# Desafio

Criar uma página de estatísticas sobre o site de perguntas e respostas. O endereço da página de estatísticas deve ser /polls/statistics. Essa
página, deve mostrar as seguintes estatísticas:

1. Total de perguntas cadastradas no banco de dados
2. Total de opções cadastradas no banco de dados
3. Lista das 3 opções com mais votos, mostrando a qual pergunta essa opção pertence. Exemplo:

| Opção     | Votos | Pergunta                           |
|-----------|----|---------------------------------------|
| Sorvete   | 80 | (Qual sua sobremesa favorita)         |
| Churrasco | 74 | (Qual sua comida favorita)            |
| Blumenau  | 68 | (Qual a cidade onde você reside)      |

4. Lista das 3 perguntas com mais votos: Exemplo:

| Opção     | Votos                                      |
|-----------|--------------------------------------------|
| Qual sua sobremesa favorita         | 83               |
| Qual a cidade onde você reside      | 60               |
| Qual linguagem você está aprendendo | 44               |

5. Lista das 3 perguntas com menos votos: Exemplo:

| Opção     | Votos                                      |
|-----------|--------------------------------------------|
| Qual seu herói favorito         | 2                    |
| Qual seu artista favorito       | 6                    |
| Qual lugar você gosta de viajar | 9                    |


Link da documentação: https://docs-djangoproject-com.translate.goog/pt-br/4.1/ref/models/querysets/?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt-BR&_x_tr_pto=wapp