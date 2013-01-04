# What happens if you bowl a game where every throw hits a random amount of pins?
#   Same bowling scoring
#   Bowler hits a random number of pins (that are left)

GAMES = 1000000
scores = []
max = 0

class Array
  def to_s
    self.map { |frame| frame_to_s(frame) }.join ' | '
  end
end

def frame_to_s(frame)
  if frame.count == 1
    'X'
  elsif frame.count == 2
    if frame[0] + frame[1] == 10
      (frame[0].to_s + '/').gsub /0/, '-'
    else
      (frame[0].to_s + frame[1].to_s).gsub /0/, '-'
    end
  else
    frame.map { |i| i == 10 ? 'X' : (i == 0 ? '-' : i.to_s) }.join
  end

end

GAMES.times do |i|
  score = 0
  doublers = []
  frames = []

  9.times do |frame|
    # first shot
    first_shot = Random.rand(11)
    # add the score, with multipliers
    score += first_shot * (doublers.count + 1)

    # remove one from doubler
    doublers.map! { |n| n - 1 }

    # filter out all doublers that end
    doublers.select! { |n| n > 0 }

    if first_shot == 10
      # a strike means the next two frames are doubled
      frames << [first_shot]
      doublers << 2
      next
    end

    # second shot
    second_shot = Random.rand(11 - first_shot)

    score += second_shot * (doublers.count + 1)

    doublers.map!    { |n| n - 1 }
    doublers.select! { |n| n > 0 }

    if first_shot + second_shot == 10
      # spare, the next shot is doubled
      doublers << 1
    end

    frames << [first_shot, second_shot]

  end

  # tenth frame
  first_shot = Random.rand(11)
  score += first_shot * (doublers.count + 1)

  doublers.map!    { |n| n - 1 }
  doublers.select! { |n| n > 0 }

  if first_shot == 10
    # new pins
    second_shot = Random.rand(11)
  else
    second_shot = Random.rand(11 - first_shot)
  end
  score += second_shot * (doublers.count + 1)

  if first_shot == 10 || first_shot + second_shot == 10
    # strike or spare: access to the third shot
    if second_shot == 10 || (first_shot != 10 && first_shot + second_shot == 10)
      # new pins if XX or _/
      third_shot = Random.rand(11)
    else
      third_shot = Random.rand(11 - second_shot)
    end

    score += third_shot

    frames << [first_shot, second_shot, third_shot]
  else
    frames << [first_shot, second_shot]
  end

  scores << score
  if score > max
    max = score
    puts "New max score! #{score}: #{frames}"
  end

end

puts scores.max
puts scores.min
puts scores.reduce(:+).to_f / scores.count
