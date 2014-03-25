subset([], _).
subset([H|T1], [H|T2]) :- subset(T1, T2).
subset(X, [_|T]) :- subset(X, T).
