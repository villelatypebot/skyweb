# 🤖 Skyscanner Bot API - Projeto Completo

## 📋 Resumo do Projeto

Desenvolvi um bot completo que automatiza a busca por voos mais baratos no Skyscanner, com as seguintes características:

### ✅ Funcionalidades Implementadas

1. **🔍 Scraping Automatizado**
   - Busca voos mais baratos no Skyscanner
   - Extração de preços, companhias aéreas, horários e links diretos
   - Navegação automatizada com Playwright

2. **🌐 Suporte a Proxy 5G**
   - Configuração flexível de proxy no formato `http://username:password@ip:port`
   - Contorna limitações geográficas
   - Testado com o proxy fornecido

3. **🚀 API REST Completa**
   - Endpoint de health check
   - Endpoint de busca de voos
   - Suporte a CORS para integração web
   - Documentação completa da API

4. **📦 Deploy Ready**
   - Configurado para GitHub e Render
   - Dockerfile otimizado
   - Instruções detalhadas de deploy
   - Estrutura de projeto profissional

## 📁 Estrutura do Projeto

```
skyscanner_bot_api/
├── src/
│   ├── routes/
│   │   ├── flights.py          # 🛫 API de busca de voos
│   │   └── user.py             # 👤 Template de usuários
│   ├── models/
│   │   └── user.py             # 📊 Modelos de dados
│   ├── static/                 # 🌐 Arquivos estáticos
│   ├── database/               # 💾 Banco SQLite
│   ├── scraper.py              # 🕷️ Core do scraping
│   └── main.py                 # 🚀 Aplicação Flask
├── venv/                       # 🐍 Ambiente virtual
├── requirements.txt            # 📦 Dependências
├── Dockerfile                  # 🐳 Configuração Docker
├── .gitignore                  # 🚫 Arquivos ignorados
├── README.md                   # 📖 Documentação principal
├── DEPLOY_RENDER.md           # 🚀 Guia de deploy
├── example_usage.py           # 💡 Exemplo de uso
├── test_api.py                # 🧪 Testes da API
└── PROJETO_COMPLETO.md       # 📋 Este arquivo
```

## 🔧 Tecnologias Utilizadas

- **Python 3.11** - Linguagem principal
- **Flask** - Framework web
- **Playwright** - Automação de navegador
- **SQLite** - Banco de dados
- **Docker** - Containerização
- **Render** - Plataforma de deploy

## 🌟 Endpoints da API

### Health Check
```
GET /api/flights/health
```

### Buscar Voos
```
POST /api/flights/search
```

**Parâmetros:**
```json
{
  "origin": "MXP",
  "destination": "AMS", 
  "departure_date": "2025-08-04",
  "return_date": "2025-08-08",
  "adults": 1,
  "cabin_class": "economy",
  "proxy": "http://username:password@ip:port"
}
```

**Resposta:**
```json
{
  "status": "success",
  "flights": [{
    "price": "R$ 1.280",
    "currency": "BRL",
    "airline": "Wizz Air Malta + easyJet",
    "departure_details": "07:10 (MXP) -> 08:25+1 (AMS)",
    "return_details": "20:55 (AMS) -> 11:25+1 (MXP)",
    "direct_link": "https://www.skyscanner.com.br/transport_deeplink/..."
  }]
}
```

## 🚀 Como Usar

### 1. Instalação Local

```bash
# Clone o projeto
git clone <repositorio>
cd skyscanner_bot_api

# Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\\Scripts\\activate  # Windows

# Instale dependências
pip install -r requirements.txt
playwright install chromium

# Execute a aplicação
python src/main.py
```

### 2. Teste da API

```bash
# Health check
curl http://localhost:5000/api/flights/health

# Busca de voos
curl -X POST http://localhost:5000/api/flights/search \\
  -H "Content-Type: application/json" \\
  -d '{
    "origin": "MXP",
    "destination": "AMS",
    "departure_date": "2025-08-04", 
    "return_date": "2025-08-08"
  }'
```

### 3. Uso com Proxy

```python
import requests

data = {
    "origin": "MXP",
    "destination": "AMS",
    "departure_date": "2025-08-04",
    "return_date": "2025-08-08",
    "proxy": "http://manyfriends5gproxy:pBb7ctn7S6Ws@x325.fxdx.in"
}

response = requests.post(
    'http://localhost:5000/api/flights/search',
    json=data
)
print(response.json())
```

## 🌐 Deploy no Render

### Método Rápido

1. **Faça push para GitHub:**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/seu-usuario/skyscanner-bot-api.git
git push -u origin main
```

2. **Configure no Render:**
   - Acesse [render.com](https://render.com)
   - New → Web Service
   - Conecte o repositório GitHub
   - Build Command: `pip install -r requirements.txt && playwright install chromium`
   - Start Command: `python src/main.py`

3. **Deploy automático!** 🎉

## 📚 Documentação Incluída

1. **README.md** - Documentação completa da API
2. **DEPLOY_RENDER.md** - Guia detalhado de deploy
3. **example_usage.py** - Exemplos práticos de uso
4. **test_api.py** - Testes automatizados

## 🔒 Configuração de Proxy

O bot suporta proxies 5G no formato:
- `http://username:password@ip:port`
- `https://username:password@ip:port`

Exemplo com seu proxy:
```json
{
  "proxy": "http://manyfriends5gproxy:pBb7ctn7S6Ws@x325.fxdx.in"
}
```

## ⚡ Performance e Limitações

### Otimizações Implementadas
- Timeouts configuráveis
- Headless browser para performance
- CORS habilitado para integração web
- Estrutura modular para manutenção

### Limitações Conhecidas
- Dependente da estrutura HTML do Skyscanner
- Proxies podem ter limitações de velocidade
- Render gratuito tem timeout de 30s (considere planos pagos)

## 🛠️ Próximos Passos Sugeridos

1. **Cache de Resultados** - Implementar Redis para cache
2. **Rate Limiting** - Evitar sobrecarga da API
3. **Autenticação** - JWT para controle de acesso
4. **Monitoramento** - Logs e métricas detalhadas
5. **Múltiplos Sites** - Expandir para outros sites de viagem

## 🎯 Resultados Entregues

✅ **Bot funcional** que busca voos automaticamente  
✅ **API REST** completa com documentação  
✅ **Suporte a proxy 5G** configurável  
✅ **Deploy ready** para GitHub e Render  
✅ **Documentação completa** e exemplos de uso  
✅ **Código profissional** com estrutura modular  

## 📞 Suporte

O projeto está completo e pronto para uso. Todos os arquivos necessários estão incluídos com documentação detalhada para facilitar a implementação e manutenção.

**Arquivos principais para começar:**
1. `README.md` - Documentação da API
2. `example_usage.py` - Exemplos práticos
3. `DEPLOY_RENDER.md` - Guia de deploy

🚀 **Seu bot está pronto para voar!** ✈️

