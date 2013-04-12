#!usr/bin/env ruby -w

def to_pig_latin(s)
  if s =~ /^[aeiou]/
    s + 'way'
  else
    s.gsub(/^([bcdfghjklmnpqrstvwxyz]+)(.*)$/) { |m| "#{$2}#{$1}ay" }
  end
end

while line = gets
  words = line.chomp.split ' '
  words.map! { |w| to_pig_latin w.downcase }
  puts words.join ' '
end
