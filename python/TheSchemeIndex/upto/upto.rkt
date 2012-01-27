(define (upto n)
   (reverse (upto-helper n)))

(define (upto-helper n)
   (if (= n 0)
      '()
      (cons n (upto-helper (- n 1)))))