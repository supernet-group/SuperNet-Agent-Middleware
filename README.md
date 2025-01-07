# Supernet-Agent-Middleware

Supernet-Agent-Middleware is a middleware that connects Supernet-Agents backend with Supernet-AIOS fronend.

## 1. Structure

The middleware is divided into two parts:

- **supernet-agent-manager**: Support for user's agent management, including agent creation, deletion, model selection, and agent query.

- **supernet-agent-client**: Support for single agent configuration, including prompt setting, model's parameter setting, and agent's function call.

## 2. Usage

**dev**
```
uvicorn main:app --reload
```