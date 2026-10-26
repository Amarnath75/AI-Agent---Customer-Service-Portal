# Databricks notebook source
# DBTITLE 1,Query the product docs vector index
from databricks.sdk import WorkspaceClient

# The standalone databricks.vector_search package is not available on this compute.
# The pre-installed Databricks SDK provides the same query API and authenticates
# automatically with notebook credentials (no service principal env vars needed).
w = WorkspaceClient()

results = w.vector_search_indexes.query_index(
    index_name="agentic_catalog.agentic_schema.product_docs_index",
    columns=["indexed_doc", "product_id"],
    query_text="Where i can find tutorial for AccountEase Pro",
    query_type="HYBRID",
    num_results=3,
)

display(results)