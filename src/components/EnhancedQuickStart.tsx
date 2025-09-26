import React, { useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { 
  Terminal, 
  Play, 
  CheckCircle2, 
  GitBranch, 
  Zap,
  Copy,
  ExternalLink,
  ArrowRight,
  Clock,
  Target,
  Rocket
} from 'lucide-react';

const EnhancedQuickStart = () => {
  const [copiedIndex, setCopiedIndex] = useState<number | null>(null);

  const copyToClipboard = async (text: string, index: number) => {
    try {
      await navigator.clipboard.writeText(text);
      setCopiedIndex(index);
      setTimeout(() => setCopiedIndex(null), 2000);
    } catch (err) {
      console.error('Failed to copy text: ', err);
    }
  };

  const commands = [
    {
      category: "System Status & Updates",
      icon: <Zap className="w-5 h-5" />,
      color: "text-green-400",
      commands: [
        { cmd: "python3 cli/start.py status", desc: "Check overall system status" },
        { cmd: "python3 cli/start.py system update", desc: "Update development tools" },
        { cmd: "python3 cli/start.py system projects", desc: "Monitor project repositories" }
      ]
    },
    {
      category: "Quality Control",
      icon: <CheckCircle2 className="w-5 h-5" />,
      color: "text-blue-400",
      commands: [
        { cmd: "python3 cli/start.py audit --project /path/to/project", desc: "Audit project quality" },
        { cmd: "python3 cli/start.py templates list", desc: "List available templates" }
      ]
    },
    {
      category: "Git Workflow",
      icon: <GitBranch className="w-5 h-5" />,
      color: "text-purple-400",
      commands: [
        { cmd: 'BRANCH="$(date +%Y%m%d-%H%M%S)-feat-name"', desc: "Create properly named branch" },
        { cmd: "git checkout -b $BRANCH", desc: "Switch to new branch" },
        { cmd: "git push -u origin $BRANCH", desc: "Push and track branch" },
        { cmd: 'gh pr create --title "feat: description"', desc: "Create pull request" }
      ]
    }
  ];

  const phases = [
    {
      phase: "Phase 001",
      status: "Complete",
      icon: <CheckCircle2 className="w-6 h-6" />,
      color: "text-green-400",
      bgColor: "bg-green-400/10",
      borderColor: "border-green-400/30",
      items: [
        "UV-First Python: Mandatory compliance",
        "Quality Controller: Complete CLI system", 
        "System Management: Enhanced updater",
        "Git Standards: Branch naming & preservation",
        "AI Integration: Unified AGENTS.md"
      ]
    },
    {
      phase: "Phase 002",
      status: "Planned",
      icon: <Clock className="w-6 h-6" />,
      color: "text-blue-400",
      bgColor: "bg-blue-400/10",
      borderColor: "border-blue-400/30",
      items: [
        "spec-kit Integration: Enhanced automation",
        "Project Bootstrapping: Automated creation",
        "Cross-Project Sync: Standards enforcement", 
        "Advanced Validation: Complete lifecycle"
      ]
    },
    {
      phase: "Deployment",
      status: "Zero-Cost",
      icon: <Rocket className="w-6 h-6" />,
      color: "text-purple-400",
      bgColor: "bg-purple-400/10", 
      borderColor: "border-purple-400/30",
      items: [
        "Local CI/CD: No GitHub Actions charges",
        "GitHub Pages: Free hosting",
        "Astro.build: Optimized performance",
        "Professional: Enterprise-grade quality"
      ]
    }
  ];

  return (
    <section id="quick-start" className="py-24 bg-gradient-to-b from-background to-background/50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Header */}
        <div className="text-center mb-16 animate-fade-in">
          <div className="inline-flex items-center px-4 py-2 rounded-full bg-primary/10 border border-primary/20 text-primary text-sm font-medium mb-6">
            <Terminal className="w-4 h-4 mr-2" />
            Get Started
          </div>
          <h2 className="text-4xl lg:text-5xl font-bold text-foreground mb-6">
            Quick Start Guide
          </h2>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto leading-relaxed">
            Get started with the Start Project Quality Controller in minutes with our comprehensive CLI system
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">
          
          {/* Commands Section */}
          <div className="space-y-6 animate-slide-in-left">
            {commands.map((section, sectionIndex) => (
              <Card key={sectionIndex} className="bg-card/50 backdrop-blur-sm border-border hover:shadow-lg transition-all duration-300">
                <CardHeader>
                  <CardTitle className="flex items-center text-lg">
                    <span className={`${section.color} mr-3`}>{section.icon}</span>
                    {section.category}
                  </CardTitle>
                </CardHeader>
                <CardContent className="space-y-3">
                  {section.commands.map((command, cmdIndex) => {
                    const globalIndex = sectionIndex * 10 + cmdIndex;
                    return (
                      <div key={cmdIndex} className="group">
                        <div className="text-xs text-muted-foreground mb-1">{command.desc}</div>
                        <div className="relative bg-muted/50 rounded-lg p-3 font-mono text-sm">
                          <code className={`${section.color} pr-10`}>{command.cmd}</code>
                          <Button
                            size="icon"
                            variant="ghost"
                            className="absolute right-2 top-1/2 -translate-y-1/2 h-6 w-6 opacity-0 group-hover:opacity-100 transition-opacity duration-200"
                            onClick={() => copyToClipboard(command.cmd, globalIndex)}
                          >
                            {copiedIndex === globalIndex ? (
                              <CheckCircle2 className="w-3 h-3 text-green-400" />
                            ) : (
                              <Copy className="w-3 h-3" />
                            )}
                          </Button>
                        </div>
                      </div>
                    );
                  })}
                </CardContent>
              </Card>
            ))}
          </div>

          {/* Phases Section */}
          <div className="space-y-6 animate-slide-in-right">
            {phases.map((phase, index) => (
              <Card key={index} className={`${phase.bgColor} border ${phase.borderColor} hover:shadow-lg transition-all duration-300 hover:-translate-y-1`}>
                <CardHeader>
                  <div className="flex items-center justify-between">
                    <CardTitle className="flex items-center text-lg">
                      <span className={`${phase.color} mr-3`}>{phase.icon}</span>
                      {phase.phase}
                    </CardTitle>
                    <span className={`px-2 py-1 rounded-full text-xs font-medium ${phase.color} bg-current/10`}>
                      {phase.status}
                    </span>
                  </div>
                </CardHeader>
                <CardContent>
                  <ul className="space-y-2">
                    {phase.items.map((item, i) => (
                      <li key={i} className="flex items-start text-sm">
                        <div className={`w-1.5 h-1.5 rounded-full ${phase.color.replace('text-', 'bg-')} mr-3 mt-2 flex-shrink-0`} />
                        <span className="text-muted-foreground">{item}</span>
                      </li>
                    ))}
                  </ul>
                  {phase.phase === "Phase 002" && (
                    <Button 
                      variant="ghost" 
                      size="sm"
                      className={`w-full mt-4 ${phase.color} hover:bg-accent transition-all duration-300`}
                    >
                      Coming Soon
                      <ArrowRight className="w-4 h-4 ml-2" />
                    </Button>
                  )}
                  {phase.phase === "Deployment" && (
                    <div className="mt-4 p-3 bg-muted/30 rounded-lg">
                      <div className="text-sm font-medium text-foreground mb-1">Live Site</div>
                      <div className="text-xs text-muted-foreground">
                        https://kairin.github.io/start/
                      </div>
                    </div>
                  )}
                </CardContent>
              </Card>
            ))}
          </div>
        </div>

        {/* CTA Section */}
        <div className="text-center mt-16 animate-fade-in">
          <Card className="max-w-2xl mx-auto bg-gradient-to-r from-primary/10 to-secondary/10 border-primary/20">
            <CardContent className="p-8">
              <Target className="w-12 h-12 text-primary mx-auto mb-4" />
              <h3 className="text-2xl font-semibold text-foreground mb-4">
                Ready to Get Started?
              </h3>
              <p className="text-muted-foreground mb-6">
                Clone the repository and start managing your projects with professional quality standards
              </p>
              <div className="flex flex-col sm:flex-row gap-4 justify-center">
                <Button size="lg" className="bg-primary hover:bg-primary/90" asChild>
                  <a href="https://github.com/kairin/start" target="_blank" rel="noopener noreferrer">
                    <Play className="w-4 h-4 mr-2" />
                    Get Started Now
                    <ExternalLink className="w-4 h-4 ml-2" />
                  </a>
                </Button>
                <Button variant="outline" size="lg" asChild>
                  <a href="https://github.com/kairin/start/blob/main/CHANGELOG.md" target="_blank" rel="noopener noreferrer">
                    View Changelog
                  </a>
                </Button>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  );
};

export default EnhancedQuickStart;