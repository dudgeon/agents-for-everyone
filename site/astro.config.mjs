import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://agents-for-everyone.ai-pm.cc',
  integrations: [tailwind()],
  output: 'static',
});
