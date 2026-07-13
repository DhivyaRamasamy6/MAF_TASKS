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

---
## 7. Tool Schema and Tool Description Quality Testing

Evaluated how tool metadata affects the agent's ability to select and invoke the correct tool.

### Practiced

- Created tools with poor and improved descriptions
- Compared tool selection accuracy
- Tested the impact of:
  - Tool name
  - Tool description
- Observed how descriptive metadata improves tool-calling reliability
---

---
## 8. Tool Calling Loop

Built a Customer Support Assistant capable of automatically selecting and invoking the appropriate tool based on the user's request.

### Implemented Tools

- `get_customer` – Retrieve customer information.
- `get_invoice` – Retrieve invoice details.
- `create_ticket` – Create a customer support ticket.

### Agent Responsibilities

- Identify the user's intent.
- Select the appropriate tool.
- Invoke the tool with the correct parameters.
- Use the tool's output to generate the final response.
- Avoid fabricating customer, invoice, or ticket information.

### Tesing 
Here tested with 20 related prompts and analyzed how the agent responses
---

---
## 9.Human Approval for Tools (Tool approval mode)

Built a **Leave Approval Agent** using **Microsoft Agent Framework** with **Tool Approval Mode (Human-in-the-Loop)**.

### Features
- Created a Leave Approval Assistant.
- Implemented `submit_leave_request` with `approval_mode="always_require"`
- Validated leave requests using Pydantic models.
- Paused tool execution until human approval was received.
- Resumed agent execution after approval and completed the workflow.
- Handled both approval and rejection scenarios

---

---
## 10.MCP Tool – HRMS Employee Lookup

### Objective

Build a small HRMS MCP (Model Context Protocol) server that exposes employee lookup tools and connect it to a Microsoft Agent Framework (MAF) agent.

### Features

- Created an MCP server using the Python MCP SDK.
- Connected the MCP server to a PostgreSQL database using SQLAlchemy.
- Implemented repository pattern for database operations.
- Exposed employee lookup functionality as MCP tools.
- Connected the MCP server to a Microsoft Agent Framework agent using `MCPStdioTool`.
- Enabled the agent to automatically discover and invoke MCP tools based on user requests.
---

---
## 11.Agent as a Tool

### Objective

Create a Manager Agent that delegates tasks to specialized agents by treating them as tools.

## Features

- Created a **Manager Agent** to coordinate multiple agents.
- Implemented a **Data Agent** for retrieving factual information.
- Implemented a **Writing Agent** for generating professional summaries and reports.
- Configured the Manager Agent to invoke the appropriate agent based on the user's request.
- Demonstrated the **Agent as a Tool** pattern in Microsoft Agent Framework.
---

---
## 12. Multi-turn Conversation and Session Management

### Objective

Implement multi-turn conversations using Microsoft Agent Framework sessions and manage conversation history. Start with the built-in **InMemoryHistoryProvider** for development, then redesign the solution to use **Redis** or **Cosmos DB** for production.

## Features

- Created and managed agent session.
- Maintained conversation context across multiple user interactions.
- Used the built-in `InMemoryHistoryProvider` to store chat history during development.
- Demonstrated session serialization and restoration using `to_dict()` and `from_dict()`.
- Integrated `RedisHistoryProvider` for persistent, shared conversation history.
---