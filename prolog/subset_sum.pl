% subset(X, Y) :- X is a subset of Y
subset([], []).
subset([H|T1], [H|T2]) :- subset(T1, T2).
subset(L, [_|T]) :- subset(L, T).

% sum(L, N) :- sum of elements in L is equal to N
sum([], 0).
sum([H|T], N) :- sum(T, N1), N is N1 + H.

% subset_sum(X, L, N) :- subset X of L sums to N
subset_sum(X, L, N) :- subset(X, L), sum(X, N).
