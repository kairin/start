#!/bin/bash

# Enhanced Development Tools Update Manager for Phase 001
# Manages updates for NVM, Oh My Zsh, and system development tools
# Part of the start project quality controller system

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# Directories
NVM_DIR="$HOME/.nvm"
OMZ_DIR="$HOME/.oh-my-zsh"
APPS_DIR="$HOME/Apps"

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${PURPLE}=== $1 ===${NC}"
}

# Function to check if directory exists and is a git repo
check_git_repo() {
    local dir=$1
    local name=$2
    
    if [[ ! -d "$dir" ]]; then
        print_error "$name directory not found at $dir"
        return 1
    fi
    
    if [[ ! -d "$dir/.git" ]]; then
        print_error "$name is not a git repository"
        return 1
    fi
    
    return 0
}

# Function to check NVM status
check_nvm() {
    print_status "Checking NVM..."
    
    if ! check_git_repo "$NVM_DIR" "NVM"; then
        return 1
    fi
    
    cd "$NVM_DIR"
    
    # Get current version
    local current_version=$(git describe --tags --abbrev=0 2>/dev/null || echo "unknown")
    
    # Fetch latest tags
    git fetch origin --tags &>/dev/null
    
    # Get latest version
    local latest_version=$(git describe --tags $(git rev-list --tags --max-count=1) 2>/dev/null)
    
    echo "  Current: $current_version"
    echo "  Latest:  $latest_version"
    
    if [[ "$current_version" != "$latest_version" ]]; then
        print_warning "NVM update available: $current_version → $latest_version"
        return 2  # Update available
    else
        print_success "NVM is up to date"
        return 0  # Up to date
    fi
}

# Function to check Oh My Zsh status
check_omz() {
    print_status "Checking Oh My Zsh..."
    
    if ! check_git_repo "$OMZ_DIR" "Oh My Zsh"; then
        return 1
    fi
    
    cd "$OMZ_DIR"
    
    # Get current commit
    local current_commit=$(git rev-parse HEAD)
    
    # Fetch latest
    git fetch origin master &>/dev/null
    
    # Get latest commit
    local latest_commit=$(git rev-parse origin/master)
    
    # Count commits behind
    local commits_behind=$(git rev-list --count HEAD..origin/master)
    
    echo "  Current: $(git log --oneline -1 | cut -d' ' -f1)"
    echo "  Latest:  $(git log --oneline -1 origin/master | cut -d' ' -f1)"
    
    if [[ "$commits_behind" -gt 0 ]]; then
        print_warning "Oh My Zsh has $commits_behind new commit(s) available"
        return 2  # Update available
    else
        print_success "Oh My Zsh is up to date"
        return 0  # Up to date
    fi
}

# Function to update NVM
update_nvm() {
    print_status "Updating NVM..."
    
    cd "$NVM_DIR"
    
    # Fetch all tags
    git fetch origin --tags &>/dev/null
    
    # Get latest version
    local latest_version=$(git describe --tags $(git rev-list --tags --max-count=1) 2>/dev/null)
    
    # Reset to latest tag (handles divergent branches)
    if git reset --hard "$latest_version" &>/dev/null; then
        print_success "NVM updated to $latest_version"
        echo "  💡 Remember to restart your terminal or run: source ~/.bashrc"
        return 0
    else
        print_error "Failed to update NVM"
        return 1
    fi
}

# Function to update Oh My Zsh
update_omz() {
    print_status "Updating Oh My Zsh..."
    
    cd "$OMZ_DIR"
    
    # Pull latest changes
    if git pull origin master &>/dev/null; then
        local latest_commit=$(git log --oneline -1 | cut -d' ' -f1)
        print_success "Oh My Zsh updated to $latest_commit"
        print_success "Changes are already active in your shell"
        return 0
    else
        print_error "Failed to update Oh My Zsh"
        return 1
    fi
}

# Function to check project git repositories for updates
check_projects() {
    print_status "Checking project repositories for updates..."
    
    if [[ ! -d "$APPS_DIR" ]]; then
        print_warning "Apps directory not found at $APPS_DIR"
        return 1
    fi
    
    cd "$APPS_DIR"
    local projects_with_updates=0
    
    for dir in */; do
        if [[ -d "$dir/.git" ]]; then
            echo "  Checking $dir..."
            cd "$dir"
            
            # Fetch latest changes
            git fetch --all &>/dev/null 2>&1 || continue
            
            # Check if behind remote
            local behind=$(git rev-list --count HEAD..origin/$(git branch --show-current) 2>/dev/null || echo "0")
            local uncommitted=$(git status --porcelain | wc -l)
            
            if [[ "$behind" -gt 0 ]]; then
                print_warning "  $dir has $behind new commit(s) available"
                ((projects_with_updates++))
            elif [[ "$uncommitted" -gt 0 ]]; then
                print_warning "  $dir has $uncommitted uncommitted changes"
            else
                echo "    ✅ Up to date"
            fi
            
            cd "$APPS_DIR"
        fi
    done
    
    if [[ $projects_with_updates -gt 0 ]]; then
        print_warning "$projects_with_updates project(s) have updates available"
        echo "  Run individual 'git pull' commands to update projects"
    else
        print_success "All projects are up to date"
    fi
}

# Function to check system packages
check_system_packages() {
    print_status "Checking system packages..."
    
    # Check for available updates
    local updates=$(apt list --upgradable 2>/dev/null | grep -c upgradable || echo "0")
    
    if [[ "$updates" -gt 0 ]]; then
        print_warning "$updates system package(s) can be upgraded"
        echo "  Run 'sudo apt update && sudo apt upgrade' to update system packages"
    else
        print_success "System packages are up to date"
    fi
}

# Function to show help
show_help() {
    echo "Enhanced Development Tools Update Manager - Phase 001"
    echo ""
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  check      Check for available updates (default)"
    echo "  update     Check and apply development tool updates"
    echo "  system     Check system package updates"
    echo "  projects   Check project repository updates"
    echo "  help       Show this help message"
    echo ""
    echo "Managed tools:"
    echo "  • NVM (Node Version Manager)"
    echo "  • Oh My Zsh (Zsh framework)"
    echo "  • Project repositories in $APPS_DIR"
    echo "  • System packages (check only)"
    echo ""
    echo "Examples:"
    echo "  $0              # Check for updates"
    echo "  $0 check        # Check for updates"
    echo "  $0 update       # Update development tools"
    echo "  $0 system       # Check system packages"
    echo "  $0 projects     # Check project repositories"
}

# Main function
main() {
    local command=${1:-check}
    
    print_header "Phase 001 Development Tools Manager"
    
    case "$command" in
        "check")
            echo "🔍 Checking for updates..."
            echo ""
            
            local nvm_status=0
            local omz_status=0
            
            check_nvm
            nvm_status=$?
            
            echo ""
            
            check_omz
            omz_status=$?
            
            echo ""
            check_projects
            
            echo ""
            check_system_packages
            
            echo ""
            
            if [[ $nvm_status -eq 2 || $omz_status -eq 2 ]]; then
                print_warning "Updates are available! Run '$0 update' to apply development tool updates."
            elif [[ $nvm_status -eq 0 && $omz_status -eq 0 ]]; then
                print_success "All development tools are up to date! 🎉"
            fi
            ;;
            
        "update")
            echo "🔄 Checking and applying development tool updates..."
            echo ""
            
            # Check NVM
            check_nvm
            local nvm_check=$?
            
            if [[ $nvm_check -eq 2 ]]; then
                echo ""
                update_nvm
            fi
            
            echo ""
            
            # Check Oh My Zsh
            check_omz
            local omz_check=$?
            
            if [[ $omz_check -eq 2 ]]; then
                echo ""
                update_omz
            fi
            
            echo ""
            print_success "Development tool update process completed! 🎉"
            print_status "Note: Project repositories should be updated individually"
            ;;
            
        "system")
            echo "🖥️ Checking system packages..."
            echo ""
            check_system_packages
            ;;
            
        "projects")
            echo "📂 Checking project repositories..."
            echo ""
            check_projects
            ;;
            
        "help"|"-h"|"--help")
            show_help
            ;;
            
        *)
            print_error "Unknown command: $command"
            echo ""
            show_help
            exit 1
            ;;
    esac
}

# Run main function
main "$@"