from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# test comment 2

monthly_challenges = {
    "january": "january challenge",
    "february": "february challenge",
    "march": "march challenge",
    "april": "april challenge",
    "may": "may challenge",
    "june": "june challenge",
    "july": "july challenge",
    "august": "august challenge",
    "september": "september challenge",
    "october": "october challenge",
    "november": "november challenge",
    "december": "december challenge",
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months,
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid")
    
    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month,
        })
    except:
        return HttpResponseNotFound("<h1>not found</h1>")
