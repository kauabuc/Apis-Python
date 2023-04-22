from django.db import models


class Links(models.Model):
    link_redirecionado = models.URLField()
    link_encurtado = models.CharField(max_length=8, unique=True)

    def __str__(self) -> str:
        return self.link_encurtado
