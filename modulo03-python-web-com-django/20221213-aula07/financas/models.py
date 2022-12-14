from django.db import models
from django.contrib.auth.models import User


class ContaFinanceira(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, null=False)
    saldo = models.FloatField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_contas_financeiras'


class Transacao(models.Model):

    # Quando temos chaves estrangeiras em uma model que referenciam
    # o mesmo campo na model relacionada, precisamos informar o argumento
    # 'related_name', pois senão o Django não consegue diferenciar
    # os campos

    conta_debito = models.ForeignKey(
        ContaFinanceira, models.CASCADE, related_name='conta_debito'
    )

    conta_credito = models.ForeignKey(
        ContaFinanceira, models.CASCADE, related_name='conta_credito'
    )

    valor = models.FloatField()

    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tb_transacoes'
