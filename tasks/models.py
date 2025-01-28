from django.db import models

class Tasks(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_entrega = models.DateField(blank=True, null=True)
    arquivo = models.FileField(upload_to='arquivos/%Y/%m/%d/', blank=True, null=True)
    entregue = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' tarefa de ' + self.autor.username