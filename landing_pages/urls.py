from django.urls import path 
from .views import (
    about_us,
    contact_us,
    author,
    render_snippet,
    presentation
)

urlpatterns = [
    path('about_us/', about_us, name='about_us'),
    path('contact_us/', contact_us, name='contact_us'),
    path('author/', author, name='author'),
    path('<section>/<snippet_name>/', render_snippet, name='render_snippet'),
    path('presentation/', presentation, name='presentation'),
]
