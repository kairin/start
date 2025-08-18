# 🐧 01: Removing Snap for a Cleaner System

Welcome to the first step of setting up your developer environment! Our goal here is to create a clean, fast, and professional foundation. We'll start by removing "Snap," a default software packaging system on Ubuntu.

### 🤔 What is Snap and Why Remove It?

Snap is a packaging system created by Canonical, the company behind Ubuntu. It bundles applications with everything they need to run, which can make them isolated and secure. However, for development work, many professionals prefer to remove Snaps because they can sometimes be slower, take up more disk space, and offer less control than traditional packages managed by `apt` (Advanced Package Tool), which is Ubuntu's powerful, native package manager.

By removing Snap, we are taking control of our system to ensure it's optimized for performance and flexibility.

### ✨ The Goal

Our objective is to completely remove Snap and its packages, and prevent it from being reinstalled, ensuring a clean slate for the tools we *do* want to install.

```mermaid
graph TD
    subgraph "Goal: A Snap-Free System"
        A[List all installed Snaps] --> B[Remove each Snap package one by one];
        B --> C[Uninstall the Snap system (snapd)];
        C --> D[Clean up leftover files and folders];
        D --> E[Block Snap from being reinstalled in the future];
    end
```

---

Choose the guide that best fits your experience level below.

<details>
<summary>
  <strong>🌱 I'm a Complete Beginner</strong> - Click for a gentle, step-by-step guide.
</summary>

### Let's Clean Up Your System!

We'll be using the terminal for this. Remember, you can open it with `Ctrl+Alt+T`. We'll copy and paste each command one by one. Many commands start with `sudo`, which stands for "Super User Do." It's like telling the computer you're the administrator and have permission to make important changes.

**Step 1: See What Snaps Are Installed**

First, let's see which Snap packages are on your system.

```bash
# This command lists all installed snap packages.
snap list
```
You'll see a list of programs. We need to remove them all.

**Step 2: Remove the Snap Packages**

Remove each package from the list you saw. The names might be slightly different on your system, but they will be similar to the ones below. If you get an error that a package is not installed, just move to the next one!

```bash
# Use 'sudo snap remove' for each package.
sudo snap remove --purge firefox
sudo snap remove --purge snap-store
sudo snap remove --purge gnome-42-2204
sudo snap remove --purge gtk-common-themes
sudo snap remove --purge snapd-desktop-integration
sudo snap remove --purge firmware-updater
sudo snap remove --purge bare
sudo snap remove --purge core22
sudo snap remove --purge snapd
```

**Step 3: Uninstall the Snap System Itself**

Now that the packages are gone, we can remove the main `snapd` program.

```bash
# 'apt purge' completely removes a program and its configuration files.
sudo apt purge snapd -y
```
The `-y` at the end automatically answers "yes" to any questions the command asks.

**Step 4: Clean Up Leftover Folders**

Let's delete the folders where Snap kept its files.

```bash
# The 'rm -rf' command deletes folders and files. Be careful with it!
rm -rf ~/snap
sudo rm -rf /snap /var/snap /var/lib/snapd /var/cache/snapd /usr/lib/snapd
```

**Step 5: Block Snap From Coming Back**

Finally, we'll create a special rule to tell your system never to install Snap again.

First, open a text editor to create the file:
```bash
sudo nano /etc/apt/preferences.d/nosnap.pref
```
Then, copy and paste this exact text into the editor:
```
# To prevent repository packages from triggering the installation of snap,
# this file forbids snapd from being installed by APT.
Package: snapd
Pin: release a=*
Pin-Priority: -10
```
Now, press `Ctrl+X` to exit, then `Y` to save, and finally `Enter` to confirm the file name.

That's it! You've successfully cleaned your system.

</details>

<details>
<summary>
  <strong>🪟 I'm Coming From Windows</strong> - Click for a technical guide.
</summary>

### Optimizing Your Ubuntu Install

On Ubuntu, `snapd` is a pre-installed package manager, similar in concept to the Microsoft Store or winget, as it provides applications in a sandboxed environment. However, for more direct control and potentially better performance, many developers prefer to rely solely on `apt`, which is analogous to package managers like Chocolatey or Scoop on Windows.

This guide will walk you through the complete removal of `snapd` and its related packages.

**Step 1: List and Remove Existing Snap Packages**

First, enumerate all installed snaps and then remove them. This is necessary before uninstalling the `snapd` daemon itself.

```bash
# List currently installed snaps
snap list

# Purge each snap package. The list may vary on your system.
# The --purge flag ensures configuration files are also removed.
sudo snap remove --purge firefox
sudo snap remove --purge snap-store
sudo snap remove --purge gnome-42-2204
sudo snap remove --purge gtk-common-themes
sudo snap remove --purge snapd-desktop-integration
sudo snap remove --purge firmware-updater
sudo snap remove --purge bare
sudo snap remove --purge core22
sudo snap remove --purge snapd
```

**Step 2: Purge the Snapd Package**

With all dependent packages gone, you can now purge the `snapd` daemon using `apt`.

```bash
# Purge snapd and its dependencies from the system.
sudo apt purge snapd -y
```

**Step 3: Remove Snap Directories**

Clean up the residual directories used by snapd in your home and system folders.

```bash
# Remove user-specific snap directory and system-wide snap directories
rm -rf ~/snap
sudo rm -rf /snap /var/snap /var/lib/snapd /var/cache/snapd /usr/lib/snapd
```

**Step 4: Prevent Reinstallation via APT Pinning**

To ensure `apt` doesn't reinstall `snapd` as a dependency of another package in the future, we'll use APT pinning to block the `snapd` package.

```bash
# Create a preference file for apt
sudo nano /etc/apt/preferences.d/nosnap.pref
```
Insert the following content into the file. This sets the priority for the `snapd` package to a negative value, effectively preventing `apt` from ever choosing to install it.
```
# To prevent repository packages from triggering the installation of snap,
# this file forbids snapd from being installed by APT.
Package: snapd
Pin: release a=*
Pin-Priority: -10
```
Press `Ctrl+X`, then `Y`, then `Enter` to save and close `nano`.

Your system is now free of `snapd`.

</details>

<details>
<summary>
  <strong>🚀 I'm an Experienced User</strong> - Click for the quick script.
</summary>

### Snap Removal Script

Here is a script to list, remove, purge, and block `snapd`.

```bash
# 1. List snaps to identify them
snap list

# 2. Remove all snaps (edit this list based on the output above)
sudo snap remove --purge firefox
sudo snap remove --purge snap-store
sudo snap remove --purge gnome-42-2204
sudo snap remove --purge gtk-common-themes
sudo snap remove --purge snapd-desktop-integration
sudo snap remove --purge firmware-updater
sudo snap remove --purge bare
sudo snap remove --purge core22
sudo snap remove --purge snapd

# 3. Purge snapd and clean up directories
sudo apt purge snapd -y
rm -rf ~/snap
sudo rm -rf /snap /var/snap /var/lib/snapd /var/cache/snapd /usr/lib/snapd

# 4. Block snapd from being reinstalled
echo -e "# To prevent repository packages from triggering the installation of snap,\n# this file forbids snapd from being installed by APT.\nPackage: snapd\nPin: release a=*\nPin-Priority: -10" | sudo tee /etc/apt/preferences.d/nosnap.pref

echo "Snapd has been removed and blocked."
```

</details>

---

### Next Steps

With the system foundation clean, you're ready for the next step.

➡️ **Next: [02: Installing Firefox](./02-installing-firefox.md)**

↩️ **Back to [Main Menu](../../README.md)**
