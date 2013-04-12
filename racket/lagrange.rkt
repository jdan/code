#lang racket

; lagrange polynomials

(require "polynomial.rkt")

; given a list of pairs (x y)
; return a new list with only the x's
(define get-xs
  (lambda (ls)
    (map car ls)))

; given a list of pairs (x y)
; return a new list with only the y's
(define get-ys
  (lambda (ls)
    (map cadr ls)))

; given a list of elements and an element
; return the list without that element
(define except
  (lambda (ls e)
    (filter (lambda (i) (not (eq? e i))) ls)))

; given a list of x's and a given x-coordinate
; return a polynomial that evaluates to 1 for a given number
;   and 0 for all else
(define kronecker-delta
  (lambda (ls x)
    (let ([divisor (/ (foldl * 1 ; goes in the denominator
                             (map (lambda (e) (- x e)) (except ls x))))]
          [poly (foldl multiply '(1) (list (compose (except ls x))))])
      (multiply (list divisor) poly))))

; given a list of coordinates
; return a lagrange polynomial
;   which is a polynomial containing all points
(define lagrange-polynomial
  (lambda (coords)
    (let ([xs (get-xs coords)])
      (foldl add '(0)            ; combine all kronecker-deltas for each point
             (map (lambda (pair) ; multiplied by its y-value
                    (multiply (cdr pair) (kronecker-delta xs (car pair))))
                  coords)))))