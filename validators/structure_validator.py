#!/usr/bin/env python3
"""
Project Structure Validator for Phase 001

Validates that projects meet the quality standards defined in 
standards/project-structure.yaml
"""

import yaml
import json
from pathlib import Path
from typing import Dict, List, Tuple, Any

class ProjectValidator:
    """Validates project structure and quality compliance"""
    
    def __init__(self, standards_dir: Path = None):
        if standards_dir is None:
            # Default to standards directory relative to this file
            self.standards_dir = Path(__file__).parent.parent / "standards"
        else:
            self.standards_dir = Path(standards_dir)
            
        self.standards = self._load_standards()
    
    def _load_standards(self) -> Dict[str, Any]:
        """Load project structure standards from YAML"""
        standards_file = self.standards_dir / "project-structure.yaml"
        if not standards_file.exists():
            raise FileNotFoundError(f"Standards file not found: {standards_file}")
            
        with open(standards_file, 'r') as f:
            return yaml.safe_load(f)
    
    def detect_project_type(self, project_path: Path) -> str:
        """Detect the type of project based on key files"""
        if (project_path / "astro.config.mjs").exists():
            return "astro"
        elif (project_path / "pyproject.toml").exists():
            return "python"  
        elif (project_path / "package.json").exists():
            return "nodejs"
        else:
            return "unknown"
    
    def validate_required_files(self, project_path: Path) -> Tuple[List[str], List[str]]:
        """Validate required files exist. Returns (passed, failed)"""
        passed = []
        failed = []
        
        # Check universal required files
        for file_spec in self.standards.get("required_files", []):
            file_path = project_path / file_spec["path"]
            
            if file_spec.get("type") == "directory":
                if file_path.is_dir():
                    passed.append(f"✅ {file_spec['path']} (directory)")
                else:
                    failed.append(f"❌ {file_spec['path']} (directory missing)")
            else:
                if file_path.exists() and file_path.is_file():
                    passed.append(f"✅ {file_spec['path']}")
                else:
                    failed.append(f"❌ {file_spec['path']}")
        
        return passed, failed
    
    def validate_project_type_requirements(self, project_path: Path, project_type: str) -> Tuple[List[str], List[str]]:
        """Validate project-type specific requirements"""
        passed = []
        failed = []
        
        if project_type == "unknown":
            failed.append("❌ Cannot determine project type")
            return passed, failed
            
        type_requirements = self.standards.get("project_types", {}).get(project_type, {})
        
        # Check required files for this project type
        for file_spec in type_requirements.get("required_files", []):
            file_path = project_path / file_spec["path"]
            
            if file_spec.get("type") == "directory":
                if file_path.is_dir():
                    passed.append(f"✅ {file_spec['path']} ({project_type} directory)")
                else:
                    failed.append(f"❌ {file_spec['path']} ({project_type} directory missing)")
            else:
                if file_path.exists() and file_path.is_file():
                    passed.append(f"✅ {file_spec['path']} ({project_type} file)")
                else:
                    failed.append(f"❌ {file_spec['path']} ({project_type} file missing)")
        
        # Check forbidden files for Python projects (UV enforcement)
        if project_type == "python":
            forbidden_files = type_requirements.get("forbidden_files", [])
            for file_spec in forbidden_files:
                file_path = project_path / file_spec["path"]
                if file_path.exists():
                    reason = file_spec.get("reason", "Forbidden for UV projects")
                    failed.append(f"❌ {file_spec['path']} - {reason}")
                else:
                    passed.append(f"✅ No forbidden file: {file_spec['path']}")
        
        return passed, failed
    
    def validate_agents_md(self, project_path: Path) -> Tuple[List[str], List[str]]:
        """Validate AGENTS.md file content"""
        passed = []
        failed = []
        
        agents_file = project_path / "AGENTS.md"
        
        if not agents_file.exists():
            failed.append("❌ AGENTS.md file missing")
            return passed, failed
        
        try:
            content = agents_file.read_text()
            
            # Basic content checks
            required_sections = [
                "# ",  # Title
                "## ",  # At least one section header
            ]
            
            for section in required_sections:
                if section in content:
                    passed.append(f"✅ AGENTS.md has proper structure")
                else:
                    failed.append(f"❌ AGENTS.md missing proper structure")
                    break
            
            # Check if not just a template/placeholder
            if len(content.strip()) < 100:
                failed.append("❌ AGENTS.md appears to be empty or placeholder")
            elif "TODO" in content or "PLACEHOLDER" in content.upper():
                failed.append("❌ AGENTS.md contains TODO/placeholder content")
            else:
                passed.append("✅ AGENTS.md has meaningful content")
                
        except Exception as e:
            failed.append(f"❌ Error reading AGENTS.md: {e}")
        
        return passed, failed
    
    def validate_git_setup(self, project_path: Path) -> Tuple[List[str], List[str]]:
        """Validate git repository setup"""
        passed = []
        failed = []
        
        git_dir = project_path / ".git"
        gitignore_file = project_path / ".gitignore"
        
        if git_dir.exists() and git_dir.is_dir():
            passed.append("✅ Git repository initialized")
        else:
            failed.append("❌ Not a git repository")
            return passed, failed
        
        if gitignore_file.exists():
            passed.append("✅ .gitignore file present")
        else:
            failed.append("❌ .gitignore file missing")
        
        return passed, failed
    
    def audit_project(self, project_path: str) -> Dict[str, Any]:
        """Perform complete project audit"""
        project_path = Path(project_path)
        
        if not project_path.exists():
            return {
                "error": f"Project path does not exist: {project_path}",
                "score": 0,
                "total": 0
            }
        
        # Detect project type
        project_type = self.detect_project_type(project_path)
        
        # Run all validations
        all_passed = []
        all_failed = []
        
        # Required files validation
        passed, failed = self.validate_required_files(project_path)
        all_passed.extend(passed)
        all_failed.extend(failed)
        
        # Project type specific validation
        passed, failed = self.validate_project_type_requirements(project_path, project_type)
        all_passed.extend(passed)
        all_failed.extend(failed)
        
        # AGENTS.md validation
        passed, failed = self.validate_agents_md(project_path)
        all_passed.extend(passed)
        all_failed.extend(failed)
        
        # Git setup validation
        passed, failed = self.validate_git_setup(project_path)
        all_passed.extend(passed)
        all_failed.extend(failed)
        
        # Calculate score
        total_checks = len(all_passed) + len(all_failed)
        score = len(all_passed)
        percentage = (score / total_checks * 100) if total_checks > 0 else 0
        
        return {
            "project_path": str(project_path),
            "project_type": project_type,
            "passed": all_passed,
            "failed": all_failed,
            "score": score,
            "total": total_checks,
            "percentage": percentage,
            "quality_level": self._get_quality_level(percentage)
        }
    
    def _get_quality_level(self, percentage: float) -> str:
        """Get quality level based on percentage score"""
        if percentage >= 90:
            return "Excellent"
        elif percentage >= 75:
            return "Good"
        elif percentage >= 60:
            return "Acceptable"
        elif percentage >= 40:
            return "Needs Improvement"
        else:
            return "Poor"

def main():
    """CLI interface for the validator"""
    import sys
    import argparse
    
    parser = argparse.ArgumentParser(description="Project Structure Validator")
    parser.add_argument("project_path", help="Path to project to validate")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    
    args = parser.parse_args()
    
    validator = ProjectValidator()
    result = validator.audit_project(args.project_path)
    
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if "error" in result:
            print(f"Error: {result['error']}")
            sys.exit(1)
        
        print(f"Project: {result['project_path']}")
        print(f"Type: {result['project_type']}")
        print(f"Score: {result['score']}/{result['total']} ({result['percentage']:.1f}%)")
        print(f"Quality: {result['quality_level']}")
        print()
        
        if result['passed']:
            print("✅ Passed Checks:")
            for check in result['passed']:
                print(f"  {check}")
        
        if result['failed']:
            print("\n❌ Failed Checks:")  
            for check in result['failed']:
                print(f"  {check}")
        
        if result['percentage'] >= 75:
            print(f"\n🎉 Project meets quality standards!")
            sys.exit(0)
        else:
            print(f"\n⚠️ Project needs improvement to meet quality standards")
            sys.exit(1)

if __name__ == "__main__":
    main()