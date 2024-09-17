import json

def verify_bazaar_data(data: dict) -> dict:
    if data.get('products', []) != []: # Check if products is not empty
        return True
    else:
        return False