%=== 1.01 (*) Find the last element of a list.

my_last(X, [X]).
my_last(X, [_|T]) :- my_last(X, T).

%=== 1.02 (*) Find the last but one element of a list.

my_last_but_one(X, [X|[_]]).
my_last_but_one(X, [_|T]) :- my_last_but_one(X, T).

%=== 1.03 (*) Find the K'th element of a list.

element_at(X, [X|_], 1).
element_at(X, [_|T], Count) :- element_at(X, T, NewCount), Count is NewCount + 1.

%=== 1.04 (*) Find the number of elements of a list.

count(0, []).
count(Count, [_|T]) :- count(NewCount, T), Count is NewCount + 1.

%=== 1.05 (*) Reverse a list.

reverseAcc([], A, A).
reverseAcc([H|T], A, Y) :- reverseAcc(T, [H|A], Y).

reverse(X, Y) :- reverseAcc(X, [], Y).

%=== 1.06 (*) Find out whether a list is a palindrome.

is_palindrone(X) :- reverse(X, X).

%=== 1.07 (**) Flatten a nested list structure.

my_flatten(X, [X]) :- \+ is_list(X).
my_flatten([], []).
my_flatten([H|T], X) :- my_flatten(H, Z1), my_flatten(T, Z2), append(Z1, Z2, X).

%=== 1.08 (**) Eliminate consecutive duplicates of list elements.

compress([], []).
compress([X], [X]).
compress([X,X|T], L) :- compress([X|T], L).
compress([X,Y|T], [X|L]) :- X \= Y, compress([Y|T], L).

