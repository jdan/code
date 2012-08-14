valid([]).
valid([Head|Tail]) :- member(Head, [a,b,c,d,e]), valid(Tail).

index(0, I, [I|_]) :- !.
index(N, I, [Head|Tail]) :- index(NN, I, Tail), !, N is NN + 1.

solution(Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20) :-

  A = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20],

  valid(),

  % the first question whose answer is B is...
  answer(Q1, a) :- index(0, b, 
  answer(Q2, b) :- Q1 \= b, Q2 = b,
