### 🔑 SSH Keys: Your Secure Authentication

SSH keys are a secure way to connect to GitHub without using a password. It's like having a secret handshake with the server! 🤝

```bash
# Generate a modern Ed25519 key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Start the SSH agent
eval "$(ssh-agent -s)"

# Add your key
ssh-add ~/.ssh/id_ed25519

# Display your public key to copy
cat ~/.ssh/id_ed25519.pub
```

**Add to GitHub**: Go to **Settings → SSH and GPG keys → New SSH key**, paste your public key, and save. saving it! 💾