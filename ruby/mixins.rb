module Enumerable

  [:adam, :chris, :ryan, :jordan].each do |item|
    define_method item do
      puts 'hello'
    end
  end

end

a = [1,2,3]
a.ryan
