## The problem:
## 
## Given a 5 x 5 array of integers, write a program to find any saddle points in the given set. A saddle point is a 
## cell whose value is greater than or equal to any in its row and less than or equal to any in its column. There 
## may be more than one saddle point. Your program will print the coordinates of any found saddle points. If there 
## are none, it should print out “No saddle points found”. 
## 
## Sample arrays:
arr1 = [[39, 43, 49, 29, 18], [30, 47, 24, 29, 15], [49, 50, 39, 20, 33], [18, 38, 35, 32, 35], [29, 44, 18, 34, 44]]
arr2 = [[50, 27, 36, 43, 39], [36, 14, 35, 40, 19], [20, 33, 48, 32, 40], [41, 40, 15, 22, 19], [21, 24, 24, 31, 18]]
arr3 = [[39, 43, 49, 29, 18], [30, 47, 24, 29, 15], [49, 50, 39, 20, 33], [18, 38, 35, 32, 38], [29, 44, 18, 34, 44]]
arr4 = [[1,2,3], [4,5,6], [7,8,9]]
arr5 = [[1,8,1], [1,5,1], [1,7,1]]

# Sort-of naive approach
#   iterate over each row
#     iterate over each item
#       if the item is equal to the row's max and its column's min => append it

def saddle(arr)
  saddle_points = []
  
  # iterate over each row
  arr.each_with_index do |row, r|
    # get the max
    max = row.max
    
    row.each_with_index do |item, c|
      # if the item is the max and the min in its column
      if item == max and item == arr.collect{|row| row[c]}.min
        saddle_points << [r,c]
      end
    end
    
  end
  
  if saddle_points.empty?
    'No saddle points found'
  else
    saddle_points.inspect
  end
end

# Possible improvements
# 1.
# filter out everything but the max values for each row and
#                               min values for each column
# and check for overlaps
# 
# 2.
# Store the max and min for row and column (respectively) ahead of time
#   so we only need to calculate them once

[arr1, arr2, arr3, arr4, arr5].each do |a|
  puts saddle(a)
end