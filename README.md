# Agentic AI Customer Service Assistant on Databricks

An end-to-end Generative AI application that uses an LLM-powered AI agent to answer customer questions by retrieving information from both structured business data and unstructured documents.

The project brings together **LLMs, RAG, Vector Search, Unity Catalog, Model Serving, and Databricks Apps** to demonstrate how an AI agent can connect knowledge sources with a user-facing application.

## Architecture

```text
                 UNSTRUCTURED KNOWLEDGE
                  PDF Documents (500)
                          |
                    Text Chunking
                          |
                     Embeddings
                          |
                  Databricks Vector Search
                          |
                          v
                    +-----------+
                    |           |
                    | AI Agent  | ------> Model Serving
                    |  (LLM)    |                 |
                    |           |                 v
                    +-----------+          Databricks App
                          ^                       |
                          |                       v
                    Unity Catalog              End User
                      Functions
                          ^
                          |
                    STRUCTURED DATA
                       Delta Tables
```

## Key Components

### 1. Unstructured Knowledge Base

PDF documents provide product information and other customer-support knowledge.

Processing workflow:
- Extract text from PDF documents.
- Split the text into manageable chunks.
- Generate embeddings for semantic retrieval.
- Store and retrieve document content through a Databricks Vector Search index.
- Use retrieved content to provide context for LLM responses.

### 2. Structured Knowledge Base

Structured business data is stored in Delta Tables and accessed through Unity Catalog functions.

The agent can call the configured functions to retrieve relevant business information, such as customer service history and return policy details.

### 3. LLM-Powered AI Agent

The Databricks agent interprets a user's question and determines which configured tool can help answer it.

The agent integrates:
- **Vector Search** for retrieving relevant document content.
- **Unity Catalog functions** for accessing structured information.
- **LLM reasoning and tool calling** to coordinate retrieval and formulate responses.

### 4. Model Serving

The agent is exposed through a Databricks Model Serving endpoint so that the application can invoke it.

### 5. Databricks App

The application provides a user-facing interface for submitting questions and viewing the agent's responses.

## Technology Stack

- Databricks
- Large Language Models (LLMs)
- Generative AI and Agentic AI
- Python
- MLflow
- Databricks Vector Search
- Delta Lake
- Unity Catalog
- Model Serving
- Databricks Apps
- Retrieval-Augmented Generation (RAG)

## Example Use Cases

**Return policy questions**

Ask the agent about return policies and retrieve relevant information from the configured knowledge source.

**Product documentation search**

Ask about a product, such as the TechPro X200, and receive a response grounded in relevant documentation when that information is available.

**Customer service history**

Request a service-history summary using a test customer record available through the configured Unity Catalog function.

## Project Workflow

1. Prepare the source PDF documents.
2. Extract and process document content.
3. Generate embeddings and populate the Vector Search index.
4. Prepare structured data in Delta Tables.
5. Configure Unity Catalog functions.
6. Build the LLM-powered agent and connect its tools.
7. Register and deploy the agent through Model Serving.
8. Connect the endpoint to a Databricks App.
9. Test responses across document retrieval and structured-data use cases.

## Repository Structure

The repository may contain the following files, depending on your workspace setup:

```text
databricks-agentic-ai-customer-service/
├── app/
│   ├── app.py
│   └── app.yaml
├── agent.py
├── notebooks/
│   ├── Parse_PDF_Docs.py
│   ├── Enrich_PDF_Files.py
│   ├── Query_VS_index.py
│   └── Create_User_Defined_Functions.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup and Configuration

Before running the project, configure the required resources in your Databricks workspace:

1. Workspace access and compute.
2. Unity Catalog catalog, schema, tables, and function permissions.
3. Vector Search endpoint and index.
4. Required LLM serving endpoint.
5. MLflow model registration and Model Serving deployment.
6. Databricks App configuration and resource permissions.

Update resource names and configuration values to match your workspace. Do not include credentials or access tokens in source files.

## Testing

Example questions to test:

- What is the return policy?
- Find product documentation for laptops and summarize the key features of the TechPro X200.
- Can you summarize the service history for a test customer?

Validate that the agent calls the appropriate tool and returns a relevant response for each question.

## Security Considerations

- Never commit API keys, passwords, access tokens, or `.env` files.
- Use synthetic customer data in demonstrations.
- Apply Unity Catalog permissions according to least-privilege principles.
- Verify data access and endpoint permissions before deployment.
- Avoid exposing confidential business or customer information.

## Learning Objectives

This project explores how to connect data engineering foundations with modern GenAI application development, including document processing, semantic search, tool-calling agents, data governance, model deployment, and application integration.

---

**Note:** This repository documents the intended architecture. Actual resource names, deployment configuration, testing results, and production-readiness claims should be updated to reflect the implementation in your workspace.
