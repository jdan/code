#lang racket

(define estimate
  (lambda (dec iter)
    (estimate-helper dec iter 1 1)))

(define estimate-helper
  (lambda (dec iter num denom)
    (if (= 0 iter)
        (cons num denom)
        (cond ((> (/ num denom) dec)
               (estimate-helper dec (- iter 1) num (+ denom 1)))
              ((< (/ num denom) dec)
               (estimate-helper dec (- iter 1) (+ num 1) denom))
              (else
               (cons num denom))))))