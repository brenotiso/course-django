from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from django.http import Http404
from django.contrib.auth.decorators import login_required
from .models import (
    Publication,
    Comment
)
from .forms import Comment_Form


def publication_detail(request, id_publication):
    publication = get_object_or_404(Publication, pk=id_publication)
    comments = Comment.objects.filter(publication=id_publication)

    commet_form = Comment_Form()
    context = {
        'publication': publication,
        'comments': comments,
        'commet_form': commet_form
    }
    return render(request, 'core/publication.html', context)


@login_required
def comment(request, id_publication):
    publication = get_object_or_404(Publication, pk=id_publication)

    if request.method == "POST":
        commet_form = Comment_Form(request.POST)
        if commet_form.is_valid():
            print('asdasdas')
            comment = commet_form.save(commit=False)
            comment.user = request.user
            comment.publication = publication
            comment.save()

            comments = Comment.objects.filter(publication=id_publication)
            commet_form = Comment_Form()
            context = {
                'publication': publication,
                'comments': comments,
                'commet_form': commet_form
            }
            return redirect(publication_detail, id_publication)

    return Http404()
