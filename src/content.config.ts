import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const writing = defineCollection({
  // Every .md file under src/content/writing/ becomes an entry in this collection.
  loader: glob({ pattern: '**/*.md', base: './src/content/writing' }),
  // A post's section comes from its folder path, e.g.
  // physics/mechanics/average-velocity.md → section "physics / mechanics".
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    description: z.string(),
  }),
});

export const collections = { writing };
