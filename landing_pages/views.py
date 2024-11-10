from django.shortcuts import render

# Create your views here.
def about_us(request): 
    show_white = True
    context = {
        'arrow': show_white,
    }
    template = 'landing_pages/about_us.html'

    return render(request, template, context)

def contact_us(request): 
    context = {}
    template = 'landing_pages/contact_us.html'

    return render(request, template, context)

def author(request):
    author = True
    context = {
        'author': author,
    }
    template = 'landing_pages/author.html'

    return render(request, template, context)

def render_snippet(request, section, snippet_name):
    snippet = True
    context = {
        'snippet': snippet,
    }
    snippet_path = f"sections/{section}/{snippet_name}.html"

    return render(request, snippet_path, context)

def presentation(request):
    template = 'presentation.html'
    context = {}
    return render(request, template, context)