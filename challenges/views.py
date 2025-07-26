from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Get Abbasid mastery at AoE 4!",
    "february": "Get Byzantine mastery at AoE 4!",
    "march": "Get Japanese mastery at AoE 4!",
    "april": "Get English mastery at AoE 4!",
    "may": "Get French mastery at AoE 4!",
    "june": "Get Delhi mastery at AoE 4!",
    "july": "Get Rus mastery at AoE 4!",
    "august": "Get HRE mastery at AoE 4!",
    "setember": "Get Mongols mastery at AoE 4!",
    "october": "Get Chinese mastery at AoE 4!",
    "november": "Get Ottomans at AoE 4!",
    "december": None
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months_list": months
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    try:
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")

    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month_name": month,
            "text": challenge_text
        })
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
