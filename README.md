# Microsoft Agent Framework (MAF) – Practice

## Overview

This repository contains my hands-on practice with the Microsoft Agent Framework (MAF). 

---

## Topics Covered

### 1. Development Environment Setup

Configured the local development environment for building AI agents.

#### Setup Included

- Python virtual environment
- Required dependencies installation
- Environment variable configuration
- Azure credentials setup

#### Technologies

- Python
- FastAPI
- Microsoft Agent Framework
- Azure AI Foundry
- VS Code

---

### 2. First Simple Agent

Created a basic conversational agent.

- Agent creation
- Agent initialization
- Sending prompts
- Receiving responses
- Running an agent locally


---

### 3. Model Providers and Service Connectors

Integrated different model providers with the agent.

#### Practiced

- Azure AI Foundry,OpenAI,Ollama providers
- FoundryChatClient,OpenAIChatClient,OllamaChatClient

---

### 4. Agent Instructions and Role Design

Designed specialized agents by defining clear instructions.

#### Practiced

- Agent roles
- Business context
- System instructions
- Behavior boundaries
- Scope control
- Response format
- Refusal rules
- Tone definition

Example Roles

- HR Assistant
- Finance Assistant
- Data Engineering Assistant

---

---
### 5. Running Agents

Implemented both Non-streaming and streaming responses.

#### Non-Streaming
Waits for the complete response before returning.

#### Streaming

Returns the response token by token.

Integrated streaming using
- FastAPI StreamingResponse
- text/plain
---


---
## 6. Tool Calling – Order Status Agent

Built an Order Status Assistant that uses a custom tool to retrieve the status of an order.

### Practiced

- Creating custom tools using `@tool`
- Registering tools with an agent
- Tool invocation by the LLM
- Integrating tool-enabled agents with FastAPI
---








