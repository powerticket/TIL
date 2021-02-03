function ab () {
  const gulp = require('gulp')
  const babel = require('gulp-babel')
  gulp.src("es6/**/*.js")
    .pipe(babel())
    .pipe(gulp.dest("dist"))
  gulp.src("public/es6/**/*.js")
    .pipe(babel())
    .pipe(gulp.dest("dist"))
}

function defaultTask (ab) {
  // place code for your default task here
  ab()
}

exports.default = defaultTask