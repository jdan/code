for (var i = 1; i <= 5; i++) {
  setTimeout(function(n) {
    console.log('Iteration #' + n);
  }, 100, i);
}