Builder := Object clone

Builder indent := 0
Builder forward := method(
  writeln(spaces(indent), "<", call message name, ">")
  self indent := self indent + 1
  call message arguments foreach(arg,
    content := self doMessage(arg)
    if(content type == "Sequence", writeln(spaces(indent + 1), content))
  )
  self indent := self indent - 1
  writeln(spaces(indent), "</", call message name, ">")
)

spaces := method(n,
  r := ""
  for(i, 1, n, r := r .. "  ")
  r
)

Builder ul( li("Io"), li("Lua"), li("JavaScript"))
