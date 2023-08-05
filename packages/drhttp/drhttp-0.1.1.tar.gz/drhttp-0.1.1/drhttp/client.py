import aiohttp
import asyncio
import datetime
import logging
import json
import re
import threading

class DrHTTPClient:
    # dsn example : https://<api_key>@api.drhttp.com
    def __init__(self, dsn, event_loop=None):
        self.protocol, self.api_key, self.url = re.split('://|@', dsn)
        if event_loop:
            self.event_loop = event_loop 
        else:
            self.event_loop = asyncio.new_event_loop()
            self.event_loop.set_debug(True)
            self.event_loop_thread = threading.Thread(target = self.event_loop.run_forever)
            self.event_loop_thread.setDaemon(True)
            self.event_loop_thread.start()

    async def sendData(self, data):
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'DrHTTP-ApiKey': self.api_key
        }
        
        url = '{protocol}://{url}/api/v1/http_record/record'.format(protocol=self.protocol, url=self.url)
        """ sync version
        req = urllib.request.Request(url, data=body, headers=headers)
        try:
            return urllib.request.urlopen(req).read()
        except:
            return None
        """    
        async with aiohttp.ClientSession(loop=self.event_loop) as session:
            async with session.post(url, json=data, headers=headers) as response:
                return await response.text()

    def record(self, datetime, user_identifier,
                    method, uri, request_headers, request_data,
                    status, response_headers=None, response_data=None):
        data = {
            "datetime": datetime.isoformat(),
            "method": method,
            "uri": uri,
            "status": status,
            "request" : {
                'headers': {k: v for k,v in request_headers.items()},
                'body': request_data.decode("utf-8")
            }
        }
        if user_identifier:
            data["user_identifier"] = user_identifier
        if response_headers or response_data:
            data["response"] = {}
        if response_headers:
            data["response"]['headers'] = {k: v for k,v in response_headers.items()}
        if response_data:
            data["response"]['body'] = response_data.decode("utf-8")
        
        asyncio.run_coroutine_threadsafe(self.sendData(data), self.event_loop)
        

