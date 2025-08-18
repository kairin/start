### ✅ Verification Checklist

Run these commands to make sure everything is set up correctly.

```bash
# System tools
git --version                    # Should show 2.40+
curl --version                    # Should be installed
python3 --version                 # Should show 3.10+

# Node.js ecosystem
nvm --version                     # Should show 0.40+
node --version                    # Should show v18+ or LTS
npm --version                     # Should show 9+

# Development tools
code --version                    # VS Code version
claude --version                  # Claude Code version
gh --version                      # GitHub CLI version

# Authentication status
gh auth status                    # Should show logged in
ssh -T git@github.com            # Should show authentication success

# Test Gemini CLI
npx @google/gemini-cli --version  # Should run without errors
```

### 🤫 Environment Variables Best Practice

Create a `.env.example` file for your projects to show what environment variables are needed.

```bash
cat > .env.example << 'EOL'
# Copy this to .env and fill in your values
NODE_ENV=development
PORT=3000
GEMINI_API_KEY=your_key_here
GITHUB_TOKEN=your_token_here
EOL
```

**Never commit the actual `.env` file!** It should always be in your `.gitignore`.