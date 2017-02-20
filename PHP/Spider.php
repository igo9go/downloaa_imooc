<?php

/**
 * Created by PhpStorm.
 * User: zhouqiang
 * Date: 2017/2/7
 * Time: 下午2:11
 */
require 'HtmlDownloader.php';
require 'HtmlParser.php';

class Spider
{
    const    COURSEURL = "http://www.imooc.com/learn/"; //课程链接
    //COURSEURL = "http:;//coding.imooc.com/learn/list/74.html"
    const    CHOOSE = ['H', 'M', 'L'];//视频品质
    const    STATE = 'H';//视频默认品质
    const    INFOR = ['L' => '普清', 'M' => '高清', 'H' => '超清'];//视频品质描述
    const    PERSUM = 0.0;//用于描述总进度
    const   PERLIST = [];//记录每个线程的进度

    private $htmlData;

    public function __construct($id)
    {
        $this->downloader = new HtmlDownloader();
        $this->parser = new HtmlParser();
        $this->id = $id;
    }

    public function run()
    {
        echo "#####################################################################\n";
        echo "#慕课网视频抓取器\n";
        echo "author:igo9go\n";
        echo "github:https://github.com/igo9go/\n";
        echo "#到慕课网官网打开想要下载的课程的章节列表页面，查看当前url链接\n";
        echo "#例如http://www.imooc.com/learn/615，则课程编号为615\n";
        echo "#####################################################################\n";
        $url = self::COURSEURL . $this->id;


        echo "将要下载的课程连接为" . $url . "\n";
        echo "开始解析视频,请稍后\n";
        $this->crawl($url);
        echo "共有" . count($this->htmlData['data']) . "条视频\n";
        echo "课程名称:" . $this->htmlData['subject'] . PHP_EOL;
        echo "开始下载,请等待";

        $fildir = './' . $this->htmlData['subject'];
        if (!is_dir($fildir)) {
            mkdir($fildir);
        }
        $i = 1;
        foreach ($this->htmlData['data'] as $item) {
            $file = file_get_contents($item['url']);
            $fileName = $item['title'] . '.mp4';
            file_put_contents($fildir . '/' . $fileName, $file);
            echo '第' . $i . '个视频已完成下载' . PHP_EOL;
            $i++;
        }
        return '下载完成';
    }

    public function crawl($url)
    {
        $htmlContent = $this->downloader->download($url);
        $this->htmlData = $this->parser->parse($htmlContent);
    }
}