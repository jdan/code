#lang racket

(define (i n)
  (reverse (i_ n)))

(define (i_ n)
  (if (zero? n)
      '()
      (cons n (i_ (- n 1)))))

(define btoi (lambda (c) (if c 1 0)))

(struct complex (real imag))
(define (putc c) (list (complex-real c) (complex-imag c)))

(define c_add
  (lambda (c1 c2)
    (complex (+ (complex-real c1) (complex-real c2)) (+ (complex-imag c1) (complex-imag c2)))))

(define c_mult
  (lambda (c1 c2)
    (complex (- (* (complex-real c1) (complex-real c2)) (* (complex-imag c1) (complex-imag c2)))
             (+ (* (complex-real c1) (complex-imag c2)) (* (complex-real c2) (complex-imag c1))))))

