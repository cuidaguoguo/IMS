/**
 * Created by Administrator on 2017/12/23.
 */

// $(function () {
//     var account = $("input[id='account']").val("");
//     var password = $("input[id='password']").val("");
// });


//判断信息是否填写完成
function login() {
    var password = document.getElementById("password").value;
    var account = document.getElementById("account").value;
    if(password === null || password === undefined || password === ''){
        alert("请输入账号")
    }else if(account === null || account === undefined || account === ''){
        alert("请输入账号")
    }
}