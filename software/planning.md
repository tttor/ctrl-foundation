# Planning software

\item JuliaPOMDP \cite{Egorov2017}: \url{https://github.com/JuliaPOMDP/POMDPs.jl}
\item APPL \cite{Hsu2017}
\item Tapir \cite{Klimenko2014}
\item ZMDP: \url{https://github.com/trey0/zmdp}
\item madp: \url{http://www.fransoliehoek.net/madp}
\item BRRL: \url{https://github.com/mcastron/BBRL}
\item OPPT: \url{http://robotics.itee.uq.edu.au/~oppt/}
\item Symbolic Perseus: \url{https://cs.uwaterloo.ca/~ppoupart/software.html#symbolic-perseus}
https://github.com/pemami4911/POMDPy

### APPL
APPL\footnote{\url{http://bigbird.comp.nus.edu.sg/pmwiki/farm/appl}}
is a C++ toolkit for approximate POMDP planning.
It contains 3 packages, i.e.
APPL offline implementing SARSOP,
APPL online implementing DESPOT,
APPL continuous implementing MCVI.

### TAPIR
Dmitri~et~al~\cite{Klimenko2014} present the TAPIR toolkit that contains the implementation of ABT~\cite{Kurniawati2016}.
Tapir is in C++.

They present comparisons against POMCP~\cite{Silver2010} in two standard benchmarking problems, namely: tag and rock-sample.
For each problem, they carried out two scenarios: with and without POMDP model changes.
Such changes come from map alteration (obstacle addition or removal) and sensor sensing errors.

The experiment results show that ABT outperforms POMCP in both scenarios.
In without-change scenario, ABT's total rewards is \emph{slightly} better than POMCP's.
ABT has big advantage in with-change scenario.
This is because it reuses and improves the built tree from previous planning.

In extreme cases, where there is no change or there is much change, ABT performance is almost similar with POMCP.
Therefore, in TAPIR, there is an option for planning from scratch.

There is no comparison with DESPOT~\cite{Somani2013}.
There is no report on planning time that includes additional expenses for refining the tree after model changes.
