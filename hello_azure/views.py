from rest_framework.response import Response


# from snippets.models import Snippet
# from snippets.serializers import SnippetSerializer
# from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging
import time
class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        logging.info('inside get')
        wait_time = int(request.GET.get("wait_time"))
        print(wait_time)
        time.sleep(wait_time)
        return Response({'status':'SUCCESS'})