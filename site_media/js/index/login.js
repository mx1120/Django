/**
 * Created by Administrator on 2017/11/13.
 */

define(function (require, exports, module) {
    $('#btn').on('click',function () {
	    var username = $("#username").val(),
		    password = $("#password").val()
        $.post('/login/', {'username':username, 'password':password}, function (data) {
            var res = JSON.parse(data)
	        console.info(res)
            if(res.response == 'fail'){
                alert(res.message)
            }
        })
    })
})