## 💻 Part 4: VS Code Installation

### 🚀 Installing VS Code the Right Way

We'll install VS Code from Microsoft's official repository for the best performance.

```bash
# Install prerequisites
sudo apt update
sudo apt install software-properties-common apt-transport-https wget gpg

# Add Microsoft's GPG key
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg

# Add the repository
sudo sh -c 'echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'

# Install VS Code
sudo apt update
sudo apt install code
```

### ⚙️ Essential VS Code Configuration

Open VS Code settings.json (Ctrl+, then click the {} icon) and add:

```json
{
  // Readable font with ligatures
  "editor.fontSize": 14,
  "editor.fontFamily": "Fira Code, Consolas, monospace",
  "editor.fontLigatures": true,
  
  // Auto-save prevents losing work
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000,
  
  // Format code automatically
  "editor.formatOnSave": true,
  "editor.formatOnPaste": true,
  
  // Better code suggestions
  "editor.suggestOnTriggerCharacters": true,
  
  // Python uses 4 spaces
  "[python]": {
    "editor.tabSize": 4
  },
  
  // JavaScript/TypeScript uses 2 spaces
  "[javascript]": {
    "editor.tabSize": 2
  }
}
```

### 🧩 Must-Have Extensions

Install these extensions to supercharge your development:

**Core Development**:
- **Prettier**: Automatic code formatting ✨
- **ESLint**: JavaScript error detection 🔍
- **GitLens**: Enhanced Git capabilities 🐙
- **Live Server**: Instant web preview 🌐

**Language Support**:
- **Python**: Complete Python development 🐍
- **JavaScript (ES6) code snippets**: Speed up JavaScript coding ⚡

**Productivity**:
- **Path Intellisense**: Autocomplete file paths 📁
- **TODO Highlight**: Track tasks in code ✅