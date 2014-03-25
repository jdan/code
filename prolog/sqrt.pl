flsqrt(X, N) :- X >= 0, between(0, X, N), (N*N) =< X, (N+1)*(N+1) > X, !.
