require './fraction'

# Returns an array representing the elements in the continued
# fraction expansion of a given fraction
def continued_fraction q
  # Base case
  # return the numeration if we are a whole number
  return [q.numer] if q.denom == 1
  
  # Get leading digit
  # the largest integer that fits inside the fraction
  head = q.to_i

  # The recursive step is to return the continued fraction
  # representation of the inverse of the remaining fraction
  # after subtracting head
  tail = continued_fraction (q - head).inv

  # The result is the head and tail combined
  return [head] + tail
end

# Reopening the Array class to display the appropriate
# continued fraction syntax by override to_s
# [a0; a1, a2, ..., an]
class Array
  def to_s
    '[' + self.first.to_s + '; ' + self[1..-1].join(', ') + ']'
  end
end

puts (continued_fraction Fraction.new(649, 200)).to_s
