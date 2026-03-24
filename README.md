# 🎬 Recomendador de Filmes

[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=3776AB)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green?style=for-the-badge&logo=fastapi&logoColor=009688)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Render](https://img.shields.io/badge/Render-Deployed-blue?style=for-the-badge&logo=render)](https://render.com/)
[![GitHub stars](https://img.shields.io/github/stars/Ronbragaglia/recomendador-filmes?style=social)](https://github.com/Ronbragaglia/recomendador-filmes/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Ronbragaglia/recomendador-filmes?style=social)](https://github.com/Ronbragaglia/recomendador-filmes/network/members)

🔹 Um sistema de recomendação de filmes utilizando FastAPI, Machine Learning e hospedado no Render.

## ✨ Funcionalidades

### 🎯 Core
- **Recomendação de Filmes**: Sistema inteligente que sugere filmes baseados em preferências do usuário
- **API RESTful**: Endpoints para obter recomendações
- **Machine Learning**: Modelos treinados com datasets populares (MNIST, California Housing, Ancombe)
- **Personalização**: Recomendações adaptadas ao perfil do usuário
- **Algoritmos Múltiplos**: Suporte a diferentes estratégias de recomendação

### 🚀 Performance
- **FastAPI**: Framework assíncrono de alta performance
- **Cache**: Sistema de cache para respostas rápidas
- **Otimização**: Modelos otimizados para inferência rápida
- **Escalabilidade**: Arquitetura preparada para escala

### 📊 Analytics
- **Métricas**: Monitoramento de performance e uso
- **Logging**: Sistema de logs detalhado
- **A/B Testing**: Suporte para testar diferentes algoritmos
- **Feedback**: Coleta de feedback dos usuários

## 🛠️ Tecnologias Utilizadas

### Backend
- **Python 3.11+**: Linguagem principal
- **FastAPI**: Framework web moderno e rápido
- **Pydantic**: Validação de dados com type hints
- **scikit-learn**: Biblioteca de Machine Learning
- **NumPy/Pandas**: Processamento de dados
- **SQLite**: Banco de dados leve

### Deploy
- **Render**: Plataforma de hospedagem
- **Docker**: Suporte a containers
- **GitHub Actions**: CI/CD automatizado

### Development
- **Poetry**: Gerenciamento de dependências
- **pytest**: Framework de testes
- **Black**: Formatação de código
- **mypy**: Verificação de tipos

## 🚀 Como Usar

### Instalação Local

```bash
# Clone o repositório
git clone https://github.com/Ronbragaglia/recomendador-filmes.git

# Entre no diretório
cd recomendador-filmes

# Instale as dependências
pip install -r requirements.txt

# Ou use Poetry (recomendado)
poetry install
```

### Executar Localmente

```bash
# Execute a API
python app.py

# Ou use uvicorn para produção
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### Testar a API

#### Via Python
```python
import requests

response = requests.get("http://localhost:8000/")
print(response.json())
# Output: {"message": "API funcionando corretamente!"}

# Obter recomendações
response = requests.post(
    "http://localhost:8000/recommendations/",
    json={"user_id": 1, "num_recommendations": 5}
)
print(response.json())
# Output: {"user_id": 1, "recommendations": ["Filme 1", "Filme 2", ...]}
```

#### Via cURL
```bash
# Testar endpoint raiz
curl http://localhost:8000/

# Obter recomendações
curl -X POST http://localhost:8000/recommendations/ \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1, "num_recommendations": 5}'
```

#### Via Postman
1. Importe a coleção fornecida
2. Configure o ambiente
3. Teste os endpoints

### Testar no Google Colab

[![Abrir no Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ronbragaglia/recomendador-filmes/blob/main/recomendador_filmes.ipynb)

Clique no botão acima para abrir o notebook no Google Colab e testar a API sem instalar nada!

## 📚 Documentação da API

### Endpoints

#### GET `/`
**Descrição**: Verifica se a API está funcionando

**Resposta**:
```json
{
  "message": "API funcionando corretamente!"
}
```

#### POST `/recommendations/`
**Descrição**: Obtém recomendações de filmes para um usuário

**Request Body**:
```json
{
  "user_id": 1,
  "num_recommendations": 5
}
```

**Parâmetros**:
- `user_id` (int, obrigatório): ID do usuário
- `num_recommendations` (int, obrigatório): Número de recomendações desejadas (1-20)

**Resposta**:
```json
{
  "user_id": 1,
  "recommendations": [
    "Filme 1",
    "Filme 2",
    "Filme 3",
    "Filme 4",
    "Filme 5"
  ]
}
```

**Códigos de Status**:
- `200`: Sucesso
- `400`: Requisição inválida
- `500`: Erro interno do servidor

## 🔧 Configuração

### Variáveis de Ambiente

```bash
# Configurações da API
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True

# Configurações de ML
MODEL_PATH=./models/
CACHE_TTL=3600
MAX_RECOMMENDATIONS=20

# Configurações de Banco de Dados
DATABASE_URL=sqlite:///./movies.db
```

### Arquivo de Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
# API
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=False

# Machine Learning
MODEL_TYPE=collaborative
CACHE_ENABLED=True
CACHE_TTL=3600

# Database
DATABASE_URL=sqlite:///./movies.db
```

## 🧪 Testes

### Executar Testes

```bash
# Execute todos os testes
pytest

# Execute com cobertura
pytest --cov=app --cov-report=html

# Execute testes específicos
pytest tests/test_api.py
pytest tests/test_ml.py
```

### Estrutura de Testes

```
tests/
├── test_api.py          # Testes da API
├── test_ml.py           # Testes de Machine Learning
├── test_integration.py   # Testes de integração
└── conftest.py         # Configuração dos testes
```

## 📊 Datasets Utilizados

### MNIST
- **Descrição**: Dataset de dígitos manuscritos
- **Uso**: Reconhecimento de padrões
- **Tamanho**: 60,000 imagens de treinamento
- **Localização**: `sample_data/mnist_train_small.csv`, `sample_data/mnist_test.csv`

### California Housing
- **Descrição**: Preços de casas na Califórnia
- **Uso**: Regressão e previsão
- **Tamanho**: 20,640 exemplos de treinamento
- **Localização**: `sample_data/california_housing_train.csv`, `sample_data/california_housing_test.csv`

### Ancombe's Dataset
- **Descrição**: Dados demográficos
- **Uso**: Classificação e análise
- **Tamanho**: 1,746 exemplos
- **Localização**: `sample_data/anscombe.json`

## 🐛 Troubleshooting

### Problemas Comuns

#### API não inicia
```bash
# Verifique se a porta está em uso
netstat -ano | grep :8000

# Verifique se há processos Python
ps aux | grep python

# Tente outra porta
API_PORT=8001 python app.py
```

#### Erro de importação
```bash
# Reinstale as dependências
pip install --upgrade -r requirements.txt

# Ou use ambiente virtual
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Modelo não carrega
```bash
# Verifique se os arquivos de modelo existem
ls -la models/

# Verifique o caminho no arquivo de configuração
cat .env | grep MODEL_PATH

# Re-treine o modelo se necessário
python scripts/train_model.py
```

## 📈 Roadmap

### Versão 1.0 (Atual)
- ✅ API básica de recomendação
- ✅ Suporte a múltiplos datasets
- ✅ Deploy no Render

### Versão 1.1 (Próximo)
- [ ] Sistema de autenticação
- [ ] Recomendações baseadas em histórico
- [ ] Filtros por gênero, ano, etc.
- [ ] Sistema de avaliação (likes/dislikes)
- [ ] Cache distribuído com Redis

### Versão 2.0 (Futuro)
- [ ] Interface web completa
- [ ] Integração com APIs de filmes (TMDB, IMDB)
- [ ] Sistema de recomendação híbrido (collaborative + content-based)
- [ ] Dashboard de analytics
- [ ] A/B testing automático
- [ ] Exportação de modelos para ONNX

## 🤝 Contribuindo

### Como Contribuir

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/minha-feature`)
3. Faça suas mudanças
4. Commit suas mudanças (`git commit -m 'feat: adiciona nova feature'`)
5. Push para a branch (`git push origin feature/minha-feature`)
6. Abra um Pull Request

### Diretrizes

- Siga o PEP 8 para código Python
- Use type hints em todas as funções
- Escreva testes para novas funcionalidades
- Atualize a documentação
- Mantenha os commits pequenos e focados

### Reportar Bugs

Encontrou um bug? Por favor, abra uma issue no [GitHub Issues](https://github.com/Ronbragaglia/recomendador-filmes/issues) com:
- Descrição detalhada
- Passos para reproduzir
- Comportamento esperado
- Comportamento atual
- Ambiente (Python, OS, etc.)

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

Desenvolvido por [Rone Bragaglia](https://github.com/Ronbragaglia)

## 🙏 Agradecimentos

- [FastAPI](https://fastapi.tiangolo.com/) pelo excelente framework
- [scikit-learn](https://scikit-learn.org/) pela biblioteca de ML
- [Render](https://render.com/) pela hospedagem gratuita
- Comunidade Python pelas contribuições

---

**⭐ Se este projeto foi útil para você, considere dar uma estrela no GitHub!**

[![GitHub Repo](https://img.shields.io/badge/GitHub-recomendador--filmes-brightgreen?style=for-the-badge&logo=github)](https://github.com/Ronbragaglia/recomendador-filmes)
