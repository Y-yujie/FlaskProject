function bindEmailCaptchaClick(){
    //  $ 是jquery的获取元素方式，#是id选择器
    $("#captcha-btn").click(function (event){
        // $(this)当前按钮的jQuery对象,
        var $this = $(this);
        // 阻止默认事件
        event.preventDefault();

        var email = $("input[name='email']").val();  // 获取用户输入的值
        $.ajax({
            url: "/auth/captcha/email?email="+email,
            type: "GET",
            success: function (result){
                var code = result['code'];
                if (code==200){
                    var countdown = 60;
                    // 开始倒计时前，不能再点击
                    $this.off("click");
                    // 每间隔多少毫秒执行某个函数
                    var timer = setInterval(function (){
                        $this.text(countdown);
                        countdown-=1;
                        if(countdown <= 0){
                            // 清掉定时器
                            clearInterval(timer);
                            $this.text("获取验证码")
                        //     重新绑定点击事件
                            bindEmailCaptchaClick();
                        }
                    }, 1000)
                }
            },
            fail: function (error){
                console.log(error);
            }
        })
    });
}
// DOM模型，等文档全部加载完，才会执行函数
$(function (){
    bindEmailCaptchaClick()
});