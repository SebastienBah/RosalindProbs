# Problem

  * The population begins in the first month with a pair of newborn rabbits.
  * Rabbits reach reproductive age after one month.
  * In any given month, every rabbit of reproductive age mates with another rabbit of reproductive age.
  * Exactly one month after two rabbits mate, they produce one male and one female rabbit.
  * Rabbits die after m months.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

# Given
Positive integers n≤100 and m≤20.

# Return
The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months
