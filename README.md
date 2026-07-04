# ioRo3781.github.io

Personal site, built with [Astro](https://astro.build). Plain CSS, no UI
framework, markdown content collections for writing, LaTeX math via
remark-math/rehype-katex.

## Structure

```
src/
  content/writing/    markdown posts (one file per post)
  content.config.ts   schema for the "writing" collection
  layouts/            BaseLayout (site chrome) and PostLayout (post header)
  pages/              index.astro, about.astro, writing/index.astro, writing/[slug].astro
  styles/global.css   all site styling
public/images/<slug>/ images for a given post
```

## Writing a new post

Copy `src/content/writing/example-post.md`, rename the file, and edit the
frontmatter (`title`, `date`, `description`) and body. Put any images for
the post in `public/images/<new-slug>/`.

## Commands

| Command         | Action                                      |
| :--------------- | :------------------------------------------ |
| `npm install`     | Install dependencies                        |
| `npm run dev`      | Start local dev server at `localhost:4321`  |
| `npm run build`    | Build the production site to `./dist/`      |
| `npm run preview`  | Preview the production build locally        |

## Deployment

Every push to `main` triggers `.github/workflows/deploy.yml`, which builds
the site and publishes it to GitHub Pages.
