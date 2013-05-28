# fraction.rb
# by Jordan Scales (http://jordanscales.com)
# 27 May 2013

class Object
  def attr_alias _alias, _orig
    alias_method _alias, _orig              if defined? _orig
    alias_method "#{_alias}=", "#{_orig}="  if defined? "#{_orig}"
  end
end

class Fraction

  attr_reader :numer, :denom

  def initialize(numer = 1, denom = 1)
    @numer = numer
    @denom = denom

    reduce!
  end

  # Setter methods
  # fraction reduces after setting
  def numer= numer
    @numer = numer

    reduce!
  end

  def denom= denom
    @denom = denom

    reduce!
  end

  # alias the methods
  attr_alias :numerator, :numer
  attr_alias :denominator, :denom

  # math functions

  # adds a given fraction
  def + other
    Fraction.new @numer * other.denom + other.numer * @denom, @denom * other.denom
  end

  # subtracts a given function
  def - other
    Fraction.new @numer * other.denom - other.numer * @denom, @denom * other.denom
  end

  # multiplies a given fraction
  def * other
    Fraction.new @numer * other.numer, @denom * other.denom
  end

  # divides a given fraction
  def / other
    self * other.inv
  end

  # returns a new fraction, equivalent to its inverse
  def inv
    Fraction.new @denom, @numer
  end

  # inverts a given fraction (persistent)
  def inv!
    @numer, @denom = @denom, @numer
    self
  end

  # display
  def to_s
    "#{@numer} / #{@denom}"
  end

  private
  def gcd(a, b)
    if a == b
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
