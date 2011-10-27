#---
# Excerpted from "Programming Ruby 1.9",
# published by The Pragmatic Bookshelf.
# Copyrights apply to this code. It may not be used to create training material, 
# courses, books, articles, and the like. Contact us if you are in doubt.
# We make no guarantees that this code is fit for any purpose. 
# Visit http://www.pragmaticprogrammer.com/titles/ruby3 for more book information.
#---
require 'dl/import'

module User32
  extend DL::Importer
  dlload 'user32.dll'

  extern "int MessageBoxA(long, const char *, const char *, int)"
end

MB_OKCANCEL = 1

User32.MessageBoxA(0, "OK?", "Please Confirm", MB_OKCANCEL)
