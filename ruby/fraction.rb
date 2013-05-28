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

    reduce
  end

  # Setter methods
  # fraction reduces after setting
  def numer= numer
    @numer = numer

    reduce
  end

  def denom= denom
    @denom = denom

    reduce
  end

  # alias the methods
  attr_alias :numerator, :numer
  attr_alias :denominator, :denom

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

  def reduce
    g = gcd(@numer, @denom)
    @numer /= g
    @denom /= g
  end

end
