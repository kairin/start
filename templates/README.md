# Project Templates

This directory contains project templates that ensure consistency across all your projects.

## Available Templates

### Python Projects
- `python-project/` - Standard Python project with spec-kit integration
- `python-mcp/` - Python project with MCP server capabilities 
- `python-research/` - Research and analysis tools

### Node.js Projects  
- `node-astro-project/` - Astro-based projects for GitHub Pages
- `node-mcp/` - Node.js MCP server projects
- `node-cli/` - Command-line interface tools

### Configuration Projects
- `config-manager/` - Configuration and dotfiles management
- `ghostty-config/` - Terminal configuration projects

### Research Tools
- `research-tool/` - Data analysis and research projects
- `ai-agent/` - AI assistant and agent projects

## Usage

```bash
# List available templates
start templates list

# Create new project from template
start bootstrap --template python-project --name my-new-app

# Update existing project to match template standards
start apply-template --template python-project --target /path/to/project
```

Each template includes:
- Proper directory structure
- Required configuration files (AGENTS.md, .claude/, etc.)
- Standard build and deployment scripts
- Quality assurance configurations
- MCP server integration when applicable