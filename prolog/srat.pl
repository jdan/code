valid([]).
valid([Head|Tail]) :- member(Head, [a,b,c]), valid(Tail).

index(0, I, [I|_]) :- !.
index(N, I, [Head|Tail]) :- index(NN, I, Tail), !, N is NN + 1.

question1(a, b).
question1(b, c).
question1(c, a).

question2(a, A) :- index(2, b, A).
question2(b, A) :- index(0, b, A).
question2(c, A) :- index(1, b, A).

question3(a, A) :- index(N, a, A), N >= 2.
question3(b, A) :- index(N, b, A), N >= 2.
question3(c, A) :- index(N, c, A), N >= 2.

solution(Q1, Q2, Q3) :-

  SolArr = [Q1, Q2, Q3],

  valid(SolArr),

  question1(Q1, Q2),
  question2(Q2, SolArr),
  question3(Q3, SolArr).

