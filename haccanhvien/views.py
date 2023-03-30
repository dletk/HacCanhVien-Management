
from django.http import HttpResponse
from django.template import loader

from .models.san_pham import Mo


# Create your views here.
def index(request):
    return HttpResponse("Hello, world! Small step towards a big system!")


def project_plan(request):
    all_mo = Mo.objects.all()

    template = loader.get_template("project_plan.html")
    grouped_objects = []

    for obj in all_mo:
        grouped_objects.append((obj.hang, obj.cot, obj))

    context = {'grouped_objects': grouped_objects}
    return HttpResponse(template.render(context, request))
