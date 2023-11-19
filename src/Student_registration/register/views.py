from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import CollegianModel
from .ModelSerializer.CollegianSerialize import CollegianSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.core import serializers

def hello_word(request):
    return HttpResponse("helo")


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Collegian Name': '/?CollegianFirstName=Collegian_FirstName',
        'Search by Collegian code': '/?CollegianCode=Collegian_Code',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
    return Response(serializers.serialize('json',CollegianModel.objects.all()))


@api_view(['POST'])
def register_Collegian(request):
    collegian = CollegianSerializer(data=request.data)

    if CollegianModel.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This data is already existed")
    if collegian.is_valid():
        collegian.save()
        return Response(collegian.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_Collegian(request):
    if request.query_params:
        collegian = CollegianModel.objects.filter(**request.query_params.dict())
    else:
        collegian = CollegianModel.objects.all()

    if collegian:
        serializer = CollegianSerializer(collegian, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def update_Collegian(request, pk):
    collegian = CollegianModel.objects.get(pk=pk)
    data = CollegianSerializer(instance=collegian, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_Collegian(request, pk):
    collegian = get_object_or_404(CollegianModel, pk=pk)
    collegian.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
