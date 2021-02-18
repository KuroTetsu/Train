-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 16, 2021 at 03:41 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `note_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `listnote`
--

CREATE TABLE `listnote` (
  `id` int(11) NOT NULL,
  `is_archive` tinyint(1) NOT NULL DEFAULT 0,
  `notes` varchar(1000) NOT NULL,
  `is_deleted` tinyint(1) NOT NULL DEFAULT 0,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `listnote`
--

INSERT INTO `listnote` (`id`, `is_archive`, `notes`, `is_deleted`, `timestamp`) VALUES
(1, 0, 'testing pertama', 1, '2020-12-21 13:45:26'),
(2, 0, 'ini update note 2', 0, '2020-12-21 14:25:00'),
(3, 1, 'ini note ke 3', 0, '2020-12-21 14:25:34'),
(4, 0, 'ini note ke 4', 0, '2020-12-21 14:25:42'),
(5, 0, 'heeeelno', 0, '2021-01-12 23:53:46');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `listnote`
--
ALTER TABLE `listnote`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `listnote`
--
ALTER TABLE `listnote`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
