from django.shortcuts import render

from article.models import Article

def article(request):
    '''
    Render the article page
    '''
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request, 'article/article.html',context)