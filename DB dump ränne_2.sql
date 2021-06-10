-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 10, 2021 at 12:52 PM
-- Server version: 5.7.24
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ränne_2`
--

-- --------------------------------------------------------

--
-- Table structure for table `boat`
--

CREATE TABLE `boat` (
  `id` int(20) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `owner_id` int(20) DEFAULT NULL,
  `size` varchar(50) DEFAULT NULL,
  `dock` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `boat`
--

INSERT INTO `boat` (`id`, `name`, `owner_id`, `size`, `dock`) VALUES
(1, 'Tropical Breeze', 15, 'B', 1),
(2, 'Big Gust', 14, 'B', 1),
(3, 'Precious Storm', 13, 'B', 1),
(4, 'Little Victory', 12, 'B', 1),
(5, 'Hidden Wonder', 11, 'A', 1),
(6, 'Shallow Curse', 10, 'A', 1),
(7, 'Briny Home', 9, 'A', 1),
(8, 'Strange Clam', 8, 'C', 1),
(9, 'Merry Echo', 7, 'C', 2),
(10, 'Lady Cloud', 6, 'C', 2),
(11, 'Easy Creature', 5, 'C', 2),
(12, 'Salty Victory', 4, 'B', 2),
(13, 'Cheap Memory', 3, 'B', 3),
(14, 'Weird Wave', 2, 'B', 3),
(15, 'Moody Knot', 1, 'B', 3);

-- --------------------------------------------------------

--
-- Table structure for table `dock`
--

CREATE TABLE `dock` (
  `number` int(20) NOT NULL,
  `marina_id` int(20) DEFAULT NULL,
  `max_capacity` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `dock`
--

INSERT INTO `dock` (`number`, `marina_id`, `max_capacity`) VALUES
(1, 1, 10),
(2, 1, 20),
(3, 1, 30);

-- --------------------------------------------------------

--
-- Table structure for table `marina`
--

CREATE TABLE `marina` (
  `id` int(20) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `dock_count` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `marina`
--

INSERT INTO `marina` (`id`, `name`, `dock_count`) VALUES
(1, 'grand marina', 3);

-- --------------------------------------------------------

--
-- Table structure for table `person`
--

CREATE TABLE `person` (
  `id` int(20) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `boat_id` int(20) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `person`
--

INSERT INTO `person` (`id`, `name`, `boat_id`, `phone`, `email`) VALUES
(1, 'Maverick Morrow', 15, '202-555-0459', 'MaverickMorrow@mail.com'),
(2, 'Salahuddin Larsen', 14, '202-555-0100', 'SalahuddinLarsen@mail.com'),
(3, 'Aman Marks', 13, '202-555-0788', 'AmanMarks@mail.com'),
(4, 'Reyansh Ho', 12, '202-555-0269', 'ReyanshHo@mail.com'),
(5, 'Omari Randall', 11, '202-555-0653', 'OmariRandall@mail.com'),
(6, 'Holly Welsh', 10, '202-555-0109', 'HollyWelsh@mail.com'),
(7, 'Emre Sheehan', 9, '202-555-0199', 'EmreSheehan@mail.com'),
(8, 'Zain Marsden', 8, '202-555-0764', 'ZainMarsden@mail.com'),
(9, 'Dulcie Daniel', 7, '202-555-0060', 'DulcieDaniel@mail.com'),
(10, 'Wiktor Keeling', 6, '202-555-0900', 'WiktorKeeling@mail.com'),
(11, 'Gemma Carlson', 5, '202-555-0406', 'GemmaCarlson@mail.com'),
(12, 'Hannah Barlow', 4, '202-555-0255', 'HannahBarlow@mail.com'),
(13, 'Conan Reeves', 3, '202-555-0967', 'ConanReeves@mail.com'),
(14, 'Arwa Riley', 2, '202-555-0263', 'ArwaRiley@mail.com'),
(15, 'Herman Tillman', 1, '202-555-0351', 'HermanTillman@mail.com');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `id` int(20) NOT NULL,
  `marina_id` int(20) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`id`, `marina_id`, `name`, `phone`, `email`, `role`) VALUES
(1, 1, 'Kacie Beattie', '202-555-0851', 'KacieBeattie@mail.com', 'reception'),
(2, 1, 'Shayan Freeman', '202-555-0033', 'ShayanFreeman@mail.com', 'dock worker'),
(3, 1, 'Felicity Kidd', '202-555-0357', 'FelicityKidd@mail.com', 'dock worker'),
(4, 1, 'Christine Gill', '202-555-0850', 'christineGill@mail.com', 'dock worker'),
(5, 1, 'Derry York', '202-555-0521', 'DerryYork@mail.com', 'assistant'),
(6, 1, 'Carla Wiley', '202-555-0530', 'CarlaWiley@mail.com', 'assistant'),
(7, 1, 'Mikaela Franks', '202-555-0521', 'MikaelaFranks@mail.com', 'reception'),
(8, 1, 'Neil Costa', '202-555-0082', 'NeilCosta@mail.com', 'dock worker'),
(9, 1, 'Niko Browning', '202-555-0943', 'NikoBrowning@mail.com', 'reception'),
(10, 1, 'Maisey Farrell', '202-555-0166', 'MaiseyFarrell@mail.com', 'janitor');

-- --------------------------------------------------------

--
-- Stand-in structure for view `v_marina_used_capacity`
-- (See below for the actual view)
--
CREATE TABLE `v_marina_used_capacity` (
`name` varchar(50)
,`count(*)` bigint(21)
);

-- --------------------------------------------------------

--
-- Structure for view `v_marina_used_capacity`
--
DROP TABLE IF EXISTS `v_marina_used_capacity`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_marina_used_capacity`  AS  select `marina`.`name` AS `name`,count(0) AS `count(*)` from ((`marina` join `dock` on((`marina`.`id` = `dock`.`marina_id`))) join `boat` on((`dock`.`number` = `boat`.`dock`))) group by `marina`.`name` ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `boat`
--
ALTER TABLE `boat`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dock`
--
ALTER TABLE `dock`
  ADD PRIMARY KEY (`number`);

--
-- Indexes for table `marina`
--
ALTER TABLE `marina`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `person`
--
ALTER TABLE `person`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
