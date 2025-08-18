## 🐙 GitHub CLI: Command-Line GitHub Mastery

The GitHub CLI (`gh`) brings GitHub to your terminal, so you can do everything without leaving the command line.

### 📥 Installing GitHub CLI

```bash
# Add GitHub's GPG key
sudo mkdir -p -m 755 /etc/apt/keyrings
wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null
sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg

# Add repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null

# Install
sudo apt update
sudo apt install gh
```

### 🔐 Authenticating with GitHub

```bash
# Start interactive authentication
gh auth login

# Choose:
# - GitHub.com
# - HTTPS (recommended for beginners)
# - Authenticate with web browser
# - Complete OAuth flow
```

### 🚀 Essential GitHub CLI Workflows

```bash
# Clone repositories quickly
gh repo clone username/repository

# Create a new repository
gh repo create my-project --public

# Work with pull requests
gh pr create --title "Add new feature" --body "Description here"
gh pr list
gh pr merge --squash

# Manage issues
gh issue create --title "Bug report" --body "Steps to reproduce..."
gh issue list
```