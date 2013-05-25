var students = {
  length: 0,

  add: function(student) {
    Array.prototype.push.call(this, student);
  }
};

var student_test = function() {
  assert(students.length == 0, "No students added yet");

  students.add({ name: 'Jordan', age: 20 });
  assert(students.length == 1, "One student added");
  assert(students[0].name == 'Jordan', "Jordan was added");
};

window.onload = student_test;
