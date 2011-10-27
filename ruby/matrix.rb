puts (['   ']+('A'..'Z').to_a).join(' ')
puts '  +'+'-'*52
('A'..'Z').to_a.each do |c| 
  puts c+' | '+(1.upto(26).collect{ |i| (('A'..'Z').to_a+('a'..'z').to_a+('0'..'9').to_a)[rand(62)]}.join(' '))
end