import React, { useState, useEffect } from 'react';
import { Button } from './ui/button';
import { Card, CardContent } from './ui/card';
import { Progress } from './ui/progress';
import { 
  Rocket, 
  CheckCircle, 
  GitBranch, 
  Zap, 
  Shield, 
  Code2,
  ArrowRight,
  Github,
  ExternalLink
} from 'lucide-react';

const EnhancedHero = () => {
  const [progress, setProgress] = useState(0);
  const [currentFeature, setCurrentFeature] = useState(0);

  const features = [
    { icon: <Code2 className="w-5 h-5" />, text: "UV-First Python", color: "text-green-400" },
    { icon: <CheckCircle className="w-5 h-5" />, text: "Quality Controller", color: "text-blue-400" },
    { icon: <GitBranch className="w-5 h-5" />, text: "Git Standards", color: "text-purple-400" },
    { icon: <Zap className="w-5 h-5" />, text: "Zero-Cost Deploy", color: "text-yellow-400" },
  ];

  useEffect(() => {
    const progressTimer = setInterval(() => {
      setProgress(prev => prev >= 100 ? 0 : prev + 2);
    }, 100);

    const featureTimer = setInterval(() => {
      setCurrentFeature(prev => (prev + 1) % features.length);
    }, 2000);

    return () => {
      clearInterval(progressTimer);
      clearInterval(featureTimer);
    };
  }, []);

  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
      {/* Animated Background */}
      <div className="absolute inset-0 bg-gradient-to-br from-slate-950 via-blue-950 to-indigo-950">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_50%,rgba(59,130,246,0.1),transparent_70%)] animate-pulse-gentle"></div>
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-blue-500/10 rounded-full blur-3xl animate-bounce-gentle"></div>
        <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-indigo-500/10 rounded-full blur-3xl animate-bounce-gentle" style={{animationDelay: '1s'}}></div>
      </div>

      <div className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        
        {/* Badge */}
        <div className="inline-flex items-center px-6 py-3 rounded-full bg-primary/20 border border-primary/30 text-primary backdrop-blur-sm mb-8 animate-fade-in">
          <Rocket className="w-4 h-4 mr-2" />
          <span className="text-sm font-medium">Version 2.0.0 - Project Quality Controller</span>
          <Shield className="w-4 h-4 ml-2" />
        </div>

        {/* Main Heading */}
        <h1 className="text-6xl lg:text-8xl font-bold bg-gradient-to-r from-white via-blue-100 to-indigo-200 bg-clip-text text-transparent mb-6 animate-slide-up">
          Start
        </h1>

        <div className="h-16 mb-8 animate-slide-up" style={{animationDelay: '0.2s'}}>
          <h2 className="text-3xl lg:text-4xl font-semibold text-muted-foreground">
            Project Quality Controller
          </h2>
        </div>

        {/* Description */}
        <p className="text-xl text-muted-foreground max-w-4xl mx-auto mb-12 leading-relaxed animate-fade-in" style={{animationDelay: '0.4s'}}>
          A unified system for managing <strong className="text-foreground">project quality, standards, and development environment consistency</strong> across all your projects.
        </p>

        {/* Feature Carousel */}
        <div className="mb-12 animate-slide-up" style={{animationDelay: '0.6s'}}>
          <Card className="max-w-md mx-auto bg-card/50 backdrop-blur-sm border-primary/20">
            <CardContent className="p-6">
              <div className="flex items-center justify-center space-x-3 text-lg font-medium">
                <span className={`transition-colors duration-500 ${features[currentFeature].color}`}>
                  {features[currentFeature].icon}
                </span>
                <span className="text-foreground">{features[currentFeature].text}</span>
              </div>
              <Progress value={progress} className="mt-4" />
            </CardContent>
          </Card>
        </div>

        {/* CTA Buttons */}
        <div className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-16 animate-slide-up" style={{animationDelay: '0.8s'}}>
          <Button 
            size="lg" 
            className="group bg-primary hover:bg-primary/90 text-primary-foreground shadow-xl hover:shadow-2xl transition-all duration-300"
            asChild
          >
            <a href="https://github.com/kairin/start" target="_blank" rel="noopener noreferrer">
              <Github className="w-5 h-5 mr-2 group-hover:rotate-12 transition-transform duration-200" />
              View on GitHub
              <ExternalLink className="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform duration-200" />
            </a>
          </Button>
          
          <Button 
            variant="outline" 
            size="lg" 
            className="group border-primary/30 bg-background/50 backdrop-blur-sm hover:bg-accent transition-all duration-300"
            asChild
          >
            <a href="#features">
              Quick Start Guide
              <ArrowRight className="w-4 h-4 ml-2 group-hover:translate-x-1 transition-transform duration-200" />
            </a>
          </Button>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-6 max-w-4xl mx-auto animate-fade-in" style={{animationDelay: '1s'}}>
          <Card className="bg-card/30 backdrop-blur-sm border-primary/20 hover:bg-card/50 transition-all duration-300">
            <CardContent className="p-4 text-center">
              <div className="text-2xl font-bold text-primary mb-1">$0</div>
              <div className="text-sm text-muted-foreground">Deployment Cost</div>
            </CardContent>
          </Card>
          
          <Card className="bg-card/30 backdrop-blur-sm border-primary/20 hover:bg-card/50 transition-all duration-300">
            <CardContent className="p-4 text-center">
              <div className="text-2xl font-bold text-green-400 mb-1">100%</div>
              <div className="text-sm text-muted-foreground">UV Compliant</div>
            </CardContent>
          </Card>
          
          <Card className="bg-card/30 backdrop-blur-sm border-primary/20 hover:bg-card/50 transition-all duration-300">
            <CardContent className="p-4 text-center">
              <div className="text-2xl font-bold text-blue-400 mb-1">Phase 1</div>
              <div className="text-sm text-muted-foreground">Complete</div>
            </CardContent>
          </Card>
          
          <Card className="bg-card/30 backdrop-blur-sm border-primary/20 hover:bg-card/50 transition-all duration-300">
            <CardContent className="p-4 text-center">
              <div className="text-2xl font-bold text-purple-400 mb-1">∞</div>
              <div className="text-sm text-muted-foreground">Branch History</div>
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  );
};

export default EnhancedHero;