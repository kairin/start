#!/usr/bin/env python3
"""
UV-First Python Validator

Validates that Python projects strictly follow UV-first requirements:
- Use UV for all Python operations 
- Use system python3 only
- No legacy pip/venv/conda usage
- Proper pyproject.toml configuration
"""

import subprocess
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
import re

class UVValidator:
    """Validates UV-first Python project compliance"""
    
    def __init__(self, standards_dir: Path = None):
        if standards_dir is None:
            self.standards_dir = Path(__file__).parent.parent / "standards"
        else:
            self.standards_dir = Path(standards_dir)
            
        self.uv_requirements = self._load_uv_requirements()
    
    def _load_uv_requirements(self) -> Dict[str, Any]:
        """Load UV requirements from YAML"""
        uv_file = self.standards_dir / "python-uv-requirements.yaml"
        if not uv_file.exists():
            raise FileNotFoundError(f"UV requirements file not found: {uv_file}")
            
        with open(uv_file, 'r') as f:
            return yaml.safe_load(f)
    
    def check_uv_installed(self) -> Tuple[bool, str]:
        """Check if UV is installed and accessible"""
        try:
            result = subprocess.run(['uv', '--version'], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                version = result.stdout.strip()
                return True, f"UV installed: {version}"
            else:
                return False, "UV command failed"
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return False, "UV not installed or not in PATH"
    
    def validate_project_structure(self, project_path: Path) -> Tuple[List[str], List[str]]:
        """Validate UV-compliant project structure"""
        passed = []
        failed = []
        
        # Check required files
        required_files = self.uv_requirements.get("required_files", [])
        for file_spec in required_files:
            file_path = project_path / file_spec["path"]
            
            if file_spec.get("type") == "directory":
                if file_path.is_dir():
                    passed.append(f"✅ {file_spec['path']} directory exists")
                else:
                    failed.append(f"❌ {file_spec['path']} directory missing")
            else:
                if file_path.exists():
                    passed.append(f"✅ {file_spec['path']} exists")
                else:
                    failed.append(f"❌ {file_spec['path']} missing")
        
        # Check forbidden files
        forbidden_files = self.uv_requirements.get("forbidden_files", [])
        for file_spec in forbidden_files:
            file_path = project_path / file_spec["path"]
            
            if file_path.exists():
                reason = file_spec.get("reason", "Forbidden file")
                alternative = file_spec.get("alternative", "Use UV-compatible approach")
                failed.append(f"❌ {file_spec['path']} found - {reason}")
                failed.append(f"   → Use instead: {alternative}")
            else:
                passed.append(f"✅ No forbidden file: {file_spec['path']}")
        
        return passed, failed
    
    def validate_pyproject_toml(self, project_path: Path) -> Tuple[List[str], List[str]]:
        """Validate pyproject.toml for UV compliance"""
        passed = []
        failed = []
        
        pyproject_path = project_path / "pyproject.toml"
        
        if not pyproject_path.exists():
            failed.append("❌ pyproject.toml missing (REQUIRED for UV projects)")
            return passed, failed
        
        try:
            import tomllib
        except ImportError:
            try:
                import tomli as tomllib
            except ImportError:
                failed.append("❌ Cannot parse pyproject.toml - install tomllib/tomli")
                return passed, failed
        
        try:
            with open(pyproject_path, 'rb') as f:
                pyproject_data = tomllib.load(f)
            
            # Check for project section
            if "project" in pyproject_data:
                passed.append("✅ [project] section exists")
                
                project_section = pyproject_data["project"]
                required_fields = ["name", "version", "description"]
                
                for field in required_fields:
                    if field in project_section:
                        passed.append(f"✅ project.{field} defined")
                    else:
                        failed.append(f"❌ project.{field} missing")
                
                # Check dependencies section
                if "dependencies" in project_section:
                    passed.append("✅ project.dependencies defined")
                else:
                    failed.append("❌ project.dependencies missing (use instead of requirements.txt)")
                    
            else:
                failed.append("❌ [project] section missing in pyproject.toml")
            
            # Check for build system
            if "build-system" in pyproject_data:
                passed.append("✅ [build-system] section exists")
            else:
                failed.append("❌ [build-system] section missing")
                
        except Exception as e:
            failed.append(f"❌ Error parsing pyproject.toml: {e}")
        
        return passed, failed
    
    def validate_gitignore(self, project_path: Path) -> Tuple[List[str], List[str]]:
        """Validate .gitignore has UV-specific entries"""
        passed = []
        failed = []
        
        gitignore_path = project_path / ".gitignore"
        
        if not gitignore_path.exists():
            failed.append("❌ .gitignore missing")
            return passed, failed
        
        try:
            gitignore_content = gitignore_path.read_text()
            
            required_entries = [".venv/", "*.egg-info/", "__pycache__/"]
            
            for entry in required_entries:
                if entry in gitignore_content:
                    passed.append(f"✅ .gitignore contains {entry}")
                else:
                    failed.append(f"❌ .gitignore missing {entry}")
                    
        except Exception as e:
            failed.append(f"❌ Error reading .gitignore: {e}")
        
        return passed, failed
    
    def validate_agents_md_uv_section(self, project_path: Path) -> Tuple[List[str], List[str]]:
        """Validate AGENTS.md has UV-first requirements section"""
        passed = []
        failed = []
        
        agents_path = project_path / "AGENTS.md"
        
        if not agents_path.exists():
            failed.append("❌ AGENTS.md missing")
            return passed, failed
        
        try:
            agents_content = agents_path.read_text()
            
            uv_indicators = [
                "UV-ONLY", 
                "uv pip install",
                "uv run",
                "MANDATORY",
                "UV-First"
            ]
            
            found_indicators = []
            for indicator in uv_indicators:
                if indicator in agents_content:
                    found_indicators.append(indicator)
            
            if len(found_indicators) >= 3:
                passed.append("✅ AGENTS.md contains UV-first requirements")
            else:
                failed.append("❌ AGENTS.md missing UV-first requirements section")
                failed.append(f"   → Found only: {found_indicators}")
                failed.append("   → Must include UV-ONLY, uv pip install, uv run instructions")
            
            # Check for forbidden patterns
            forbidden_patterns = [
                "pip install",
                "python -m pip", 
                "python script.py",
                "pytest",
                "python -m venv"
            ]
            
            for pattern in forbidden_patterns:
                if pattern in agents_content and "uv run" not in agents_content[agents_content.find(pattern)-20:agents_content.find(pattern)+50]:
                    failed.append(f"❌ AGENTS.md contains forbidden pattern: {pattern}")
                    failed.append("   → Must be prefixed with 'uv run' or replaced with UV equivalent")
                    
        except Exception as e:
            failed.append(f"❌ Error reading AGENTS.md: {e}")
        
        return passed, failed
    
    def check_for_legacy_files(self, project_path: Path) -> Tuple[List[str], List[str]]:
        """Check for legacy Python dependency files that should not exist"""
        passed = []
        failed = []
        
        legacy_files = [
            "requirements.txt",
            "requirements-dev.txt", 
            "dev-requirements.txt",
            "setup.py",
            "setup.cfg",
            "Pipfile",
            "Pipfile.lock",
            "environment.yml",  # conda
            "conda.yaml"
        ]
        
        for legacy_file in legacy_files:
            file_path = project_path / legacy_file
            if file_path.exists():
                failed.append(f"❌ Legacy file found: {legacy_file}")
                failed.append("   → Remove and migrate to pyproject.toml with UV")
            else:
                passed.append(f"✅ No legacy file: {legacy_file}")
        
        return passed, failed
    
    def validate_uv_compliance(self, project_path: str) -> Dict[str, Any]:
        """Perform complete UV compliance validation"""
        project_path = Path(project_path)
        
        if not project_path.exists():
            return {
                "error": f"Project path does not exist: {project_path}",
                "uv_compliant": False
            }
        
        # Check if this is a Python project
        if not (project_path / "pyproject.toml").exists() and not any([
            (project_path / f).exists() for f in ["setup.py", "requirements.txt", "Pipfile"]
        ]):
            return {
                "error": "Not a Python project",
                "uv_compliant": False
            }
        
        # Run all UV validations
        all_passed = []
        all_failed = []
        
        # Check UV installation
        uv_installed, uv_message = self.check_uv_installed()
        if uv_installed:
            all_passed.append(f"✅ {uv_message}")
        else:
            all_failed.append(f"❌ {uv_message}")
        
        # Project structure validation
        passed, failed = self.validate_project_structure(project_path)
        all_passed.extend(passed)
        all_failed.extend(failed)
        
        # pyproject.toml validation
        passed, failed = self.validate_pyproject_toml(project_path)
        all_passed.extend(passed)
        all_failed.extend(failed)
        
        # .gitignore validation
        passed, failed = self.validate_gitignore(project_path)
        all_passed.extend(passed)
        all_failed.extend(failed)
        
        # AGENTS.md UV section validation
        passed, failed = self.validate_agents_md_uv_section(project_path)
        all_passed.extend(passed)
        all_failed.extend(failed)
        
        # Legacy files check
        passed, failed = self.check_for_legacy_files(project_path)
        all_passed.extend(passed)
        all_failed.extend(failed)
        
        # Calculate compliance
        total_checks = len(all_passed) + len(all_failed)
        score = len(all_passed)
        percentage = (score / total_checks * 100) if total_checks > 0 else 0
        
        return {
            "project_path": str(project_path),
            "uv_compliant": percentage >= 90,
            "passed": all_passed,
            "failed": all_failed,
            "score": score,
            "total": total_checks,
            "percentage": percentage,
            "compliance_level": self._get_compliance_level(percentage)
        }
    
    def _get_compliance_level(self, percentage: float) -> str:
        """Get compliance level based on percentage score"""
        if percentage >= 95:
            return "Fully UV-Compliant"
        elif percentage >= 80:
            return "Mostly UV-Compliant"  
        elif percentage >= 60:
            return "Partially UV-Compliant"
        else:
            return "Non-UV-Compliant"

def main():
    """CLI interface for UV validation"""
    import sys
    import argparse
    import json
    
    parser = argparse.ArgumentParser(description="UV-First Python Project Validator")
    parser.add_argument("project_path", help="Path to Python project to validate")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    validator = UVValidator()
    result = validator.validate_uv_compliance(args.project_path)
    
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if "error" in result:
            print(f"Error: {result['error']}")
            sys.exit(1)
        
        print(f"Project: {result['project_path']}")
        print(f"UV Compliance: {'✅ YES' if result['uv_compliant'] else '❌ NO'}")
        print(f"Score: {result['score']}/{result['total']} ({result['percentage']:.1f}%)")
        print(f"Level: {result['compliance_level']}")
        print()
        
        if result['passed']:
            print("✅ UV Compliance Checks Passed:")
            for check in result['passed']:
                print(f"  {check}")
        
        if result['failed']:
            print("\n❌ UV Compliance Issues:")  
            for check in result['failed']:
                print(f"  {check}")
        
        if result['uv_compliant']:
            print(f"\n🎉 Project is UV-compliant!")
            sys.exit(0)
        else:
            print(f"\n⚠️ Project must be updated for UV compliance")
            sys.exit(1)

if __name__ == "__main__":
    main()