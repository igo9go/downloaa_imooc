<?php

/**
 * Created by PhpStorm.
 * User: zhouqiang
 * Date: 2017/2/7
 * Time: 下午2:10
 */
class HtmlDownloader
{
    public static function download($url = '')
    {
        $header = array(
            'http' =>array(
                'header' =>
                    "Host: www.imooc.com\r\n" .
                    "Referer: http://m.120ask.com/health/show?page=2&id=84882&type=17\r\n" .
                    "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36\r\n"
            ),
        );
        $context = stream_context_create($header);
        $data = file_get_contents($url, 0, $context);
        return $data;
    }

}