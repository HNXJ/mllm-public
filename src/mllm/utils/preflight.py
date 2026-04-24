import requests

def verify_model_loaded(model_name, engine_url='http://localhost:4474'):
    try:
        response = requests.get(f'{engine_url}/v1/models')
        models = response.json().get('data', [])
        loaded_ids = [m['id'] for m in models]
        if model_name in loaded_ids:
            return True
        return False
    except Exception as e:
        return False
