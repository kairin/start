import React from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Button } from './ui/button';
import { 
  Code2, 
  CheckCircle2, 
  Settings, 
  GitBranch, 
  Bot, 
  DollarSign,
  ArrowRight,
  Zap,
  Shield,
  Monitor
} from 'lucide-react';

const EnhancedFeatures = () => {
  const features = [
    {
      icon: <Code2 className="w-8 h-8" />,
      title: "UV-First Python",
      description: "Mandatory UV-only development for all Python projects. Zero tolerance for pip, venv, or conda.",
      details: ["uv pip install", "uv run python", "System Python3 only"],
      gradient: "from-green-400/20 to-emerald-600/20",
      borderColor: "border-green-500/30",
      iconColor: "text-green-400"
    },
    {
      icon: <CheckCircle2 className="w-8 h-8" />,
      title: "Quality Controller",
      description: "Complete CLI system for auditing project compliance and enforcing standards across repositories.",
      details: ["Project auditing", "Standards validation", "Compliance scoring"],
      gradient: "from-blue-400/20 to-cyan-600/20",
      borderColor: "border-blue-500/30",
      iconColor: "text-blue-400"
    },
    {
      icon: <Settings className="w-8 h-8" />,
      title: "System Management",
      description: "Enhanced development tools updater for NVM, Oh My Zsh, and comprehensive project monitoring.",
      details: ["NVM updates", "Oh My Zsh sync", "Project monitoring"],
      gradient: "from-purple-400/20 to-violet-600/20",
      borderColor: "border-purple-500/30",
      iconColor: "text-purple-400"
    },
    {
      icon: <GitBranch className="w-8 h-8" />,
      title: "Git Standards",
      description: "Mandatory branch naming with complete history preservation. Zero-deletion policy enforced.",
      details: ["YYYYMMDD-HHMMSS format", "Branch preservation", "History integrity"],
      gradient: "from-yellow-400/20 to-orange-600/20",
      borderColor: "border-yellow-500/30",
      iconColor: "text-yellow-400"
    },
    {
      icon: <Bot className="w-8 h-8" />,
      title: "AI Integration",
      description: "Unified AGENTS.md instructions for Claude Code, Gemini CLI, and GitHub Copilot CLI.",
      details: ["Multi-AI support", "Unified instructions", "MCP integration"],
      gradient: "from-indigo-400/20 to-purple-600/20",
      borderColor: "border-indigo-500/30",
      iconColor: "text-indigo-400"
    },
    {
      icon: <DollarSign className="w-8 h-8" />,
      title: "Zero-Cost Deployment",
      description: "Local CI/CD pipeline with GitHub Pages. No GitHub Actions charges - ever.",
      details: ["Local builds only", "GitHub Pages hosting", "No recurring costs"],
      gradient: "from-pink-400/20 to-rose-600/20",
      borderColor: "border-pink-500/30",
      iconColor: "text-pink-400"
    }
  ];

  const specs = [
    { icon: <Zap className="w-5 h-5" />, label: "Build Time", value: "~1.3s" },
    { icon: <Shield className="w-5 h-5" />, label: "Security", value: "Enterprise" },
    { icon: <Monitor className="w-5 h-5" />, label: "Compatibility", value: "All Platforms" },
  ];

  return (
    <section id="features" className="py-24 bg-background/50 backdrop-blur-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        
        {/* Section Header */}
        <div className="text-center mb-16 animate-fade-in">
          <div className="inline-flex items-center px-4 py-2 rounded-full bg-primary/10 border border-primary/20 text-primary text-sm font-medium mb-6">
            Phase 001 Complete
          </div>
          <h2 className="text-4xl lg:text-5xl font-bold text-foreground mb-6">
            Professional Quality Control
          </h2>
          <p className="text-xl text-muted-foreground max-w-3xl mx-auto leading-relaxed">
            Complete project management system with zero-cost deployment and enterprise-grade standards enforcement
          </p>
        </div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8 mb-16">
          {features.map((feature, index) => (
            <Card 
              key={index}
              className={`group bg-gradient-to-br ${feature.gradient} border ${feature.borderColor} hover:shadow-2xl hover:shadow-blue-500/10 transition-all duration-500 hover:-translate-y-2 animate-slide-up`}
              style={{animationDelay: `${index * 0.1}s`}}
            >
              <CardHeader className="space-y-4">
                <div className={`inline-flex p-3 rounded-lg bg-background/50 w-fit ${feature.iconColor} group-hover:scale-110 transition-transform duration-300`}>
                  {feature.icon}
                </div>
                <div>
                  <CardTitle className="text-xl font-semibold text-foreground mb-2 group-hover:text-primary transition-colors duration-300">
                    {feature.title}
                  </CardTitle>
                  <CardDescription className="text-muted-foreground leading-relaxed">
                    {feature.description}
                  </CardDescription>
                </div>
              </CardHeader>
              
              <CardContent className="space-y-4">
                <div className="space-y-2">
                  {feature.details.map((detail, i) => (
                    <div key={i} className="flex items-center text-sm">
                      <div className={`w-1.5 h-1.5 rounded-full ${feature.iconColor.replace('text-', 'bg-')} mr-3`} />
                      <span className="text-muted-foreground">{detail}</span>
                    </div>
                  ))}
                </div>
                
                <Button 
                  variant="ghost" 
                  size="sm"
                  className={`w-full mt-4 ${feature.iconColor} hover:bg-accent group-hover:translate-x-1 transition-all duration-300`}
                >
                  Learn More 
                  <ArrowRight className="w-4 h-4 ml-2" />
                </Button>
              </CardContent>
            </Card>
          ))}
        </div>

        {/* Specs */}
        <div className="bg-card/30 backdrop-blur-sm border border-border rounded-xl p-8 animate-fade-in">
          <h3 className="text-2xl font-semibold text-foreground text-center mb-8">
            Technical Specifications
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {specs.map((spec, index) => (
              <div key={index} className="text-center group">
                <div className="inline-flex items-center justify-center w-12 h-12 rounded-lg bg-primary/10 text-primary mb-4 group-hover:scale-110 transition-transform duration-300">
                  {spec.icon}
                </div>
                <div className="text-lg font-semibold text-foreground mb-2">{spec.value}</div>
                <div className="text-sm text-muted-foreground">{spec.label}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
};

export default EnhancedFeatures;