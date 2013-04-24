-module(sevenlangs).
-export([numwords/1]).

numwords([]) -> 1;                            % Base case, one word?
numwords([32 | Rest]) -> 1 + numwords(Rest);  % 32 = SPACE
numwords([_  | Rest]) -> numwords(Rest).