-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2023-03-22 10:57:44
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
-- 表的结构 `fax_currency`
--

CREATE TABLE `fax_currency` (
  `id` int(10) UNSIGNED NOT NULL,
  `code` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT '币种代码',
  `name` varchar(100) NOT NULL COMMENT '名称',
  `value` float(10,2) NOT NULL DEFAULT '0.00' COMMENT '汇率',
  `admin_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='汇率设置';

--
-- 转存表中的数据 `fax_currency`
--

INSERT INTO `fax_currency` (`id`, `code`, `name`, `value`, `admin_id`) VALUES
(10, 'USD', '美元', 1.00, NULL),
(11, 'GBP', '英镑', 0.89, NULL);

--
-- 转储表的索引
--

--
-- 表的索引 `fax_currency`
--
ALTER TABLE `fax_currency`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `fax_currency`
--
ALTER TABLE `fax_currency`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
