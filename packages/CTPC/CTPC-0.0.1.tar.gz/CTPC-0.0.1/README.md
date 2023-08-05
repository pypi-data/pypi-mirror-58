# ctpc

#### 介绍
致力于将汉语关键词转变成Python代码
基于中文的业务驱动的进行测试

#### 软件架构
基于Selenium库进行二次开发便以编写业务驱动

#### 安装教程

    pip install ctpc

 使用代码之前请确保您的电脑中已经安装好浏览器及对应的驱动内容
 <br>
    chrome
    [chromedriver](http://npm.taobao.org/mirrors/chromedriver/) √
    <br>
    ie
    [iedriverserver](http://selenium-release.storage.googleapis.com/index.html) ×<br>
    firefox
    [geckodriver](https://github.com/mozilla/geckodriver/releases/) ×

<b style="color:red">chrome与chromdriver驱动之间存在不兼容问题，所以最好都下载最新版本为最佳效果</b>

#### 使用说明

实例：

    from ctpc import run

    """
        run的参数注解
            case    :用例文件的内容[支持：txt/csv,json]
            limiter :用户文件数据的分隔符[支持：',', '\t']
    """

    # 如果您的脚本写在了TEXT文本中可以使用如下脚本
    with open('xiaobai.txt', 'r') as f:
        run(case=f.read(), limiter=',')

    # 如果您的脚本写在了CSV文本中可以使用如下脚本
    with open('xiaobai.txt', 'r') as f:
        run(case=f.read(), limiter=',')


Case文件实例

    打开,,https://www.baidu.com,
    输入,//*[@id="kw"],小白科技,
    点击,//*[@id="su"],,
    等待,,5,

    打开,,https://www.baidu.com,
    输入,//*[@id="kw"],小白科技,
    点击,//*[@id="su"],,
    等待,,5,

备注：<br>
空白行为区别不同Case的作用（同上实例为两条<b style="color:red">Case</b>）


#### 参与贡献
了解[项目源码](https://gitee.com/big_touch/ctpc)<br>

作者: <b title="微信号：KonaSoft">@Tser</b><br>
©<b title="公众号：big_touch">小白科技</b>
