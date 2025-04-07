import requests
from typing import Any
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("crimedetect")

@mcp.tool()
async def get_research(message: str) -> str:
    """
    Get latest news about the recent crime detective news on various blockchains
    
    """
    url = "https://api.messari.io/ai/v1/chat/completions"
    payload = {
        "messages": [
            {"role": "user", "content": message}
        ],
        "verbosity": "verbose",
        "response_format": "markdown",
        "inline_citations": True,
        "stream": False
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-MESSARI-API-KEY": "API-KEY"
    }
    response = requests.post(url, json=payload, headers=headers)
    
    return response.text

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
