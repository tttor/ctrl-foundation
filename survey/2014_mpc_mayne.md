# Model predictive control: Recent developments and future promise
* David Q. Mayne
* Automatica 50 (2014) 2967–2986

## intro
*  MPC: applying at state x the first control in a finite sequence of control
actions obtained by solving online a constrained, discrete-time,
optimal control problem, traded arduous off-line computation of a
control law u = κ(x) for repeated on-line solution of a constrained
dynamic optimal control problem; this trade-off was perfectly
acceptable for control applications for which the optimal control
problem could be solved within one sampling interval.

* (nominal or deterministic MPC) vs (MPC of uncertain systems)

##  MPC of deterministic systems
* In MPC, at each event (x, t ) (state x, time t) a control se-
quence is computed by solving an optimal control problem, and
the first control in this sequence applied to the plant.
* for a deterministic control problem,
feedback is not necessary
* In deterministic MPC the state is assumed known
* For a deterministic problem, the optimal
control for a given state may be determined either by solving an
open-loop control problem for the given initial state or by solving
the dynamic programming equations over the horizon length N or
T (the dynamic programming solution gives, of course, the optimal
control for any admissible state and any horizon).

* **robust MPC** is that the state and
control constraints have to be satisfied by the controlled system
for all realizations of the uncertainty.
