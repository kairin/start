#!/usr/bin/env python3
"""
Start - Phase 001 Project Quality Controller CLI

A unified command-line interface for managing project quality, standards,
and development environment consistency across all your projects.
"""

import argparse
import sys
import os
import subprocess
from pathlib import Path

# Colors for output
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    NC = '\033[0m'  # No Color

def print_status(message):
    print(f"{Colors.BLUE}[INFO]{Colors.NC} {message}")

def print_success(message):
    print(f"{Colors.GREEN}[SUCCESS]{Colors.NC} {message}")

def print_warning(message):
    print(f"{Colors.YELLOW}[WARNING]{Colors.NC} {message}")

def print_error(message):
    print(f"{Colors.RED}[ERROR]{Colors.NC} {message}")

def print_header(message):
    print(f"{Colors.PURPLE}=== {message} ==={Colors.NC}")

def get_start_root():
    """Get the root directory of the start project"""
    return Path(__file__).parent.parent

def run_command(command, cwd=None, capture_output=False):
    """Run a shell command"""
    try:
        if capture_output:
            result = subprocess.run(command, shell=True, cwd=cwd, 
                                  capture_output=True, text=True)
            return result.stdout.strip(), result.stderr.strip(), result.returncode
        else:
            result = subprocess.run(command, shell=True, cwd=cwd)
            return "", "", result.returncode
    except Exception as e:
        return "", str(e), 1

def cmd_system(args):
    """System management commands"""
    start_root = get_start_root()
    script_path = start_root / "scripts" / "system-update.sh"
    
    if not script_path.exists():
        print_error(f"System update script not found at {script_path}")
        return 1
    
    if args.system_command == "update":
        print_header("System Update")
        _, _, code = run_command(f"{script_path} update")
        return code
    elif args.system_command == "check":
        print_header("System Check")
        _, _, code = run_command(f"{script_path} check")
        return code
    elif args.system_command == "projects":
        print_header("Project Check")
        _, _, code = run_command(f"{script_path} projects")
        return code
    else:
        print_error(f"Unknown system command: {args.system_command}")
        return 1

def cmd_templates(args):
    """Template management commands"""
    start_root = get_start_root()
    templates_dir = start_root / "templates"
    
    if args.template_command == "list":
        print_header("Available Project Templates")
        if templates_dir.exists():
            templates = [d.name for d in templates_dir.iterdir() if d.is_dir()]
            if templates:
                for template in templates:
                    print(f"  📋 {template}")
            else:
                print_warning("No templates found")
        else:
            print_error("Templates directory not found")
        return 0
    else:
        print_warning(f"Template command '{args.template_command}' not implemented yet")
        return 0

def cmd_audit(args):
    """Project audit commands"""
    if args.project:
        print_header(f"Auditing Project: {args.project}")
        project_path = Path(args.project)
        
        if not project_path.exists():
            print_error(f"Project path does not exist: {args.project}")
            return 1
        
        # Import validators
        sys.path.append(str(get_start_root() / "validators"))
        from structure_validator import ProjectValidator
        
        # Check if it's a Python project for UV validation
        is_python_project = (project_path / "pyproject.toml").exists() or \
                           (project_path / "setup.py").exists() or \
                           (project_path / "requirements.txt").exists()
        
        # Basic structure audit
        validator = ProjectValidator()
        result = validator.audit_project(args.project)
        
        print(f"Project Type: {result['project_type']}")
        print(f"Structure Score: {result['score']}/{result['total']} ({result['percentage']:.1f}%)")
        print(f"Quality Level: {result['quality_level']}")
        print()
        
        if result['passed']:
            for check in result['passed']:
                print(check)
        
        if result['failed']:
            for check in result['failed']:
                print(check)
        
        # UV compliance check for Python projects  
        if is_python_project:
            print("\n" + "="*50)
            print_header("UV-First Python Compliance Check")
            
            try:
                from uv_validator import UVValidator
                uv_validator = UVValidator()
                uv_result = uv_validator.validate_uv_compliance(args.project)
                
                print(f"UV Compliance: {'✅ YES' if uv_result['uv_compliant'] else '❌ NO'}")
                print(f"UV Score: {uv_result['score']}/{uv_result['total']} ({uv_result['percentage']:.1f}%)")
                print(f"Compliance Level: {uv_result['compliance_level']}")
                print()
                
                if uv_result['failed']:
                    print("❌ UV Compliance Issues:")
                    for issue in uv_result['failed']:
                        print(f"  {issue}")
                
                # Overall compliance
                if not uv_result['uv_compliant']:
                    print_error("⚠️ Python project MUST be UV-compliant")
                    return 1
                else:
                    print_success("✅ Python project is UV-compliant")
                    
            except ImportError as e:
                print_error(f"UV validator not available: {e}")
                return 1
        
        # Overall result
        if result['percentage'] >= 75 and (not is_python_project or uv_result.get('uv_compliant', False)):
            print_success("🎉 Project meets all quality standards!")
            return 0
        else:
            print_warning("⚠️ Project needs improvement to meet quality standards")
            return 1
    else:
        print_error("Project path required for audit")
        return 1

def cmd_bootstrap(args):
    """Bootstrap new project from template"""
    print_warning("Bootstrap command not implemented yet in Phase 001")
    print_status("This will be available in Phase 002 with spec-kit integration")
    return 0

def cmd_standards(args):
    """Standards management commands"""
    print_warning("Standards management not implemented yet in Phase 001")
    print_status("This will be available in Phase 002 with full validation")
    return 0

def cmd_status(args):
    """Show overall system status"""
    print_header("Start - Project Quality Controller Status")
    
    start_root = get_start_root()
    print(f"📂 Start Root: {start_root}")
    
    # Check directories
    dirs_to_check = ["templates", "standards", "scripts", "validators", "cli", "docs"]
    for dir_name in dirs_to_check:
        dir_path = start_root / dir_name
        if dir_path.exists():
            print_success(f"✅ {dir_name}/ directory")
        else:
            print_warning(f"❌ {dir_name}/ directory")
    
    # Check key files
    key_files = [
        "scripts/system-update.sh",
        "standards/agents-md.template",
        "cli/start.py"
    ]
    
    for file_path in key_files:
        full_path = start_root / file_path
        if full_path.exists():
            print_success(f"✅ {file_path}")
        else:
            print_warning(f"❌ {file_path}")
    
    print("\n" + "="*50)
    print("Phase 001 Status: Basic structure complete")
    print("Next: Phase 002 - spec-kit integration")
    
    return 0

def main():
    parser = argparse.ArgumentParser(
        description="Start - Phase 001 Project Quality Controller",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  start status                           # Show system status
  start system check                     # Check for system updates
  start system update                    # Update development tools
  start audit --project /path/to/project # Audit project quality
  start templates list                   # List available templates

Phase 001 Features:
  ✅ System management (NVM, Oh My Zsh)
  ✅ Basic project auditing
  ✅ Template structure (ready for Phase 002)
  ⏳ Bootstrap (Phase 002)
  ⏳ Full standards validation (Phase 002)
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Status command
    status_parser = subparsers.add_parser('status', help='Show system status')
    
    # System management commands  
    system_parser = subparsers.add_parser('system', help='System management')
    system_parser.add_argument('system_command', 
                              choices=['check', 'update', 'projects'],
                              help='System command to run')
    
    # Template management
    templates_parser = subparsers.add_parser('templates', help='Template management')
    templates_parser.add_argument('template_command',
                                 choices=['list'],
                                 help='Template command to run')
    
    # Project audit
    audit_parser = subparsers.add_parser('audit', help='Audit project quality')
    audit_parser.add_argument('--project', '-p', required=True,
                             help='Path to project to audit')
    
    # Bootstrap (placeholder for Phase 002)
    bootstrap_parser = subparsers.add_parser('bootstrap', help='Bootstrap new project')
    bootstrap_parser.add_argument('--template', '-t', help='Template name')
    bootstrap_parser.add_argument('--name', '-n', help='Project name')
    
    # Standards (placeholder for Phase 002)
    standards_parser = subparsers.add_parser('standards', help='Standards management')
    standards_parser.add_argument('standards_command', 
                                 choices=['sync', 'apply', 'check'],
                                 help='Standards command')
    
    args = parser.parse_args()
    
    if not args.command:
        args.command = 'status'
    
    # Route to appropriate command handler
    if args.command == 'status':
        return cmd_status(args)
    elif args.command == 'system':
        return cmd_system(args)
    elif args.command == 'templates':
        return cmd_templates(args)
    elif args.command == 'audit':
        return cmd_audit(args)
    elif args.command == 'bootstrap':
        return cmd_bootstrap(args)
    elif args.command == 'standards':
        return cmd_standards(args)
    else:
        print_error(f"Unknown command: {args.command}")
        return 1

if __name__ == "__main__":
    sys.exit(main())