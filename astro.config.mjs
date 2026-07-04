// @ts-check
import { defineConfig } from 'astro/config';
import { unified } from '@astrojs/markdown-remark';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// https://astro.build/config
export default defineConfig({
  // Needed so Astro generates correct absolute URLs (e.g. in RSS/sitemaps later).
  site: 'https://ioRo3781.github.io',

  markdown: {
    // `unified` is the remark/rehype-based processor that plugins like
    // remark-math and rehype-katex are built for.
    processor: unified({
      remarkPlugins: [remarkMath],
      rehypePlugins: [rehypeKatex],
    }),
    // Astro's built-in syntax highlighter (Shiki) needs no extra setup for Python.
    shikiConfig: {
      theme: 'github-light',
    },
  },
});
