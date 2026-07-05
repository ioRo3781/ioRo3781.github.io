---
title: "Basics on velocity and acceleration"
date: 2026-07-05
description: "Here are the basic mathematics and physics behind those topics "
---

Average velocity over time $${\Delta t}$$ is a the single, constant velocity that reproduces your actual displacement over your actual time. It's how the location changes per unit of time. If we translate it to mathematics, it would look like:

$$
v_{\text{avg}} = \frac{x(t+\Delta t)-x(t)}{\Delta t}=\frac{\Delta x}{\Delta t} 
$$

Now, let's say you need the velocity at an instant t. If you set it into $$v_{\text{avg}}$$, you get $$\Delta t=\frac{0}{0}=0$$.
So first of all, that's nonsense  and we know that we just dont use the right tool, because how can it be that at an instant t, so at a very short moment, the velocity is 0? If an object moves and you zoom into a millisecond, it would still have to travel some distance over that milisecond. 
Second, division by 0 cannot be defined. Starting from division, we might or might not know that it is defined from multiplication: $\frac{a}{b}$ means the UNIQUE number $c$ s.t. $cb=a$. If $b=0, a\neq 0$: no $c$ exists, since $c*0= 0\neq a$. If $a,b=0$, then $c$ is not unique, because any $c$ is valid for $c*0=0$.

On a position–time graph, $\bar{v}$ is the slope of the straight line
connecting the two points — a secant. The motion between them can be
arbitrarily messy; the average only sees the endpoints:

![A wiggly position-time curve with a dashed secant line connecting two marked points](/images/physics/mechanics/average-velocity/position-time.svg)

[Stub — expand with examples, and contrast with instantaneous velocity,
which lives at physics/mechanics/instantaneous-velocity.md when you
write it.]
