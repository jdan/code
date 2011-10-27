class Person
  
  def initialize (name, age)
    @name = name
    @age = age
  end
  
  def speak
    printf('Hello, my name is %s and I am %s years old.', @name, @age)
    puts ""
  end
  
end   

jordan = Person.new('Jordan',17)
jordan.speak()

taylor = Person.new('Taylor',16)
taylor.speak()