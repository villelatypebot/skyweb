# Deploy no Render - Guia Passo a Passo

Este guia explica como fazer o deploy do Skyscanner Bot API no Render.

## Pré-requisitos

1. Conta no [Render](https://render.com)
2. Conta no [GitHub](https://github.com)
3. Código do projeto no GitHub

## Método 1: Deploy via GitHub (Recomendado)

### Passo 1: Preparar o Repositório GitHub

1. Crie um novo repositório no GitHub
2. Faça push do código para o repositório:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/seu-usuario/skyscanner-bot-api.git
git push -u origin main
```

### Passo 2: Conectar GitHub ao Render

1. Acesse [Render Dashboard](https://dashboard.render.com)
2. Clique em "New +" → "Web Service"
3. Conecte sua conta GitHub se ainda não conectou
4. Selecione o repositório do projeto

### Passo 3: Configurar o Web Service

**Configurações Básicas:**
- **Name:** `skyscanner-bot-api` (ou nome de sua escolha)
- **Environment:** `Python 3`
- **Region:** Escolha a região mais próxima
- **Branch:** `main`

**Configurações de Build:**
- **Build Command:** 
  ```
  pip install -r requirements.txt && playwright install chromium
  ```
- **Start Command:** 
  ```
  python src/main.py
  ```

**Configurações Avançadas:**
- **Auto-Deploy:** `Yes` (para deploy automático em push)

### Passo 4: Variáveis de Ambiente (Opcional)

Se você quiser configurar variáveis de ambiente:

1. Na seção "Environment Variables", adicione:
   - `FLASK_ENV`: `production`
   - `PORT`: `5000` (se necessário)

### Passo 5: Deploy

1. Clique em "Create Web Service"
2. O Render iniciará o processo de build e deploy
3. Aguarde a conclusão (pode levar 5-10 minutos)

## Método 2: Deploy via Dockerfile

### Passo 1: Configurar Web Service

1. No Render Dashboard, clique em "New +" → "Web Service"
2. Conecte o repositório GitHub
3. Selecione "Docker" como Environment

### Passo 2: Configurações Docker

- **Dockerfile Path:** `Dockerfile` (padrão)
- **Docker Build Context:** `.` (raiz do projeto)

### Passo 3: Deploy

O Render usará automaticamente o Dockerfile incluído no projeto.

## Verificação do Deploy

### 1. Verificar Status

1. No dashboard do Render, verifique se o status está "Live"
2. Clique no link do serviço para acessar a URL pública

### 2. Testar a API

Use a URL fornecida pelo Render para testar:

```bash
# Health Check
curl https://seu-app.onrender.com/api/flights/health

# Busca de voos
curl -X POST https://seu-app.onrender.com/api/flights/search \\
  -H "Content-Type: application/json" \\
  -d '{
    "origin": "MXP",
    "destination": "AMS",
    "departure_date": "2025-08-04",
    "return_date": "2025-08-08"
  }'
```

## Configurações Importantes

### 1. Timeout

O Render tem um timeout padrão de 30 segundos para requisições HTTP. Como o scraping pode demorar mais, considere:

- Implementar cache de resultados
- Usar processamento assíncrono
- Otimizar o scraping

### 2. Recursos

**Plano Gratuito:**
- 512 MB RAM
- 0.1 CPU
- 750 horas/mês
- Sleep após 15 minutos de inatividade

**Planos Pagos:**
- Mais recursos
- Sem sleep
- Domínio customizado

### 3. Logs

Para visualizar logs:
1. No dashboard, clique no seu serviço
2. Vá para a aba "Logs"
3. Monitore erros e performance

## Troubleshooting

### Erro: "Build failed"

**Possíveis causas:**
- Dependências em `requirements.txt` incorretas
- Erro na instalação do Playwright
- Falta de memória durante build

**Soluções:**
- Verifique o `requirements.txt`
- Use Dockerfile para mais controle
- Considere plano pago para mais recursos

### Erro: "Service unavailable"

**Possíveis causas:**
- Aplicação não está escutando na porta correta
- Erro no código Python
- Timeout durante inicialização

**Soluções:**
- Verifique se `app.run(host='0.0.0.0', port=5000)`
- Analise os logs para erros
- Teste localmente primeiro

### Erro: "Playwright browser not found"

**Possíveis causas:**
- Navegadores não instalados corretamente
- Dependências do sistema faltando

**Soluções:**
- Use o Dockerfile que inclui dependências do sistema
- Verifique o comando de build

## Monitoramento

### 1. Health Checks

O Render monitora automaticamente a saúde do serviço através do endpoint `/api/flights/health`.

### 2. Métricas

No dashboard você pode ver:
- CPU usage
- Memory usage
- Request count
- Response times

### 3. Alertas

Configure alertas para:
- Service down
- High error rate
- Resource usage

## Atualizações

### Deploy Automático

Com auto-deploy habilitado, toda vez que você fizer push para a branch `main`, o Render fará deploy automaticamente.

### Deploy Manual

1. No dashboard, clique no seu serviço
2. Clique em "Manual Deploy"
3. Selecione a branch/commit
4. Clique em "Deploy"

## Custos

### Plano Gratuito
- Adequado para testes e desenvolvimento
- Limitações de recursos e tempo

### Planos Pagos
- A partir de $7/mês
- Recursos dedicados
- Sem limitações de tempo
- Suporte prioritário

## Segurança

### 1. Variáveis de Ambiente

Nunca commite informações sensíveis no código. Use variáveis de ambiente para:
- Chaves de API
- Credenciais de proxy
- Configurações secretas

### 2. HTTPS

O Render fornece HTTPS automaticamente para todos os serviços.

### 3. Rate Limiting

Considere implementar rate limiting para evitar abuso da API.

## Suporte

- [Documentação do Render](https://render.com/docs)
- [Community Forum](https://community.render.com)
- [Status Page](https://status.render.com)

## Próximos Passos

Após o deploy bem-sucedido:

1. Configure monitoramento
2. Implemente cache para melhor performance
3. Adicione autenticação se necessário
4. Configure domínio customizado (planos pagos)
5. Implemente backup de dados se aplicável

