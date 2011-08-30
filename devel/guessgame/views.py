# Create your views here.
import random
import datetime
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from guessgame.models import Game 

def newgame(requst): 
    game = Game(number=random.randrange(1,20), pub_date=datetime.datetime.now()) 
    game.save()
    return render_to_response('guessgame/results.html', {'game':game})
    
def index(request): 
    latest_games_list = Game.objects.all().order_by('-pub_date')[:5]
    return render_to_response('guessgame/index.html', {'latest_games_list': latest_games_list})
   
def detail(request, game_id): 
    p = get_object_or_404(Game, pk=game_id) 
    return render_to_response('guessgame/detail.html', {'game':p},
                               context_instance=RequestContext(request))


def results(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render_to_response('guessgame/results.html', {'game': game})

def pick(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    try:
        pick = request.POST['number']
    except KeyError:
        return render_to_response('guessgame/detail.html', 
        {'game': game,
         'error_message': "You didn't make a guess", 
        }, context_instance=RequestContext(request))
    else:
        guess = game.guess_set.create(guess=pick) 
        guess.save()    
        return HttpResponseRedirect(reverse('guessgame.views.results', args=(game.id,)))
