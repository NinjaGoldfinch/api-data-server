#import json

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

from data_classes import bazaar_data
from verify_data import verify_bazaar_data

# Starlette functions

async def recieve_bazaar_data(request):
    request_data = await request.json()
    
    if verify_bazaar_data(request_data):
        num_of_products = len(request_data.get('products', []).keys())
        print(f"Recieved valid bazaar data\nLast Updated: {request_data.get('lastUpdated', None)}\nNumber of products: {num_of_products}")
        return JSONResponse(bazaar_data(request_data).products_formatted)

routes = [
    Route('/bazaar', recieve_bazaar_data, methods=['POST'])
]

app = Starlette(routes=routes)