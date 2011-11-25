#lang racket

(define (prime-factorization n)
  (pf-helper 2 n))

(define (pf-helper curr n)
  (if (= n 1)
      '()
      (if (= 0 (modulo n curr))
          (cons curr (pf-helper 2 (/ n curr)))
          (pf-helper (+ curr 1) n))))

(define (distinct ls)
  (d-helper ls 1))

(define (d-helper ls last)
  (if (null? ls)
      '()
      (if (= (car ls) last)
          (d-helper (cdr ls) last)
          (cons (car ls) (d-helper (cdr ls) (car ls))))))

(define (totient n)
  (* n (t-helper (distinct (prime-factorization n)))))

(define (t-helper ls)
  (if (null? ls)
      1
      (* (- 1 (/ 1 (car ls))) (t-helper (cdr ls)))))

(define (sigma f start end)
  (if (> start end)
      0
      (+ (f start) (sigma f (+ start 1) end))))

(define (euler72 limit)
  (sigma totient 2 limit))

(euler72 1e5)
