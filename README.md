# ioRo3781.github.io

Personal site, built with [Astro](https://astro.build). Plain CSS, no UI
framework, markdown content collections for writing, LaTeX math via
remark-math/rehype-katex.

## Structure

```
src/
  content/writing/    markdown posts in nested topic folders, e.g.
                      physics/mechanics/average-velocity.md
  content.config.ts   schema for the "writing" collection
  layouts/            BaseLayout (site chrome) and PostLayout (post header)
  pages/              index.astro, about.astro, writing/index.astro, writing/[...slug].astro
  styles/global.css   all site styling
public/images/<path>/ images for a post, mirroring its content path
```

The folder path is the post's section: it becomes the URL
(`/writing/physics/mechanics/average-velocity/`), the grouping heading on
the writing page, and the breadcrumb above the post title. Folders can nest
as deep as needed.

## Writing a new post

Copy `src/content/writing/mathematics/example-post.md` into the right topic
folder (create new folders freely), rename the file, and edit the
frontmatter (`title`, `date`, `description`) and body. Put any images for
the post in `public/images/<same path>/`.

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
