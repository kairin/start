import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import react from '@astrojs/react';

// Start Project Quality Controller - Astro Configuration
// Zero-cost GitHub Pages deployment with local CI/CD
export default defineConfig({
  // GitHub Pages deployment configuration
  site: 'https://kairin.github.io',
  base: '/start',

  // Integrations for modern web development
  integrations: [
    tailwind({
      // Enable base styles for CSS custom properties
      applyBaseStyles: true,
    }),
    react(), // For interactive components
  ],

  // TypeScript strict mode enforcement
  typescript: {
    strict: true,
  },

  // Build optimization for performance
  build: {
    // Inline stylesheets for better performance
    inlineStylesheets: 'auto',
    // Asset optimization
    assets: '_astro',
  },

  // Build output directory for GitHub Pages
  outDir: './docs',

  // Vite configuration for zero-cost deployment
  vite: {
    plugins: [
      // Automatically create .nojekyll file for GitHub Pages
      {
        name: 'create-nojekyll',
        async writeBundle() {
          const fs = await import('fs');
          const path = await import('path');
          const nojekyllPath = path.join('./docs', '.nojekyll');

          // Ensure docs directory exists
          if (!fs.existsSync('./docs')) {
            console.warn('⚠️ WARNING: docs directory not found for .nojekyll creation');
            return;
          }

          // Create .nojekyll file (CRITICAL for GitHub Pages)
          fs.writeFileSync(nojekyllPath, '');
          console.log('✅ Created .nojekyll file for GitHub Pages');

          // Verify _astro directory exists (critical for asset loading)
          const astroDir = path.join('./docs', '_astro');
          if (fs.existsSync(astroDir)) {
            const files = fs.readdirSync(astroDir);
            console.log(`✅ _astro directory confirmed (${files.length} files)`);
          } else {
            console.warn('⚠️ WARNING: _astro directory not found - assets may not load');
          }

          // Create CNAME file for custom domain (if needed)
          // Uncomment and modify if using custom domain:
          // const cnamePath = path.join('./docs', 'CNAME');
          // fs.writeFileSync(cnamePath, 'your-custom-domain.com');
        }
      }
    ],
    build: {
      // Optimize bundle size for fast loading
      rollupOptions: {
        output: {
          manualChunks: {
            // Keep vendor dependencies separate and small
            vendor: ['astro', 'react', 'react-dom'],
            ui: ['lucide-react', 'clsx'],
          },
        },
      },
      // Minification for production
      minify: 'esbuild',
      // No source maps for smaller bundles
      sourcemap: false,
    },
    // Development server optimization
    server: {
      // Fast hot reload
      hmr: {
        overlay: false, // Reduce overhead
      },
    },
  },

  // Static site generation for GitHub Pages
  output: 'static',

  // SEO and performance optimization
  compilerOptions: {
    // Enable optimizations for Lighthouse scores 95+
    preserveComments: false,
  },

  // Zero-cost deployment markers
  // ✅ GitHub Pages serves docs/ folder automatically
  // ✅ No GitHub Actions required
  // ✅ Local CI/CD prevents remote build costs
  // ✅ .nojekyll automatic creation
  // ✅ Performance optimized for fast loading
});