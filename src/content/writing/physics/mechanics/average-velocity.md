---
title: Basics on velocity and acceleration
date: 2026-07-05
description: " Here are the basic mathematics and physics behind those topics " 
---

## 1.1 Average Velocity and its limitations

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

Lets say something informal like of what we want to mean by a limit."$f(x)$ approaches $L$ as $x$ approaches $a$". Let's translate it into the language of mathematics, since such an important concept must be consistent.

Definition of limit: $L:=\lim_{x \to a} f(x)$ means: $\forall \varepsilon>0$  $\exists \delta>0$ s.t. $\forall x$ with $0<|x-a|<\delta$, we have $f(x)-L|<\varepsilon$.

Let's get some geometrical intuition first, for that the following diagramm will help you.
Play with it yourself: pick an $\varepsilon$ (the allowed distance from $L$), then try to find a $\delta$ (how close $x$ must stay to $a$) small enough that the graph stays inside the $\varepsilon$ area.

<iframe src="/graphs/epsilon_delta.html" title="Interactive epsilon-delta demo" width="100%" height="520" style="border: 1px solid var(--color-border); border-radius: 4px;" loading="lazy"></iframe>


We are going to really deep dive into the concept of the limit. You can skip some parts of it, since in this post im going to really explain anything deeply I myself struggled with fully understanding and anything which I think is important to cover deeply. 

## 1.2.1 Absolute beginning



What is a function? A function is a rule f which takes an input and returns EXACTLY ONE output. The domain is the set/collection of values which the function takes as an input, the range or codomain is the set/collection of outputs.

What idea are we trying to understand? As the input $x$ gets near to $a$, the output $f(x)$ gets near some fixed number $L$. So $L$ isnt the behaviour itself, but rather some specific $y$-value that is showing the behaviour of a function near a point $a$. That's already it. The whole rigor lies pretty much in describing what we mean by "gets near" mathematically.

Why isn't "get near" good enough? "Near" has no fixed meaning. Near compared to what? We also don't want $f(x)$ to be somewhat near $L$, we want it to be arbitrarily near $L$. 

What do we mean by "gets"? When we hear words like "gets closer" or "approaches", we naturally imagine some kind of motion. That intuition is useful, but it is still only an intuition, only  a mental picture. For us being sure that some intuition is consistent, this picture must be translated into a precise definition and all reasoning has to be justified by that definition rather then some intuiton.



## 1.2.2 Building the definition

Replace the "$f(x)$ gets near $L$" with "No matter how near someone demands $f(x)$ to be to $L$, you can always guarantee it by controlling the closeness of $x$ to $a$".
You can imagine it as a game between you and some opponent:
Your opponent names the accuracy: "Get your $f(x)$ within this much $L$." That "this much" is $\varepsilon$.
You respond with a closeness: "Keep $x$ within this much of $a$, and I guarantee it." That "this much" is $\delta$, a closeness on the input.
The claim $lim=L$ is that you can meet every demand your opponent can make. It's a logical claim about all possible demands at once.

Now we can zoom in at each part of the definition above and explain the reason behind it.

1. $\forall \varepsilon>0$

Why every $\varepsilon$. Remember that we wanted $f(x)$ to be arbitrarily near $L$? This is it. To know how the function behaves as it approaches a point $a$, we have to zoom in really, really close. To abstract this "really, really close" we define it as arbitrarily close using $\forall \varepsilon$, meaning we can zoom in infinetely on the target, all without touching $a$ itself. In fact, the function may not even be defined at $f(a)$ or the function could be something like $f(x)=x^2$ except for $x=3$ where it could be defined as $f(3)=14$, but the limit only cares and tells us about what the neighbours near that specific outlier tell us. So if the left and right neighbours agree they are walking towards the same height, the height is this limit. A limit is only undefined when the neighbours don't agree upon one specific value($f(x)=-1$ for $x<0$ and $f(x)=1$ for $x>0$ as $x$ approaches 0), they head towards infinity($f(x)=\frac{1}{x^2}$ as $x$ approaches 0), they can't give you a straight answer($f(x)=\sin(\frac{1}{x})$ as $x$ approaches 0).

Why $\varepsilon>0$? First of all, $\varepsilon=0 \rightarrow |f(x)-L|<0$ which is impossible since an absolute value is defined to be either positive or zero, so you would never be able to satisfy this condition and no limits would exist. Second, $\varepsilon$ is, as already mentioned, a ceiling s.t. we could get arbitrarily close to a destination without actually arriving there and the ceiling equal to 0 would arrive there. Third, what happens if we set $|f(x)-L|\leq 0$? Think about it.



2. $\exists \delta>0$

Why exists? You don't need every input closeness to work-you only need to produce one that works for a specific $\varepsilon$.
Why $\delta>0$? If we would have $\delta=0$, then the limit would loose its meaning and we would have to look at $x=a$. If it was negative, then the condition with absolute value would make no sense. 


3. $\forall x$ with $0<|x-a|<\delta$

It should be smaller then delta, since this is the ceiling the distance $|x-a|$ should be smaller then. $\forall x$ guarantees that you can choose any $x$ inside the ceiling.
It should be bigger than zero, because if that would be the case, you would include $a$ and the definition would collapse "limit at $a$" into "value at $a$".

4. $|f(x)-L|<\varepsilon$

It's just the ceiling translated into mathematics, just "error output tolerance smaller then $\epsilon$".

5. The order $\forall \varepsilon$ then $\exists \delta$ 

Still remember the game? This order just means that your opponent moves first with $\varepsilon$ and then you produce $\delta$. Your $\delta$ is allowed to depend on $\epsilon$. If you would reverse the order, you would say that you pick one fixed $\delta$ for any $\epsilon$, which is almost never satisfiable, except you have a function $f(x)=L$. $\forall \delta \exists \varepsilon$ is also nonsense. Choose some $\varepsilon$ and $\delta$ on the interactive graph above, s.t. they satisfy the conditions of the definition, but so that if you drag $\varepsilon$ down or $\delta$ up, they don't fit anymore. Now we can examine what happens as you either increase or decrease the value of each ceiling:

1.$\varepsilon$

If you make it bigger, then the old $\delta$ fits perfectly, because you give the $y$-axis just more room for values, while the old outputs specified by our $\delta$ don't change. However, if you make it smaller, the old outputs fall outside the new, more restricted output window and you have to choose a new, smaller $\delta$ to cut of the $x$ values whose $f(x)$ are now outside the ceiling.

2.$\delta$

If you make it larger, you introduce new $x$ values whose corresponding $f(x)$, if they exist, are outside our established $\varepsilon$ boundary. If you decrease it, the condition still holds as you are looking at a smaller subsets of the outputs which were inside the ceiling.

By that rules, if your opponent starts and gives you some $\delta$, you can just choose an absurdly large $\varepsilon$, which tells you nothing about the functions behaviour around some point. So in our original definition, you shrink $\varepsilon$ and your opponent has to shrink $\delta$. If we had $\forall \delta \exists \varepsilon$ and your opponent would want to get closer to a point by shrinking $\delta$, he would only make it even easier for us to choose a new $\varepsilon$.


So, here is the definition again. Write it down and say it out loud: 

**Definition**. Let $f$ be a function and $a$ a point that the domain of $f$ approaches(what "approaches" means is covered a bit later).
We say $\lim\limits_{x \to a} f(x)=L$ when:$\forall \varepsilon>0$ $\exists \delta>0$, s.t. $\forall x$ in the domain with $0<|x-a|<\delta$, we have $|f(x)-L|<\varepsilon$. 

For any accuracy you demand on the output, I can name a closeness on the input that guarantees it, for any input that close except the point itself.



## 1.2.3 Another way to look at this

For a function $f:X\rightarrow Y$ and a subset $A\subseteq X$, the **image** is denoted as $f(A)$ and defined as:

$$
f(A)= {y\in Y|\exists x \in A : f(x)=y}
$$
Choose some specific $\delta$ and take every single x value inside that window and plug them into your function to see where they land on the y-axis.
You get a set of output values

$$
S(\delta)= {f(x)|x\in X, 0<|x-a|<\delta}
$$
This is an image of $X$ under $f$, the size of which is specified by $\delta$. It represents the total vertical spread of your outputs inside the ceiling $\delta$. As you shrink $\delta$, the whole spread $S(\delta)$ gets smaller. Let's call the vertical distance between your highest and lowest $y$ values "diameter". As you zoom in infinetely on the $x$-axis, the diameter is shrinking more and more to 0 and eventually it is crushed flat into a single point, which is $L$. Now imagine a step function. As $S(\delta)$ approaches the jump, the outputs are strictly divided by some fixed width, which literally means that they can't agree upon one single value, because otherwise the diameter would shrink to 0 because the outputs would collapse into one identical value. 



## 1.2.4 Limit uniqueness

Imagine a function would have two limits at the same point, formally:


$\lim\limits_{x\to a}f(x)=L$ and $\lim\limits_{x\to a}f(x)=M$  

Is this possible? Look at the diagram below and let's try to prove it, but first **try it for yourself!**
![Two disjoint horizontal areas of half-width d/2 around L and M, a delta-window around a, and a point f(x₀) that would have to lie in both areas at once](/images/physics/mechanics/average-velocity/limit-uniqueness.svg)
Note: The diagram abstracts the graph a bit by drawing no function, because the proof doesn't require a function.

**Theorem**. If $\lim\limits_{x\to a}f(x)=L$ and $\lim\limits_{x\to a}f(x)=M$, then $L=M$.
    Proof. For a limit to exist, the statement must be true $\forall \varepsilon$. What happens if we choose $\varepsilon=\frac{d}{2}$ and some $x_{0}$? From this choice, it follows that:
$$
d=|L-M|\leq |L-f(x_{0})| + |M-f(x_{0})|<2\varepsilon=d
$$
Which of course is nonsense, since $d < d$ and your trip from $L$ to $M$ which happens trough $f(x_{0})$ is less then the trips direct length , altough you cover it. Both of those statements force $L=M$.
An even simpler proof:
Look at $|L-M|<\varepsilon$. What is the nonnegative number below every possible positive number? Right. Hence, $L-M$.
Another way to look a


## 1.2.5 Limit laws



