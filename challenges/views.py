from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": "Get Malians at AoE 4!",
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)


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
        return render(request, "challenges/challenge.html")
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
