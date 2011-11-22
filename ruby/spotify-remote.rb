require 'sinatra'

get '/' do
  head = '<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.6/jquery.min.js"></script>
          <script type="text/javascript">
            $(document).ready(function() {
              $("a").click(function(e) {
                e.preventDefault();
                $.get($(this).attr("data"));
                if ($(this).attr("data") == "pause") {
                  $(this).attr("data", "play");
                  $(this).text(">");
                } else if ($(this).attr("data") == "play") {
                  $(this).attr("data", "pause");
                  $(this).text("||");
                }
              });
            });
          </script>'
  body = '<div style="font-size: 400%; text-decoration: none"><a href="#" data="prev">&lt;&lt;</a> - <a href="#" data="pause">||</a> - <a href="#" data="next">&gt;&gt;</a></div>'
  
  return head + body
end

get '/next' do
  `osascript -e 'tell application "Spotify" to next track'`
end

get '/prev' do
  `osascript -e 'tell application "Spotify" to previous track'`
end

get '/play' do
  `osascript -e 'tell application "Spotify" to play'`
end

get '/pause' do
  `osascript -e 'tell application "Spotify" to pause'`
end