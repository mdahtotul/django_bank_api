from django.shortcuts import render
from bank.models import Branch
from core.constants import get_all_domains


def home(request):
    branches = Branch.objects.all()
    if branches.exists():
        branch = branches.first()
        print(branch)
        branch.count += 1
        branch.save()
    else:
        branch = Branch.objects.create()

    domain_name = f"{request.scheme}://{request.META['HTTP_HOST']}"
    all_domains = get_all_domains(domain_name)
    return render(request, "route.html", {"all_domains": all_domains, "branch": branch})