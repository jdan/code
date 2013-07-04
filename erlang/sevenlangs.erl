-module(sevenlangs).
-export([numWords/1, countToTen/0, errorOutput/1, assocValue/2, ticTacToe/1]).

%% Count the number of words in a string
numWords([]) -> 1;                            % Base case, one word?
numWords([32 | Rest]) -> 1 + numWords(Rest);  % 32 = SPACE
numWords([_  | Rest]) -> numWords(Rest).

%% Count to 10
countToTenHelper(0) -> [];
countToTenHelper(N) -> [N | countToTenHelper(N-1)].

reverse([]) -> [];
reverse([H|T]) -> reverse(T) ++ [H].

countToTen() -> reverse(countToTenHelper(10)).

%% Match error output
errorOutput(success) -> "success";
errorOutput({error, Message}) -> "error: " ++ Message.

%%% Day 2 %%%

%% Find the associated value in a list of tuples for a given key
assocValue([], _) -> {error, "Keyword not found."};
assocValue([{Key, Val}|_], Key) -> Val;
assocValue([_|Tail], Key) -> assocValue(Tail, Key).

%% Take a shopping list of [{item, quantity, price}, ...] and return
%% [{item, total_price}, ...]
%
%  > ShoppingList = [{shoes, 2, 10.50}, {carrots, 8, 0.25}, {books, 1, 15}].
%  [{shoes,2,10.5},{carrots,8,0.25},{books,1,15}]
%
%  > [{Item, Price * Quantity} || {Item, Quantity, Price} <- ShoppingList].
%  [{shoes,21.0},{carrots,2.0},{books,15}]

%% Given a tic-tac-toe board, determine the winner, or no_winner
ticTacToe(Board) ->
  case Board of
    { x, x, x,
      _, _, _,
      _, _, _ } -> x;

    { _, _, _,
      x, x, x,
      _, _, _ } -> x;

    { _, _, _,
      _, _, _,
      x, x, x } -> x;

    { x, _, _,
      x, _, _,
      x, _, _ } -> x;

    { _, x, _,
      _, x, _,
      _, x, _ } -> x;

    { _, _, x,
      _, _, x,
      _, _, x } -> x;

    { x, _, _,
      _, x, _,
      _, _, x } -> x;

    { _, _, x,
      _, x, _,
      x, _, _ } -> x;

    { o, o, o,
      _, _, _,
      _, _, _ } -> o;

    { _, _, _,
      o, o, o,
      _, _, _ } -> o;

    { _, _, _,
      _, _, _,
      o, o, o } -> o;

    { o, _, _,
      o, _, _,
      o, _, _ } -> o;

    { _, o, _,
      _, o, _,
      _, o, _ } -> o;

    { _, _, o,
      _, _, o,
      _, _, o } -> o;

    { o, _, _,
      _, o, _,
      _, _, o } -> o;

    { _, _, o,
      _, o, _,
      o, _, _ } -> o;

    _ -> no_winner
  end.
