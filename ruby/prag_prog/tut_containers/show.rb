#---
# Excerpted from "Programming Ruby 1.9",
# published by The Pragmatic Bookshelf.
# Copyrights apply to this code. It may not be used to create training material, 
# courses, books, articles, and the like. Contact us if you are in doubt.
# We make no guarantees that this code is fit for any purpose. 
# Visit http://www.pragmaticprogrammer.com/titles/ruby3 for more book information.
#---
def col(val)
  puts "<col><p>#{val}</p></col>"
end
def show(cmd)
  eval cmd, TOPLEVEL_BINDING
  puts "<row>"
  col cmd
  col "&rarr;"
  col eval 'a.inspect', TOPLEVEL_BINDING
  puts "</row>"
end
