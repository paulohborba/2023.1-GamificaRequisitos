from django.contrib import admin
from .models import Turma, Atividade, Equipe, Aluno

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'data_criacao')
    list_fields = ('nome', 'descricao')
    list_filter = ('nome', 'data_criacao')

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'turma')
    list_fields =  ('nome', 'descricao', 'turma')
    list_filter = ('turma', )

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'equipe', 'turma_da_equipe')
    list_fields = ('nome', 'equipe', 'turma_da_equipe')
    list_filter = ('equipe',)

    def turma_da_equipe(self, obj):
        return obj.equipe.turma.nome

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turma', 'pontos', 'data_entrega', 'data_criacao')
    list_fields = ('nome', 'turma', 'pontos', 'data_entrega')
    list_filter = ('turma', 'data_entrega')