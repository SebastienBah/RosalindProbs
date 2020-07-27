# Problem
In 1202, Leonardo of Pisa (commonly known as Fibonacci) considered a mathematical exercise regarding the reproduction of a population of rabbits. He made the following simplifying assumptions about the population:

  * The population begins in the first month with a pair of newborn rabbits.
  * Rabbits reach reproductive age after one month.
  * In any given month, every rabbit of reproductive age mates with another rabbit of reproductive age.
  * Exactly one month after two rabbits mate, they produce one male and one female rabbit.
  * Rabbits never die or stop reproducing.

When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively larger values of n. This problem introduces us to the computational technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases.

# Given
Positive integers n≤40 and k≤5.

# Return
The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
