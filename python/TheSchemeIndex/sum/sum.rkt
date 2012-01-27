(define (sum ls)
   (if (null? ls)
      0
      (+ (car ls) (sum (cdr ls)))))