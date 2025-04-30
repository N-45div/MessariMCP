# Messari Influencer Mindshare and Asset Analysis

This repository contains a Python script for analyzing mindshare data of cryptocurrency assets using the Messari API. The script fetches mindshare data, performs anomaly detection, visualizes trends, and provides insights into significant spikes in attention for a given asset. The analysis is tailored for use in Google Colab, with plotting and readable insights displayed directly in the notebook.

---

## Overview

The Python script provides several functions to facilitate mindshare analysis for both cryptocurrency assets and Key Opinion Leaders (KOLs) on social media platforms like Twitter. Below is a description of each function:

---

#### `call_mistral`

- **Purpose**: Interacts with the Mistral API to perform **sentiment analysis** on text data (e.g., summaries of trending topics).
- **Returns**: A JSON object with the sentiment (`positive`, `negative`, or `neutral`) and an insight into how the topic may influence crypto market attention.
- **Features**:
  - Includes **retry logic** for handling rate limits.
  - Caches responses to **avoid redundant API calls**.
- **Used In**: KOL mindshare analysis to explain **anomalies** by sentiment-analyzing related trending topics.

---

#### `get_trending_details`

- **Purpose**: Fetches **trending topics** from the Messari API within a given date range and topic classes (e.g., `"Macro Commentary, Project Announcements, Legal and Regulatory"`).
- **Returns**: A dictionary of trending topics for the specified criteria.
- **Used For**: Providing context for **mindshare anomalies** in the KOL analysis by correlating spikes with relevant market news and events.

---

#### `analyze_mindshare_data`

- **Purpose**: Retrieves **mindshare data** for a specific Twitter handle (e.g., `@AltcoinGordon`) from the Messari API.
- **Processes**:
  - Detects **anomalies** in mindshare scores using **z-scores** (default threshold: `2.0`).
  - **Plots** mindshare scores over time with anomalies **highlighted in red**.
  - Provides insights on:
    - **Trends** (upward/downward/stable)
    - **Score and rank ranges**
    - **List of anomalies**
  - Uses `call_mistral` + `get_trending_details` to add **sentiment + market explanation** to detected anomalies.
- **Display**: Results are shown **directly in Google Colab**.
- **Best For**: KOL mindshare tracking and insight generation.

---

#### `analyze_asset_mindshare`

- **Purpose**: Retrieves **mindshare data** for a specific cryptocurrency asset (e.g., `official-trump` for $TRUMP, `mantra-dao` for $OM).
- **Processes**:
  - Detects **anomalies** in asset mindshare scores using **z-scores** (default threshold: `2.0`).
  - **Plots** scores over time with anomalies **highlighted in orange**.
  - Provides concise insights about:
    - **Mindshare trends**
    - **Score and rank ranges**
    - **Anomaly dates and scores**
- **Display**: Designed to work **directly in Google Colab** for interactive visual exploration.
- **Best For**: Analyzing market attention shifts for individual crypto assets.

---

## 🚀 Running the MCP Server

The MCP Server provides a backend for broader mindshare comparison functionality.

- Navigate to the server code: `server.py`
- Ensure the Messari API key is configured correctly.

---

## API List

The following APIs are used in this project:

- **Copilot Agent API**
- **Current Topics API**
- **X-Users Mindshare Over Time API**
- **Mindshare of Asset Over Time API**
- **Asset Details API**

---

## 🔑 Key Features

- **Mindshare Data Fetching**: Uses the Messari API to retrieve daily mindshare data for assets.
- **Anomaly Detection**: Identifies significant spikes in mindshare scores using a z-score threshold (default: 2.0).
- **Visualization**: Plots mindshare scores over time with anomalies highlighted in Google Colab.
- **Insights**: Provides readable insights about trends, score ranges, rank ranges, and anomalies.
- **Extensible**: Designed to work alongside KOL mindshare analysis (e.g., for Twitter handles) with potential for combined analysis.

---

## 📂 Code Links in the repository

- **Colab Notebook**: [LLM_Mindshare_asset_analysis.ipynb](https://github.com/N-45div/MessariMCP/blob/main/colab/LLM_Mindshare_asset_analysis.ipynb)
- **MCP Server Code**: [server.py](https://github.com/N-45div/MessariMCP/blob/main/server.py)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Messari**: For providing the API.
- **Google Colab**: For enabling interactive visualization.
- **Mistral AI**: For optional sentiment integration.
