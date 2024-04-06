
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .extractor import extract_data

class DataExtractorAPI(APIView):
    def post(self, request, *args, **kwargs):
       
        url = request.data.get('url')
        schema = request.data.get('schema')

        if not url or not schema:
            return Response({'error': 'URL and schema are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = extract_data(url, schema)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
