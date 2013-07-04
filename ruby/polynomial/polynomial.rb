
class Polynomial

  attr_reader :coeffs

  # Polynomial.new ([1, 2, 3])
  #   => 1 + 2x + 3x^2
  def initialize(coeffs = [])
    @coeffs = coeffs
  end

  # Adding two polynomials together
  def + other
    if @coeffs.count > other.coeffs.count
      Polynomial.new @coeffs.zip(other.coeffs).map{ |a| a.map(&:to_f).inject(&:+) }
    else
      Polynomial.new other.coeffs.zip(@coeffs).map{ |a| a.map(&:to_f).inject(&:+) }
    end
  end

  # + but persistent
  def plus! other
    if @coeffs.count > other.coeffs.count
      @coeffs = @coeffs.zip(other.coeffs).map{ |a| a.map(&:to_f).inject(&:+) }
    else
      @coeffs = other.coeffs.zip(@coeffs).map{ |a| a.map(&:to_f).inject(&:+) }
    end
  end

  # Multiplying two polynomials together
  def * other
    result = Polynomial.new
    @coeffs.each_with_index do |c, i|
      result.plus! other.scale(c).shift(i)
    end
    result
  end

  def scale n
    Polynomial.new @coeffs.map { |c| c * n }
  end

  # Multiplies the polynomial by x^n
  def shift n
    Polynomial.new @coeffs.unshift(*([0]*n))
  end

  # evaluates the polynomial at a value `n`
  def at n
    @coeffs.each_with_index.map{ |c,i| c * (n**i) }.inject(&:+)
  end

end

coords = [[1, 1], [2, 6], [3, 2], [5, 10]]

xs = coords.map(&:first)
ys = coords.map{ |p| p[1] }

def lagrange_polynomial xs, choice
  poly = Polynomial.new([1]) # unit
  xs.each do |i|
    if choice != i
      # multiply by (x - i)
      poly = poly * Polynomial.new([-i, 1])

      # divide by (choice - i)
      poly = poly * Polynomial.new([1.0 / (choice - i)])
    end
  end

  poly
end

poly = lagrange_polynomial([1,2,3,4], 1)
p poly
p poly.at(1)
p poly.at(2)
p poly.at(3)
p poly.at(4)
