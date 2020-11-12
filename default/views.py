from django.shortcuts import render
from django.views.generic import *
from .models import Poll, Option

# Create your views here.

class PollList(ListView):
    model= Poll

class PollDetail(DetailView):
    model= Poll

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        options = Options.objects.filter(poll_id=self.kwargs['pk'])
        ctx['option_list'] = options
        return ctx
class PollVote(RedirectView):
    def get_redirect_url(self, * args, ** kwargs):
        option= Option.objects.get(id=self.kwargs['oid'])
        option.count += 1   
        option.save()
       return '/poll/{}/'. format(option.poll_id)
       # return'/poll/'+str(option.poll_id)+'/'
