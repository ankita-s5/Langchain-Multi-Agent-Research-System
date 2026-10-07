# Langchain Multi-Agent Research System

A Python-based research assistant powered by LangChain and LLMs to search the web, extract relevant information from sources, draft a structured report, and critique the result before returning it to the user.

The application combines multiple specialized agents to mimic a research workflow: search for sources, read the best candidate pages, synthesize findings into a report, and then evaluate the output for quality.

## Features

- Multi-agent research workflow using LangChain agents
- Web search via Tavily
- Source scraping and content extraction via requests + trafilatura + readability
- Structured report generation with Gemini/OpenAI-compatible models
- Critical review step to score and refine the output
- Interactive UI built with Streamlit

## Tech Stack

- Python 3.10+
- Streamlit for the frontend experience
- LangChain + LangChain Core for orchestration and agent tooling
- Google Gemini via `langchain-google-genai`
- Tavily API for search
- BeautifulSoup, readability-lxml, trafilatura for content extraction
- python-dotenv for environment configuration
- rich for terminal output

## Project Structure

```text
Langchain-Multi-Agent-Research-System/
├── app.py                  # Streamlit application entry point
├── main.py                 # Script-based research runner
├── requirements.txt        # Python dependencies
├── .env                    # Local environment variables (not committed in production)
├── src/
│   ├── agents/
│   │   └── agents.py       # Search agent, reader agent, writer chain, critic chain
│   ├── pipelines/
│   │   └── pipeline.py     # End-to-end research workflow orchestration
│   ├── tools/
│   │   └── tools.py        # Tavily search and scraping utilities
│   └── __init__.py
├── demo.excalidraw        # UI / architecture mockup
├── LICENSE
└── README.md
```

## Brief Architecture

The system follows a simple agent pipeline:

1. Search Agent
   - Uses Tavily to find recent and relevant web sources.
   - Returns summarized search results with titles, URLs, and snippets.

2. Reader Agent
   - Selects the most useful URL from search results.
   - Scrapes the content and extracts readable text using multiple fallback strategies.

3. Writer Chain
   - Combines the search result and scraped content.
   - Produces a structured, professional research report.

4. Critic Chain
   - Reviews the generated report.
   - Outputs a score, strengths, improvement suggestions, and a verdict.

5. Streamlit UI
   - Presents the research workflow in a user-friendly interface.
   - Lets users submit a topic and review the generated results.

## Installation

### 1) Clone the repository

```bash
git clone https://github.com/ankita-s5/Langchain-Multi-Agent-Research-System.git
cd Langchain-Multi-Agent-Research-System
```

### 2) Create a virtual environment

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

### 4) Configure environment variables

Create a `.env` file in the project root with the following variables:

```env
GEMINI_API_KEY=your_google_gemini_api_key
tavily_APIKEY=your_tavily_api_key
```

You can obtain:
- a Gemini API key from Google AI Studio
- a Tavily API key from the Tavily dashboard

## Running the App

### Streamlit app

```bash
streamlit run app.py
```

This launches the interactive research assistant in your browser.

### Script-based execution

```bash
python main.py
```

This runs a single research pipeline using a sample topic.

## Example Usage

In the Streamlit app, enter a research topic such as:

```text
The impact of AI on the job market in 2026
```

The app will:
- search the web,
- read the relevant source,
- generate a structured report,
- provide a critique with a score.

## Notes

- The project is designed for research and experimentation with agent-based workflows.
- The scraping layer may vary in reliability depending on website structure and anti-bot protections.
- For production use, consider adding caching, retry logic, rate limiting, and output validation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
