# Skyscanner Bot API

Bot automatizado para busca de voos mais baratos no Skyscanner com suporte a proxy 5G.

## Funcionalidades

- 🔍 Busca automatizada de voos mais baratos no Skyscanner
- 🌐 Suporte a proxy 5G para contornar limitações geográficas
- 📊 Retorna informações detalhadas dos voos (preço, companhia aérea, horários, link direto)
- 🚀 API REST para integração fácil
- 📱 Suporte a CORS para uso em aplicações web

## Endpoints da API

### Health Check
```
GET /api/flights/health
```

Verifica se a API está funcionando.

**Resposta:**
```json
{
  "status": "success",
  "message": "API de busca de voos está funcionando."
}
```

### Buscar Voos
```
POST /api/flights/search
```

Busca voos mais baratos entre duas cidades.

**Parâmetros (JSON):**
```json
{
  "origin": "MXP",              // Código IATA do aeroporto de origem (obrigatório)
  "destination": "AMS",         // Código IATA do aeroporto de destino (obrigatório)
  "departure_date": "2025-08-04", // Data de ida no formato YYYY-MM-DD (obrigatório)
  "return_date": "2025-08-08",    // Data de volta no formato YYYY-MM-DD (obrigatório)
  "adults": 1,                    // Número de adultos (opcional, padrão: 1)
  "cabin_class": "economy",       // Classe da cabine (opcional, padrão: "economy")
  "proxy": "http://username:password@ip:port" // Proxy 5G (opcional)
}
```

**Resposta de Sucesso:**
```json
{
  "status": "success",
  "message": "Voos encontrados com sucesso.",
  "flights": [
    {
      "price": "R$ 1.280",
      "currency": "BRL",
      "departure_date": "2025-08-04",
      "return_date": "2025-08-08",
      "airline": "Wizz Air Malta + easyJet / Vueling Airlines + Aeroitalia",
      "departure_details": "07:10 (MXP) -> 08:25+1 (AMS), 1 parada",
      "return_details": "20:55 (AMS) -> 11:25+1 (MXP), 1 parada",
      "direct_link": "https://www.skyscanner.com.br/transport_deeplink/..."
    }
  ]
}
```

**Resposta de Erro:**
```json
{
  "status": "error",
  "message": "Descrição do erro"
}
```

## Instalação Local

### Pré-requisitos
- Python 3.11+
- pip

### Passos

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd skyscanner_bot_api
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\\Scripts\\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Instale os navegadores do Playwright:
```bash
playwright install chromium
```

5. Execute a aplicação:
```bash
python src/main.py
```

A API estará disponível em `http://localhost:5000`

## Deploy no Render

### Método 1: Deploy Automático via GitHub

1. Faça push do código para um repositório GitHub
2. Conecte sua conta Render ao GitHub
3. Crie um novo Web Service no Render
4. Selecione o repositório
5. Configure as seguintes variáveis:
   - **Build Command:** `pip install -r requirements.txt && playwright install chromium`
   - **Start Command:** `python src/main.py`
   - **Environment:** Python 3.11

### Método 2: Deploy via Dockerfile

1. Use o Dockerfile incluído no projeto
2. Configure o Web Service no Render para usar Docker
3. O deploy será feito automaticamente

## Uso com Proxy 5G

Para usar um proxy 5G, inclua o parâmetro `proxy` na requisição:

```json
{
  "origin": "MXP",
  "destination": "AMS",
  "departure_date": "2025-08-04",
  "return_date": "2025-08-08",
  "proxy": "http://username:password@ip:port"
}
```

### Formatos de Proxy Suportados
- `http://username:password@ip:port`
- `https://username:password@ip:port`

## Exemplo de Uso

### cURL
```bash
curl -X POST http://localhost:5000/api/flights/search \\
  -H "Content-Type: application/json" \\
  -d '{
    "origin": "MXP",
    "destination": "AMS",
    "departure_date": "2025-08-04",
    "return_date": "2025-08-08",
    "adults": 1,
    "cabin_class": "economy"
  }'
```

### Python
```python
import requests

data = {
    "origin": "MXP",
    "destination": "AMS",
    "departure_date": "2025-08-04",
    "return_date": "2025-08-08",
    "adults": 1,
    "cabin_class": "economy"
}

response = requests.post(
    'http://localhost:5000/api/flights/search',
    json=data
)

print(response.json())
```

### JavaScript
```javascript
const data = {
  origin: "MXP",
  destination: "AMS",
  departure_date: "2025-08-04",
  return_date: "2025-08-08",
  adults: 1,
  cabin_class: "economy"
};

fetch('http://localhost:5000/api/flights/search', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(data)
})
.then(response => response.json())
.then(data => console.log(data));
```

## Estrutura do Projeto

```
skyscanner_bot_api/
├── src/
│   ├── routes/
│   │   ├── flights.py      # Endpoints da API de voos
│   │   └── user.py         # Endpoints de usuário (template)
│   ├── models/
│   │   └── user.py         # Modelos de dados (template)
│   ├── static/             # Arquivos estáticos
│   ├── database/           # Banco de dados SQLite
│   ├── scraper.py          # Lógica de scraping do Skyscanner
│   └── main.py             # Ponto de entrada da aplicação
├── venv/                   # Ambiente virtual
├── requirements.txt        # Dependências Python
├── Dockerfile             # Configuração Docker
├── test_api.py            # Testes da API
└── README.md              # Este arquivo
```

## Limitações e Considerações

- O scraping depende da estrutura HTML do Skyscanner, que pode mudar
- Proxies podem ter limitações de velocidade ou disponibilidade
- O Skyscanner pode implementar medidas anti-bot
- Recomenda-se usar com moderação para evitar bloqueios

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto é fornecido "como está" para fins educacionais. Use por sua própria conta e risco.

## Suporte

Para dúvidas ou problemas, abra uma issue no repositório GitHub.

