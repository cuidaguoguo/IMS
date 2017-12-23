/**
 * Created by Administrator on 2017/12/23.
 */

// $(function () {
//     var account = $("input[id='account']").val("");
//     var password = $("input[id='password']").val("");
//
// });


//判断信息是否填写完成
function login() {
    var account = $("input[id='account']").val();
    var password = $("input[id='password']").val();
    if(password === null || password === undefined || password === ''){
        alert("请输入密码")
    }else if(account === null || account === undefined || account === ''){
        alert("请输入账号")
    }else{
        $.post("loginb",{password:password,account:account},function (result) {
            result = JSON.parse(result);
                if (result["status"] === 0) {
                    alert(result["message"]);
                    window.location.reload();
                } else if (result["status"] === 1) {
                    var username =  $.cookie('username', result["username"]);
                    var teacherid = $.cookie('teacherid',result["teacherid"]);
                    window.location.href =  '/frontIMS/index'
                } else {
                    alert('服务器异常');
                    window.location.reload()
                }
        })
    }
}