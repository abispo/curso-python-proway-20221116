from django.db import models


class Question(models.Model):

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Data de publicação')

    def __str__(self):
        return self.question_text

    class Meta:
        db_table = 'tb_questions'


class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    class Meta:
        db_table = 'tb_choices'


class Comment(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        db_table = "tb_comments"
