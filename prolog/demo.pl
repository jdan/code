% The element N is a member
% of X
member([H|_], H).
member([_|T], H) :- member(T, H).
