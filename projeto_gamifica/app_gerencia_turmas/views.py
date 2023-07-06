from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Turma, Equipe, Aluno, Atividade
from random import sample
import pandas as pd

def pagina_inicial(request):
    turmas = Turma.objects.all()
    context = {'turmas': turmas}
    return render(request, 'app_gerencia_turmas/pagina_inicial.html', context)

def turma_detalhe(request, turma_id):
    turma = get_object_or_404(Turma, id=turma_id)
    atividades = Atividade.objects.filter(turma=turma)
    context = {'turma': turma, 'atividades': atividades}
    return render(request, 'app_gerencia_turmas/turma_detalhe.html', context)

def atividade_detalhe(request, atividade_id):
    atividade = get_object_or_404(Atividade, id=atividade_id)
    context = {'atividade': atividade}
    return render(request, 'app_gerencia_turmas/atividade_detalhe.html', context)

def equipe_detalhe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    context = {'equipe': equipe}
    return render(request, 'app_gerencia_turmas/equipe_detalhe.html', context)

def cadastro_alunos(request):
    turmas = Turma.objects.all()

    if request.method == 'POST':
        arquivo = request.FILES['arquivo']
        turma_id = request.POST.get('turma')
        quantidade_equipes = int(request.POST.get('equipes'))

        if arquivo.name.endswith('.xlsx'):
            df = pd.read_excel(arquivo)
            alunos = list(df.to_dict('records'))
            random_alunos = sample(alunos, len(alunos))  # Embaralhar a ordem dos alunos

            try:
                turma = Turma.objects.get(id=turma_id)
                equipes_criadas = []

                # Criar as equipes
                for i in range(1, quantidade_equipes + 1):
                    equipe = Equipe.objects.create(nome=f'Equipe {i}', turma=turma)
                    equipes_criadas.append(equipe)

                # Distribuir os alunos nas equipes
                num_equipes = len(equipes_criadas)
                equipe_index = 0

                for aluno in random_alunos:
                    matricula = aluno['Matricula']
                    email = aluno['Email']
                    username = matricula

                    # Verificar se o usuário já existe
                    try:
                        user = User.objects.get(username=username)
                        # Se o usuário já existe, atualizar as informações
                        user.email = email
                        user.save()
                    except User.DoesNotExist:
                        # Se o usuário não existe, criar um novo usuário
                        password = User.objects.make_random_password()
                        user = User.objects.create_user(username=username, password=password, email=email)

                    # Associar o aluno à equipe
                    equipe_atual = equipes_criadas[equipe_index]
                    aluno = Aluno.objects.create(nome=username, equipe=equipe_atual)
                    equipe_atual.aluno_set.add(aluno)
                    equipe_atual.save()

                    equipe_index = (equipe_index + 1) % num_equipes

                messages.success(request, 'Usuários criados e distribuídos com sucesso!')
            except Turma.DoesNotExist:
                messages.warning(request, f'Turma {turma_id} não encontrada.')
        else:
            messages.error(request, 'Arquivo inválido. Por favor, selecione um arquivo .xlsx.')

    context = {'turmas': turmas}
    return render(request, 'app_gerencia_turmas/cadastro_alunos.html', context)
