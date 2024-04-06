from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ExtractionSchema
from .serializers import ExtractionSchemaSerializer

from .extractor import extract_data
class ExtractionAPIView(APIView):
    def post(self, request):
        serializer = ExtractionSchemaSerializer(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data['url']
            schema = serializer.validated_data['schema']
            # ... perform extraction
            try:
                data = extract_data(url, schema)
                return Response(data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
