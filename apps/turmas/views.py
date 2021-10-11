from django.shortcuts import render


def homeLocalidade(request):
    # localidade = Turma.objects.all().order_by("modalidade")
    return render(request, 'home_turmas.html')
