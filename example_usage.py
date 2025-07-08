#!/usr/bin/env python3
"""
Exemplo de uso da API do Skyscanner Bot
"""

import requests
import json
import time

# Configuração da API
API_BASE_URL = "http://localhost:5000/api"  # Altere para a URL do seu deploy

def test_health_check():
    """Testa se a API está funcionando"""
    print("🔍 Testando health check...")
    try:
        response = requests.get(f"{API_BASE_URL}/flights/health")
        if response.status_code == 200:
            print("✅ API está funcionando!")
            print(f"   Resposta: {response.json()}")
            return True
        else:
            print(f"❌ Erro no health check: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Erro de conexão: {e}")
        return False

def search_flights(origin, destination, departure_date, return_date, proxy=None):
    """Busca voos usando a API"""
    print(f"🛫 Buscando voos de {origin} para {destination}...")
    
    data = {
        "origin": origin,
        "destination": destination,
        "departure_date": departure_date,
        "return_date": return_date,
        "adults": 1,
        "cabin_class": "economy"
    }
    
    # Adicionar proxy se fornecido
    if proxy:
        data["proxy"] = proxy
        print(f"   🌐 Usando proxy: {proxy}")
    
    try:
        response = requests.post(
            f"{API_BASE_URL}/flights/search",
            json=data,
            headers={'Content-Type': 'application/json'},
            timeout=120  # 2 minutos de timeout
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Voos encontrados!")
            
            if result.get('flights'):
                flight = result['flights'][0]
                print(f"   💰 Preço: {flight.get('price', 'N/A')}")
                print(f"   ✈️  Companhia: {flight.get('airline', 'N/A')}")
                print(f"   📅 Ida: {flight.get('departure_details', 'N/A')}")
                print(f"   📅 Volta: {flight.get('return_details', 'N/A')}")
                print(f"   🔗 Link: {flight.get('direct_link', 'N/A')}")
            
            return result
        else:
            print(f"❌ Erro na busca: {response.status_code}")
            try:
                error_data = response.json()
                print(f"   Mensagem: {error_data.get('message', 'Erro desconhecido')}")
            except:
                print(f"   Resposta: {response.text}")
            return None
            
    except requests.exceptions.Timeout:
        print("❌ Timeout na requisição (mais de 2 minutos)")
        return None
    except Exception as e:
        print(f"❌ Erro na requisição: {e}")
        return None

def main():
    """Função principal com exemplos de uso"""
    print("🤖 Skyscanner Bot API - Exemplo de Uso")
    print("=" * 50)
    
    # Teste 1: Health Check
    if not test_health_check():
        print("❌ API não está funcionando. Verifique se o servidor está rodando.")
        return
    
    print()
    
    # Teste 2: Busca de voos sem proxy
    print("📋 Teste 1: Busca sem proxy")
    result1 = search_flights(
        origin="MXP",           # Milão
        destination="AMS",      # Amsterdã
        departure_date="2025-08-04",
        return_date="2025-08-08"
    )
    
    print()
    
    # Teste 3: Busca de voos com proxy (descomente e configure seu proxy)
    # print("📋 Teste 2: Busca com proxy")
    # result2 = search_flights(
    #     origin="GRU",           # São Paulo
    #     destination="LHR",      # Londres
    #     departure_date="2025-09-15",
    #     return_date="2025-09-22",
    #     proxy="http://username:password@ip:port"  # Configure seu proxy aqui
    # )
    
    print()
    print("✨ Testes concluídos!")

if __name__ == "__main__":
    main()

