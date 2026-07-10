---
title: Basics on velocity and acceleration
date: 2026-07-05
description: " Here are the basic mathematics and physics behind those topics " 
---

## 1.1 Average Velocity and it's limitations

Average velocity over a time interval $\Delta t$ is the single, constant velocity that reproduces your actual displacement over your actual time. It's how the location changes per unit of time. If we translate it to mathematics, it would look like:

$$
v_{\text{avg}} = \frac{x(t+\Delta t)-x(t)}{\Delta t}=\frac{\Delta x}{\Delta t} 
$$

Now, let's say you need the velocity at an instant $t$. If you set $\Delta t = 0$ in $v_{\text{avg}}$, you get $v_{\text{avg}}=\frac{0}{0}$, which is undefined.
So first of all, we know that we just don't use the right tool, because how can it be that at an instant $t$, so at a very short moment, the velocity has no value? If an object moves and you zoom into a millisecond, it would still have to travel some distance over that millisecond.
Second, division by 0 cannot be defined. Starting from division, we might or might not know that it is defined from multiplication: $\frac{a}{b}$ means the UNIQUE number $c$ s.t. $cb=a$. If $b=0, a\neq 0$: no $c$ exists, since $c \cdot 0 = 0 \neq a$. If $a,b=0$, then $c$ is not unique, because any $c$ is valid for $c \cdot 0=0$.

Let's compute the difference quotient for a concrete motion $x(t)=t^2$:

$$
\frac{(t+\Delta t)^2 - t^2}{\Delta t}=\frac{2t\Delta t +(\Delta t)^2}{\Delta t}=2t+\Delta t \qquad (\Delta t \neq 0)
$$

So, for every nonzero,tiny $\Delta t$, the ratio is a valid number and those numbers approach $2t$ as $\Delta t$ shrinks. The endpoint $\Delta t=0$ is meaningless, but the ratio has a destination. So concluding, instantaneous velocity must be defined as the destination and not the endpoint. Velocity at $t$ is not a property of an instant, but rather  of the motion of arbitrarily small neighborhoods in of $t$.

On a position–time graph, $v_{\text{avg}}$ is the slope of the straight line
connecting the two point, which mathematically is a secant. The motion between them can be
arbitrarily messy,since  the average only sees the endpoints:

![A wiggly position-time curve with a dashed secant line connecting two marked points](/images/physics/mechanics/average-velocity/position-time.svg)


## 1.2 What exactly is this "destination", what exactly does approach mean?

Lets say something informal like "$f(x)$ approaches $L$ as $x$ approaches $a$". What do we mean by "approach"? Let's translate it into the language of mathematics, since such an important concept must be consistent.

Definition of limit: $L:=\lim_{x \to a} f(x)$ means: $\forall \varepsilon>0$  $\exists \delta>0$ s.t. $\forall x$ with $0<|x-a|<\delta$, we have $f(x)-L|<\varepsilon$.

Play with it yourself: pick an $\varepsilon$ (the allowed distance from $L$), then try to find a $\delta$ (how close $x$ must stay to $a$) small enough that the graph stays inside the $\varepsilon$ area. Here $f(x)=x^2$, $a=1$, $L=1$:

<iframe src="/graphs/epsilon_delta.html" title="Interactive epsilon-delta demo" width="100%" height="520" style="border: 1px solid var(--color-border); border-radius: 4px;" loading="lazy"></iframe>

















