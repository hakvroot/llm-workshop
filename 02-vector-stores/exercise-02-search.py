import openai
import os
import time
import httpx

vector_store_id="<TBD>"

# 1. Query the vector store
def _get_headers():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set.")
    return {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}


def vector_store_search(vector_store_id, query, filters=None, max_num_results=10, rewrite_query=False):
    endpoint = f"https://api.openai.com/v1/vector_stores/{vector_store_id}/search"
    payload = {
        "query": query,
        "max_num_results": max_num_results,
        "rewrite_query": rewrite_query
    }
    if filters:
        payload["filters"] = filters

    response = httpx.post(endpoint, headers=_get_headers(), json=payload)
    response.raise_for_status()
    return response.json()

# 2. Display the results
