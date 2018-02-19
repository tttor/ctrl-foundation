# dyna2_silver_2008.md

## problem

## idea
* dyna-2:
  * encompasses both sample-based learning and sample-based search, and
  * that generalises across states during both learning and search.
* for the transient planning memory and the permanent learning memory to remain separate, but
for both to be based on linear function approximation and both to be updated by Sarsa

## setup
* 9×9 Computer Go
* a million binary features in the function approximator, based on
templates matching small fragments of the board.

## result
* Using only the transient memory, Dyna-2 performed at least as well as UCT.
* Using both memories combined, it significantly outperformed UCT.

## misc
* spectrum of sample-based search algorithms:
  * from table-lookup to function approximation;
  * from Monte-Carlo learning to bootstrapping; and
  * from permanent to transient memories
