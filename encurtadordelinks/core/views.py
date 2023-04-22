from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import FormLinks
from .models import Links

# Create your views here.


def home(request):
    form = FormLinks()
    status = request.GET.get('status')
    return render(request, 'home.html', {'form': form, 'status': status})


def valida_link(request):
    form = FormLinks(request.POST)
    link_encurtado = form.data['link_encurtado']
    links = Links.objects.filter(link_encurtado=link_encurtado)

    if len(links) > 0:
        return redirect('/?status=1')

    if form.is_valid():
        try:
            form.save()
            return HttpResponse(f'Seu link foi criado com sucesso e é http://127.0.0.1:8000/{link_encurtado}')
        except:
            return HttpResponse('Erro interno do sistema')


def redirecionar(request, link):
    links = Links.objects.filter(link_encurtado=link)

    if len(link) == 0:
        return redirect('/')

    return redirect(links[0].link_redirecionado)
