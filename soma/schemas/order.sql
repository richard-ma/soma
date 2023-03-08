-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2023-03-07 14:01:50
-- 服务器版本： 5.6.50-log
-- PHP 版本： 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `happyingift123`
--

-- --------------------------------------------------------

--
-- 表的结构 `fax_order`
--

CREATE TABLE `fax_order` (
  `id` int(10) NOT NULL COMMENT '系统单号',
  `url` varchar(255) NOT NULL COMMENT '来源网站',
  `purl` varchar(255) NOT NULL COMMENT '收款站',
  `orderid` varchar(255) DEFAULT '',
  `payway` enum('1','2','3','4','5','6','7') DEFAULT NULL,
  `total` decimal(10,2) NOT NULL COMMENT '总计(USD)',
  `createtime` int(10) NOT NULL COMMENT '添加时间',
  `status` int(11) NOT NULL DEFAULT '1' COMMENT '订单状态',
  `username` varchar(255) NOT NULL COMMENT '收货人',
  `email` varchar(255) NOT NULL COMMENT '邮箱',
  `telephone` varchar(255) NOT NULL COMMENT '电话',
  `address` varchar(255) NOT NULL COMMENT '收货地址',
  `ip` varchar(255) NOT NULL COMMENT 'IP地址',
  `useragent` varchar(255) NOT NULL COMMENT '浏览器UA',
  `goodsname` text NOT NULL COMMENT '商品名称',
  `comment` varchar(255) NOT NULL COMMENT '备注',
  `paytime` int(10) NOT NULL COMMENT '支付时间',
  `transno` varchar(255) NOT NULL COMMENT '支付交易号',
  `shippingname` varchar(255) DEFAULT NULL COMMENT '物流名称',
  `invoiceno` varchar(25) DEFAULT NULL COMMENT '运单号',
  `account` varchar(255) NOT NULL,
  `wtype` varchar(255) DEFAULT NULL,
  `ipcountry` varchar(255) DEFAULT NULL,
  `msg` text,
  `is_send` int(1) DEFAULT '0',
  `admin_id` int(10) DEFAULT '1',
  `paypalcid` text COMMENT 'paypal clientID',
  `paypalsid` text COMMENT 'paypal sid',
  `paymode` int(1) DEFAULT '0' COMMENT '0测试支付',
  `papalmode` varchar(1) DEFAULT NULL COMMENT 'papal支付模式inoice,paypame',
  `fapiaoid` varchar(255) DEFAULT NULL COMMENT 'paypal账单号',
  `cardNumberKeyValue` varchar(255) DEFAULT NULL,
  `expireMonth` varchar(255) DEFAULT NULL,
  `expireYear` varchar(255) DEFAULT NULL,
  `cvv` varchar(255) DEFAULT NULL,
  `currencyCode` varchar(255) DEFAULT NULL,
  `zipcode` varchar(255) DEFAULT '',
  `firstname` varchar(255) DEFAULT NULL,
  `order_name` text,
  `paypal_pass` varchar(255) DEFAULT '',
  `country` varchar(255) DEFAULT '',
  `city` varchar(255) DEFAULT '',
  `state` varchar(255) DEFAULT ''
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `fax_order`
--

INSERT INTO `fax_order` (`id`, `url`, `purl`, `orderid`, `payway`, `total`, `createtime`, `status`, `username`, `email`, `telephone`, `address`, `ip`, `useragent`, `goodsname`, `comment`, `paytime`, `transno`, `shippingname`, `invoiceno`, `account`, `wtype`, `ipcountry`, `msg`, `is_send`, `admin_id`, `paypalcid`, `paypalsid`, `paymode`, `papalmode`, `fapiaoid`, `cardNumberKeyValue`, `expireMonth`, `expireYear`, `cvv`, `currencyCode`, `zipcode`, `firstname`, `order_name`, `paypal_pass`, `country`, `city`, `state`) VALUES
(1080, 'http://www.21043wp.com', '', '228', '1', '100.00', 1652870734, 1, '22', '7777@qq.com', '32324234', '美国 加州 东城区 3333ewr were wr 1024街', '110.188.234.66', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36,zh,zh-CN;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6', '111 * 1 * 100.00(USD)', '', 0, '', NULL, NULL, 'sb-c0xs18819321@business.example.com', 'opencart', NULL, NULL, 0, 1, 'Ad3NFj4ZRZScJ3a36g5SctInk5AjJNHdjbrSkdbqFAL9WFXXuzdd-B2rVbbj7aMxtBHvZFKjzVPvxKJP', 'EP6znaezkn6Kbpv-CSaTkQWjWdSufMWePzGqsBIdTJlkVatlHC6zmWQbOZg9ktK7hPJNJeK_-Av3o280', 0, '2', 'INV2-RZ2K-E7V5-JM7F-LB4U', NULL, NULL, NULL, NULL, 'USD', '0000', '11', NULL, '', '', '', ''),
(1081, 'http://www.21043wp.com', '', '229', '1', '200.00', 1652871254, 1, '22', '7777@qq.com', '32324234', '美国 加州 东城区 3333ewr were wr 1024街', '110.188.234.66', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36,zh,zh-CN;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6', '111 * 2 * 100.00(USD)', '', 0, '', NULL, NULL, 'sb-c0xs18819321@business.example.com', 'opencart', NULL, NULL, 0, 1, 'Ad3NFj4ZRZScJ3a36g5SctInk5AjJNHdjbrSkdbqFAL9WFXXuzdd-B2rVbbj7aMxtBHvZFKjzVPvxKJP', 'EP6znaezkn6Kbpv-CSaTkQWjWdSufMWePzGqsBIdTJlkVatlHC6zmWQbOZg9ktK7hPJNJeK_-Av3o280', 0, '2', NULL, NULL, NULL, NULL, NULL, 'USD', '0000', '11', NULL, '', '', '', '');

--
-- 转储表的索引
--

--
-- 表的索引 `fax_order`
--
ALTER TABLE `fax_order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id` (`payway`),
  ADD KEY `ind2` (`status`,`account`),
  ADD KEY `id2` (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `fax_order`
--
ALTER TABLE `fax_order`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '系统单号', AUTO_INCREMENT=1161;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
