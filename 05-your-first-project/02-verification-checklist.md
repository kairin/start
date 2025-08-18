# ✅ 02: The Ultimate Verification Checklist

You have installed and configured a complete, professional development environment. This is the final check to ensure every single component is working as expected.

### 🤔 Why is This Important?

Running through this checklist confirms that your tools are installed correctly, they are in your system's `PATH`, and your accounts are properly authenticated. This gives you the confidence that your foundation is solid before you start building complex projects.

### ✨ The Goal

Our objective is to run a series of commands and verify their output, ensuring every part of our setup is correct.

---

## The Checklist

Open your terminal and run the following commands. Check your output against the expected results.

### 1. System Tools

These are the foundational packages provided by Ubuntu.

- [ ] **Check Git Version**
  ```bash
  git --version
  ```
  *Expected Output:* Should show a version number, e.g., `git version 2.40.1`.

- [ ] **Check cURL Version**
  ```bash
  curl --version
  ```
  *Expected Output:* Should show a version number and supported protocols.

- [ ] **Check Python Version**
  ```bash
  python3 --version
  ```
  *Expected Output:* Should show a Python 3 version, e.g., `Python 3.10.12`.

### 2. Node.js Ecosystem

These commands verify that NVM is managing your Node.js environment correctly.

- [ ] **Check NVM Version**
  ```bash
  nvm --version
  ```
  *Expected Output:* Should show the NVM version number, e.g., `0.40.3`.

- [ ] **Check Node.js Version**
  ```bash
  node --version
  ```
  *Expected Output:* Should show the LTS version you installed, e.g., `v20.11.1`.

- [ ] **Check npm Version**
  ```bash
  npm --version
  ```
  *Expected Output:* Should show the npm version that came with Node.js, e.g., `10.2.4`.

### 3. Development & AI Tools

These commands verify that your code editor and AI assistants are installed.

- [ ] **Check VS Code**
  ```bash
  code --version
  ```
  *Expected Output:* Should show the version number for VS Code.

- [ ] **Check GitHub CLI**
  ```bash
  gh --version
  ```
  *Expected Output:* Should show the `gh` version number.

- [ ] **Check Claude CLI**
  ```bash
  claude --version
  ```
  *Expected Output:* Should show the version number for the Claude CLI.

- [ ] **Check Gemini CLI**
  ```bash
  gemini-cli --version
  ```
  *Expected Output:* Should show the version number for the Gemini CLI.

### 4. Authentication Status

This is the most important check. It confirms you can securely connect to GitHub.

- [ ] **Check GitHub CLI Authentication**
  ```bash
  gh auth status
  ```
  *Expected Output:* Should show a green checkmark and state that you are logged in to github.com.

- [ ] **Check SSH Key Authentication**
  ```bash
  ssh -T git@github.com
  ```
  *Expected Output:* Should show a message starting with `Hi your-username! You've successfully authenticated...`

---

## A Note on Best Practices: Environment Variables

As you build projects, you'll handle sensitive information like API keys. **Never write these directly in your code.** The professional way to handle them is with environment variables.

A common pattern is to create a `.env.example` file in your project. This file acts as a template for the actual `.env` file (which is *never* shared).

**Example `.env.example` file:**
```bash
# This is an example file. Copy it to a new file named .env and fill in your actual values.
NODE_ENV=development
PORT=3000
GEMINI_API_KEY="your_key_here"
```
You would then add `.env` to your `.gitignore` file to ensure you never accidentally commit your secret keys.

---

### Next Steps

If all your checks passed, your environment is officially ready for action!

In the next and final guide, we'll discuss what you can do from here to continue your journey as a developer.

➡️ **Next: [03: Next Steps](./03-next-steps.md)**

⬅️ **Previous: [01: Creating Your First Project](./01-project-creation.md)**

↩️ **Back to [Main Menu](../../README.md)**
