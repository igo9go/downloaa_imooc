<?php

require_once __DIR__ . '/vendor/autoload.php';
require 'Spider.php';

if (!isset($argv[1])) {
    echo '请输入需要下载的课程ID'.PHP_EOL;
    echo '如果下载的课程链接为http://www.imooc.com/learn/744'.PHP_EOL;
    echo '执行 php index.php 744';
    exit;
}
$id = $argv[1];

$spider = new Spider($id);

$spider->run();