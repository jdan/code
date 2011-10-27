require 'rubygems'
require 'sinatra'
require 'haml'

def Collatz(n)
    s_out = ""
    k = 0
    while n > 1
        k += 1
        r = n % 3
        if r == 0
            s_out += "D"
            n /= 3
        elsif r == 1
            s_out += "U"
            n = (4 * n + 2) / 3
        elsif r == 2
            s_out += "d"
            n = (2 * n - 1) / 3
        end
        if k == 15
            k = 0
            s_out += "<br />"
        end
    end
    return s_out
end

get '/' do
    haml :instruct
end

get '/:n' do |n|
    @n = n
    @r = Collatz(n.to_i)
    haml :output
end
    
__END__

@@ layout
%html
    %head
        %title Collatz Sequence
    %body(style="font-family:arial;font-weight:bold;font-size:75px;padding-left:25px;")
        =yield
        
@@ instruct
%p &nbsp;
%p &nbsp;
%p Enter integer after '/' to generate sequence.

@@ output
%span(style="font-size:95px;") Collatz Sequence for 
%i #{@n}
%br/
%p(style="font-size:95px;") #{@r}