# Sistema de Monitoramento Industrial

## 📌 Visão Geral

Sistema de monitoramento industrial que integra aquisição de dados de CLP, processamento em backend Python e visualização em dashboard web com atualização em tempo real.

Coleta dados em tempo real de um CLP Siemens via protocolo S7, processa através de uma API REST, persiste em banco de dados e exibe em um dashboard web com gráficos e alertas automáticos.

---

## 🏗️ Arquitetura

```
CLP (PLCSIM Advanced)
    ↓
Collector (Snap7 / S7 Protocol)
    ↓
Flask API (porta 5000)
    ↓
SQLite Database
    ↓
Django Dashboard (porta 8000)
```

---

## ⚙️ Tecnologias

* Python
* Flask (API de ingestão de dados)
* Django (Dashboard web)
* SQLite (Banco de dados)
* python-snap7 (Comunicação com CLP via protocolo S7)
* Requests (Comunicação HTTP entre collector e API)
* Chart.js (Gráficos em tempo real no dashboard)

---

## 🚀 Funcionalidades

### 🔌 Aquisição de Dados

* Leitura em tempo real do CLP (temperatura, pressão, status)
* Comunicação via protocolo S7 (Snap7)
* Reconexão automática em caso de perda de comunicação
* Envio de status `COMM ERROR` quando o CLP fica inacessível

### 🧠 Processamento Backend

* API REST para recebimento de dados (`POST /data`)
* Persistência dos dados em SQLite
* Detecção de alertas (`GET /alerts`)
* Validação de campos e tipos de dados

### 📊 Dashboard Web

* Atualização automática a cada 3 segundos
* Cards com valores em tempo real (temperatura, pressão, status, total de alertas)
* Gráficos de linha com histórico das últimas 30 leituras
* Tabela com as últimas 15 leituras
* Destaque visual para registros em estado de alerta

### ⚠️ Alertas

Disparados quando:

* `temperature > 80`
* `status = ERROR`
* `status = COMM ERROR` (falha de comunicação com o CLP)

---

## 📁 Estrutura do Projeto

```
monitoramento-industrial/
│
├── api/
│   ├── app.py          # Inicialização da aplicação Flask
│   ├── routes.py       # Endpoints da API
│   ├── services.py     # Formatação dos dados
│   └── database.py     # Conexão e queries SQLite
│
├── collector/
│   └── plc_reader.py   # Leitura do CLP via Snap7
│
├── dashboard/
│   ├── core/           # Configurações Django
│   └── monitor/        # App de monitoramento
│       ├── models.py
│       ├── views.py
│       ├── admin.py
│       └── templates/
│           └── monitor/
│               └── dashboard.html
│
├── database/
│   └── database.db     # Banco de dados SQLite
│
├── venv/               # Ambiente virtual
└── start.bat           # Inicializa todos os serviços
```

---

## ▶️ Como Executar

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Iniciar todos os serviços

```bash
start.bat
```

Isso irá iniciar:

* Flask API (porta 5000)
* Collector do CLP
* Django Dashboard (porta 8000)

### 3. Acessar o sistema

* Dashboard: `http://127.0.0.1:8000`
* API: `http://127.0.0.1:5000`
* Django Admin: `http://127.0.0.1:8000/admin`

Para acessar em rede local:

```bash
python manage.py runserver 0.0.0.0:8000
```

---

## 📡 Endpoints da API

### POST /data

Recebe leitura do CLP:

```json
{
  "temperature": 85.3,
  "pressure": 5.2,
  "status": "RUN"
}
```

Em caso de falha de comunicação com o CLP:

```json
{
  "temperature": null,
  "pressure": null,
  "status": "COMM ERROR"
}
```

### GET /data

Retorna todos os dados armazenados.

### GET /alerts

Retorna registros anômalos com base nas regras:

* `temperature > 80`
* `status = ERROR`
* `status = COMM ERROR`

---

## 🔧 Integração com CLP

* Testado com Siemens PLCSIM Advanced
* Comunicação via Snap7 (protocolo S7)
* Leitura do DB1, offset 0, 10 bytes:
  * Bytes 0–3: temperatura (REAL, big-endian)
  * Bytes 4–7: pressão (REAL, big-endian)
  * Bytes 8–9: status (INT, big-endian)
* Requisitos no TIA Portal:
  * DB não otimizado
  * PUT/GET habilitado

---

## 🎯 Objetivo

Este projeto demonstra:

* Integração entre automação industrial e desenvolvimento de software
* Aquisição de dados em tempo real via protocolo S7
* Desenvolvimento de API REST com Flask
* Visualização de dados em tempo real com Django e Chart.js
* Tratamento de falhas de comunicação industrial

---

## 🚀 Possíveis Melhorias Futuras

* WebSocket para atualização sem polling
* Sistema de autenticação
* Migração para PostgreSQL
* Containerização com Docker
* Exportação de relatórios em PDF
