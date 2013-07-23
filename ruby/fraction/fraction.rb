# rational.rb
# by Jordan Scales (http://jordanscales.com)
# 27 May 2013

class Fraction

  include Comparable

  attr_reader :numer, :denom
  alias :numerator    :numer
  alias :denominator  :denom

  def initialize(numer = 1, denom = 1)
    # only integer arguments
    @numer = numer.to_i
    @denom = denom.to_i

    # handle denominator of 0
    if @denom == 0
      raise ZeroDivisionError
    # handle negatives
    elsif @denom < 0
      # let the numerator show the negative sign
      @numer *= -1
      @denom *= -1
    end

    reduce!
  end

  # math functions

  # adds a given fraction
  def + other
    other = Fraction.new(other) if other.instance_of? Fixnum
    Fraction.new(@numer * other.denom + other.numer * @denom, @denom * other.denom)
  end

  # subtracts a given function
  def - other
    other = Fraction.new(other) if other.instance_of? Fixnum
    Fraction.new(@numer * other.denom - other.numer * @denom, @denom * other.denom)
  end

  # multiplies a given fraction
  def * other
    other = Fraction.new(other) if other.instance_of? Fixnum
    Fraction.new(@numer * other.numer, @denom * other.denom)
  end

  # divides a given fraction
  def / other
    other = Fraction.new(other) if other.instance_of? Fixnum
    self * other.inv
  end

  # returns a new fraction, equivalent to its inverse
  def inv
    Fraction.new(@denom, @numer)
  end

  # inverts a given fraction (persistent)
  def inv!
    @numer, @denom = @denom, @numer
    self
  end

  # comparator
  def <=> other
    @numer * other.denom <=> other.numer * @denom
  end

  # to float
  def to_f
    @numer.to_f / @denom
  end

  # to integer (integer divison)
  def to_i
    @numer / @denom
  end

  # display
  def to_s
    "#{@numer} / #{@denom}"
  end

  private
  def gcd(a, b)
    a = a.abs
    b = b.abs

    return b if a == 0
    return a if b == 0

    if a == 1 || b == 1
      1
    elsif a == b
      a
    elsif a > b
      gcd(a-b, b)
    else
      gcd(a, b-a)
    end
  end

  # reduces a fraction (persistent)
  def reduce!
    g = gcd(@numer, @denom)
    @numer /= g
    @denom /= g
    self
  end

end
