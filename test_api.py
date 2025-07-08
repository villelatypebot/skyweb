import requests
import json

# Teste básico da API
def test_health_check():
    try:
        response = requests.get('http://localhost:5000/api/flights/health')
        print("Health Check:", response.json())
        return response.status_code == 200
    except Exception as e:
        print(f"Erro no health check: {e}")
        return False

def test_flight_search():
    try:
        data = {
            "origin": "MXP",
            "destination": "AMS", 
            "departure_date": "2025-08-04",
            "return_date": "2025-08-08",
            "adults": 1,
            "cabin_class": "economy"
            # Sem proxy para teste inicial
        }
        
        response = requests.post(
            'http://localhost:5000/api/flights/search',
            json=data,
            headers={'Content-Type': 'application/json'}
        )
        
        print("Flight Search Response:")
        print(json.dumps(response.json(), indent=2))
        return response.status_code == 200
        
    except Exception as e:
        print(f"Erro na busca de voos: {e}")
        return False

if __name__ == "__main__":
    print("=== Testando API do Skyscanner Bot ===")
    
    print("\n1. Testando Health Check...")
    if test_health_check():
        print("✓ Health check passou")
    else:
        print("✗ Health check falhou")
    
    print("\n2. Testando busca de voos...")
    if test_flight_search():
        print("✓ Busca de voos passou")
    else:
        print("✗ Busca de voos falhou")

