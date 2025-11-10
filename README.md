# 🚚 Rota Inteligente – Otimização de Entregas com IA

## 📘 1. Descrição do Problema
O desafio consiste em otimizar as rotas de entrega de uma empresa (exemplo: Sabor Express), reduzindo o tempo total percorrido e agrupando pedidos próximos.  
A solução usa técnicas de **Inteligência Artificial e Grafos**, simulando um sistema básico de **Planejamento de Rotas Inteligentes**.

## 🎯 Objetivos
- Representar o mapa como um grafo (nós = locais, arestas = conexões).
- Calcular rotas mínimas usando o algoritmo **A\***.
- Agrupar entregas próximas usando **K-Means**.
- Gerar um **diagrama visual** das rotas e clusters.

## 🚀 Execução
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
bash scripts/run_demo.sh
```
Resultados e diagramas são salvos em `docs/outputs/`.
