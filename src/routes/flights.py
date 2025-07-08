from flask import Blueprint, request, jsonify
from src.scraper import get_cheapest_flight
import asyncio

flights_bp = Blueprint('flights', __name__)

@flights_bp.route('/flights/search', methods=['POST'])
def search_flights():
    try:
        data = request.get_json()
        
        # Validar dados obrigatórios
        required_fields = ['origin', 'destination', 'departure_date', 'return_date']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'status': 'error',
                    'message': f'Campo obrigatório ausente: {field}'
                }), 400
        
        # Extrair dados da requisição
        origin = data['origin']
        destination = data['destination']
        departure_date = data['departure_date']
        return_date = data['return_date']
        adults = data.get('adults', 1)
        cabin_class = data.get('cabin_class', 'economy')
        proxy = data.get('proxy', None)
        
        # Executar o scraping
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        flight_data = loop.run_until_complete(
            get_cheapest_flight(
                origin=origin,
                destination=destination,
                departure_date=departure_date,
                return_date=return_date,
                adults=adults,
                cabin_class=cabin_class,
                proxy=proxy
            )
        )
        
        loop.close()
        
        if flight_data:
            return jsonify({
                'status': 'success',
                'message': 'Voos encontrados com sucesso.',
                'flights': [flight_data]
            })
        else:
            return jsonify({
                'status': 'error',
                'message': 'Não foi possível encontrar voos para os parâmetros fornecidos.'
            }), 404
            
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Erro interno do servidor: {str(e)}'
        }), 500

@flights_bp.route('/flights/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'success',
        'message': 'API de busca de voos está funcionando.'
    })

