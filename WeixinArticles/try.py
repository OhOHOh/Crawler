import re
import requests
from bs4 import BeautifulSoup

# <a target="_blank" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207022&amp;ver=1036&amp;signature=Hwf7MUmnUTvDqdJBTw5OVUNQ5z5vlqFnI1anjbS9gQz1f4ykQ0KGHFBvsUDGixEUusiIkqAiAAL1bCzTYE7UFHLQZcWqb-y20*DaNfL1ZfFOE6aghXhLcKwcaQyL3BTp&amp;new=1" id="sogou_vr_11002601_title_0" uigs="article_title_0" data-share="http://weixin.sogou.com/api/share?timestamp=1533207022&amp;signature=qIbwY*nI6KU9tBso4VCd8lYSesxOYgLcHX5tlbqlMR8N6flDHs4LLcFgRw7FjTAORzX5jGtjOLt9MDriAC6SPfYvUjB7g6TV9aO9qSlkPjTBIxTArirVeh7wfHqqFWLGVN7N79E3Cj9k*-MXqu2CE5kC5wtNbJ9EFa85tVI5JsLNs-XK8nF3Od4f5-zmfLf*EQ*JADZ56C5h5cenZmMa9fQOsnAGu0XCX4RW4CCZCjo=">手把手教你利用【<em><!--red_beg-->Python<!--red_end--></em>】进行数据分析</a>

# http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207022&amp;ver=1036&amp;signature=Hwf7MUmnUTvDqdJBTw5OVUNQ5z5vlqFnI1anjbS9gQz1f4ykQ0KGHFBvsUDGixEUusiIkqAiAAL1bCzTYE7UFHLQZcWqb-y20*DaNfL1ZfFOE6aghXhLcKwcaQyL3BTp&amp;new=1
# https://mp.weixin.qq.com/s?src=11&timestamp=1533207022&ver=1036&signature=Hwf7MUmnUTvDqdJBTw5OVUNQ5z5vlqFnI1anjbS9gQz1f4ykQ0KGHFBvsUDGixEUusiIkqAiAAL1bCzTYE7UFHLQZcWqb-y20*DaNfL1ZfFOE6aghXhLcKwcaQyL3BTp&new=1
# http://weixin.sogou.com/api/share?timestamp=1533207022&amp;signature=qIbwY*nI6KU9tBso4VCd8lYSesxOYgLcHX5tlbqlMR8N6flDHs4LLcFgRw7FjTAORzX5jGtjOLt9MDriAC6SPfYvUjB7g6TV9aO9qSlkPjTBIxTArirVeh7wfHqqFWLGVN7N79E3Cj9k*-MXqu2CE5kC5wtNbJ9EFa85tVI5JsLNs-XK8nF3Od4f5-zmfLf*EQ*JADZ56C5h5cenZmMa9fQOsnAGu0XCX4RW4CCZCjo=
# https://mp.weixin.qq.com/s?src=11&timestamp=1533207022&ver=1036&signature=Hwf7MUmnUTvDqdJBTw5OVUNQ5z5vlqFnI1anjbS9gQz1f4ykQ0KGHFBvsUDGixEUusiIkqAiAAL1bCzTYE7UFHLQZcWqb-y20*DaNfL1ZfFOE6aghXhLcKwcaQyL3BTp&new=1

url = 'http://weixin.sogou.com/weixin?query=python&type=2&page=1'
headers = {
        'cookies': 'IPLOC=CN3100; SUV=000D111E6FBB318359C8BE86BA771808; SUID=E10888755218910A000000005B5FC0B8; SNUID=33DB5BA7D2D6A1930107F3C5D30E662B; ABTEST=0|1533001944|v1; weixinIndexVisited=1; JSESSIONID=aaalDPdRsj9b2-zSmJHsw; sct=2; ppinf=5|1533110038|1534319638|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo0OlRhbmt8Y3J0OjEwOjE1MzMxMTAwMzh8cmVmbmljazo0OlRhbmt8dXNlcmlkOjQ0Om85dDJsdUdjVU52NU92cGRLbUxjM3dNbjcyUzBAd2VpeGluLnNvaHUuY29tfA; pprdig=JzM58wY31Xko_FtUAZz3TZYsLjXqLlh0NhfcUTSrpOKSnsM_mDj8QvaQvnuu2WHs96s6iQUTiqsF5XQxdXof1os_EOMXGVKgkAG2gm_p9j8EkpZqILsJz2Y--hsG50UInyUFogKv2KaiAiWAwDP3C-dx7Tlbp40vFeuuL92hFew; sgid=02-34274603-AVthZxaUsZp4ACtJ9b5kOia8; ppmdig=1533110038000000f06734556f3a35c65309af2683c0784b',
        'Host': 'weixin.sogou.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
    }
# response = requests.get(url, headers)
html = '''
/Users/runshen/.pyenv/versions/3.6.2/bin/python /Users/runshen/work/pythonWork/CrawlerCQC/WeixinArticles/try.py

<!doctype html>
<html>
<head>
    <link rel="shortcut icon" href="//www.sogou.com/images/logo/new/favicon.ico?v=4" type="image/x-icon">
    <link href="//dlweb.sogoucdn.com/logo/images/2018/apple-touch-icon.png" id="apple-touch-icon" rel="apple-touch-icon-precomposed"/>
    <link href="//www.sogou.com/sug/css/m3.min.v.7.css" rel="stylesheet" type="text/css">
    <link href="/new/pc/css/weixin-public-new.min.css?v=20180504" rel="stylesheet" type="text/css">
    
        <link href="/new/pc/css/datepicker.min.css?v=20161107" rel="stylesheet" type="text/css">
    
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta http-equiv="Access-Control-Allow-Origin" content="*">
    <meta content="width=device-width,initial-scale=1.0" id="vp" name="viewport">
    <title>python的相关微信公众号文章 – 搜狗微信搜索</title>
    
    <script>
        var sst = {h_s :(new Date()).getTime()};
        var newpage = 1;
        var passportUserId = "";
        var oldQuery = "python";
        var gbkQuery = "python";
        var uuid = "01bd40ce-40dc-45d1-b8b0-8c2a22d58619";
        var keywords_string = "python";
        var sab = "3";
        var keywords = oldQuery.split(' ');
        var now = 1533207502201;
        var idc = "sjs";
        var clientIp = "117.136.8.227";
        var isIpad = false;
        //var article_anti_url = "";
    </script>
    <script>
        //以下为动态的全局 js，防止外部网站通过 window.opener.location 篡改我们的页面，以后不要通过 window.location 获取当前地址，只能用 document.location
        
    </script>
    <script src="/js/jquery-1.11.0.min.js" charset="gbk"></script>
    <script src="/new/pc/js/https_util.min.js?v=20180607"></script>
    <script src="/js/lib/juicer-min.js"></script>
    <script src="/new/weixin/js/common.min.js?v=20180607"></script>
    <script src="/new/pc/js/common.min.js?v=20180607"></script>
    
    <script>
        var uigs_para = {
            "uigs_t": "1533207502201",
            "uigs_productid": "vs_web",
            "terminal"      : "web",
            "vstype"        : "weixin",
            "pagetype"      : "result",
            "channel"       : "result_article",
            "s_from"        : "",
            "sourceid"      : "",
            "type"          : "weixin_search_pc",
            "uigs_cookie"   : "SUID,sct",
            "uuid"          : "01bd40ce-40dc-45d1-b8b0-8c2a22d58619",
            "query"         : "python",
            "weixintype"    : "2",
            "exp_status"    : "-1",
            "exp_id_list"   : "0_0",
            "wuid"          : "",
            "snuid"         : "B25ADA2752542023E2DADB4852D87B74",
            "rn"            : 1,
            "login"         : passportUserId ? "1" : "0",
            "uphint"        : 1,
            "bottomhint"    : 1,
            "page"          : "1"
        };
    </script>
</head>
<body>
    

<!--start header-->
<div class="header-box">
    
    <div class="login-info">
        <a id="top_login" href="javascript:void(0);" uigs="home_login_top">登录</a>
    </div>

    <div class="header" id="scroll-header">
        <a title="回到搜狗首页" href="/" name="scroll-nav" class="logo" uigs="home"></a>
        <ul class="searchnav" name="scroll-nav">
            <li><a id="sogou_xinwen" href="http://news.sogou.com/news?ie=utf8&p=40230447&query=python" onclick="navBar(this,'query=');" uigs="nav_xinwen">新闻</a></li>
            <li><a id="sogou_wangye" href="http://www.sogou.com/web?ie=utf8&query=python" onclick="navBar(this,'query=');" uigs="nav_wangye">网页</a></li>
            <li class="cur"><a href="javascript:void(0)">微信</a></li>
            <li><a id="sogou_zhihu" href="http://zhihu.sogou.com/zhihu?ie=utf8&p=73351201&query=python" onclick="navBar(this,'query=')" uigs="nav_zhihu">知乎</a></li>
            <li><a id="sogou_tupian" href="http://pic.sogou.com/pics?ie=utf8&p=40230504&query=python" onclick="navBar(this,'query=')" uigs="nav_tupian">图片</a></li>
            <li><a id="sogou_shipin" href="https://v.sogou.com/v?ie=utf8&p=40230608&query=python" onclick="navBar(this,'query=')" uigs="nav_shipin">视频</a></li>
            <li><a id="sogou_mingyi" href="http://mingyi.sogou.com/mingyi?ie=utf8&query=python" onclick="navBar(this,'query=')" uigs="nav_mingyi">明医</a></li>
            <li><a id="sogou_yingwen" href="http://english.sogou.com/english?b_o_e=1&ie=utf8&query=python" onclick="navBar(this,'query=')" uigs="nav_yingwen">英文</a></li>
            <li><a id="sogou_wenwen" href="http://wenwen.sogou.com/s/?ch=weixinsearch&w=python" data-index="http://wenwen.sogou.com/?ch=weixinsearch" onclick="navBar(this,'w=')" uigs="nav_wenwen">问问</a></li>
            <li><a id="sogou_dangjian" href="http://dangjian.sogou.com/dangjian?ie=utf-8&query=python" onclick="navBar(this,'query=')" uigs="nav_dangjian">党建</a></li>
            <li><a id="top_more" href="http://www.sogou.com/docs/more.htm?v=1" target="_blank" uigs="nav_more">更多>></a></li>
        </ul>
        

<form name="searchForm" action="/weixin">
    <div class="querybox">
        <div class="qborder">
            <div class="qborder2">
                <input type="hidden" name="type" value="2"/>
                <input type="hidden" name="s_from" value="input"/>
                <input type="text" class="query" name="query" id="query" ov="python" value="python" autocomplete="off"/>
                
                    <input type="hidden" name="ie" value="utf8"/>
                
                <a href="javascript:void(0)" class="qreset2" name="reset" uigs="search_reset"></a>
            </div>
        </div>
        <input type="button" value="搜文章" class="swz" onclick="search(this,2)" uigs="search_article"/>
        <input type="button" value="搜公众号" class="swz2" onclick="search(this,1)" uigs="search_account"/>
        <input type="hidden" name="_sug_" value="n"/>
        <input type="hidden" name="_sug_type_" value=""/>
    </div>
</form>
        
<dl class="hint2" id="float_uphint" style="display: none">
	<dt>相关推荐：</dt>
	<dd>
	<a target="_blank" uigs="article_up_hint_0"  href="/weixin?type=2&ie=utf8&query=python%E6%80%8E%E4%B9%88%E8%AF%BB&s_from=up_hint">python怎么读</a>
</dd><dd>
	<a target="_blank" uigs="article_up_hint_1"  href="/weixin?type=2&ie=utf8&query=python%E6%98%AF%E4%BB%80%E4%B9%88&s_from=up_hint">python是什么</a>
</dd><dd>
	<a target="_blank" uigs="article_up_hint_2"  href="/weixin?type=2&ie=utf8&query=python%E6%95%99%E7%A8%8B&s_from=up_hint">python教程</a>
</dd><dd>
	<a target="_blank" uigs="article_up_hint_3"  href="/weixin?type=2&ie=utf8&query=php&s_from=up_hint">php</a>
</dd>
</dl>

    </div>
</div>
<!--end header-->
    
    <div class="wrapper" id="wrapper">
        <div class="main-left" id="main">
            
<div class="dy-pop2 dy-pop5 float" id="share_box" style="display: none">
    <a href="javascript:void(0)" class="close" data-except="1" uigs="other_float_share_close"></a>
    <div class="fxico-box">
        <a href="javascript:void(0)" class="sina" data-except="1" uigs="other_float_share_sina"></a>
        <a href="javascript:void(0)" class="weixin" data-except="1" uigs="other_float_share_weixin"></a>
        <a href="javascript:void(0)" class="zone" target="_blank" data-except="1" uigs="other_float_share_zone"></a>
        <a href="javascript:void(0)" class="tieba" target="_blank" data-except="1" uigs="other_float_share_tieba"></a>
        <a href="javascript:void(0)" class="tx" target="_blank" data-except="1" uigs="other_float_share_tx"></a>
        <a href="javascript:void(0)" class="renren" target="_blank" data-except="1" uigs="other_float_share_renren"></a>
        <a href="javascript:void(0)" class="douban" target="_blank" data-except="1" uigs="other_float_share_douban"></a>
        <a href="javascript:void(0)" class="qq" target="_blank" data-except="1" uigs="other_float_share_qq"></a>
    </div>
</div>


<div class="dy-pop2 dy-pop5 float" id="erweima_box" style="display: none"></div>
<script type="text/template" id="erweima_tpl">
    <a href="javascript:void(0)" class="close" data-except="1" uigs="other_float_weixin_close"></a>
    <div class="fxico-box2">微信扫一扫关注<br/><img width="104" height="104" src="${imgsrc}"/></div>
</script>
            

<script>
    //高级工具参数对象
    var toolParas = {
        tsn : '0',
        ft : '',
        et : '',
        interation : '',
        wxid : '',
        usip : ''
    };
    var from_tool = '0';
</script>
<div class="wx-topbox">
    <div class="all-time">
        <div class="all-time-y2 ">
            <div class="all-time-y all-time-y-v1" id="text">
                以下内容来自微信公众平台<div class="tool" id="tool_show"><a href="javascript:void(0)" uigs="select_show">搜索工具</a></div>
            </div>
            
                <div class="all-time-y" id="tool">
                    <span class="all-wy-box">
                        <a href="javascript:void(0)" class="btn-time" id="time" data-except="1">全部时间</a>
                        <div class="time-box float" style="width:120px; left:0px; display: none;">
                            <i></i>
                            <a href="javascript:void(0)" class="time-range" data-type="0" uigs="select_time_all">全部时间</a>
                            <a href="javascript:void(0)" class="time-range" data-type="1" uigs="select_time_day">一天内</a>
                            <a href="javascript:void(0)" class="time-range" data-type="2" uigs="select_time_week">一周内</a>
                            <a href="javascript:void(0)" class="time-range" data-type="3" uigs="select_time_month">一月内</a>
                            <a href="javascript:void(0)" class="time-range" data-type="4" uigs="select_time_year">一年内</a>
                            <div class="zdy">
                                <span>自定义</span>
                                <input type="text" id="date_start" placeholder="从">
                                <input type="text" id="date_end" placeholder="至">
                                <p class="input-box-err" style="display: none;">时间格式错误</p>
                                <a href="javascript:void(0)" class="enter" id="time_enter" data-except="1" uigs="select_time_zdy">确认</a>
                            </div>
                        </div>
                    </span>
                    <span class="line"></span>
                    <span class="all-wy-box">
                        <a href="javascript:void(0)" class="btn-time" id="type" data-except="1">全部类型</a>
                        <div class="time-box float" style="left: -19px; display: none;">
                            <form action="javascript:void(0)" data-except="1">
                                <i></i>
                                
                                <span><input type="checkbox" class="check" value="458754" id="check_pic" data-except="1"><label for="check_pic" data-except="1">图集</label></span>
                                
                                <span><input type="checkbox" class="check" value="458756" id="check_video" data-except="1"><label for="check_video" data-except="1">含视频</label></span>
                                <a href="javascript:void(0)" class="enter" id="type_enter" data-except="1" uigs="select_type_yes">确认</a>
                            </form>
                        </div>
                    </span>
                    <span class="line"></span>
                    <span class="all-wy-box">
                        <a href="javascript:void(0)" class="btn-time" id="search" data-except="1">账号内搜索</a>
                        <div class="time-box float" style="width:200px; left:-116px; display: none;">
                            <form action="javascript:void(0)">
                                <i></i>
                                <span class="input-box">
                                    <input type="text" class="s-sea" placeholder="输入公众号或微信号" data-except="1">
                                    <a href="javascript:void(0)" id="search_enter" data-except="1" uigs="select_search_yes"></a>
                                </span>
                                <p class="input-box-err" style="display: none;">没有找到相应的公众号</p>
                            </form>
                        </div>
                    </span>
                    <span class="line"></span>
                    <div class="tool" id="tool_hide" style="display: none"><a href="javascript:void(0)" uigs="select_hide">收起工具</a></div>
                    <div class="tool tool-v1" id="tool_clear" style="display: none"><a href="javascript:void(0)" uigs="select_clear">取消筛选</a></div>
                </div>
            
        </div>
    </div>
</div>

    <script src="/new/pc/js/datepicker.min.js?v=20161107"></script>
    <script src="/new/pc/js/tool.min.js?v=20180509"></script>

<div class="top-hintBox" id="stable_uphint" style="display: none;">
	<dl class="hint2">
		<dt>相关推荐：</dt>
		<dd>
		<a target="_blank" uigs="article_up_hint_0"  href="/weixin?type=2&ie=utf8&query=python%E6%80%8E%E4%B9%88%E8%AF%BB&s_from=up_hint">python怎么读</a>
	</dd><dd>
		<a target="_blank" uigs="article_up_hint_1"  href="/weixin?type=2&ie=utf8&query=python%E6%98%AF%E4%BB%80%E4%B9%88&s_from=up_hint">python是什么</a>
	</dd><dd>
		<a target="_blank" uigs="article_up_hint_2"  href="/weixin?type=2&ie=utf8&query=python%E6%95%99%E7%A8%8B&s_from=up_hint">python教程</a>
	</dd><dd>
		<a target="_blank" uigs="article_up_hint_3"  href="/weixin?type=2&ie=utf8&query=php&s_from=up_hint">php</a>
	</dd>
	</dl>
</div>


<div class="news-box">
    
<ul class="news-list">
	
		<!-- a -->
		<li id="sogou_vr_11002601_box_0" d="ab735a258a90e8e1-6bee54fcbd896b2a-d7d77f64d26ef38a1f4ffe11fe92b984">
<div class="img-box">
<a data-z="art" target="_blank" id="sogou_vr_11002601_img_0" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=Hwf7MUmnUTvDqdJBTw5OVUNQ5z5vlqFnI1anjbS9gQz1f4ykQ0KGHFBvsUDGixEU19bibyVDYwrNzTN8R0AI6BUVHKUymMd1vo9UCc-rs3Peh4qnBjy5jQhDGASBgPLI&amp;new=1" uigs="article_image_0"><img src="//img01.sogoucdn.com/net/a/04/link?appid=100520033&amp;url=http://mmbiz.qpic.cn/mmbiz_jpg/l34aovS2ONPDgT7KFsnEEdRtr9uribf6TZIpia9nKw9s5qg63CVoH1Ft4J84Ke1Okc4EWTibE4MQd187utficwcncw/0?wx_fmt=jpeg" onload="resizeImage(this,140,105)" onerror="errorImage(this)"></a>
</div>
<div class="txt-box">
<h3>
<a target="_blank" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=Hwf7MUmnUTvDqdJBTw5OVUNQ5z5vlqFnI1anjbS9gQz1f4ykQ0KGHFBvsUDGixEU19bibyVDYwrNzTN8R0AI6BUVHKUymMd1vo9UCc-rs3Peh4qnBjy5jQhDGASBgPLI&amp;new=1" id="sogou_vr_11002601_title_0" uigs="article_title_0" data-share="http://weixin.sogou.com/api/share?timestamp=1533207502&amp;signature=qIbwY*nI6KU9tBso4VCd8lYSesxOYgLcHX5tlbqlMR8N6flDHs4LLcFgRw7FjTAORzX5jGtjOLt9MDriAC6SPfYvUjB7g6TV9aO9qSlkPjTBIxTArirVeh7wfHqqFWLGVN7N79E3Cj9k*-MXqu2CE5kC5wtNbJ9EFa85tVI5JsLNs-XK8nF3Od4f5-zmfLf*JizdL1ZVB5L9cRlUl50E2jpHyU7fDxi1*jZxZCi-jeo=">手把手教你利用【<em><!--red_beg-->Python<!--red_end--></em>】进行数据分析</a>
</h3>
<p class="txt-info" id="sogou_vr_11002601_summary_0">培训咨询微信:13600977889回复&ldquo;大数据&rdquo;得到大数据学习资料回复&ldquo;经典&rdquo;下载经典影音 动漫 周星驰合集 余罪 等好料回复&ldquo;关注...</p>
<div class="s-p" t="1533204951">
<a class="account" target="_blank" id="sogou_vr_11002601_account_0" i="oIWsFt9Aqk5OTgGvUXI-YGt5Q89Y" href="http://mp.weixin.qq.com/profile?src=3&amp;timestamp=1533207502&amp;ver=1&amp;signature=5PrHYogSCRS2EwTkPAjqeHbSR1gP5dDw5VoiV3sV05fWK3LrXSyPMCmnOV6rjnJ75ifco8DRsusGOlk3867bjA==" data-headimage="http://wx.qlogo.cn/mmhead/Q3auHgzwzM6D0ibpSxOoeuPqr9MR0d583l8J8vjGFlicf17j0AYRX1wA/0" data-isV="1" uigs="article_account_0">中云大数据分析</a><span class="s2"><script>document.write(timeConvert('1533204951'))</script></span>
<div class="moe-box">
<span style="display:none;" class="sc"><a data-except="1" class="sc-a" href="javascript:void(0)" uigs="share_0"></a></span><span style="display:none;" class="fx"><a data-except="1" class="fx-a" href="javascript:void(0)" uigs="like_0"></a></span>
</div>
</div>
</div>
</li>

		<!-- z -->
	
		<!-- a -->
		<li id="sogou_vr_11002601_box_1" d="ab735a258a90e8e1-6bee54fcbd896b2a-80d802fb0e6120677c388a0a675b5d6c">
<div class="img-box">
<a data-z="art" target="_blank" id="sogou_vr_11002601_img_1" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=sPx5cbdqM0qcQRoh2ZRz0aqYwcv8PRG-9g1OtQdcY6pcIZ0b5dM*pvQWEUqQHrvk8NXTElehy*WO1FzqNCl48OD2B*K3Q4cw1875D97WcoRlWjZqNlSnusBryQgssa6m&amp;new=1" uigs="article_image_1"><img src="//img01.sogoucdn.com/net/a/04/link?appid=100520033&amp;url=http://mmbiz.qpic.cn/mmbiz_jpg/MOv840XPG5UQ7ic9fxadCFITcD55UtD0icut1gt1T9cEgRzkibn74ricgzQgfBZCmzzYhTqJ73kXKamIRG3GQAxfIg/0?wx_fmt=jpeg" onload="resizeImage(this,140,105)" onerror="errorImage(this)"></a>
</div>
<div class="txt-box">
<h3>
<a target="_blank" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=sPx5cbdqM0qcQRoh2ZRz0aqYwcv8PRG-9g1OtQdcY6pcIZ0b5dM*pvQWEUqQHrvk8NXTElehy*WO1FzqNCl48OD2B*K3Q4cw1875D97WcoRlWjZqNlSnusBryQgssa6m&amp;new=1" id="sogou_vr_11002601_title_1" uigs="article_title_1" data-share="http://weixin.sogou.com/api/share?timestamp=1533207502&amp;signature=qIbwY*nI6KU9tBso4VCd8lYSesxOYgLcHX5tlbqlMR8N6flDHs4LLcFgRw7FjTAOAJ-1-S2BS6PwpCr5eN2x5uE1BnL8RIDZHeIlNLkzD1ZQVKvnmSMMx3ucUeS48x9xJzySPm-ejFfRwx4TxRZFXqpzQ65AvLXxNf5ahDythQKYBZQ2yAtqxcNyZ8YikMjHozbpSjnh2UPn4MkvQy5-u5QZr1I4sTGdKoEUBYB5XK4="><em><!--red_beg-->Python<!--red_end--></em>为什么是编程语言中最skr的?</a>
</h3>
<p class="txt-info" id="sogou_vr_11002601_summary_1">源/大数据文摘 编译 / 小七、Virgil、Alieen<em><!--red_beg-->Python<!--red_end--></em>的出现让计算机编程语言不再是生僻的专业技能,而是常人都能学习和使用的万金油...</p>
<div class="s-p" t="1533126618">
<a class="account" target="_blank" id="sogou_vr_11002601_account_1" i="oIWsFt-sUnUVNS30blV2VPnwhfI0" href="http://mp.weixin.qq.com/profile?src=3&amp;timestamp=1533207502&amp;ver=1&amp;signature=Gac3ehstJCNYEV894MsFZsnt8-kUpSHTy4qCQcrX9eCx-w*VFo9h*QmlF8kNxpQbmHN3sbXJtAjf0EY6woAjRg==" data-headimage="http://wx.qlogo.cn/mmhead/Q3auHgzwzM7jO6ZicoGkauoZHl3Od2AGEZ1HnpVDPzSPsjDPteR1ZYQ/0" data-isV="1" uigs="article_account_1">AI时间</a><span class="s2"><script>document.write(timeConvert('1533126618'))</script></span>
<div class="moe-box">
<span style="display:none;" class="sc"><a data-except="1" class="sc-a" href="javascript:void(0)" uigs="share_1"></a></span><span style="display:none;" class="fx"><a data-except="1" class="fx-a" href="javascript:void(0)" uigs="like_1"></a></span>
</div>
</div>
</div>
</li>

		<!-- z -->
	
		<!-- a -->
		<li id="sogou_vr_11002601_box_2" d="ab735a258a90e8e1-6bee54fcbd896b2a-96d7760b334d7473830b5f774ecbcaee">
<div class="img-box">
<a data-z="art" target="_blank" id="sogou_vr_11002601_img_2" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=Kdz8SwidKHuc-6lVebvzdLNCbpXn7UYMQ9OjxO2UK1ES3VAAONPJ6ZNWxNXtdndmCEfOM1eZl*sapSSeFDRAOdiB1rVODxCuYfGyZgraz*N3BLPTM1r7V8gkMjWDQXK-&amp;new=1" uigs="article_image_2"><img src="//img01.sogoucdn.com/net/a/04/link?appid=100520033&amp;url=http://mmbiz.qpic.cn/mmbiz_jpg/Pn4Sm0RsAuhSvZMAt2zKcxGQN3l1NV4LGQw5AicApKjJvjYdMY3YPW59CKGH7GgqmvDYd2Uar2WHpQ1mpzwevZw/0?wx_fmt=jpeg" onload="resizeImage(this,140,105)" onerror="errorImage(this)"></a>
</div>
<div class="txt-box">
<h3>
<a target="_blank" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=Kdz8SwidKHuc-6lVebvzdLNCbpXn7UYMQ9OjxO2UK1ES3VAAONPJ6ZNWxNXtdndmCEfOM1eZl*sapSSeFDRAOdiB1rVODxCuYfGyZgraz*N3BLPTM1r7V8gkMjWDQXK-&amp;new=1" id="sogou_vr_11002601_title_2" uigs="article_title_2" data-share="http://weixin.sogou.com/api/share?timestamp=1533207502&amp;signature=qIbwY*nI6KU9tBso4VCd8lYSesxOYgLcHX5tlbqlMR8N6flDHs4LLcFgRw7FjTAO7iy2zEfnrg2GpROYWYV1hReLi3x9jrpIhalUHlSsdL6ZNbkEB8ho1K1qTZOxhxRMbFcBf0kez0vJhFtrJk4x08M5hFx3jvIlTvkkD1gG*HcKSA6UIivT7k2AfAywN5X9vf-3HKzZ-RM*lVEafIUp7FJDJpoR-c9uLXOWfZy4Efk="><em><!--red_beg-->Python<!--red_end--></em> 彻底甩掉 Java,位居 48 种编程语言之首!</a>
</h3>
<p class="txt-info" id="sogou_vr_11002601_summary_2"><em><!--red_beg-->Python<!--red_end--></em> 再占榜首,Java 屈居第四2018 IEEE Spectrum 编程语言排行榜 Top 10去年,<em><!--red_beg-->Python<!--red_end--></em>(得分 100 分) 仅以 0.3 分的优势击败了 ...</p>
<div class="s-p" t="1533107390">
<a class="account" target="_blank" id="sogou_vr_11002601_account_2" i="oIWsFt6HGMaRoWYyRbYCb5or9GTg" href="http://mp.weixin.qq.com/profile?src=3&amp;timestamp=1533207502&amp;ver=1&amp;signature=B8LotqP-Y1OqKIEnKb*NccVMGWVZQLBCuEvFgxrTLOJRvU37hny0HtKtI4RpMQYewhUl9wjXILeX*0SgSD22hw==" data-headimage="http://wx.qlogo.cn/mmhead/Q3auHgzwzM5cvOsZy9wYacdpSLicuibpMXzQHTKxLdh69fP0FFtliazuQ/0" data-isV="1" uigs="article_account_2">CSDN</a><span class="s2"><script>document.write(timeConvert('1533107390'))</script></span>
<div class="moe-box">
<span style="display:none;" class="sc"><a data-except="1" class="sc-a" href="javascript:void(0)" uigs="share_2"></a></span><span style="display:none;" class="fx"><a data-except="1" class="fx-a" href="javascript:void(0)" uigs="like_2"></a></span>
</div>
</div>
</div>
</li>

		<!-- z -->
	
		<!-- a -->
		<li id="sogou_vr_11002601_box_3" d="ab735a258a90e8e1-6bee54fcbd896b2a-de6221d3e4e3f86df62cf6b046fee87c">
<div class="img-box">
<a data-z="art" target="_blank" id="sogou_vr_11002601_img_3" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=YaTWkdN4HHTb4WMx-CBcmgqrwKAMnKB12l*K73IGBXBTeMVKUwUEmvwsoxmFOWKbpxAgFceOJbSPGsT8iVJH8qHK4gs7kpaqGeJD5hOyUIW3H-aQ5Nodx3AJe2bnJG5G&amp;new=1" uigs="article_image_3"><img src="//img01.sogoucdn.com/net/a/04/link?appid=100520033&amp;url=http://mmbiz.qpic.cn/mmbiz_jpg/uQpFsiblRrdZ9KQqY0fkibc8Clb5rjKkxGBvWWI1wRbUfK6HVnCMuHMcm3RdAQzNrNxbPLLUg4kTsV33dvItyKwA/0?wx_fmt=jpeg" onload="resizeImage(this,140,105)" onerror="errorImage(this)"></a>
</div>
<div class="txt-box">
<h3>
<a target="_blank" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=YaTWkdN4HHTb4WMx-CBcmgqrwKAMnKB12l*K73IGBXBTeMVKUwUEmvwsoxmFOWKbpxAgFceOJbSPGsT8iVJH8qHK4gs7kpaqGeJD5hOyUIW3H-aQ5Nodx3AJe2bnJG5G&amp;new=1" id="sogou_vr_11002601_title_3" uigs="article_title_3" data-share="http://weixin.sogou.com/api/share?timestamp=1533207502&amp;signature=qIbwY*nI6KU9tBso4VCd8lYSesxOYgLcHX5tlbqlMR8N6flDHs4LLcFgRw7FjTAONvNxxJA*I4Yo*6qjhLnF2s2QoiH2SAvxGcKtysMwV7o3H6nkphMBf5csoSHN4gmGahLs0*GD5abUanIdnibgcov3*KwJ3YxxZeqAD7etnEB*RMgYqj94pD4CXLs*oP0AnrHMOzhP9QHRPQEv5tWTRXizXkk3J*SVDy8wPk47PCw=">零基础如何优雅地入门<em><!--red_beg-->Python<!--red_end--></em></a>
</h3>
<p class="txt-info" id="sogou_vr_11002601_summary_3">&ldquo;<em><!--red_beg-->Python<!--red_end--></em>爆红背后的原因是什么?为什么身边的小伙伴都开始学习<em><!--red_beg-->Python<!--red_end--></em>?怎样零基础开始学习这门语言?学习难点在哪里?DT财经...</p>
<div class="s-p" t="1531830646">
<a class="account" target="_blank" id="sogou_vr_11002601_account_3" i="oIWsFt-AMY8g42ZzPpyV_52l-m4w" href="http://mp.weixin.qq.com/profile?src=3&amp;timestamp=1533207502&amp;ver=1&amp;signature=RdA3Dg*EFR3plZ3RY-U59EPQAwVjjPBZ4RM9mlpN0ZOgGW*z1t*sEhhYv8WbA9m0A81PYQmuWZKutHgL5wT55Q==" data-headimage="http://wx.qlogo.cn/mmhead/Q3auHgzwzM694K5hVmRpsia3xz2EAH6qTBzJf5kyOo2VHPw83PHSnCA/0" data-isV="1" uigs="article_account_3">DT数据侠</a><span class="s2"><script>document.write(timeConvert('1531830646'))</script></span>
<div class="moe-box">
<span style="display:none;" class="sc"><a data-except="1" class="sc-a" href="javascript:void(0)" uigs="share_3"></a></span><span style="display:none;" class="fx"><a data-except="1" class="fx-a" href="javascript:void(0)" uigs="like_3"></a></span>
</div>
</div>
</div>
</li>

		<!-- z -->
	
		<!-- a -->
		<li id="sogou_vr_11002601_box_4" d="ab735a258a90e8e1-6bee54fcbd896b2a-5980d58ff5d1603b8dd80668e4d3e359">
<div class="img-box">
<a data-z="art" target="_blank" id="sogou_vr_11002601_img_4" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=Ta0-4YclP3pgReh3FbpEKUtB1k2GT1aopAyrR5AedM9dsZALJOqwwRkLcc8oxkYe8c7foAPVcSY4yZ2mSdX2Ds2BFT5OFjuTp-7SXerYj-2gOz7aR7HLboso5EQJ58RI&amp;new=1" uigs="article_image_4"><img src="//img01.sogoucdn.com/net/a/04/link?appid=100520033&amp;url=http://mmbiz.qpic.cn/mmbiz_jpg/IP70Vic417DM6da2qxFoGpV2bHZJhnzoFgPnHsfJ8vJ7WJDGQWOibwcpZFDfY9ibRpWFHyC1vjPeIHSZUsyc7oycw/0?wx_fmt=jpeg" onload="resizeImage(this,140,105)" onerror="errorImage(this)"></a>
</div>
<div class="txt-box">
<h3>
<a target="_blank" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=Ta0-4YclP3pgReh3FbpEKUtB1k2GT1aopAyrR5AedM9dsZALJOqwwRkLcc8oxkYe8c7foAPVcSY4yZ2mSdX2Ds2BFT5OFjuTp-7SXerYj-2gOz7aR7HLboso5EQJ58RI&amp;new=1" id="sogou_vr_11002601_title_4" uigs="article_title_4" data-share="http://weixin.sogou.com/api/share?timestamp=1533207502&amp;signature=qIbwY*nI6KU9tBso4VCd8lYSesxOYgLcHX5tlbqlMR8N6flDHs4LLcFgRw7FjTAOQbPqii7K8u4eMT5cr-AN7sm4oBG1jgUJyOo6wAhzrWtXU70KgobJXF88kMpi3w2m5GzEpRLYkKfTiSE1cpidrCkHSj8-Mt6BTsub8nK0G62mFK2E8SVjgdOd2zn2nCYKzoQR*DWXgPS4HtiI9GzS-SRJZiTi6wMntvaGZJVauS4="><em><!--red_beg-->Python<!--red_end--></em>入门学习篇(10)-循环语句</a>
</h3>
<p class="txt-info" id="sogou_vr_11002601_summary_4">下面是在大多数编程语言中的循环语句的一般形式:2<em><!--red_beg-->Python<!--red_end--></em>循环语句简介<em><!--red_beg-->Python<!--red_end--></em>提供了for循环和while循环(在<em><!--red_beg-->Python<!--red_end--></em>中没有do..while...</p>
<div class="s-p" t="1530789252">
<a class="account" target="_blank" id="sogou_vr_11002601_account_4" i="oIWsFt_Id9NTbaO6ms2zvSBm2RzI" href="http://mp.weixin.qq.com/profile?src=3&amp;timestamp=1533207502&amp;ver=1&amp;signature=QFfdaX3kDbw3ybfihT-8ASZmZiSzl44OwgLyFSsl8JlXkvjHZ1DZq2mDYCenF5eqVU*I8qiA*dGuCvQVix0D0g==" data-headimage="http://wx.qlogo.cn/mmhead/Q3auHgzwzM4OoofsMPibTjGSeibBDwydF3TP9yG2UQmnlsNHFKe0Juyg/0" data-isV="1" uigs="article_account_4">马哥Linux运维</a><span class="s2"><script>document.write(timeConvert('1530789252'))</script></span>
<div class="moe-box">
<span style="display:none;" class="sc"><a data-except="1" class="sc-a" href="javascript:void(0)" uigs="share_4"></a></span><span style="display:none;" class="fx"><a data-except="1" class="fx-a" href="javascript:void(0)" uigs="like_4"></a></span>
</div>
</div>
</div>
</li>

		<!-- z -->
	
		<!-- a -->
		<li id="sogou_vr_11002601_box_5" d="ab735a258a90e8e1-6bee54fcbd896b2a-c30cea31fa01766135a17ace06716430">
<div class="img-box">
<a data-z="art" target="_blank" id="sogou_vr_11002601_img_5" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=Ta0-4YclP3pgReh3FbpEKUtB1k2GT1aopAyrR5AedM8ScHrUCmvIYmU6uzDd53nNYDpgnn6vqMomKf24vf0Z7B*y4Qf1jjj9K2f0YO2THUvEiLCN35B0czABustFDftz&amp;new=1" uigs="article_image_5"><img src="//img01.sogoucdn.com/net/a/04/link?appid=100520033&amp;url=http://mmbiz.qpic.cn/mmbiz_jpg/IP70Vic417DN4Qt3ibPt1Hl3zdWiatAGAv4d1ricF7Y9ScfgP7MetNoPNdUuXfeYFgJKafe69iavCQe4y54icA1Z4jYw/0?wx_fmt=jpeg" onload="resizeImage(this,140,105)" onerror="errorImage(this)"></a>
</div>
<div class="txt-box">
<h3>
<a target="_blank" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=Ta0-4YclP3pgReh3FbpEKUtB1k2GT1aopAyrR5AedM8ScHrUCmvIYmU6uzDd53nNYDpgnn6vqMomKf24vf0Z7B*y4Qf1jjj9K2f0YO2THUvEiLCN35B0czABustFDftz&amp;new=1" id="sogou_vr_11002601_title_5" uigs="article_title_5" data-share="http://weixin.sogou.com/api/share?timestamp=1533207502&amp;signature=qIbwY*nI6KU9tBso4VCd8lYSesxOYgLcHX5tlbqlMR8N6flDHs4LLcFgRw7FjTAOQbPqii7K8u4eMT5cr-AN7sm4oBG1jgUJyOo6wAhzrWt3iwuOAUE7hUQI*hpXkIMVlJ*33bVYqD2bDJ*5pXXMZmqt-ujOrKB2Yg0VRuusplyxozqfWJKO5QQ-SXVZivV3wQ9qvNPi5wbfAIZMKrGZEpqvKScdKw5iE13RRp5s0gQ=">用<em><!--red_beg-->Python<!--red_end--></em>制作迷宫GIF</a>
</h3>
<p class="txt-info" id="sogou_vr_11002601_summary_5">问:我是一个<em><!--red_beg-->Python<!--red_end--></em>迷,并且对迷宫的生成和迷宫解决的办法非常感兴趣.我很羡慕别人能够做出生成迷宫的动画.我如何能够用...</p>
<div class="s-p" t="1531131300">
<a class="account" target="_blank" id="sogou_vr_11002601_account_5" i="oIWsFt_Id9NTbaO6ms2zvSBm2RzI" href="http://mp.weixin.qq.com/profile?src=3&amp;timestamp=1533207502&amp;ver=1&amp;signature=QFfdaX3kDbw3ybfihT-8ASZmZiSzl44OwgLyFSsl8JlXkvjHZ1DZq2mDYCenF5eqVU*I8qiA*dGuCvQVix0D0g==" data-headimage="http://wx.qlogo.cn/mmhead/Q3auHgzwzM4OoofsMPibTjGSeibBDwydF3TP9yG2UQmnlsNHFKe0Juyg/0" data-isV="1" uigs="article_account_5">马哥Linux运维</a><span class="s2"><script>document.write(timeConvert('1531131300'))</script></span>
<div class="moe-box">
<span style="display:none;" class="sc"><a data-except="1" class="sc-a" href="javascript:void(0)" uigs="share_5"></a></span><span style="display:none;" class="fx"><a data-except="1" class="fx-a" href="javascript:void(0)" uigs="like_5"></a></span>
</div>
</div>
</div>
</li>

		<!-- z -->
	
		<!-- a -->
		<li id="sogou_vr_11002601_box_6" d="ab735a258a90e8e1-6bee54fcbd896b2a-89b640a8a3393df3c5f2ccbb9cd2c7d7">
<div class="img-box">
<a data-z="art" target="_blank" id="sogou_vr_11002601_img_6" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=Mp6KmhWNNU9*TQtI4S-w-BhutVTwR0RNU2BbTPoy2vyrtKg9UOpkEmeF0R2lv4tHWZbDBFl3N71Njc91dqzP4C6s7y*egzQcuh5qDJKewA82DbFmD8uIJ3DzpC1hLwdA&amp;new=1" uigs="article_image_6"><img src="//img01.sogoucdn.com/net/a/04/link?appid=100520033&amp;url=http://mmbiz.qpic.cn/mmbiz_jpg/ZF7JxHJcXRdc9RicqXhKs2AInvo8JzWejkAlpPRrAGeeSzo59NnCWiaxdCTh1CPcicOUSlzYc049lMDFwooqaAjSw/0?wx_fmt=jpeg" onload="resizeImage(this,140,105)" onerror="errorImage(this)"></a>
</div>
<div class="txt-box">
<h3>
<a target="_blank" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=Mp6KmhWNNU9*TQtI4S-w-BhutVTwR0RNU2BbTPoy2vyrtKg9UOpkEmeF0R2lv4tHWZbDBFl3N71Njc91dqzP4C6s7y*egzQcuh5qDJKewA82DbFmD8uIJ3DzpC1hLwdA&amp;new=1" id="sogou_vr_11002601_title_6" uigs="article_title_6" data-share="http://weixin.sogou.com/api/share?timestamp=1533207502&amp;signature=qIbwY*nI6KU9tBso4VCd8lYSesxOYgLcHX5tlbqlMR8N6flDHs4LLcFgRw7FjTAOS5Vo-6tx3AxYp-qrDJFJpJlJ6Y7bc-abe-j-fmZwk3lTNpLPFld319Jp6*O6gTM6CxHllI07psz-1fgGIqDD5IweMqo3MvW23o5MUDX7B7C6UzgK9RCmrGVTLtB9g2s4fMdG3SpBtcIQew9ovcDEwgLf4D5khvc7kMGnUm06fRA=">2018为什么你一定要学<em><!--red_beg-->Python<!--red_end--></em>?</a>
</h3>
<p class="txt-info" id="sogou_vr_11002601_summary_6">在壹课君看来,编程语言首推<em><!--red_beg-->Python<!--red_end--></em>,为什么这么说呢?<em><!--red_beg-->Python<!--red_end--></em>在2017年世界脚本语言排行榜中排名第1,也是多领域首选语言,作为...</p>
<div class="s-p" t="1531098047">
<a class="account" target="_blank" id="sogou_vr_11002601_account_6" i="oIWsFt697VgYfuqBShtybcxgj9dY" href="http://mp.weixin.qq.com/profile?src=3&amp;timestamp=1533207502&amp;ver=1&amp;signature=1Z5nuiaPZvBw2brz6plYrnWecsCi1mJGLfsKcIYYw2dr45-8xKvnB4t2PYgt21vFcH8MubRzmluQNrIJuck**A==" data-headimage="http://wx.qlogo.cn/mmhead/Q3auHgzwzM6e5SXcxKHZTKfyql10nugMbISjBySrmtozSk9luewpzw/0" data-isV="1" uigs="article_account_6">壹课</a><span class="s2"><script>document.write(timeConvert('1531098047'))</script></span>
<div class="moe-box">
<span style="display:none;" class="sc"><a data-except="1" class="sc-a" href="javascript:void(0)" uigs="share_6"></a></span><span style="display:none;" class="fx"><a data-except="1" class="fx-a" href="javascript:void(0)" uigs="like_6"></a></span>
</div>
</div>
</div>
</li>

		<!-- z -->
	
		<!-- a -->
		<li id="sogou_vr_11002601_box_7" d="ab735a258a90e8e1-6bee54fcbd896b2a-a6237771aae7edbcb772dbe506031ae4">
<div class="img-box">
<a data-z="art" target="_blank" id="sogou_vr_11002601_img_7" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=YaTWkdN4HHTb4WMx-CBcmgqrwKAMnKB12l*K73IGBXDDYOI8E7yH*MZhdpv1QJ-WaiFsrJugpbLEwUpkvOgQOIzzEbECZectK72*Fn6dr4Va-D6cj5lEWIC-H1vOkAmP&amp;new=1" uigs="article_image_7"><i></i><img src="//img01.sogoucdn.com/net/a/04/link?appid=100520033&amp;url=http://mmbiz.qpic.cn/mmbiz_jpg/uQpFsiblRrdapvbHfcIs6WJRnPiauBqGPHicRmIdvGY465adWLib81eibQPXygx01GpxoPk8v5RKICmpveciaJF09f0g/0?wx_fmt=jpeg" onload="resizeImage(this,140,105)" onerror="errorImage(this)"></a>
</div>
<div class="txt-box">
<h3>
<a target="_blank" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=YaTWkdN4HHTb4WMx-CBcmgqrwKAMnKB12l*K73IGBXDDYOI8E7yH*MZhdpv1QJ-WaiFsrJugpbLEwUpkvOgQOIzzEbECZectK72*Fn6dr4Va-D6cj5lEWIC-H1vOkAmP&amp;new=1" id="sogou_vr_11002601_title_7" uigs="article_title_7" data-share="http://weixin.sogou.com/api/share?timestamp=1533207502&amp;signature=qIbwY*nI6KU9tBso4VCd8lYSesxOYgLcHX5tlbqlMR8N6flDHs4LLcFgRw7FjTAONvNxxJA*I4Yo*6qjhLnF2s2QoiH2SAvxGcKtysMwV7oo-FKh3uI4PjtpTYPAg2b5Ql49lwCVbXduC*nWHz5HYkCwkHjki9IvG7I-yVB8ZQZf2EixgUtnAT75bZwElb*81Z0wCA4N6IwZaQFGuK4lO9ksbRJn8aBwVKbY2HrWIS8=">数据侠<em><!--red_beg-->Python<!--red_end--></em>训练营招募正式启动!</a>
</h3>
<p class="txt-info" id="sogou_vr_11002601_summary_7">学习最流行的编程语言轻松掌握简单高效的编程技巧来自美国的热门权威训练营45小时,带你从零开始学习<em><!--red_beg-->Python<!--red_end--></em>你是否适合参与?...</p>
<div class="s-p" t="1530159566">
<a class="account" target="_blank" id="sogou_vr_11002601_account_7" i="oIWsFt-AMY8g42ZzPpyV_52l-m4w" href="http://mp.weixin.qq.com/profile?src=3&amp;timestamp=1533207502&amp;ver=1&amp;signature=RdA3Dg*EFR3plZ3RY-U59EPQAwVjjPBZ4RM9mlpN0ZOgGW*z1t*sEhhYv8WbA9m0A81PYQmuWZKutHgL5wT55Q==" data-headimage="http://wx.qlogo.cn/mmhead/Q3auHgzwzM694K5hVmRpsia3xz2EAH6qTBzJf5kyOo2VHPw83PHSnCA/0" data-isV="1" uigs="article_account_7">DT数据侠</a><span class="s2"><script>document.write(timeConvert('1530159566'))</script></span>
<div class="moe-box">
<span style="display:none;" class="sc"><a data-except="1" class="sc-a" href="javascript:void(0)" uigs="share_7"></a></span><span style="display:none;" class="fx"><a data-except="1" class="fx-a" href="javascript:void(0)" uigs="like_7"></a></span>
</div>
</div>
</div>
</li>

		<!-- z -->
	
		<!-- a -->
		<li id="sogou_vr_11002601_box_8" d="ab735a258a90e8e1-6bee54fcbd896b2a-825b7df5e273d160d57496cc9b503055">
<div class="img-box">
<a data-z="art" target="_blank" id="sogou_vr_11002601_img_8" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=CWAeTM8Wddmr03hcppEbl6Agj6oEWimMb2AR1x685xiAyWE6WO3XGiF6FBYt3jRRBVrmdbxGgwfS-lMK5nYIsQUTEI2sCvGp95t1dfBeVEkx6FvLU9pyHSn*MoCffJGN&amp;new=1" uigs="article_image_8"><img src="//img01.sogoucdn.com/net/a/04/link?appid=100520033&amp;url=http://mmbiz.qpic.cn/mmbiz_jpg/IP70Vic417DMP0aqnJU7njV6HBfVaVdg2jXlanliaF6hhduSQdPImTibModYtMiavRNXsNnqfz93dTXTkyCCF6VwpA/0?wx_fmt=jpeg" onload="resizeImage(this,140,105)" onerror="errorImage(this)"></a>
</div>
<div class="txt-box">
<h3>
<a target="_blank" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=CWAeTM8Wddmr03hcppEbl6Agj6oEWimMb2AR1x685xiAyWE6WO3XGiF6FBYt3jRRBVrmdbxGgwfS-lMK5nYIsQUTEI2sCvGp95t1dfBeVEkx6FvLU9pyHSn*MoCffJGN&amp;new=1" id="sogou_vr_11002601_title_8" uigs="article_title_8" data-share="http://weixin.sogou.com/api/share?timestamp=1533207502&amp;signature=qIbwY*nI6KU9tBso4VCd8lYSesxOYgLcHX5tlbqlMR8N6flDHs4LLcFgRw7FjTAOZmcufk5cnpzH5ffn8y2z8MKVP-gsAvH0ytGgAL3qzNFKMbBM5NoNt7gDUHYfrPPC-xfx-6UwAp2c01AX3TmIQKxGhhf6IY7RzHIxk8H4ekOCGMRa-97qc7jlvPO2d3Hus04FekFq2vs2ESxSXPaHNKcYrYRumnSTvX2emLuWbdQ="><em><!--red_beg-->Python<!--red_end--></em>入门教程:超详细1小时学会<em><!--red_beg-->Python<!--red_end--></em></a>
</h3>
<p class="txt-info" id="sogou_vr_11002601_summary_8">1.Hello world安装完<em><!--red_beg-->Python<!--red_end--></em>之后,打开IDLE(<em><!--red_beg-->Python<!--red_end--></em> GUI) ,该程序是<em><!--red_beg-->Python<!--red_end--></em>语言解释器,你写的语句能够立即运行.我们写下一句著名...</p>
<div class="s-p" t="1531966052">
<a class="account" target="_blank" id="sogou_vr_11002601_account_8" i="oIWsFt27JUkHJQB9KekgoPArjaJg" href="http://mp.weixin.qq.com/profile?src=3&amp;timestamp=1533207502&amp;ver=1&amp;signature=-6VZnekOTxeAbwAgVNiwCCkc1xoNjR9zSgQ5rRXal4XcOCBF8jRhaRxqXTApPNaN3nPh*mHJLIWjLXR7iKVi8A==" data-headimage="http://wx.qlogo.cn/mmhead/Q3auHgzwzM6XZXC2kSj1mV1Ow6dicCOAU5nScjqNk3uAS91iblEjawPg/0" data-isV="1" uigs="article_account_8">嗨码歌</a><span class="s2"><script>document.write(timeConvert('1531966052'))</script></span>
<div class="moe-box">
<span style="display:none;" class="sc"><a data-except="1" class="sc-a" href="javascript:void(0)" uigs="share_8"></a></span><span style="display:none;" class="fx"><a data-except="1" class="fx-a" href="javascript:void(0)" uigs="like_8"></a></span>
</div>
</div>
</div>
</li>

		<!-- z -->
	
		<!-- a -->
		<li id="sogou_vr_11002601_box_9" d="ab735a258a90e8e1-6bee54fcbd896b2a-c0a7ed88fef92a5379228d29e02fb719">
<div class="img-box">
<a data-z="art" target="_blank" id="sogou_vr_11002601_img_9" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=Kdz8SwidKHuc-6lVebvzdLNCbpXn7UYMQ9OjxO2UK1FS8xXRENWysOIABVZS0visOlS-ewDCq-dVKl-jy3UPuU3rZelXcTSkP-ao3xWXUBwYbMcDzx5puaS30FRRfnN3&amp;new=1" uigs="article_image_9"><img src="//img01.sogoucdn.com/net/a/04/link?appid=100520033&amp;url=http://mmbiz.qpic.cn/mmbiz_jpg/Pn4Sm0RsAugKg2phQXGJlKaYMpgYoLHkpshMiaKlzTLSmKSNAgt27NYz45DdtQBer9G9Ex0uXDViawia5EU7gVcXQ/0?wx_fmt=jpeg" onload="resizeImage(this,140,105)" onerror="errorImage(this)"></a>
</div>
<div class="txt-box">
<h3>
<a target="_blank" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=Kdz8SwidKHuc-6lVebvzdLNCbpXn7UYMQ9OjxO2UK1FS8xXRENWysOIABVZS0visOlS-ewDCq-dVKl-jy3UPuU3rZelXcTSkP-ao3xWXUBwYbMcDzx5puaS30FRRfnN3&amp;new=1" id="sogou_vr_11002601_title_9" uigs="article_title_9" data-share="http://weixin.sogou.com/api/share?timestamp=1533207502&amp;signature=qIbwY*nI6KU9tBso4VCd8lYSesxOYgLcHX5tlbqlMR8N6flDHs4LLcFgRw7FjTAO7iy2zEfnrg2GpROYWYV1hReLi3x9jrpIhalUHlSsdL5XBYLbEfGKAeisytcU57*v36XSB9qh0kyMQ3rYN8DFawMCpxNOJzqt3eSTNU3uPJOq6cA*1zpiFTutw5Xm6bz6DMSdLRHwiNHmJTc41HKe0LN7WT11ITL8RLqw67nJ-g8="><em><!--red_beg-->Python<!--red_end--></em>自动生成表情包,<em><!--red_beg-->Python<!--red_end--></em>在手,从此斗图无敌手!</a>
</h3>
<p class="txt-info" id="sogou_vr_11002601_summary_9">作者 | <em><!--red_beg-->Python<!--red_end--></em>雁横如需转载,请联系原作者授权作为一个数据分析师,应该信奉一句话&mdash;&mdash;＂一图胜千言＂.不过这里要说的并不是数...</p>
<div class="s-p" t="1532070039">
<a class="account" target="_blank" id="sogou_vr_11002601_account_9" i="oIWsFt6HGMaRoWYyRbYCb5or9GTg" href="http://mp.weixin.qq.com/profile?src=3&amp;timestamp=1533207502&amp;ver=1&amp;signature=B8LotqP-Y1OqKIEnKb*NccVMGWVZQLBCuEvFgxrTLOJRvU37hny0HtKtI4RpMQYewhUl9wjXILeX*0SgSD22hw==" data-headimage="http://wx.qlogo.cn/mmhead/Q3auHgzwzM5cvOsZy9wYacdpSLicuibpMXzQHTKxLdh69fP0FFtliazuQ/0" data-isV="1" uigs="article_account_9">CSDN</a><span class="s2"><script>document.write(timeConvert('1532070039'))</script></span>
<div class="moe-box">
<span style="display:none;" class="sc"><a data-except="1" class="sc-a" href="javascript:void(0)" uigs="share_9"></a></span><span style="display:none;" class="fx"><a data-except="1" class="fx-a" href="javascript:void(0)" uigs="like_9"></a></span>
</div>
</div>
</div>
</li>

		<!-- z -->
	
</ul>
    

<div class="hintBox">
	<table id="hint_container" class="hint">
		<caption>相关搜索</caption>
		<tbody>
		
		<tr>
			
			<td><a href="/weixin?type=2&ie=utf8&query=python%E4%B8%8B%E8%BD%BD&s_from=bottom_hint" uigs="article_bottom_hint_0">python下载</a></td>
			
			<td><a href="/weixin?type=2&ie=utf8&query=php&s_from=bottom_hint" uigs="article_bottom_hint_1">php</a></td>
			
			<td><a href="/weixin?type=2&ie=utf8&query=python%E5%A4%9A%E7%BA%BF%E7%A8%8B&s_from=bottom_hint" uigs="article_bottom_hint_2">python多线程</a></td>
			
			<td><a href="/weixin?type=2&ie=utf8&query=python%E9%9D%A2%E8%AF%95%E9%A2%98&s_from=bottom_hint" uigs="article_bottom_hint_3">python面试题</a></td>
			
		</tr>
		
		<tr>
			
			<td><a href="/weixin?type=2&ie=utf8&query=python%E5%BB%96%E9%9B%AA%E5%B3%B0&s_from=bottom_hint" uigs="article_bottom_hint_4">python廖雪峰</a></td>
			
			<td><a href="/weixin?type=2&ie=utf8&query=python%E6%8B%9B%E8%81%98&s_from=bottom_hint" uigs="article_bottom_hint_5">python招聘</a></td>
			
			<td><a href="/weixin?type=2&ie=utf8&query=python%E7%88%AC%E8%99%AB&s_from=bottom_hint" uigs="article_bottom_hint_6">python爬虫</a></td>
			
			<td><a href="/weixin?type=2&ie=utf8&query=python123&s_from=bottom_hint" uigs="article_bottom_hint_7">python123</a></td>
			
		</tr>
		
		</tbody>
	</table>
</div>

<div class="p-fy" id="pagebar_container">
	<span>1</span><a id="sogou_page_2" href="?User-Agent=Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_13_5%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F61.0.3163.79+Safari%2F537.36&Upgrade-Insecure-Requests=1&query=python&Host=weixin.sogou.com&cookies=IPLOC%3DCN3100%3B+SUV%3D000D111E6FBB318359C8BE86BA771808%3B+SUID%3DE10888755218910A000000005B5FC0B8%3B+SNUID%3D33DB5BA7D2D6A1930107F3C5D30E662B%3B+ABTEST%3D0%7C1533001944%7Cv1%3B+weixinIndexVisited%3D1%3B+JSESSIONID%3DaaalDPdRsj9b2-zSmJHsw%3B+sct%3D2%3B+ppinf%3D5%7C1533110038%7C1534319638%7CdHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo0OlRhbmt8Y3J0OjEwOjE1MzMxMTAwMzh8cmVmbmljazo0OlRhbmt8dXNlcmlkOjQ0Om85dDJsdUdjVU52NU92cGRLbUxjM3dNbjcyUzBAd2VpeGluLnNvaHUuY29tfA%3B+pprdig%3DJzM58wY31Xko_FtUAZz3TZYsLjXqLlh0NhfcUTSrpOKSnsM_mDj8QvaQvnuu2WHs96s6iQUTiqsF5XQxdXof1os_EOMXGVKgkAG2gm_p9j8EkpZqILsJz2Y--hsG50UInyUFogKv2KaiAiWAwDP3C-dx7Tlbp40vFeuuL92hFew%3B+sgid%3D02-34274603-AVthZxaUsZp4ACtJ9b5kOia8%3B+ppmdig%3D1533110038000000f06734556f3a35c65309af2683c0784b&type=2&page=2&ie=utf8" uigs="page_2">2</a><a id="sogou_page_3" href="?User-Agent=Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_13_5%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F61.0.3163.79+Safari%2F537.36&Upgrade-Insecure-Requests=1&query=python&Host=weixin.sogou.com&cookies=IPLOC%3DCN3100%3B+SUV%3D000D111E6FBB318359C8BE86BA771808%3B+SUID%3DE10888755218910A000000005B5FC0B8%3B+SNUID%3D33DB5BA7D2D6A1930107F3C5D30E662B%3B+ABTEST%3D0%7C1533001944%7Cv1%3B+weixinIndexVisited%3D1%3B+JSESSIONID%3DaaalDPdRsj9b2-zSmJHsw%3B+sct%3D2%3B+ppinf%3D5%7C1533110038%7C1534319638%7CdHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo0OlRhbmt8Y3J0OjEwOjE1MzMxMTAwMzh8cmVmbmljazo0OlRhbmt8dXNlcmlkOjQ0Om85dDJsdUdjVU52NU92cGRLbUxjM3dNbjcyUzBAd2VpeGluLnNvaHUuY29tfA%3B+pprdig%3DJzM58wY31Xko_FtUAZz3TZYsLjXqLlh0NhfcUTSrpOKSnsM_mDj8QvaQvnuu2WHs96s6iQUTiqsF5XQxdXof1os_EOMXGVKgkAG2gm_p9j8EkpZqILsJz2Y--hsG50UInyUFogKv2KaiAiWAwDP3C-dx7Tlbp40vFeuuL92hFew%3B+sgid%3D02-34274603-AVthZxaUsZp4ACtJ9b5kOia8%3B+ppmdig%3D1533110038000000f06734556f3a35c65309af2683c0784b&type=2&page=3&ie=utf8" uigs="page_3">3</a><a id="sogou_page_4" href="?User-Agent=Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_13_5%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F61.0.3163.79+Safari%2F537.36&Upgrade-Insecure-Requests=1&query=python&Host=weixin.sogou.com&cookies=IPLOC%3DCN3100%3B+SUV%3D000D111E6FBB318359C8BE86BA771808%3B+SUID%3DE10888755218910A000000005B5FC0B8%3B+SNUID%3D33DB5BA7D2D6A1930107F3C5D30E662B%3B+ABTEST%3D0%7C1533001944%7Cv1%3B+weixinIndexVisited%3D1%3B+JSESSIONID%3DaaalDPdRsj9b2-zSmJHsw%3B+sct%3D2%3B+ppinf%3D5%7C1533110038%7C1534319638%7CdHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo0OlRhbmt8Y3J0OjEwOjE1MzMxMTAwMzh8cmVmbmljazo0OlRhbmt8dXNlcmlkOjQ0Om85dDJsdUdjVU52NU92cGRLbUxjM3dNbjcyUzBAd2VpeGluLnNvaHUuY29tfA%3B+pprdig%3DJzM58wY31Xko_FtUAZz3TZYsLjXqLlh0NhfcUTSrpOKSnsM_mDj8QvaQvnuu2WHs96s6iQUTiqsF5XQxdXof1os_EOMXGVKgkAG2gm_p9j8EkpZqILsJz2Y--hsG50UInyUFogKv2KaiAiWAwDP3C-dx7Tlbp40vFeuuL92hFew%3B+sgid%3D02-34274603-AVthZxaUsZp4ACtJ9b5kOia8%3B+ppmdig%3D1533110038000000f06734556f3a35c65309af2683c0784b&type=2&page=4&ie=utf8" uigs="page_4">4</a><a id="sogou_page_5" href="?User-Agent=Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_13_5%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F61.0.3163.79+Safari%2F537.36&Upgrade-Insecure-Requests=1&query=python&Host=weixin.sogou.com&cookies=IPLOC%3DCN3100%3B+SUV%3D000D111E6FBB318359C8BE86BA771808%3B+SUID%3DE10888755218910A000000005B5FC0B8%3B+SNUID%3D33DB5BA7D2D6A1930107F3C5D30E662B%3B+ABTEST%3D0%7C1533001944%7Cv1%3B+weixinIndexVisited%3D1%3B+JSESSIONID%3DaaalDPdRsj9b2-zSmJHsw%3B+sct%3D2%3B+ppinf%3D5%7C1533110038%7C1534319638%7CdHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo0OlRhbmt8Y3J0OjEwOjE1MzMxMTAwMzh8cmVmbmljazo0OlRhbmt8dXNlcmlkOjQ0Om85dDJsdUdjVU52NU92cGRLbUxjM3dNbjcyUzBAd2VpeGluLnNvaHUuY29tfA%3B+pprdig%3DJzM58wY31Xko_FtUAZz3TZYsLjXqLlh0NhfcUTSrpOKSnsM_mDj8QvaQvnuu2WHs96s6iQUTiqsF5XQxdXof1os_EOMXGVKgkAG2gm_p9j8EkpZqILsJz2Y--hsG50UInyUFogKv2KaiAiWAwDP3C-dx7Tlbp40vFeuuL92hFew%3B+sgid%3D02-34274603-AVthZxaUsZp4ACtJ9b5kOia8%3B+ppmdig%3D1533110038000000f06734556f3a35c65309af2683c0784b&type=2&page=5&ie=utf8" uigs="page_5">5</a><a id="sogou_page_6" href="?User-Agent=Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_13_5%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F61.0.3163.79+Safari%2F537.36&Upgrade-Insecure-Requests=1&query=python&Host=weixin.sogou.com&cookies=IPLOC%3DCN3100%3B+SUV%3D000D111E6FBB318359C8BE86BA771808%3B+SUID%3DE10888755218910A000000005B5FC0B8%3B+SNUID%3D33DB5BA7D2D6A1930107F3C5D30E662B%3B+ABTEST%3D0%7C1533001944%7Cv1%3B+weixinIndexVisited%3D1%3B+JSESSIONID%3DaaalDPdRsj9b2-zSmJHsw%3B+sct%3D2%3B+ppinf%3D5%7C1533110038%7C1534319638%7CdHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo0OlRhbmt8Y3J0OjEwOjE1MzMxMTAwMzh8cmVmbmljazo0OlRhbmt8dXNlcmlkOjQ0Om85dDJsdUdjVU52NU92cGRLbUxjM3dNbjcyUzBAd2VpeGluLnNvaHUuY29tfA%3B+pprdig%3DJzM58wY31Xko_FtUAZz3TZYsLjXqLlh0NhfcUTSrpOKSnsM_mDj8QvaQvnuu2WHs96s6iQUTiqsF5XQxdXof1os_EOMXGVKgkAG2gm_p9j8EkpZqILsJz2Y--hsG50UInyUFogKv2KaiAiWAwDP3C-dx7Tlbp40vFeuuL92hFew%3B+sgid%3D02-34274603-AVthZxaUsZp4ACtJ9b5kOia8%3B+ppmdig%3D1533110038000000f06734556f3a35c65309af2683c0784b&type=2&page=6&ie=utf8" uigs="page_6">6</a><a id="sogou_page_7" href="?User-Agent=Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_13_5%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F61.0.3163.79+Safari%2F537.36&Upgrade-Insecure-Requests=1&query=python&Host=weixin.sogou.com&cookies=IPLOC%3DCN3100%3B+SUV%3D000D111E6FBB318359C8BE86BA771808%3B+SUID%3DE10888755218910A000000005B5FC0B8%3B+SNUID%3D33DB5BA7D2D6A1930107F3C5D30E662B%3B+ABTEST%3D0%7C1533001944%7Cv1%3B+weixinIndexVisited%3D1%3B+JSESSIONID%3DaaalDPdRsj9b2-zSmJHsw%3B+sct%3D2%3B+ppinf%3D5%7C1533110038%7C1534319638%7CdHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo0OlRhbmt8Y3J0OjEwOjE1MzMxMTAwMzh8cmVmbmljazo0OlRhbmt8dXNlcmlkOjQ0Om85dDJsdUdjVU52NU92cGRLbUxjM3dNbjcyUzBAd2VpeGluLnNvaHUuY29tfA%3B+pprdig%3DJzM58wY31Xko_FtUAZz3TZYsLjXqLlh0NhfcUTSrpOKSnsM_mDj8QvaQvnuu2WHs96s6iQUTiqsF5XQxdXof1os_EOMXGVKgkAG2gm_p9j8EkpZqILsJz2Y--hsG50UInyUFogKv2KaiAiWAwDP3C-dx7Tlbp40vFeuuL92hFew%3B+sgid%3D02-34274603-AVthZxaUsZp4ACtJ9b5kOia8%3B+ppmdig%3D1533110038000000f06734556f3a35c65309af2683c0784b&type=2&page=7&ie=utf8" uigs="page_7">7</a><a id="sogou_page_8" href="?User-Agent=Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_13_5%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F61.0.3163.79+Safari%2F537.36&Upgrade-Insecure-Requests=1&query=python&Host=weixin.sogou.com&cookies=IPLOC%3DCN3100%3B+SUV%3D000D111E6FBB318359C8BE86BA771808%3B+SUID%3DE10888755218910A000000005B5FC0B8%3B+SNUID%3D33DB5BA7D2D6A1930107F3C5D30E662B%3B+ABTEST%3D0%7C1533001944%7Cv1%3B+weixinIndexVisited%3D1%3B+JSESSIONID%3DaaalDPdRsj9b2-zSmJHsw%3B+sct%3D2%3B+ppinf%3D5%7C1533110038%7C1534319638%7CdHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo0OlRhbmt8Y3J0OjEwOjE1MzMxMTAwMzh8cmVmbmljazo0OlRhbmt8dXNlcmlkOjQ0Om85dDJsdUdjVU52NU92cGRLbUxjM3dNbjcyUzBAd2VpeGluLnNvaHUuY29tfA%3B+pprdig%3DJzM58wY31Xko_FtUAZz3TZYsLjXqLlh0NhfcUTSrpOKSnsM_mDj8QvaQvnuu2WHs96s6iQUTiqsF5XQxdXof1os_EOMXGVKgkAG2gm_p9j8EkpZqILsJz2Y--hsG50UInyUFogKv2KaiAiWAwDP3C-dx7Tlbp40vFeuuL92hFew%3B+sgid%3D02-34274603-AVthZxaUsZp4ACtJ9b5kOia8%3B+ppmdig%3D1533110038000000f06734556f3a35c65309af2683c0784b&type=2&page=8&ie=utf8" uigs="page_8">8</a><a id="sogou_page_9" href="?User-Agent=Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_13_5%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F61.0.3163.79+Safari%2F537.36&Upgrade-Insecure-Requests=1&query=python&Host=weixin.sogou.com&cookies=IPLOC%3DCN3100%3B+SUV%3D000D111E6FBB318359C8BE86BA771808%3B+SUID%3DE10888755218910A000000005B5FC0B8%3B+SNUID%3D33DB5BA7D2D6A1930107F3C5D30E662B%3B+ABTEST%3D0%7C1533001944%7Cv1%3B+weixinIndexVisited%3D1%3B+JSESSIONID%3DaaalDPdRsj9b2-zSmJHsw%3B+sct%3D2%3B+ppinf%3D5%7C1533110038%7C1534319638%7CdHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo0OlRhbmt8Y3J0OjEwOjE1MzMxMTAwMzh8cmVmbmljazo0OlRhbmt8dXNlcmlkOjQ0Om85dDJsdUdjVU52NU92cGRLbUxjM3dNbjcyUzBAd2VpeGluLnNvaHUuY29tfA%3B+pprdig%3DJzM58wY31Xko_FtUAZz3TZYsLjXqLlh0NhfcUTSrpOKSnsM_mDj8QvaQvnuu2WHs96s6iQUTiqsF5XQxdXof1os_EOMXGVKgkAG2gm_p9j8EkpZqILsJz2Y--hsG50UInyUFogKv2KaiAiWAwDP3C-dx7Tlbp40vFeuuL92hFew%3B+sgid%3D02-34274603-AVthZxaUsZp4ACtJ9b5kOia8%3B+ppmdig%3D1533110038000000f06734556f3a35c65309af2683c0784b&type=2&page=9&ie=utf8" uigs="page_9">9</a><a id="sogou_page_10" href="?User-Agent=Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_13_5%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F61.0.3163.79+Safari%2F537.36&Upgrade-Insecure-Requests=1&query=python&Host=weixin.sogou.com&cookies=IPLOC%3DCN3100%3B+SUV%3D000D111E6FBB318359C8BE86BA771808%3B+SUID%3DE10888755218910A000000005B5FC0B8%3B+SNUID%3D33DB5BA7D2D6A1930107F3C5D30E662B%3B+ABTEST%3D0%7C1533001944%7Cv1%3B+weixinIndexVisited%3D1%3B+JSESSIONID%3DaaalDPdRsj9b2-zSmJHsw%3B+sct%3D2%3B+ppinf%3D5%7C1533110038%7C1534319638%7CdHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo0OlRhbmt8Y3J0OjEwOjE1MzMxMTAwMzh8cmVmbmljazo0OlRhbmt8dXNlcmlkOjQ0Om85dDJsdUdjVU52NU92cGRLbUxjM3dNbjcyUzBAd2VpeGluLnNvaHUuY29tfA%3B+pprdig%3DJzM58wY31Xko_FtUAZz3TZYsLjXqLlh0NhfcUTSrpOKSnsM_mDj8QvaQvnuu2WHs96s6iQUTiqsF5XQxdXof1os_EOMXGVKgkAG2gm_p9j8EkpZqILsJz2Y--hsG50UInyUFogKv2KaiAiWAwDP3C-dx7Tlbp40vFeuuL92hFew%3B+sgid%3D02-34274603-AVthZxaUsZp4ACtJ9b5kOia8%3B+ppmdig%3D1533110038000000f06734556f3a35c65309af2683c0784b&type=2&page=10&ie=utf8" uigs="page_10">10</a>
			<a id="sogou_next" href="?User-Agent=Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_13_5%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F61.0.3163.79+Safari%2F537.36&Upgrade-Insecure-Requests=1&query=python&Host=weixin.sogou.com&cookies=IPLOC%3DCN3100%3B+SUV%3D000D111E6FBB318359C8BE86BA771808%3B+SUID%3DE10888755218910A000000005B5FC0B8%3B+SNUID%3D33DB5BA7D2D6A1930107F3C5D30E662B%3B+ABTEST%3D0%7C1533001944%7Cv1%3B+weixinIndexVisited%3D1%3B+JSESSIONID%3DaaalDPdRsj9b2-zSmJHsw%3B+sct%3D2%3B+ppinf%3D5%7C1533110038%7C1534319638%7CdHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo0OlRhbmt8Y3J0OjEwOjE1MzMxMTAwMzh8cmVmbmljazo0OlRhbmt8dXNlcmlkOjQ0Om85dDJsdUdjVU52NU92cGRLbUxjM3dNbjcyUzBAd2VpeGluLnNvaHUuY29tfA%3B+pprdig%3DJzM58wY31Xko_FtUAZz3TZYsLjXqLlh0NhfcUTSrpOKSnsM_mDj8QvaQvnuu2WHs96s6iQUTiqsF5XQxdXof1os_EOMXGVKgkAG2gm_p9j8EkpZqILsJz2Y--hsG50UInyUFogKv2KaiAiWAwDP3C-dx7Tlbp40vFeuuL92hFew%3B+sgid%3D02-34274603-AVthZxaUsZp4ACtJ9b5kOia8%3B+ppmdig%3D1533110038000000f06734556f3a35c65309af2683c0784b&type=2&page=2&ie=utf8" class="np" uigs="page_next">下一页</a>
		
		<div class="mun">找到约9,537条结果<!--resultbarnum:9,537--></div>
</div>
    
</div>


        </div>
        
            <div class="snb-right" id="right">
                
    <div id="account" class="aside" style="display: none">
        <p class="tit-pub">相关公众号<a target="_blank" href="/weixin?type=1&ie=utf8&query=python" uigs="right0_more">更多</a></p>
        <div class="gzh-list" style="display: none"></div>
        
		<!-- a -->
		<div class="gzh-box">
<div class="img-box2">
<a target="_blank" uigs="right0_image_10" href="http://mp.weixin.qq.com/profile?src=3&amp;timestamp=1533207502&amp;ver=1&amp;signature=Eu9LOYSA47p6WE0mojhMtFR-gSr7zsQOYo6*w5VxrUjzLMKj9*O71kaJLlF*5XCPWqhAmAcVBGeF5swN3WO7GA=="><img height="58" width="58" src="http://img01.sogoucdn.com/app/a/100520090/oIWsFt7sphQ8ZOcauN9EXjjeCxi4" onerror="this.src=&quot;//weixin.sogou.com/wechat/images/account/def56-56.png&quot;;this.onerror=null;"></a>
</div>
<div class="txt-box2">
<p class="gzh-name">
<a target="_blank" uigs="right0_name_10" href="http://mp.weixin.qq.com/profile?src=3&amp;timestamp=1533207502&amp;ver=1&amp;signature=Eu9LOYSA47p6WE0mojhMtFR-gSr7zsQOYo6*w5VxrUjzLMKj9*O71kaJLlF*5XCPWqhAmAcVBGeF5swN3WO7GA=="><em><!--red_beg-->python<!--red_end--></em></a>
</p>
<p class="gzh-num">微信号：<label name="em_weixinhao">python6359</label>
</p>
</div>
<dl style="display: none">
<dt>功能介绍：</dt>
<dd>这里有完整的<em><!--red_beg-->python<!--red_end--></em>学习课程(学习方法、知识点、小案例、项目实战经验)关注我;开启<em><!--red_beg-->python<!--red_end--></em>学霸模式!</dd>
</dl>
</div>

		<!-- z -->
	
    </div>
    <script>
        if(uigs_para && 1){
            var right = "";
            for(var i = 0; i < 1; i++){
                right = right + "-right0_" + i;
            }
            uigs_para.right = right.substring(1);//右侧相关公众号展现的标记
        }
    </script>


<div id="hotword" class="aside" style="display: none">
    <p class="tit-pub">搜索热词<span class="hot">热度</span></p>
    <ol class="hot-news"></ol>
</div>
<script type="text/template" id="hotword_tpl">
    {@if hotwordList}
        {@each hotwordList as wordItem, index}
            {@if wordItem.word}
                <li>
                    <i class="{@if index == 0}hot-one{@else if index == 1}hot-two{@else if index == 2}hot-three{@/if}">${index|indexPlus}</i>
                    <a target="_blank" id="sogou_wx_hotword_${index}" href="${wordItem.word|buildQueryLink}" uigs="right1_${index|indexPlus}">${wordItem.word|unescapeWord}</a>
                    <span class="lan-line"><span style="width:${index|getRange,7}"></span></span>
                </li>
            {@/if}
        {@/each}
    {@/if}
</script>

<script src="/new/pc/js/right.min.js?v=20170315"></script>

            </div>
        
    </div>
    <div class="back-top" style="display: none;"><a href="javascript:void(0);" uigs="other_float_back_top"></a></div>
    
    <div class="bottom-form">
        

<form name="searchForm" action="/weixin">
    <div class="querybox">
        <div class="qborder">
            <div class="qborder2">
                <input type="hidden" name="type" value="2"/>
                <input type="hidden" name="s_from" value="input"/>
                <input type="text" class="query" name="query" id="query" ov="python" value="python" autocomplete="off"/>
                
                    <input type="hidden" name="ie" value="utf8"/>
                
                <a href="javascript:void(0)" class="qreset2" name="reset" uigs="search_reset"></a>
            </div>
        </div>
        <input type="button" value="搜文章" class="swz" onclick="search(this,2)" uigs="search_article"/>
        <input type="button" value="搜公众号" class="swz2" onclick="search(this,1)" uigs="search_account"/>
        <input type="hidden" name="_sug_" value="n"/>
        <input type="hidden" name="_sug_type_" value=""/>
    </div>
</form>
    </div>

<div class="footer-box" id="s_footer">
    <div class="footer">
        <a id="sogou_webhelp" href="http://help.sogou.com/" target="_blank" uigs="bottom_ssbz">搜索帮助</a>&nbsp;<a href="http://fankui.help.sogou.com/index.php/web/web/index/type/4" target="_blank" uigs="bottom_yjfk">意见反馈及投诉</a>&nbsp;<script src="/websearch/wexinurlenc_sogou_profile.jsp"></script>&copy;&nbsp;2018&nbsp;SOGOU.COM&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://www.sogou.com/docs/terms.htm" target="_blank" uigs="bottom_mzsm">免责声明</a>&nbsp;<a href="http://corp.sogou.com/private.html" target="_blank" uigs="bottom_yszc">隐私政策</a>
    </div>
</div>
    
        <script src="/new/pc/js/article.min.js?v=20161212"></script>
    
    <script>
        var WX_SUGG_PAGE_FROM="pcArtSearch";
        
        var SugPara = {
            "bigsize":true,
            "enableSug":true,
            "sugType":"wxart",
            "domain":"w.sugg.sogou.com",
            "productId":"web",
            "sugFormName":"sf",
            "submitId":"stb",
            "suggestRid":"01015002",
            "normalRid":"01019900",
            "oms":1,
            "nofixwidth":1,
            "useParent":1
        };
        uigs_para.exp_id = "null_0-null_1-null_2-null_3-null_4-null_5-null_6-null_7-null_8-null_9-";
        uigs_para.exp_id = uigs_para.exp_id.substring(0, uigs_para.exp_id.length - 1);
    </script>
    <script src="/new/weixin/js/uigs.min.js?v=20180607"></script>
    <script src="/new/pc/js/log.min.js?v=20170321"></script>
    <script src="/new/pc/js/event.min.js?v=20180607"></script>
    <script src="/new/pc/js/search.min.js?v=20161107"></script>
    <script src="/new/pc/js/suggestion.min.js?v=20180607"></script>
    <script src="/new/weixin/js/form.min.js?v=20170101"></script>
</body>
</html>
<!--1533207502201-->
<!--zly--><!--weixin-->


Process finished with exit code 0
'''
# soup = BeautifulSoup(html, 'lxml')
# print(soup.select())
url_pattern = re.compile('<a.*?href="(.*?)".*?data-share')
result = re.findall(url_pattern, html)
if result:
    print(len(result))
    for item in result:
        item = item.replace('amp;', '')
        print(item)


# <a target="_blank" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=Hwf7MUmnUTvDqdJBTw5OVUNQ5z5vlqFnI1anjbS9gQz1f4ykQ0KGHFBvsUDGixEU19bibyVDYwrNzTN8R0AI6BUVHKUymMd1vo9UCc-rs3Peh4qnBjy5jQhDGASBgPLI&amp;new=1" id="sogou_vr_11002601_title_0" uigs="article_title_0" data-share="http://weixin.sogou.com/api/share?timestamp=1533207502&amp;signature=qIbwY*nI6KU9tBso4VCd8lYSesxOYgLcHX5tlbqlMR8N6flDHs4LLcFgRw7FjTAORzX5jGtjOLt9MDriAC6SPfYvUjB7g6TV9aO9qSlkPjTBIxTArirVeh7wfHqqFWLGVN7N79E3Cj9k*-MXqu2CE5kC5wtNbJ9EFa85tVI5JsLNs-XK8nF3Od4f5-zmfLf*JizdL1ZVB5L9cRlUl50E2jpHyU7fDxi1*jZxZCi-jeo=">手把手教你利用【<em><!--red_beg-->Python<!--red_end--></em>】进行数据分析</a>
# <a target="_blank" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=sPx5cbdqM0qcQRoh2ZRz0aqYwcv8PRG-9g1OtQdcY6pcIZ0b5dM*pvQWEUqQHrvk8NXTElehy*WO1FzqNCl48OD2B*K3Q4cw1875D97WcoRlWjZqNlSnusBryQgssa6m&amp;new=1" id="sogou_vr_11002601_title_1" uigs="article_title_1" data-share="http://weixin.sogou.com/api/share?timestamp=1533207502&amp;signature=qIbwY*nI6KU9tBso4VCd8lYSesxOYgLcHX5tlbqlMR8N6flDHs4LLcFgRw7FjTAOAJ-1-S2BS6PwpCr5eN2x5uE1BnL8RIDZHeIlNLkzD1ZQVKvnmSMMx3ucUeS48x9xJzySPm-ejFfRwx4TxRZFXqpzQ65AvLXxNf5ahDythQKYBZQ2yAtqxcNyZ8YikMjHozbpSjnh2UPn4MkvQy5-u5QZr1I4sTGdKoEUBYB5XK4="><em><!--red_beg-->Python<!--red_end--></em>为什么是编程语言中最skr的?</a>

# <a target="_blank" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533207502&amp;ver=1036&amp;signature=Kdz8SwidKHuc-6lVebvzdLNCbpXn7UYMQ9OjxO2UK1FS8xXRENWysOIABVZS0visOlS-ewDCq-dVKl-jy3UPuU3rZelXcTSkP-ao3xWXUBwYbMcDzx5puaS30FRRfnN3&amp;new=1" id="sogou_vr_11002601_title_9" uigs="article_title_9" data-share="http://weixin.sogou.com/api/share?timestamp=1533207502&amp;signature=qIbwY*nI6KU9tBso4VCd8lYSesxOYgLcHX5tlbqlMR8N6flDHs4LLcFgRw7FjTAO7iy2zEfnrg2GpROYWYV1hReLi3x9jrpIhalUHlSsdL5XBYLbEfGKAeisytcU57*v36XSB9qh0kyMQ3rYN8DFawMCpxNOJzqt3eSTNU3uPJOq6cA*1zpiFTutw5Xm6bz6DMSdLRHwiNHmJTc41HKe0LN7WT11ITL8RLqw67nJ-g8="><em><!--red_beg-->Python<!--red_end--></em>自动生成表情包,<em><!--red_beg-->Python<!--red_end--></em>在手,从此斗图无敌手!</a>




# <a target="_blank" href="http://mp.weixin.qq.com/s?src=11&amp;timestamp=1533210790&amp;ver=1036&amp;signature=Kdz8SwidKHuc-6lVebvzdLNCbpXn7UYMQ9OjxO2UK1EDRBrT0QMIPW3KxADnJ0DY0UG2OAYGmZX6ygXYL2c-SC5gcPYbGBMEzVqFw27QcB6UeVoI-XTcjQblSKKpxvI7&amp;new=1" id="sogou_vr_11002601_title_0" uigs="article_title_0" data-share="http://weixin.sogou.com/api/share?timestamp=1533210790&amp;signature=qIbwY*nI6KU9tBso4VCd8lYSesxOYgLcHX5tlbqlMR8N6flDHs4LLcFgRw7FjTAO7iy2zEfnrg2GpROYWYV1hReLi3x9jrpIhalUHlSsdL5XBYLbEfGKAeisytcU57*v36XSB9qh0kyMQ3rYN8DFawMCpxNOJzqt3eSTNU3uPJOq6cA*1zpiFTutw5Xm6bz6SHZBZQxIDg-SRP6onoKpvQx5ZyJCJqrxVoQdsED90eQ="><em><!--red_beg-->Python<!--red_end--></em>自动生成表情包,<em><!--red_beg-->Python<!--red_end--></em>在手,从此斗图无敌手!</a>
