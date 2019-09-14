from django.urls import path
from .views import (
    publication_detail,
    comment
)

urlpatterns = [
    path('publication/<int:id_publication>', publication_detail, name='publication_detail'),
    path('publication/<int:id_publication>/comment', comment, name='comment_on_publication')
]
