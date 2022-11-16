from rest_framework.response import Response
from rest_framework.views import APIView

from Apps.proveedores.models import Proveedores

class ProveedoresView(APIView):
    def get(self, request):
        proveedores = Proveedores.objects.all()
        return Response({"proveedores": proveedores})