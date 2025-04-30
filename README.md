# Messari Influencer Mindshare and Asset Analysis

This repository contains a Python script for analyzing mindshare data of cryptocurrency assets using the Messari API. The script fetches mindshare data, performs anomaly detection, visualizes trends, and provides insights into significant spikes in attention for a given asset. The analysis is tailored for use in Google Colab, with plotting and readable insights displayed directly in the notebook.

---

## Overview

The script provides a function, `analyze_asset_mindshare`, which retrieves mindshare data for a specified cryptocurrency asset (e.g., `official-trump` for $TRUMP, `mantra-dao` for $OM) from the Messari API. It processes the data to:

- Detect anomalies in mindshare scores using z-scores.
- Plot the mindshare scores over time with anomalies highlighted.
- Provide concise insights into trends and anomalies.

The script also includes a related server implementation (MCP Server) for broader integration.

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
## 🚀 Running the MCP Server

The MCP Server provides a backend for broader mindshare comparison functionality.

- Navigate to the server code: `server.py`
- Ensure the Messari API key is configured correctly.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Messari**: For providing the API.
- **Google Colab**: For enabling interactive visualization.
- **Mistral AI**: For optional sentiment integration.
