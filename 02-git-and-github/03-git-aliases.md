### ⚡ Professional Git Aliases for Efficiency

Aliases are shortcuts for your most used Git commands. They save you time and typing! 🏃💨

```bash
# Essential shortcuts
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status

# Beautiful log visualization
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

# Quick operations
git config --global alias.unstage "reset HEAD --"
git config --global alias.last "log -1 HEAD"
```