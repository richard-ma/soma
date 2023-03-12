-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2023-03-09 15:53:13
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
-- 表的结构 `fax_stripe`
--

CREATE TABLE `fax_stripe` (
  `id` int(10) NOT NULL COMMENT '编号',
  `url` varchar(255) NOT NULL COMMENT '收款站地址',
  `email` varchar(100) NOT NULL COMMENT 'stripe账户',
  `mode` enum('0','1') NOT NULL COMMENT '账户类型',
  `pays` enum('2','1','3') NOT NULL DEFAULT '2',
  `limitway` enum('3','4','2','1') NOT NULL DEFAULT '4' COMMENT '收款限定',
  `onemin` int(10) NOT NULL DEFAULT '0' COMMENT '单笔最小金额',
  `onemax` int(10) NOT NULL DEFAULT '0' COMMENT '单笔最大金额',
  `totalmoney` int(10) NOT NULL DEFAULT '2000' COMMENT '限定收款金额',
  `curmoney` float(10,2) NOT NULL DEFAULT '0.00' COMMENT '当前收款金额',
  `totalnum` int(10) NOT NULL DEFAULT '100' COMMENT '限定收款笔数',
  `curnum` int(10) NOT NULL DEFAULT '0' COMMENT '当前收款笔数',
  `status` int(1) NOT NULL DEFAULT '1' COMMENT '是否启用',
  `beizhu` text COMMENT '备注',
  `updatetime` int(10) DEFAULT NULL,
  `scid` varchar(255) NOT NULL,
  `lcid` varchar(255) NOT NULL,
  `ssid` varchar(255) NOT NULL,
  `lsid` varchar(255) NOT NULL,
  `type` enum('0','1') DEFAULT '0',
  `sid` int(10) DEFAULT NULL,
  `lasttime` int(10) DEFAULT '0',
  `admin_id` int(11) DEFAULT NULL,
  `purl` varchar(255) DEFAULT ''
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='stripe管理';

--
-- 转存表中的数据 `fax_stripe`
--

INSERT INTO `fax_stripe` (`id`, `url`, `email`, `mode`, `pays`, `limitway`, `onemin`, `onemax`, `totalmoney`, `curmoney`, `totalnum`, `curnum`, `status`, `beizhu`, `updatetime`, `scid`, `lcid`, `ssid`, `lsid`, `type`, `sid`, `lasttime`, `admin_id`, `purl`) VALUES
(7, '', 'liguomin999@outlook.com', '0', '1', '4', 10, 5000, 1998, 1580.15, 100, 20, 1, '', 1674560896, 'pk_test_51KF9O1Jpnil9nGGC195dlScuB0n0Dy69hJCOgYKh4dRUOevnJF5YeZO6TYF9sDDNyY34S04HC4dV1urna0QOKKUN00cmFIPGEY', '', 'sk_test_51KF9O1Jpnil9nGGCbVuivxcfz6r9X8Hgr9fRTFfVluNYrONCxxw8nxOhLfYdiULMIT7Nz6456n3yBsJUoLCN6BFF00bv7fIPC9', '', '1', 0, 1675426799, NULL, 'https://kergol.com'),
(8, '', 'kediakiaf48101@gmail.com', '0', '1', '4', 10, 5000, 2000, 900.15, 100, 14, 1, '', 1675157975, 'pk_test_51M2qGME2DyM8oPgkakG4iC4iOrTW2oFAgmcgSy2vPVa62QPJCp1nX9Kb7utJyXmtKhXvrFYWAmFENJUogF4vE6zO00x5PjjWeH', '', 'sk_test_51M2qGME2DyM8oPgk0ky3mEc9LU4NYIYSqcfBXJmJQBQCO0dzm5CJFLdoRqDMp9VCIKSYyEVgGYxBDRLF0HD4A8Ua00IWHHUXxz', '', '1', 0, 1675427088, NULL, 'https://zawery.com');

--
-- 转储表的索引
--

--
-- 表的索引 `fax_stripe`
--
ALTER TABLE `fax_stripe`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `fax_stripe`
--
ALTER TABLE `fax_stripe`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT COMMENT '编号', AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
