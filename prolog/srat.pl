valid([]).
valid([Head|Tail]) :- member(Head, [a,b,c,d,e]), valid(Tail).

% count(3, a, [a,a,a,b,c]).
count(0, _, []).
count(N, I, [I|Tail]) :- count(NN, I, Tail), N is NN + 1.
count(N, I, [Other|Tail]) :- I \= Other, count(N, I, Tail).

% 1. The first question whose answer is B is question
question1(a, S) :- nth0(0, S, b).
question1(b, S) :- nth0(1, S, b).
question1(c, S) :- nth0(2, S, b).
question1(d, S) :- nth0(3, S, b).
question1(e, S) :- nth0(4, S, b).

% 2. The only two consecutive questions with identical answers are questions
question2(a, S) :- nth0(5, S, I), nth0(6, S, I).
question2(b, S) :- nth0(6, S, I), nth0(7, S, I).
question2(c, S) :- nth0(7, S, I), nth0(8, S, I).
question2(d, S) :- nth0(8, S, I), nth0(9, S, I).
question2(e, S) :- nth0(9, S, I), nth0(10, S, I).

% 3. The number of questions with the answer E is
question3(a, S) :- count(0, e, S).
question3(b, S) :- count(1, e, S).
question3(c, S) :- count(2, e, S).
question3(d, S) :- count(3, e, S).
question3(e, S) :- count(4, e, S).

% 4. The number of questions with the answer A is
question4(a, S) :- count(4, a, S).
question4(b, S) :- count(5, a, S).
question4(c, S) :- count(6, a, S).
question4(d, S) :- count(7, a, S).
question4(e, S) :- count(8, a, S).

% 5. The answer to this question is the same as the answer to question
question5(a, S) :- nth0(0, S, a).
question5(b, S) :- nth0(1, S, b).
question5(c, S) :- nth0(2, S, c).
question5(d, S) :- nth0(3, S, d).
question5(e, S) :- nth0(4, S, e).

% 6. The answer to question 17 is
question6(a, S) :- nth0(16, S, c).
question6(b, S) :- nth0(16, S, d).
question6(c, S) :- nth0(16, S, e).
question6(d, S) :- nth0(16, S, a) ; nth0(16, S, b).
question6(e, S) :- false.

% 7. Alphabetically, the answer to this question and the answer to the following question are
question7(a, S) :- nth0(7, S, e).
question7(b, S) :- nth0(7, S, e).
question7(c, S) :- nth0(7, S, e).
question7(d, S) :- nth0(7, S, e).
question7(e, S) :- nth0(7, S, e).

% 8. The number of questions whose answers are vowels is
question8(a, S) :- count(T1, a, S), count(T2, e, S), T1 + T2 =:= 4.
question8(b, S) :- count(T1, a, S), count(T2, e, S), T1 + T2 =:= 5.
question8(c, S) :- count(T1, a, S), count(T2, e, S), T1 + T2 =:= 6.
question8(d, S) :- count(T1, a, S), count(T2, e, S), T1 + T2 =:= 7.
question8(e, S) :- count(T1, a, S), count(T2, e, S), T1 + T2 =:= 8.

% 9. The next question with the same answer as this one is question
question9(a, S) :- nth0(9, S, a).
question9(b, S) :- nth0(10, S, b).
question9(c, S) :- nth0(11, S, c).
question9(d, S) :- nth0(12, S, d).
question9(e, S) :- nth0(13, S, e).

% 10. The answer to question 16 is
question10(a, S) :- nth0(15, S, d).
question10(b, S) :- nth0(15, S, a).
question10(c, S) :- nth0(15, S, e).
question10(d, S) :- nth0(15, S, b).
question10(e, S) :- nth0(15, S, c).

% 11. The number of questions preceding this one with the answer B is
question11(a, S) :- append(L1, L2, S), length(L1, 10), count(0, b, L1).
question11(b, S) :- append(L1, L2, S), length(L1, 10), count(1, b, L1).
question11(c, S) :- append(L1, L2, S), length(L1, 10), count(2, b, L1).
question11(d, S) :- append(L1, L2, S), length(L1, 10), count(3, b, L1).
question11(e, S) :- append(L1, L2, S), length(L1, 10), count(4, b, L1).

% 12. The number of questions whose answer is a consonant is
question12(a, S) :- count(T1, b, S), count(T2, c, S), count(T3, d, S), T is T1 + T2 + T3, T rem 2 =:= 0.
question12(b, S) :- count(T1, b, S), count(T2, c, S), count(T3, d, S), T is T1 + T2 + T3, T rem 2 =\= 0.
question12(c, S) :- count(T1, b, S), count(T2, c, S), count(T3, d, S), T is T1 + T2 + T3, member(T, [1,4,9,16]).
question12(d, S) :- count(T1, b, S), count(T2, c, S), count(T3, d, S), T is T1 + T2 + T3, member(T, [2,3,5,7,11,13,17,19]).
question12(e, S) :- count(T1, b, S), count(T2, c, S), count(T3, d, S), T is T1 + T2 + T3, member(T, [5,10,15,20]).

% 13. The only odd-numbered problem with answer A is
question13(a, S) :- nth0(8, S, a).
question13(b, S) :- nth0(10, S, a).
question13(c, S) :- nth0(12, S, a).
question13(d, S) :- nth0(14, S, a).
question13(e, S) :- nth0(16, S, a).

% 14. The number of questions with answer D is
question14(a, S) :- count(6, d, S).
question14(b, S) :- count(7, d, S).
question14(c, S) :- count(8, d, S).
question14(d, S) :- count(9, d, S).
question14(e, S) :- count(10, d, S).

% 15. The answer to question 12 is
question15(a, S) :- nth0(11, S, a).
question15(b, S) :- nth0(11, S, b).
question15(c, S) :- nth0(11, S, c).
question15(d, S) :- nth0(11, S, d).
question15(e, S) :- nth0(11, S, e).

% 16. The answer to question 10 is
question16(a, S) :- nth0(9, S, d).
question16(b, S) :- nth0(9, S, c).
question16(c, S) :- nth0(9, S, b).
question16(d, S) :- nth0(9, S, a).
question16(e, S) :- nth0(9, S, e).

% 17. The answer to question 6 is
question17(a, S) :- nth0(5, S, c).
question17(b, S) :- nth0(5, S, d).
question17(c, S) :- nth0(5, S, e).
question17(d, S) :- nth0(5, S, a) ; nth0(5, S, b).
question17(e, S) :- false.

% 18. The number of questions with answer A equals the number of questions with answer
question18(a, S) :- count(C1, a, S), count(C2, b, S), C1 =:= C2.
question18(b, S) :- count(C1, a, S), count(C2, c, S), C1 =:= C2.
question18(c, S) :- count(C1, a, S), count(C2, d, S), C1 =:= C2.
question18(d, S) :- count(C1, a, S), count(C2, e, S), C1 =:= C2.
question18(e, S) :- true.

% 19. The answer to this question is:
question19(X, S) :- member(X, [a,b,c,d,e]).

% 20. Standardized test is to intelligence as barometer is to
question20(e, S).

solution(Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20) :-

  SolArr = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20],

  valid(SolArr),

  question1(Q1, SolArr),
  question2(Q2, SolArr),
  question3(Q3, SolArr),
  question4(Q4, SolArr),
  question5(Q5, SolArr),
  question6(Q6, SolArr),
  question7(Q7, SolArr),
  question8(Q8, SolArr),
  question9(Q9, SolArr),
  question10(Q10, SolArr),
  question11(Q11, SolArr),
  question12(Q12, SolArr),
  question13(Q13, SolArr),
  question14(Q14, SolArr),
  question15(Q15, SolArr),
  question16(Q16, SolArr),
  question17(Q17, SolArr),
  question18(Q18, SolArr),
  question19(Q19, SolArr),
  question20(Q20, SolArr).

