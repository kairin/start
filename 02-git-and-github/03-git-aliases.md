# ⚡ 03: Supercharging Git with Aliases

Now that you're set up with Git, let's make it faster and easier to use. We can do this with **aliases**, which are custom shortcuts for longer Git commands.

### 🤔 Why Use Aliases?

Using aliases is a classic productivity hack for developers.
*   **It saves time:** Typing `git st` is much faster than `git status`.
*   **It reduces typos:** Fewer characters to type means fewer chances for mistakes.
*   **It makes complex commands easy:** You can turn a long, complicated command into a short, memorable alias.

### ✨ The Goal

We will add a set of popular and useful aliases to your Git configuration. Once you get used to them, you'll never want to go back!

| Instead of typing... | You can just type... |
| :--- | :--- |
| `git status` | `git st` |
| `git checkout` | `git co` |
| `git commit` | `git ci` |
| `git log --graph --oneline`| `git lg` |

---

Choose the guide that best fits your experience level below.

<details>
<summary>
  <strong>🌱 I'm a Complete Beginner</strong> - Click for a gentle introduction to aliases.
</summary>

### Creating Nicknames for Commands

An alias is just a nickname. We're going to teach Git some short nicknames for the commands you'll use most often.

We'll add each one using the `git config --global` command, just like we did when we set up your name and email.

**Step 1: Add Your First Aliases**

Let's create four simple aliases. Copy and paste these commands into your terminal one by one.

```bash
# Alias for 'git status'
git config --global alias.st status

# Alias for 'git commit'
git config --global alias.ci commit

# Alias for 'git branch'
git config --global alias.br branch

# Alias for 'git checkout'
git config --global alias.co checkout
```

**Step 2: Try Them Out!**

Now, instead of typing `git status`, you can just run:
```bash
git st
```
Instead of `git checkout main`, you can run:
```bash
git co main
```
It might feel strange at first, but it will quickly become second nature and save you a lot of typing!

**Step 3: A Powerful Alias for Viewing History**

This next alias is much longer. It creates a `git lg` command that displays your project's history in a beautiful, compact way. Just copy and paste the whole block.

```bash
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```
Now, whenever you are in a Git project, run `git lg` to see a clean, visual history of all the commits. It's much easier to read than the standard `git log`.

</details>

<details>
<summary>
  <strong>🪟 I'm Coming From Windows</strong> - Click for a technical guide.
</summary>

### Creating Git-Specific Aliases

If you've used `Set-Alias` in PowerShell or `doskey` in the Windows Command Prompt, you're already familiar with the concept of aliasing. Git has its own built-in alias system that works on any platform. These are stored in your `.gitconfig` file.

**Step 1: Set Up Foundational Aliases**

These are common, high-frequency commands that are prime candidates for aliasing.

```bash
git config --global alias.st status
git config --global alias.ci commit
git config --global alias.br branch
git config --global alias.co checkout
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
```

**Step 2: Configure a Prettier Log Alias**

This is a widely-used alias, often called `lg` or `ll`, that formats the `git log` output for maximum readability, showing the graph, relative time, and author.

```bash
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```
Running `git lg` provides a much more comprehensive overview of the project history than the default `git log`.

You can view all your configured aliases by running `git config --get-regexp alias`.

</details>

<details>
<summary>
  <strong>🚀 I'm an Experienced User</strong> - Click for the quick script.
</summary>

### Git Alias Setup Script

Here is a script to add a set of common and useful Git aliases to your global `.gitconfig`.

```bash
# Standard command shortcuts
git config --global alias.st status
git config --global alias.ci commit
git config --global alias.br branch
git config --global alias.co checkout
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'

# Pretty log
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

# Show aliases
echo "Git aliases configured:"
git config --get-regexp alias
```

</details>

---

### Next Steps

With these handy shortcuts in your toolkit, you're ready to interact with GitHub from the command line using their official CLI tool.

➡️ **Next: [04: Using the GitHub CLI](./04-github-cli.md)**

⬅️ **Previous: [02: Setting Up SSH Keys](./02-ssh-keys.md)**

↩️ **Back to [Main Menu](../../README.md)**
