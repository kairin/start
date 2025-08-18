## 🐙 Part 2: Git Configuration for Professional Workflows

### 👤 Setting Up Your Developer Identity

Your Git identity is like your signature on all your future work. It's important to get it right!

Here's how Git works:

```mermaid
graph TD
    subgraph Your Computer
        A[Working Directory] -- git add --> B[Staging Area];
        B -- git commit --> C[Local Repository];
    end
    C -- git push --> D[Remote Repository (GitHub)];
    D -- git pull --> A;
```

This diagram shows the flow of your code from your computer to the cloud.

```bash
# Your identity in every commit
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"

# Use VS Code for commit messages and diffs
git config --global core.editor "code --wait"

# Modern branch naming
git config --global init.defaultBranch main

# Enhanced diff visualization
git config --global merge.conflictstyle diff3
git config --global diff.algorithm histogram

# Cleaner history with rebase
git config --global pull.rebase true

# Automatic cleanup of deleted remote branches
git config --global fetch.prune true
```