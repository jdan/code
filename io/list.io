squareBrackets := method(
  l := List clone
  call message arguments foreach(arg,
    l append(doMessage(arg))
  )
)

[1,[1,2],3,4,5] println
