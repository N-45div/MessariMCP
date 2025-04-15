import requests
import io
import base64
import json
import statistics
import matplotlib.pyplot as plt
from typing import Dict, Any, List
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

@mcp.tool()
async def get_asset_details(message: str) -> str:
    """
    Get latest details about a cryptocurrency asset by its slug

    """
    url = f"https://api.messari.io/metrics/v2/assets/details?slugs={message}"
    headers = {
        "accept": "application/json",
        "x-messari-api-key": "API-KEY"
    }
    
    response = requests.get(url, headers=headers)
    response_data = json.loads(response.text)
    
    if "data" not in response_data or not response_data["data"]:
        return f"No data found for {message}"
    
    # Extract data for the first asset
    coin_data = response_data["data"][0]
    
    # Price history data
    price_history_data = [
        {"date": "24h ago", "price": coin_data["marketData"]["ohlcv24HourUsd"]["open"]},
        {"date": "now", "price": coin_data["marketData"]["priceUsd"]}
    ]
    
    # OHLC data
    ohlc_data = [
        {
            "period": "Last 24 Hours",
            "open": coin_data["marketData"]["ohlcv24HourUsd"]["open"],
            "high": coin_data["marketData"]["ohlcv24HourUsd"]["high"],
            "low": coin_data["marketData"]["ohlcv24HourUsd"]["low"],
            "close": coin_data["marketData"]["ohlcv24HourUsd"]["close"],
            "volume": coin_data["marketData"]["ohlcv24HourUsd"]["volume"]
        },
        {
            "period": "Last Hour",
            "open": coin_data["marketData"]["ohlcv1HourUsd"]["open"],
            "high": coin_data["marketData"]["ohlcv1HourUsd"]["high"],
            "low": coin_data["marketData"]["ohlcv1HourUsd"]["low"],
            "close": coin_data["marketData"]["ohlcv1HourUsd"]["close"],
            "volume": coin_data["marketData"]["ohlcv1HourUsd"]["volume"]
        }
    ]
    
    # ROI data
    roi_data = []
    for period, value in coin_data["returnOnInvestment"].items():
        roi_data.append({"period": period, "percent_change": value})
    
    close_prices = [entry["close"] for entry in ohlc_data]
    volatility = statistics.stdev(close_prices)
    
    # Create a structured result object
    result = {
        "asset_info": {
            "name": coin_data["name"],
            "symbol": coin_data["symbol"],
            "current_price": coin_data["marketData"]["priceUsd"],
            "market_cap": coin_data["marketData"]["marketcap"]["circulatingUsd"],
            "rank": coin_data["rank"],
            "category": coin_data["category"],
            "sector": coin_data["sector"]
        },
        "price_history": price_history_data,
        "ohlc_data": ohlc_data,
        "roi_data": roi_data,
        "volatility": volatility
    }
    
    # Return the data as a JSON string
    return json.dumps(result)

@mcp.tool()
async def get_trending_details(classes: str) -> str:
    """
    Get latest trending topics with X posts for better engagement in the crypto world.

    Args:
        classes (str): Comma-separated list of topic classes to filter trends (e.g., "Legal and Regulatory,Macro Commentary").

    Returns:
        str: JSON string containing trending topics, summaries, references, and relevant X posts.
    """
    url = f"https://api.messari.io/signal/v0/topics/global/current?sort=trending&classes={classes}"
    headers = {
        "accept": "application/json",
        "x-messari-api-key": "YOUR-API-KEY-HERE"  # Replace with your actual Messari API key
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        response_data = response.json()
    except requests.RequestException as e:
        return json.dumps({"error": f"Failed to fetch data: {str(e)}"})

    if "data" not in response_data or not response_data["data"]:
        return json.dumps({"error": "No data found for the prompt"})
    
    trend_data_list = response_data["data"]
    result = {"Top Trending in Crypto Market": []}
    
    # Process the list of trending topics
    for trend_data in trend_data_list:
        # Prioritize title, summary, and headline (content)
        trending_item = {
            "Title": trend_data.get("title", "No title"),
            "Summary": trend_data.get("summary", "No summary"),
            "Headline": trend_data.get("content", "No content")
        }
        
        # Extract only the top 2 references from topDocuments
        references = []
        x_posts = []
        if "topDocuments" in trend_data and trend_data["topDocuments"]:
            # Limit to top 2 documents for references
            top_docs = trend_data["topDocuments"][:2]
            for doc in top_docs:
                doc_type = doc.get("type", "Unknown")
                url = doc.get("url", "No URL")
                references.append({
                    "url": url,
                    "type": doc_type
                })
                # If the document is an X post, add it to the x_posts list
                if doc_type == "x_post":
                    x_posts.append({
                        "url": url,
                        "content": "Content not directly available via API; visit the URL for details."
                    })
        
        trending_item["References"] = references
        if x_posts:
            trending_item["Related X Posts"] = x_posts
        
        # Add rank information if available
        if "rank" in trend_data:
            trending_item["Rank"] = trend_data["rank"]
        
        # Add the primary symbol if available
        if "assets" in trend_data and trend_data["assets"] and len(trend_data["assets"]) > 0:
            trending_item["Symbol"] = trend_data["assets"][0].get("symbol", "Unknown")
        
        result["Top Trending in Crypto Market"].append(trending_item)
    
    return json.dumps(result, indent=2)
    
if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
