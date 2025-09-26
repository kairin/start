# Project Standards

This directory defines the quality standards and requirements for all projects.

## Standard Files

### Core Standards
- `agents-md.template` - AGENTS.md structure and requirements
- `project-structure.yaml` - Required files and directory structure
- `git-workflows.yaml` - Git branch naming and workflow standards
- `mcp-requirements.yaml` - MCP server integration standards

### Quality Requirements  
- `code-quality.yaml` - Linting, formatting, and testing requirements
- `documentation.yaml` - Documentation standards and templates
- `deployment.yaml` - GitHub Pages and deployment configurations

### Integration Standards
- `spec-kit.yaml` - spec-kit integration requirements  
- `ai-assistant.yaml` - Claude, Gemini, Copilot integration standards
- `development-tools.yaml` - Required development environment setup

## Usage

```bash
# Check project compliance with standards
start audit --project /path/to/project

# Apply specific standard to project
start standards apply --standard agents-md --project /path/to/project

# Update all projects with new standards
start standards sync --all-projects
```

All standards are designed to work with your existing projects while ensuring consistency and quality across your entire development ecosystem.