# Minimalist wallpaper
# by Jordan Scales (http://jordanscales.com)
# 5 Apr 2013

class Wallpaper < Processing::App

  WIDTH  = 1920
  HEIGHT = 1080

  def setup
    size WIDTH, HEIGHT
    no_loop
    no_stroke
  end

  def draw
    dark_blue = color('#69799A')
    light_blue = color('#ADB4C4')
    beige = color('#CFB899')
    orange = color('#E39E5B')
    red = color('#A43C23')

    background = beige
    colors = [dark_blue, light_blue, orange, red]

    bar_height = 180

    # draw the background
    fill(background)
    rect(0, 0, WIDTH, HEIGHT)

    4.times do |i|
      x1 = WIDTH / 4.0 * i
      x2 = x1 + WIDTH / 4.0

      fill(colors[i])
      rect(x1, 0, x2, bar_height)
    end

    save('wallpaper.png')
  end

end
