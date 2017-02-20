<?php

/**
 * Created by PhpStorm.
 * User: zhouqiang
 * Date: 2017/2/7
 * Time: 下午2:10
 */
use Symfony\Component\DomCrawler\Crawler;


class HtmlParser
{
    const DOWNLOAD_URL = 'http://www.imooc.com/course/ajaxmediainfo/?mid={}&mode=flash';//下载链接

    public $res = [];

    public function parse($htmlContent = '')
    {
        if (!$htmlContent) return '';
        $crawler = new Crawler($htmlContent);

        $subject = $crawler->filter('#main > div.course-infos > div.w.pr > div.hd.clearfix > h2')->text();

        $course = $crawler->filterXPath('//*[@id="main"]/div[2]/div[1]/div[1]/div[3]/div/ul/li/a')->each(
            function (Crawler $node, $i) {
                $url = explode('/', $node->filter('a')->attr('href'));
                $id = $url[2];
                $downloadData = json_decode(file_get_contents(str_replace('{}', $id, self::DOWNLOAD_URL)), true);
                return [
                    'id' => $url['2'],
                    'title' => str_replace(['\r','\n','开始学习',' ',], ['','','',''], trim($node->text())),
                    //'title' => str_replace('开始学习', '', trim($node->text())),
                    'url' => $downloadData['data']['result']['mpath'][2]
                ];
            });
        $result = [
            'subject' => $subject,
            'data' => $course
        ];
        return $result;
    }
}
