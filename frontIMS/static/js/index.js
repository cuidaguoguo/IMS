/**
 * Created by Administrator on 2017/12/23.
 */
$(function () {
   $("#11").addClass("on");
});
//教师管理
$("#11").click(function () {
    $("#11").addClass("on");
    $("#22").removeClass("on");
    $("#33").removeClass("on");
    $("#44").removeClass("on");
    $("#55").removeClass("on");
});
$("#22").click(function () {
    $("#11").removeClass("on");
    $("#22").addClass("on");
    $("#33").removeClass("on");
    $("#44").removeClass("on");
    $("#55").removeClass("on");
});
$("#33").click(function () {
    $("#11").removeClass("on");
    $("#22").removeClass("on");
    $("#33").addClass("on");
    $("#44").removeClass("on");
    $("#55").removeClass("on");
});
$("#44").click(function () {
    $("#11").removeClass("on");
    $("#22").removeClass("on");
    $("#33").removeClass("on");
    $("#44").addClass("on");
    $("#55").removeClass("on");
});
$("#55").click(function () {
    $("#11").removeClass("on");
    $("#22").removeClass("on");
    $("#33").removeClass("on");
    $("#44").removeClass("on");
    $("#55").addClass("on");
});



