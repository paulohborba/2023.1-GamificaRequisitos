from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import RelatedFieldListFilter
from django.db.models import Q
from .models import Turma, Atividade, Equipe, Aluno, RealizacaoAtividade

@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'data_criacao')
    list_fields = ('nome', 'descricao')
    list_filter = ('data_criacao',)

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome','saldo_pontos', 'descricao', 'turma')
    list_fields =  ('nome', 'descricao', 'turma')
    list_filter = ('turma',)

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'equipe', 'nome_da_turma', 'descricao_da_turma')
    list_fields = ('nome', 'equipe', 'nome_da_turma')
    list_filter = ('equipe',)

    def nome_da_turma(self, obj):
        return obj.equipe.turma.nome
    
    def descricao_da_turma(self, obj):
        return obj.equipe.turma.descricao

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'turma', 'pontos', 'data_entrega', 'data_criacao')
    list_fields = ('nome', 'turma', 'pontos', 'data_entrega')
    list_filter = ('turma', 'data_entrega')

class EquipeTurmaFilter(RelatedFieldListFilter):
    def field_choices(self, field, request, model_admin):
        # Obtém a turma selecionada no filtro de atividades
        turma_id = request.GET.get('atividade__turma__id')
        if turma_id:
            # Filtra as equipes pela turma selecionada
            return field.get_choices(
                include_blank=False,
                limit_choices_to=Q(turma__id=turma_id),
            )
        else:
            return field.get_choices(
                include_blank=False,
            )
@admin.register(RealizacaoAtividade)
class RealizacaoAtividadeAdmin(admin.ModelAdmin):
    list_display = ('atividade', 'equipe', 'realizada_com_sucesso')
    list_filter = (
        ('atividade__turma', EquipeTurmaFilter),
        'equipe',
        'realizada_com_sucesso',
    )
    