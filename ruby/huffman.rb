#!/usr/bin/ruby

class HuffmanNode
  
  attr_accessor :left, :right, :data, :rank
  
  # static hash which will contain our translations
  @@hash = {}
  
  def initialize(*args)
    if args.size == 1
      @data = args[0]
      @rank = 1
    elsif args.size == 2
      @left = args[0]
      @right = args[1]
      @rank = @left.rank + @right.rank
    end
  end
  
  def to_s
    "#{@data}: #{@rank}"
  end
  
  def encode(s='')
    if @left.nil?
      @@hash[@data] = s
    else
      @left.encode(s + '0')
      @right.encode(s + '1')
    end
  end
  
  def decode(s, head)
    if s == ''
      @data.nil? ? '' : @data
    elsif @left.nil?
      @data + head.decode(s, head)
    else
      if s[0,1] == '0'
        @left.decode(s[1..s.size], head)
      else
        @right.decode(s[1..s.size], head)
      end
    end
  end
  
  def hash
    @@hash
  end
  
end

def queue(list, item)
  a = 0
  b = list.size
  
  while b - a > 1
    m = (b + a) / 2
    
    if item.rank > list[m].rank
      a = m
    else
      b = m
    end
  end
  
  list.insert(b, item)
end

def main
  input = ''
  nodes = []
  
  # ARGV has priority
  #    otherwise, collectively read from stdin
  
  if ARGV.empty?
    while s = gets do 
      input += s
    end
  else
    input = ARGV.join(' ')
  end
  
  # make a node for each character
  #    or add to a node's rank if it already exists
  input.split('').each do |char|
    found = false
    nodes.each do |node|
      if node.data == char
        node.rank += 1
        found = true
        break
      end
    end
    
    if !found
      nodes << HuffmanNode.new(char)
    end
  end
  
  # now we want to sort our nodes
  #    create an empty list to start
  nodes_t = []
  
  # use our queue function to populate our temporary list
  nodes.each do |node|
    queue(nodes_t, node)
  end
  
  # copy it back
  nodes = nodes_t
  
  # now, compress the PQ into a tree
  while nodes.size > 1
    # reverse (hack, since our queue function sucks)
    nodes = nodes.reverse()
    hn = HuffmanNode.new(nodes.pop, nodes.pop)
    nodes = nodes.reverse()
    queue(nodes, hn)
  end
  
  head = nodes.first
  
  # encode the tree, stores in @@hash
  head.encode
  hash = head.hash
  
  # now, let's return the compressed input
  compressed = input.split('').collect{ |c| hash[c] }.join('')
  
  size = compressed.size
  original_size = input.size * 8
  
  puts compressed
  puts 
  puts "Original: #{original_size} bits"
  puts "Compressed: #{size} bits"
  puts 
  puts "Dictionary"
  p hash
  puts
  puts "Decoding 001111001"
  puts "Result: " + head.decode('001111001', head)
  
end

if __FILE__ == $PROGRAM_NAME
  main
end