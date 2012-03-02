#lang racket

(define quicksort
  (lambda (ls)
    (if (null? ls)
        '()
        (append (quicksort (filter < (car ls) (cdr ls)))
                (list (car ls))
                (quicksort (filter >= (car ls) (cdr ls)))))))

(define filter
  (lambda (op pivot ls)
    (if (null? ls)
        '()
        (if (op (car ls) pivot)
            (cons (car ls) (filter op pivot (cdr ls)))
            (filter op pivot (cdr ls))))))

