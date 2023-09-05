from django.shortcuts import render
from core.constants import get_all_domains


def home(request):
    domain_name = f"{request.scheme}://{request.META['HTTP_HOST']}"
    all_domains = get_all_domains(domain_name)
    return render(request, "route.html", {"all_domains": all_domains})