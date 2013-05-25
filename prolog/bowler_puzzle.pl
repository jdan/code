% http://www.brainbashers.com/showpuzzles.asp?puzzle=ZZPN
%
% Solution by Jordan Scales (http://jordanscales.com)
% 23 May 2013
%
% At a recent bowling match, two games were played.
%
% Kev beat Stuart in both games, also Richard beat John in both games. 
% The winner in game 1 came second in game 2. Richard won game 2 and 
% John beat Stuart in game 1. No player got the same placing twice.
%
% Can you determine who finished where in each game?

% Players sorted from highest score to lowest

% X appears before Y in the list (X scored higher than Y)
higher(X, Y, [X | T]) :- member(Y, T).
higher(X, Y, [_ | T]) :- higher(X, Y, T).

% the index of X in a list
index(X, [X | _], 0).
index(X, [_ | T], N) :- index(X, T, N1), N is N1 + 1.

% two lists are different if no item at the same index is equal
different([], []).
different([X | T1], [Y | T2]) :- X \== Y, different(T1, T2).

scores(Game1, Game2) :-
  permutation(Game1, [kev, stuart, richard, john]),
  permutation(Game2, [kev, stuart, richard, john]),
  higher(kev, stuart, Game1),
  higher(kev, stuart, Game2),
  higher(richard, john, Game1),
  higher(richard, john, Game2),
  index(X, Game1, 0),
  index(X, Game2, 1),
  index(richard, Game2, 0),
  higher(john, stuart, Game1),
  different(Game1, Game2).

% RESULT
% ?- scores(X, Y).
% X = [kev, richard, john, stuart],
% Y = [richard, kev, stuart, john] ;
