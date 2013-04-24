-module(sevenlangs).
-export([numWords/1, countToTen/0, errorOutput/1]).

numWords([]) -> 1;                            % Base case, one word?
numWords([32 | Rest]) -> 1 + numWords(Rest);  % 32 = SPACE
numWords([_  | Rest]) -> numWords(Rest).

countToTenHelper(0) -> [];
countToTenHelper(N) -> [N | countToTenHelper(N-1)].

reverse([]) -> [];
reverse([H|T]) -> reverse(T) ++ [H].

countToTen() -> reverse(countToTenHelper(10)).

errorOutput(success) -> "success";
errorOutput({error, Message}) -> "error: " ++ Message.
