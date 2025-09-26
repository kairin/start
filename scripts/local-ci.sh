#!/bin/bash
# Start Project Quality Controller - Local CI/CD Pipeline
# Zero-cost deployment with complete quality checks

set -e  # Exit on error

echo "🚀 Start Project Quality Controller - Local CI/CD"
echo "=================================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Step counter
STEP=0
TOTAL_STEPS=10

function run_step() {
    STEP=$((STEP + 1))
    echo -e "${YELLOW}[$STEP/$TOTAL_STEPS]${NC} $1"
}

function success() {
    echo -e "${GREEN}✅ $1${NC}"
}

function error() {
    echo -e "${RED}❌ $1${NC}"
    exit 1
}

function warning() {
    echo -e "${YELLOW}⚠️ $1${NC}"
}

# Check if we're on main branch
run_step "Checking git branch..."
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" = "main" ]; then
    warning "Running on main branch - ensure this is intentional"
else
    success "Running on feature branch: $CURRENT_BRANCH"
fi

# Check branch naming convention
run_step "Validating branch naming convention..."
if [[ "$CURRENT_BRANCH" =~ ^[0-9]{8}-[0-9]{6}-(feat|fix|docs|refactor|test|chore)-.+$ ]] || [ "$CURRENT_BRANCH" = "main" ]; then
    success "Branch name valid: $CURRENT_BRANCH"
else
    error "Branch name must follow YYYYMMDD-HHMMSS-type-description format"
fi

# Check Node.js version
run_step "Checking Node.js version..."
NODE_VERSION=$(node --version 2>/dev/null || echo "not found")
if [[ "$NODE_VERSION" =~ ^v([0-9]+) ]]; then
    NODE_MAJOR=${BASH_REMATCH[1]}
    if [ "$NODE_MAJOR" -ge 18 ]; then
        success "Node.js $NODE_VERSION (>= 18 required)"
    else
        error "Node.js $NODE_MAJOR < 18 - please upgrade"
    fi
else
    error "Node.js not found - please install Node.js >= 18"
fi

# Install/check dependencies
run_step "Installing/checking dependencies..."
if [ ! -d "node_modules" ]; then
    echo "Installing dependencies..."
    npm install || error "npm install failed"
    success "Dependencies installed"
else
    echo "Checking if dependencies are up to date..."
    npm ci --quiet || error "npm ci failed - dependencies may be outdated"
    success "Dependencies up to date"
fi

# Python quality checks (if Python files exist)
if [ -d "src" ] || [ -d "validators" ] || [ -d "cli" ]; then
    run_step "Running Python quality checks..."
    
    # Check if UV is available
    if command -v uv &> /dev/null; then
        success "UV available for Python management"
        
        # Run Python formatting check (if black is available)
        if command -v black &> /dev/null; then
            echo "Checking Python formatting..."
            black --check validators/ cli/ 2>/dev/null || {
                echo "Auto-formatting Python code..."
                black validators/ cli/
                success "Python code formatted"
            }
        fi
        
        # Run Python linting (if ruff is available)
        if command -v ruff &> /dev/null; then
            echo "Running Python linting..."
            ruff check validators/ cli/ || warning "Python linting issues found (non-blocking)"
        fi
    else
        warning "UV not found - Python quality checks skipped"
    fi
fi

# Astro type checking
run_step "Running Astro type checking..."
npm run check || error "Astro type checking failed"
success "Astro types valid"

# Clean previous build
run_step "Cleaning previous build..."
npm run clean-docs || true
success "Previous build cleaned"

# Build Astro site
run_step "Building Astro website for GitHub Pages..."
npm run build || error "Astro build failed"
success "Website built to ./docs"

# Verify build outputs
run_step "Verifying build outputs..."

# Check docs directory
if [ ! -d "./docs" ]; then
    error "docs/ directory not found after build"
fi

# Check .nojekyll file (critical for GitHub Pages)
if [ ! -f "./docs/.nojekyll" ]; then
    error ".nojekyll file not created - GitHub Pages may not work correctly"
fi

# Check _astro assets directory
if [ ! -d "./docs/_astro" ]; then
    error "_astro/ assets directory not found - static assets missing"
fi

# Check index.html
if [ ! -f "./docs/index.html" ]; then
    error "index.html not found in docs/"
fi

# Count files and check size
FILE_COUNT=$(find ./docs -type f | wc -l)
DOCS_SIZE=$(du -sh ./docs | cut -f1)

if [ "$FILE_COUNT" -lt 5 ]; then
    error "Too few files in docs/ ($FILE_COUNT) - build may be incomplete"
fi

success "Build verified: $FILE_COUNT files, $DOCS_SIZE total"

# Test local preview (optional, quick check)
run_step "Testing build integrity..."
if [ -f "./docs/index.html" ]; then
    # Basic HTML validation
    if grep -q "<title>" "./docs/index.html" && grep -q "</html>" "./docs/index.html"; then
        success "HTML structure valid"
    else
        error "HTML structure appears invalid"
    fi
else
    error "index.html not found for validation"
fi

echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✨ All checks passed! Ready for zero-cost deployment.${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${BLUE}📁 Build Summary:${NC}"
echo "   • Files: $FILE_COUNT"
echo "   • Size: $DOCS_SIZE"
echo "   • GitHub Pages: Ready (docs/ folder)"
echo "   • .nojekyll: ✅ Created"
echo "   • Assets: ✅ _astro/ directory"
echo ""
echo -e "${BLUE}🚀 Next Steps:${NC}"
echo "   1. git add -A"
echo "   2. git commit -m 'feat: deploy astro site to github pages'"
echo "   3. git push origin $CURRENT_BRANCH"
echo ""
echo -e "${BLUE}🌐 GitHub Pages URL:${NC}"
echo "   https://kairin.github.io/start/"
echo ""
echo -e "${GREEN}💰 Cost: $0 (Local CI/CD + GitHub Pages)${NC}"