# Gemini CLI LLM

## Description
Gemini CLI LLM is a command-line interface for interacting with the Gemini API to generate content using a local large language model (LLM). This project provides a simple way to leverage the capabilities of the Gemini API directly from your terminal.

## Project Summary

### Core Components
- **Main Application** (`src/main.py`): CLI interface with command support for input, context, and summarization
- **AI Agent** (`src/utils/agent.py`): Implements GeminiAgent class with response generation, context awareness, and history tracking
- **Configuration** (`src/config/settings.py`): Manages API keys and base settings
- **Helper Functions** (`src/utils/helpers.py`): Handles request formatting, response parsing, and error management

### Current Features
✅ Implemented:
- Basic API integration
- Context-aware prompting
- Conversation history
- Text summarization
- Token usage tracking
- Unit testing foundation

### Technical Stack
- Python's `requests` library for API calls
- Type hints for code quality
- In-memory conversation history
- Token usage logging
- Unit tests with `unittest`

### Usage Examples
```bash
# Basic usage
python src/main.py --input "What is machine learning?"

# With context
python src/main.py --input "What are vectors?" --context "Machine learning concepts"

# Text summarization
python src/main.py --input "Long text here" --summarize
```

## Installation Instructions
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/gemini-cli.git
   cd gemini-cli
   ```
2. Set up a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Replace the placeholder API key in `src/config/settings.py` with your actual Gemini API key.


## Project Structure
- `src/main.py`: The entry point of the CLI application. It handles command-line arguments, sets up the API request to the Gemini API, and processes the response.
- `src/utils/helpers.py`: Contains utility functions that assist with tasks such as formatting the API request and parsing the response from the Gemini API.
- `src/utils/agent.py`: Implements the GeminiAgent class that handles advanced features like context-aware prompting, conversation history, and text summarization.
- `src/config/settings.py`: Stores configuration settings, including the API key and any other necessary parameters for connecting to the Gemini API.
- `tests/`: Contains test scripts to validate the functionality of the application, including unit tests for utility functions and integration tests for the main application.
- `.gitignore`: Specifies files and directories that should be ignored by Git, such as sensitive information like API keys and virtual environment folders.
- `requirements.txt`: Lists the Python dependencies required for the project, including libraries for making HTTP requests and handling JSON data.
- `README.md`: Comprehensive documentation for the project, explaining its purpose, setup, usage instructions, and next steps for further development.

## Advanced Features

### Context-Aware Prompting
The CLI now supports context-aware prompting to get more precise responses:
```bash
python src/main.py --input "What are vectors?" --context "Machine learning concepts"
```

### Text Summarization
Summarize long texts using the summarization feature:
```bash
python src/main.py --input "Your long text here" --summarize
```

### Conversation History
The CLI maintains a history of interactions, including:
- Prompts
- Responses
- Timestamps

## Roadmap

1. **Add Unit Tests**
   - Write unit tests for utility functions and the main logic using `pytest` or `unittest`.
   - **Status:** 🚧 Under Development

2. **Improve Error Handling**
   - Add robust error handling for API timeouts, invalid API keys, and malformed responses.
   - **Status:** ❌ Not Started

3. **Support Multiple Commands**
   - Add commands like `--history` to view past token usage, `--reset` to clear logs, or `--config` to update the API key.
   - **Status:** ❌ Not Started

4. **Add Configuration Management**
   - Replace `settings.py` with a `.env` file and use `python-dotenv` for better security.
   - **Status:** ❌ Not Started

5. **Add Logging**
   - Use Python's `logging` module to log API requests, responses, and errors for debugging.
   - **Status:** ❌ Not Started

6. **Token Usage Analytics**
   - Parse the `token_usage.txt` file to calculate total tokens used over time and display usage statistics.
   - **Status:** ❌ Not Started

7. **Interactive Mode**
   - Add an interactive mode where users can input prompts continuously without restarting the script.
   - **Status:** ❌ Not Started

8. **Dockerize the Project**
   - Create a `Dockerfile` to containerize the application for easier deployment.
   - **Status:** ❌ Not Started

9. **Add a Web Interface**
   - Use Flask or FastAPI to create a web interface for the CLI.
   - **Status:** ❌ Not Started

10. **Integrate with Other APIs**
    - Extend the project to integrate with other APIs, such as summarization, translation, or sentiment analysis.
    - **Status:** ❌ Not Started

11. **Package as a Python Library**
    - Refactor the project into a Python package and add a `setup.py` file for distribution.
    - **Status:** ❌ Not Started

12. **Add Documentation**
    - Expand the `README.md` and use tools like Sphinx to generate detailed documentation.
   - **Status:** ❌ Not Started

13. **Optimize for Performance**
    - Add caching for repeated prompts using `functools.lru_cache` or a database like SQLite.
    - **Status:** ❌ Not Started

14. **Publish to GitHub**
    - Publish the project to GitHub, add a license, and encourage contributions from the open-source community.
   - **Status:** ❌ Not Started

## New Features Status
- ✅ Context-Aware Prompting
- ✅ Conversation History
- ✅ Text Summarization
- ✅ Enhanced Error Handling
- 🚧 Retry Mechanism (max_retries=3)



## AI Memory & Persona Roadmap

### 1. Persistent Conversation Storage 🔄
- Implement PostgreSQL database to store conversations
  ```sql
  -- Create extensions for vector search capabilities
  CREATE EXTENSION IF NOT EXISTS vector;

  -- Create enum for persona types
  CREATE TYPE persona_type AS ENUM ('gym_coach', 'teacher', 'programmer', 'default');

  -- Create conversations table
  CREATE TABLE conversations (
      id SERIAL PRIMARY KEY,
      timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
      user_input TEXT NOT NULL,
      ai_response TEXT NOT NULL,
      active_persona persona_type DEFAULT 'default',
      context_tags TEXT[],
      embedding vector(1536),  -- For semantic search
      metadata JSONB
  );

  -- Create index for efficient context search
  CREATE INDEX idx_conversations_timestamp ON conversations(timestamp);
  CREATE INDEX idx_conversations_persona ON conversations(active_persona);
  CREATE INDEX idx_conversations_embedding ON conversations USING ivfflat (embedding vector_cosine_ops);
  ```

- Required PostgreSQL setup:
  ```bash
  sudo apt install postgresql postgresql-contrib
  sudo systemctl start postgresql
  sudo -u postgres createdb gemini_cli
  ```

- Dependencies to add in requirements.txt:
  ```
  psycopg2-binary>=2.9.9
  sqlalchemy>=2.0.0
  alembic>=1.12.0
  ```

- **Status:** ❌ Not Started

### 2. Persona Management System 🎭
- Create persona configuration system
- Add persona commands:
  ```bash
  python src/main.py --set-persona "gym_coach"
  python src/main.py --list-personas
  ```
- **Status:** ❌ Not Started

### 3. Context Window Management 🪟
- Implement sliding context window
- Add context pruning strategies
- **Status:** ❌ Not Started

### 4. Memory Types Implementation 🧠
- Short-term memory (current session)
- Long-term memory (persistent storage)
- Working memory (active context)
- **Status:** ❌ Not Started

### 5. Memory Search & Retrieval 🔍
- Implement vector embeddings
- Add memory commands:
  ```bash
  python src/main.py --search "previous workouts"
  python src/main.py --context-depth deep
  ```
- **Status:** ❌ Not Started

### 6. Conversation Threading 🧵
- Add thread management:
  ```bash
  python src/main.py --new-thread "workout_plan"
  python src/main.py --switch-thread "diet_advice"
  ```
- **Status:** ❌ Not Started

### 7. Memory Consolidation 📝
- Periodic memory summarization
- Knowledge base updates
- **Status:** ❌ Not Started

### 8. User Preference Learning 👤
- Track user interactions
- Adapt persona behavior
- **Status:** ❌ Not Started

### 9. API Integration 🔌
- Enhance GeminiAgent class
- Add memory management methods
- **Status:** ❌ Not Started

### 10. Performance Optimization ⚡
- Implement caching
- Optimize database queries
- **Status:** ❌ Not Started


Let's get to work. There's a lot to be done.

---
