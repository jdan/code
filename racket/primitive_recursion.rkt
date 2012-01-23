#lang racket

(define (increment n)
  (+ n 1))

; (+ n i)
(define (add n i)
  (if (< i 1)
      n
      (increment (add n (- i 1)))))

; (* n i)
(define (multiply n i)
  (if (= i 0)
      0
      (add n (multiply n (- i 1)))))

; (expt n i)
(define (exponent n i)
  (if (= i 0)
      1
      (multiply n (exponent n (- i 1)))))

; (tower n i)
(define (tower n i)
  (if (= i 0)
      1
      (exponent n (tower n (- i 1)))))