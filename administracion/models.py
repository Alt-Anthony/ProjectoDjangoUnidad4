from django.db import models

class ProjectModel(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=400)
    foto_url = models.URLField(max_length=200)
    tags = models.CharField(max_length=100, null=True)
    github_url = models.URLField(max_length=200)

    def __str__(self):
        return self.titulo + self.tags
    
    class Meta:
        db_table = 'Proyectos'

class IPs(models.Model):
    ip = models.CharField(max_length=50)

    class Meta:
        db_table = 'IP'