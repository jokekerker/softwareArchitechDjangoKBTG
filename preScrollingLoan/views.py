from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import LoanProfile


# Create your views here.
def index(request):
    latest_profile_list = LoanProfile.objects.order_by('-date_create')[:5]
    context = {'latest_profile_list': latest_profile_list}
    return render(request, 'preScrollingLoan/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(LoanProfile, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def change_status(request, profile_id):
    profile = get_object_or_404(LoanProfile, pk=profile_id)
    try:
        selected_choice = request.POST['select_state']
        amount_approve = request.POST['amount_approve']
    except (KeyError, profile.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'preScrollingLoan/index.html', {
            'profile': profile,
            'error_message': "You didn't select a choice.",
        })
    else:
        profile.status = selected_choice
        profile.amount_approve = amount_approve
        profile.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('preScrollingLoan:index'))

    # context = {}
    # return render(request, 'polls/index.html', context)
