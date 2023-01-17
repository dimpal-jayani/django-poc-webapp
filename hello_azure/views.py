import asyncio
import logging
import time
import uuid
import pandas as pd
from asgiref.sync import async_to_sync

from rest_framework.views import APIView
from rest_framework.response import Response
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
    

from concurrent.futures import ThreadPoolExecutor

class DataIngestionAPIView(APIView):
    executor = ThreadPoolExecutor(max_workers=4)

    def get(self, request):
        sync = request.GET.get("sync")
        unique_id = uuid.uuid4()
        print(f'{sync}')
        print(f'unique_id = {unique_id}')
        # sync task
        if sync:
            future = self.executor.submit(self.some_task, request, unique_id)
            result = future.result()
        else:
            print('start asynchronously')
            # Schedule the task asynchronously
            future = self.executor.submit(self.myFunc, request, unique_id)
            result = {'file_path': f'{unique_id}'}
        return Response(result)

    def some_task(self, request, unique_id):
        # Do some work here
        result = {'file_path': f'{unique_id}'}
        print(f'Do some work here sync {unique_id}')
        # dictionary of lists
        df = pd.DataFrame([{'name': 'test', 'degree': 2, 'score': 20}])
        df.to_csv(f'/tmp/sync-{unique_id}.csv')
        return result
    
    def some_task_async(self, request, unique_id):
        # Do some work here asynchronously
        result = {'file_path': f'{unique_id}'}
        # time.sleep(60)
        print('Do some work here asynchronously')
        # dictionary of lists
        df = pd.DataFrame([{'name': 'test', 'degree': 2, 'score': 20}])
        time.sleep(60)
        df.to_csv(f'/tmp/{unique_id}.csv')
        print('Done asynchronously')
        
        return result
    

    def myFunc(self, request, unique_id):
        import threading

        print('something')
        p = threading.Thread(target=self.some_task_async, args=(request, unique_id))
        p.start()  # start execution of myFunc() asychronously
        print('finish')