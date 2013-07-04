package main

import (
    "code.google.com/p/go-tour/wc"
    "strings"
)

func WordCount(s string) map[string]int {
    res := make(map[string]int)
    words := strings.Split(s, " ")
    
    for _, word := range words {
     	res[word] = res[word] + 1
    }
    
    return res
    
}

func main() {
    wc.Test(WordCount)
}