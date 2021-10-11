from django.contrib.auth.decorators import login_required
from .models import Aluno
from django.shortcuts import render, redirect
from .form import AlunoForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
# Excel
from django.views.generic import View
import xlwt
# pdf
from django.template.loader import get_template
from xhtml2pdf import pisa


# listar
@csrf_protect
def listarAlunos(request):
    titulo = 'Alunos'
    subtitle = 'Lista de alunos'
    alunos = Aluno.objects.all()
    return render(request, 'listar_alunos.html', {'titulo': titulo, 'subtitle': subtitle, 'alunos': alunos})

# Criar Alunos


@csrf_protect
def criarAlunoPublic(request):
    titulo = 'Aluno'
    subtitle = 'Criar novo Aluno(a)'
    messages.warning(request, 'Preencha todos os campos obrigatórios!')
    form = AlunoForm(request.POST or None)
    return render(request, 'criar_alunos_public.html', {'titulo': titulo, 'subtitle': subtitle, 'form': form})


def alunoNovoPublic(request):
    form = AlunoForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Registro salvo com sucesso!')
        return redirect('index')
    else:
        messages.error(
            request, 'Registro não foi salvo! Verifique se existe alguma informação errada ou incompleta.')
        return redirect('index')


# Criar Alunos
@login_required
@csrf_protect
def criarAluno(request):
    titulo = 'Aluno'
    subtitle = 'Criar novo Aluno(a)'
    messages.warning(request, 'Preencha todos os campos obrigatórios!')
    form = AlunoForm(request.POST or None)
    return render(request, 'criar_alunos.html', {'titulo': titulo, 'subtitle': subtitle, 'form': form})


@login_required
def alunoNovo(request):
    form = AlunoForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Registro salvo com sucesso!')
        return redirect('listar_alunos')
    else:
        messages.error(
            request, 'Registro não foi salvo! Verifique se existe alguma informação errada ou incompleta.')
        return redirect('listar_alunos')


@login_required
def updateAluno(request, ID_Aluno):
    data = {}
    aluno = Aluno.objects.get(ID_Aluno=ID_Aluno)
    form = AlunoForm(instance=aluno)

    data['aluno'] = aluno
    data['form'] = form

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro modificado com sucesso!')
            return redirect('listar_alunos')
    else:
        messages.info(request, 'Preencha todos os campos obrigatórios!')
        return render(request, 'update_alunos.html', data)


@login_required
def deleteAluno(request, ID_Aluno):
    titulo = 'Aluno'
    subtitle = 'Deletar Aluno(a)'
    aluno = Aluno.objects.get(ID_Aluno=ID_Aluno)

    if request.method == 'POST':
        aluno.delete()
        messages.success(request, 'Registro deletado com sucesso!')
        return redirect('listar_alunos')
    else:
        return render(request, 'delete_alunos.html', {'titulo': titulo, 'subtitle': subtitle, 'aluno': aluno})


@login_required
def visualizarAluno(request, ID_Aluno):
    data = {}
    aluno = Aluno.objects.get(ID_Aluno=ID_Aluno)
    form = AlunoForm(request.POST or None, instance=aluno)
    data['aluno'] = aluno
    data['form'] = form

    return render(request, 'visualizar_alunos.html', data)

# Excel


class alunoEXL(View):
    def get(self, request, ):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="alunos-ebd.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        # this will make a sheet named Users Data
        ws = wb.add_sheet('Alunos')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ['Nome']

        for col_num in range(len(columns)):
            # at 0 row 0 column
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = Aluno.objects.all().values_list(
            'nome')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response


# pdf
@login_required
def pdfAluno(request, ID_Aluno):
    alunos = Aluno.objects.filter(ID_Aluno=ID_Aluno)

    template_path = 'pdf/pdf_aluno.html'
    context = {'alunos': alunos}

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # attachment;
    response['Content-Disposition'] = 'filename="pdf_aluno.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
