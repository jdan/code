subset([], []).
subset([H|NTail], [H|Tail]) :- subset(NTail, Tail).
