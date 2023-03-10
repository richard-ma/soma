-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2023-03-09 15:52:59
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
-- 表的结构 `fax_shopsite`
--

CREATE TABLE `fax_shopsite` (
  `id` int(10) NOT NULL COMMENT '编号',
  `url` varchar(255) NOT NULL COMMENT '网址',
  `sitegroup` int(1) NOT NULL COMMENT '收款组',
  `paypaltype` enum('2','3','1') NOT NULL COMMENT 'Paypal账单名称',
  `status` int(1) NOT NULL DEFAULT '1' COMMENT '是否启用',
  `paypalname` varchar(255) DEFAULT NULL COMMENT 'Paypal产品名称',
  `beizhu` text COMMENT '备注',
  `updatetime` int(10) NOT NULL COMMENT '更新时间',
  `type` int(1) DEFAULT NULL COMMENT '网站类型',
  `risk` int(10) DEFAULT NULL,
  `admin_id` int(11) DEFAULT NULL,
  `paypalname_me` varchar(255) DEFAULT NULL,
  `donatename` varchar(255) DEFAULT ''
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='商户站';

--
-- 转存表中的数据 `fax_shopsite`
--

INSERT INTO `fax_shopsite` (`id`, `url`, `sitegroup`, `paypaltype`, `status`, `paypalname`, `beizhu`, `updatetime`, `type`, `risk`, `admin_id`, `paypalname_me`, `donatename`) VALUES
(21, 'https://shinegiftshop.com', 15, '1', 1, 'Order Item', '', 1675177156, 2, 0, NULL, 'Please click the change button above and choose the payment mode of family and friends transfer, otherwise the order will be refunded and will not be shipped!', 'this is donation example name.'),
(19, 'https://salesportshirts.com', 15, '1', 1, 'Order Item', '', 1675158558, 2, 0, NULL, 'Please click the change button above and choose the payment mode of family and friends transfer, otherwise the order will be refunded and will not be shipped!', 'this is donation example name.'),
(20, 'https://yeezyshoeszone.com', 15, '1', 1, 'Order Item', '', 1675176888, 2, 0, NULL, 'Please click the change button above and choose the payment mode of family and friends transfer, otherwise the order will be refunded and will not be shipped!', 'this is donation example name.'),
(22, 'https://merchale.shop', 13, '1', 1, 'Order Item', '', 1674829063, 2, 0, NULL, 'Please click the change button above and choose the payment mode of family and friends transfer, otherwise the order will be refunded and will not be shipped!', 'this is donation example name.');

--
-- 转储表的索引
--

--
-- 表的索引 `fax_shopsite`
--
ALTER TABLE `fax_shopsite`
  ADD PRIMARY KEY (`id`),
  ADD KEY `url` (`url`,`status`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `fax_shopsite`
--
ALTER TABLE `fax_shopsite`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '编号', AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
