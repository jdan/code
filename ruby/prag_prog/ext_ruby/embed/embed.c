#include "ruby.h"

int main(int argc, char **argv) {
  VALUE result;

  ruby_sysinit(&argc, &argv);
  RUBY_INIT_STACK;
  ruby_init();
  ruby_init_loadpath();

  rb_require("sum");   // or sum.rb
  rb_eval_string("$summer = Summer.new");
  rb_eval_string("$result = $summer.sum(10)");
  result = rb_gv_get("result");
  printf("Result = %d\n", NUM2INT(result));
  return ruby_cleanup(0);
}
