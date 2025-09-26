# Start - Project Quality Controller Agent Instructions

## Project Overview
Start is a **Project Quality Controller** that ensures consistency, quality, and standards across all development projects. This system manages:

- 🏗️ **Project Bootstrapping**: Create new projects with preferred standards
- ✅ **Quality Auditing**: Validate existing projects for compliance  
- 🔄 **System Management**: Manage development tools (NVM, Oh My Zsh, etc.)
- 📋 **Standards Enforcement**: Apply consistent project standards
- 🤖 **AI Integration**: Multi-AI assistant support (Claude, Gemini, Copilot)

**Phase 001**: Complete - Basic quality controller with UV-first Python enforcement
**Phase 002**: Planned - spec-kit integration for enhanced capabilities

---

## 🚨 UV-First Development Requirements

> **⚠️ MANDATORY**: All Python projects managed by Start are **UV-ONLY**. Using standard `pip` commands will cause failures.

**ALL Python package operations MUST use UV:**

```bash
# ✅ CORRECT - Always use uv
uv pip install package-name
uv run python script.py
uv run command-name

# ❌ WRONG - Never use pip directly
pip install package-name        # Will cause import errors
python script.py               # Will cause module errors
command-name                   # Will cause command not found
```

---

## MCP Server Requirements

**IMPORTANT**: Always check if the context7 MCP server is available and use it to access the latest documentation versions.

### For Claude Code:
- Run `claude mcp list` to verify context7 is connected
- If not available, run: `claude mcp add context7 -- npx -y @upstash/context7-mcp`
- Use "use context7" in prompts when referencing external libraries/frameworks for up-to-date documentation

### For Gemini CLI:
- For Gemini CLI, context7 provides up-to-date documentation for libraries and frameworks
- Use context7 to ensure you're working with the latest API specifications and best practices
- Include "use context7" in prompts when referencing external libraries/frameworks

### For GitHub Copilot CLI:
- Ensure MCP servers are globally configured for Copilot access
- Use Start's system management to maintain MCP server health

---

## Key Files and Structure

```
start/                           # Project Quality Controller
├── cli/
│   └── start.py               # Main CLI interface
├── scripts/
│   └── system-update.sh        # Enhanced dev tools updater
├── standards/
│   ├── agents-md.template      # AGENTS.md requirements
│   ├── project-structure.yaml  # File structure standards
│   └── python-uv-requirements.yaml # UV-first enforcement
├── validators/
│   ├── structure_validator.py  # Project structure validation
│   └── uv_validator.py         # UV-first compliance checking
├── templates/
│   └── python-project/         # UV-compliant Python template
└── docs/
    └── phase-001-completion.md # Implementation documentation
```

---

## Development Workflow

### 1. System Management
```bash
# Check all systems for updates
python3 cli/start.py system check

# Update development tools (NVM, Oh My Zsh)  
python3 cli/start.py system update

# Check project repositories for updates
python3 cli/start.py system projects
```

### 2. Project Quality Control
```bash
# Show system status
python3 cli/start.py status

# Audit project quality and compliance
python3 cli/start.py audit --project /path/to/project

# List available templates (Phase 002)
python3 cli/start.py templates list
```

### 3. UV-First Python Projects
```bash
# Create UV virtual environment
uv venv .venv

# Activate environment
source .venv/bin/activate

# Install dependencies (use pyproject.toml, never requirements.txt)
uv pip install -e .

# Run scripts (always prefix with uv run)
uv run python script.py
uv run pytest
uv run black .
```

---

## Build and Deployment

### Phase 001 Operations:
- **System Updates**: Automated via `scripts/system-update.sh`
- **Quality Validation**: Via CLI auditing commands
- **Standards Enforcement**: Automated validation and scoring

### Phase 002 (Planned):
- **Project Bootstrapping**: Automated project creation from templates
- **Cross-Project Sync**: Standards synchronization across all projects
- **spec-kit Integration**: Enhanced validation and automation

---

## Common Tasks

### System Maintenance:
```bash
# Check and update all development tools
python3 cli/start.py system update

# Monitor all project repositories
python3 cli/start.py system projects

# Verify system health
python3 cli/start.py status
```

### Project Quality Assurance:
```bash
# Audit single project
python3 cli/start.py audit --project /home/kkk/Apps/project-name

# Validate UV compliance (Python projects)
python3 validators/uv_validator.py /path/to/python/project

# Check project structure compliance
python3 validators/structure_validator.py /path/to/project
```

### Template Management (Phase 002):
```bash
# Create new project from template (Phase 002)
# start bootstrap --template python-project --name my-app

# Apply template standards to existing project (Phase 002)  
# start apply-template --template python-project --target /path/to/project
```

---

## Integration Requirements

### Multi-AI Assistant Support:
- **Claude Code**: Full MCP integration, UV-first awareness
- **Gemini CLI**: Context7 integration, documentation access
- **GitHub Copilot**: Global MCP server access, quality standards awareness

### Quality Standards Enforced:
- ✅ **AGENTS.md Files**: Required in all projects
- ✅ **UV-First Python**: Mandatory for all Python projects
- ✅ **Git Compliance**: Proper .gitignore, branch naming
- ✅ **Project Structure**: Consistent file organization
- ✅ **Documentation**: README.md and proper project documentation

### System Integration:
- **Development Tools**: NVM, Oh My Zsh, system packages
- **Project Monitoring**: All repositories in `/home/kkk/Apps/`
- **Quality Control**: Automated validation and compliance scoring

---

## Troubleshooting

### Common UV-Related Issues:
**ModuleNotFoundError after installation:**
```bash
# Solution: Always use uv run
uv run python script.py  # Not: python script.py
```

**Command not found errors:**
```bash
# Solution: Prefix with uv run
uv run pytest          # Not: pytest
uv run black .         # Not: black .
```

### System Update Issues:
**NVM/Oh My Zsh update failures:**
```bash
# Use Start's enhanced updater
python3 cli/start.py system update

# Manual fallback
cd ~/.nvm && git fetch origin --tags && git reset --hard [latest-tag]
cd ~/.oh-my-zsh && git pull origin master
```

### Quality Audit Failures:
**Project fails compliance check:**
```bash
# Get detailed audit report
python3 cli/start.py audit --project /path/to/project

# Check specific UV compliance (Python projects)
python3 validators/uv_validator.py /path/to/project

# Review required standards
cat standards/project-structure.yaml
```

---

## Notes for AI Assistants

### For Claude:
- This is a **Project Quality Controller** system, not just documentation
- Focus on UV-first Python development when working with Python projects
- Always validate project compliance using the CLI tools
- Use context7 MCP server for up-to-date documentation access
- When suggesting changes, ensure they align with quality standards

### For Gemini:  
- This system enforces strict quality standards across all projects
- UV-first approach is mandatory for Python projects
- Always verify latest documentation through context7 when available
- Consider system-wide impact when suggesting project changes
- Maintain consistency with established standards

### For GitHub Copilot:
- Respect UV-first requirements in all Python code suggestions
- Consider project quality standards when generating code
- Ensure suggestions align with AGENTS.md requirements
- Use established project structure patterns

---

## Phase 002 Roadmap

**Planned Enhancements:**
- 🔄 **spec-kit Integration**: Advanced project management capabilities
- 🔄 **Bootstrap Commands**: Automated project creation from templates
- 🔄 **Cross-Project Sync**: Standards synchronization across all projects
- 🔄 **Enhanced Validation**: Complete project lifecycle management
- 🔄 **AI Agent Orchestration**: Coordinated multi-AI project assistance

**Current Status**: Phase 001 Complete - Foundation operational and ready for Phase 002 enhancement