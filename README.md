# Crawling-Spiders-Optimsation-Algorithm
A novel population based neighbourhood search algorithm

The Crawling Spiders Optimization Algorithm is a Meta-Heuristic Algorithm which uses Population based Neighbourhood Search.
The Idea of this Optimiser came to me as a fun exercise when I first read about Zeno's second paradox. This optimiser sort-of uses the Idea 
from Zeno's Second paradox (Although its not certain that doing so results in any performance gains at all) [It's just a fun exercise after all].

## The Algorithm
Let me explain the Algorithm in steps as follows.
* The first step is to initialize `<n>` different points in `<m>` dimensional space.
  * Where `<n>` is the number of starting points and `<m>` is the number of parameters to optimize.
* Next We simply calculate the fitness/Cost/Objective function of these Initial `<n>` points.
* Then We find the point with minimum cost (for a minimization problem) and assign it as the **Goal**.
* We take the rest of the `<n-1>` points and then translate them toward the **Goal**.
* The Translation is done in a manner that each of the `<n-1>` points keeps reducing the distance between its location
and the location of the **Goal** by **1/2** (Inroducing Zeno's second paradox here).
* With each successive iteration (where the `<n-1>` points move toward the **Goal**), the cost is recalculated and the **Goal** is reassigned.
* Repeating the same procedure, we eventually arrive at the optima (Global or local) depending on the hyper-parameters (and yes there are hyper-parameters).

### So where is the Zeno's Second Paradox in here?
Well, when the `<n-1>` points translate toward the **Goal**, the distance is successively (1/2)-ed. This means that the points can never
actually reach the **Goal** even as the number of iterations -> infinity. [Although they can, because of the inherent aproximations of calculations in computers].

### Is the implementation of Zeno's Second Paradox beneficial to the Optimization process
* I have absolutely no Idea.
* But, It could be useful as the dimensionality of the optimization problem increases (like for example in Neural Networks). Because the 
Initial steps are very fast in this algorithm, (could be interpreted as a good or bad attribute).
* I think that this algorithm can be used as an Initialization to the actual Optimization algorithm, it narrows down the search space and allows
for fast arrival at local optima (Generally accepted as good enough in neural networks).

### The C code, dll files are the test objective functions, the Original implementation of the test objective functions is by,
N. H. Awad, M. Z. Ali, J. J. Liang, B. Y. Qu and P. N. Suganthan, "Problem Definitions and Evaluation Criteria for the CEC 2017 Special Session and Competition on Single Objective Bound Constrained Real-Parameter Numerical Optimization," Technical Report, Nanyang Technological University, Singapore, November 2016

Also a Big thank to github user `lacerdamarcelo` for making the python wrapper to the C Objective functions.

### If you find this Optimisation Idea or this repository useful in any manner, please cite 
`@misc{Athrva Pandhare,
  author = {Athrva Pandhare},
  title = {Crawling Spiders Optimisation Algorithm},
  year = {2019},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/charlespwd/project-title}},
  commit = {4f57d6a0e4c030202a07a60bc1bb1ed1544bf679}
}`
