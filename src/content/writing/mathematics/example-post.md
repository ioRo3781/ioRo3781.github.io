---
title: "Example Post: Template for Future Writing"
date: 2026-07-04
description: "A template post demonstrating headings, math, code, and images."
---

This is a template post. Copy this file, rename it, and replace the content
below — it demonstrates every piece of markdown this site supports.

## Headings

Use `##` for section headings and `###` for subsections within a post. The
post title itself (from the frontmatter `title` field) is rendered as the
page's `<h1>` by the layout, so start post content at `##`.

### A subsection

Subsections are for breaking up a long section into smaller pieces.

## Inline math

Inline math uses single dollar signs: the mass-energy equivalence
$E = mc^2$ sits right in a sentence. You can also write something more
involved inline, like $\int_0^1 x^2\,dx = \tfrac{1}{3}$, without breaking
the flow of a paragraph.

## Display math

For an equation that should stand on its own line, use double dollar signs:

$$
\frac{d}{dx}\left(\int_a^x f(t)\,dt\right) = f(x)
$$

Multi-line derivations work the same way:

$$
\begin{aligned}
(a + b)^2 &= (a + b)(a + b) \\
          &= a^2 + ab + ba + b^2 \\
          &= a^2 + 2ab + b^2
\end{aligned}
$$

## Code

Fenced code blocks get syntax highlighting automatically — just name the
language after the opening backticks:

```python
def fibonacci(n: int) -> list[int]:
    """Return the first n Fibonacci numbers."""
    sequence = [0, 1]
    for _ in range(n - 2):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]


print(fibonacci(10))
```

## Images

Post images live in a folder mirroring the post's path — this post is
`mathematics/example-post.md`, so its images go in
`public/images/mathematics/example-post/` — and are referenced with a
root-relative path:

![A simple example diagram](/images/mathematics/example-post/diagram.svg)

That's the whole template. Delete this text, keep the structure, and start
writing.
