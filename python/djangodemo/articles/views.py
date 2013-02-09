from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Articles


def home(request):
    articles = Articles.objects.filter()

    dic = {
        'articles': articles,
    }
    return render_to_response('home.html', dic, context_instance=RequestContext(request))


def article(request, url=''):
    try:
        article = Articles.objects.filter(url=url)[0]
    except:
        raise Http404

    dic = {
        'article': article,
    }
    return render_to_response('article.html', dic, context_instance=RequestContext(request))

