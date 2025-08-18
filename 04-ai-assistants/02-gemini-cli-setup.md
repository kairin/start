## 🤖 Google Gemini CLI Setup

### 🚀 Installing Gemini CLI

Gemini CLI is another great AI assistant that you can use in your terminal for code analysis and development assistance.

```bash
# Install using npx (recommended for Ubuntu)
npx @google/gemini-cli

# For global installation
npm install -g @google/gemini-cli
```

### 🔑 Authentication and Configuration

**Generate API key**:
1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Create a new API key
3. Store it securely!

```bash
# Add to ~/.bashrc
echo 'export GEMINI_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc

# Test the CLI
npx @google/gemini-cli
```

### 🌐 MCP Server Integration (Context7)

For access to the latest documentation, configure the context7 MCP server:

```bash
# The context7 configuration in ~/.gemini/settings.json should be:
{
  "selectedAuthType": "oauth-personal",
  "mcpServers": {
    "context7": {
      "httpUrl": "https://mcp.context7.com/mcp"
    }
  }
}
```

Use "use context7" in your prompts to get the latest library documentation.

### 🏠 Using a Local Model Server (Advanced)

For privacy and offline use, you can run a local AI model.

**1. Install Ollama:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**2. Pull a model:**
```bash
ollama pull gemma
```

**3. Serve the model:**
The Ollama server will start automatically.

**4. Configure Gemini CLI to use the local model:**
```bash
gemini --model ollama/gemma "your prompt"
```