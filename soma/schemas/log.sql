-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2023-04-19 22:12:02
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
-- 表的结构 `fax_log`
--

CREATE TABLE `fax_log` (
  `id` int(10) NOT NULL,
  `errorno` varchar(100) NOT NULL COMMENT '错误码',
  `desc` varchar(255) NOT NULL COMMENT '详细描述',
  `createtime` int(11) NOT NULL COMMENT '创建时间',
  `status` varchar(1) NOT NULL DEFAULT '0',
  `admin_id` int(10) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='运行日志';

--
-- 转存表中的数据 `fax_log`
--

INSERT INTO `fax_log` (`id`, `errorno`, `desc`, `createtime`, `status`, `admin_id`) VALUES
(53, '10003', '购物网站https://yeezyshoeszone.com对应的收款组不存在,订单ID：22277', 1675176844, '0', NULL),
(52, '20002', '汇率设置里对应的币种GBP不存在，订单ID:22277', 1675176743, '0', NULL);

--
-- 转储表的索引
--

--
-- 表的索引 `fax_log`
--
ALTER TABLE `fax_log`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `fax_log`
--
ALTER TABLE `fax_log`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
