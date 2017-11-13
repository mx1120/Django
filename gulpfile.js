/**
 * Created by Administrator on 2017/11/13.
 */
var gulp = require('gulp'),
    sass = require('gulp-sass');

var version = ( + new Date())

gulp.task('login', function () {
    return gulp.src(['site_media/scss/index/*.scss'])
        .pipe(sass())
        .pipe(gulp.dest('site_media/css/index'))
})

gulp.task('default', function () {
    gulp.watch('site_media/scss/index/*.scss', ['login'])
})