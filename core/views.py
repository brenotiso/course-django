from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from blog.models import Publication


def index(request):
    publications = Publication.objects.all().order_by('-date')
    context = {
        'publications': publications
    }
    return render(request, 'core/index.html', context)


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
