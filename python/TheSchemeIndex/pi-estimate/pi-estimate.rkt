(define (pi-estimate n)
  (sigma pi-formula 0 n))

(define (sigma f a b)
  (if (> a b)
      0
      (+ (f a) (sigma f (+ a 1) b))))

(define (pi-formula n)
  (/ 8 (* (+ (* 4 n) 1) (+ (* 4 n) 3))))