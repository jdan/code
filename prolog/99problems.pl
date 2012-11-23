% 1.01 (*) Find the last element of a list.

my_last(X, [X]).
my_last(X, [_|T]) :- my_last(X, T).

% 1.02 (*) Find the last but one element of a list.

my_last_but_one(X, [X|[_]]).
my_last_but_one(X, [_|T]) :- my_last_but_one(X, T).

% 1.03 (*) Find the K'th element of a list.

element_at(X, [X|T], 1).
element_at(X, [H|T], Count) :- element_at(X, T, NewCount), Count is NewCount + 1.

% 1.04 (*) Find the number of elements of a list.

count(0, []).
count(Count, [H|T]) :- count(NewCount, T), Count is NewCount + 1.

% 1.05 (*) Reverse a list.

list_join(A, A, []).
list_join(B, [], B).
list_join()