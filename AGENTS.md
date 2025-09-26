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

## Git Branch Strategy & Workflow

### 🌿 **Branch Naming Convention**
**MANDATORY**: All branches MUST follow this exact format:
```
YYYYMMDD-HHMMSS-type-description
```

**Examples:**
- `20250926-143022-feat-uv-validator-implementation`
- `20250926-150815-fix-agents-md-consolidation`
- `20250926-162340-docs-phase-001-completion`
- `20250926-174455-refactor-cli-interface-structure`

**Branch Types:**
- `feat-` : New features
- `fix-` : Bug fixes
- `docs-` : Documentation updates
- `refactor-` : Code refactoring
- `test-` : Test additions/updates
- `chore-` : Maintenance tasks

### 🗄️ **Branch Archiving Strategy**
**CRITICAL**: ALL branches are preserved permanently. NO branch deletion allowed.

#### **Complete Workflow - NEVER DELETE BRANCHES:**

```bash
# 1. Create new feature branch
git checkout main
git pull origin main
BRANCH_NAME="$(date +%Y%m%d-%H%M%S)-feat-description"
git checkout -b $BRANCH_NAME

# 2. Work on your changes
git add .
git commit -m "Descriptive commit message"

# 3. Push branch to remote (preserves it permanently)
git push -u origin $BRANCH_NAME

# 4. Create pull request via GitHub CLI or web interface
gh pr create --title "Feature: Description" --body "Detailed description"

# 5. After PR approval and merge to main
git checkout main
git pull origin main

# 6. IMPORTANT: Keep branch - DO NOT DELETE
# ❌ NEVER DO: git branch -d $BRANCH_NAME
# ❌ NEVER DO: git push origin --delete $BRANCH_NAME
# ✅ Branch remains in git history forever
```

#### **Branch Preservation Benefits:**
- 🗄️ **Complete History**: Every change is traceable forever
- 🔄 **Easy Rollbacks**: Can checkout any previous state
- 🔍 **Debugging**: Full context for any historical change
- 📊 **Analytics**: Complete development timeline preserved
- 🛡️ **Safety**: No risk of losing work or context

### 📋 **Pull Request Workflow**

#### **Creating Pull Requests:**
```bash
# After pushing your feature branch
gh pr create \
  --title "[Type]: Brief description" \
  --body "## What this does
- Detailed explanation
- List of changes  
- Testing performed

## Branch: $BRANCH_NAME
## Type: feat/fix/docs/refactor/test/chore"
```

#### **Merging Strategy:**
```bash
# Merge via GitHub web interface or CLI
# ALWAYS use "Squash and merge" or "Create a merge commit"
gh pr merge --squash  # Preferred: clean history
# OR
gh pr merge --merge   # Alternative: preserves individual commits

# After merge, sync your local main
git checkout main
git pull origin main
```

### 🔄 **Branch Management Commands**

#### **List All Branches (Local + Remote):**
```bash
# See all branches including archived ones
git branch -a

# See branch history with dates
git for-each-ref --format='%(refname:short) %(committerdate)' refs/heads

# See remote branches
git branch -r
```

#### **Working with Historical Branches:**
```bash
# Checkout any previous branch for reference
git checkout 20250926-143022-feat-uv-validator-implementation

# Create new branch based on historical one
git checkout -b 20250926-175500-feat-enhance-uv-validator 20250926-143022-feat-uv-validator-implementation

# Compare branches
git diff main..20250926-143022-feat-uv-validator-implementation
```

#### **Branch Synchronization:**
```bash
# Ensure all remote branches are visible locally
git fetch origin

# Pull all updates without deleting branches
git pull origin main
```

---

## Development Workflow

### 1. **System Management**
```bash
# Check all systems for updates
python3 cli/start.py system check

# Update development tools (NVM, Oh My Zsh)  
python3 cli/start.py system update

# Check project repositories for updates
python3 cli/start.py system projects
```

### 2. **Project Quality Control**
```bash
# Show system status
python3 cli/start.py status

# Audit project quality and compliance
python3 cli/start.py audit --project /path/to/project

# List available templates (Phase 002)
python3 cli/start.py templates list
```

### 3. **Complete Development Cycle**
```bash
# Start new feature
BRANCH_NAME="$(date +%Y%m%d-%H%M%S)-feat-your-feature-name"
git checkout -b $BRANCH_NAME

# UV-First Python Development (if applicable)
uv venv .venv
source .venv/bin/activate
uv pip install -e .

# Make changes and commit
git add .
git commit -m "feat: implement your feature"

# Push and create PR
git push -u origin $BRANCH_NAME
gh pr create --title "Feature: Your feature name"

# After merge, update main (branch stays preserved)
git checkout main
git pull origin main
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
- ✅ **Git Compliance**: YYYYMMDD-HHMMSS-type-description branch naming, NO branch deletion
- ✅ **Branch Archiving**: All branches preserved permanently for complete history
- ✅ **Pull Request Workflow**: Proper PR creation, review, and squash/merge to main
- ✅ **Project Structure**: Consistent file organization
- ✅ **Documentation**: README.md and proper project documentation

### System Integration:
- **Development Tools**: NVM, Oh My Zsh, system packages
- **Project Monitoring**: All repositories in `/home/kkk/Apps/`
- **Quality Control**: Automated validation and compliance scoring

---

## Troubleshooting

### **Git Branch Issues:**
**Branch naming errors:**
```bash
# ❌ Wrong: feature-branch, fix-bug, update-docs
# ✅ Correct: 20250926-143022-feat-new-feature

# Fix incorrect branch name
git branch -m old-name $(date +%Y%m%d-%H%M%S)-feat-corrected-name
```

**Accidental branch deletion prevention:**
```bash
# If someone tries to delete - STOP THEM
# ❌ NEVER: git branch -d branch-name  
# ❌ NEVER: git push origin --delete branch-name

# Instead, branches are preserved automatically
# All history remains in git log and remote
```

**Branch synchronization issues:**
```bash
# If remote branch not visible locally
git fetch origin

# If main is behind remote
git checkout main
git pull origin main

# View all branches including remote
git branch -a --sort=-committerdate
```

### **Pull Request Issues:**
**PR creation failures:**
```bash
# Ensure GitHub CLI is authenticated
gh auth status

# Create PR with proper branch naming
gh pr create --title "$(git branch --show-current | cut -d'-' -f3-)" \
  --body "Branch: $(git branch --show-current)"
```

**Merge conflicts:**
```bash
# Update your branch with latest main
git checkout main && git pull origin main
git checkout your-branch-name
git merge main  # Resolve conflicts
git push origin your-branch-name
```

### **Common UV-Related Issues:**
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

### **System Update Issues:**
**NVM/Oh My Zsh update failures:**
```bash
# Use Start's enhanced updater
python3 cli/start.py system update

# Manual fallback
cd ~/.nvm && git fetch origin --tags && git reset --hard [latest-tag]
cd ~/.oh-my-zsh && git pull origin master
```

### **Quality Audit Failures:**
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