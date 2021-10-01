-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: projectpartb
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `assignments`
--

DROP TABLE IF EXISTS `assignments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `assignments` (
  `as_id` int NOT NULL AUTO_INCREMENT,
  `as_title` varchar(128) NOT NULL,
  `as_descritpion` varchar(256) NOT NULL,
  `as_submission` date NOT NULL,
  `acm` double NOT NULL,
  `aom` double NOT NULL,
  PRIMARY KEY (`as_id`),
  UNIQUE KEY `as_title` (`as_title`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assignments`
--

LOCK TABLES `assignments` WRITE;
/*!40000 ALTER TABLE `assignments` DISABLE KEYS */;
INSERT INTO `assignments` VALUES (1,'Python Basic','Python Project about basic stuff for python','2021-05-25',60,40),(2,'WebDev','Web development for all languages','2021-06-16',70,30),(3,'C# Pro','C# advanced','2021-11-26',66,34),(4,'Javascript adv','javascript advanced commands','2021-05-15',70,30),(5,'Database1','Database starting tips','2020-05-04',90,10);
/*!40000 ALTER TABLE `assignments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course_assignments`
--

DROP TABLE IF EXISTS `course_assignments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course_assignments` (
  `as_id` int NOT NULL,
  `c_id` int NOT NULL,
  PRIMARY KEY (`as_id`,`c_id`),
  KEY `c_id` (`c_id`),
  CONSTRAINT `course_assignments_ibfk_1` FOREIGN KEY (`as_id`) REFERENCES `assignments` (`as_id`),
  CONSTRAINT `course_assignments_ibfk_2` FOREIGN KEY (`c_id`) REFERENCES `courses` (`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course_assignments`
--

LOCK TABLES `course_assignments` WRITE;
/*!40000 ALTER TABLE `course_assignments` DISABLE KEYS */;
INSERT INTO `course_assignments` VALUES (1,1),(2,1),(5,1),(1,4),(2,4),(2,5),(4,6),(5,7),(2,8),(4,10),(2,11),(3,11),(5,11),(2,12),(4,12);
/*!40000 ALTER TABLE `course_assignments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses` (
  `c_id` int NOT NULL AUTO_INCREMENT,
  `language` varchar(12) NOT NULL,
  `course_type` varchar(12) NOT NULL,
  `title` varchar(12) NOT NULL,
  `description` varchar(256) NOT NULL,
  PRIMARY KEY (`c_id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES (1,'python','full time','pyFt012','pyFt012: Python full time'),(2,'javascript','part time','jsPt009','jsPt009: Javascript part time'),(3,'python','part time','pyPt020','pyPt020: Python part time'),(4,'python','full time','pyFt015','pyFt015: Python full time'),(5,'python','full time','pyFt095','pyFt095: Python full time'),(6,'javascript','part time','jsPt055','jsPt055: Javascript part time'),(7,'java','part time','jvPt081','jvPt081: Java part time'),(8,'java','full time','jvFt072','jvFt072: Java full time'),(9,'java','full time','jvFt028','jvFt028: Java full time'),(10,'javascript','full time','jsFt031','jsFt031: Javascript full time'),(11,'c#','part time','c#Pt051','c#Pt051: C# part time'),(12,'javascript','full time','jsFt099','jsFt099: Javascript full time');
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_courses`
--

DROP TABLE IF EXISTS `student_courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_courses` (
  `st_id` int NOT NULL,
  `c_id` int NOT NULL,
  PRIMARY KEY (`st_id`,`c_id`),
  KEY `c_id` (`c_id`),
  CONSTRAINT `student_courses_ibfk_1` FOREIGN KEY (`st_id`) REFERENCES `students` (`st_id`),
  CONSTRAINT `student_courses_ibfk_2` FOREIGN KEY (`c_id`) REFERENCES `courses` (`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_courses`
--

LOCK TABLES `student_courses` WRITE;
/*!40000 ALTER TABLE `student_courses` DISABLE KEYS */;
INSERT INTO `student_courses` VALUES (1,1),(4,1),(1,3),(3,5),(4,5),(4,6),(2,7),(5,7),(10,7),(5,8),(6,8),(6,9),(7,9),(9,9),(8,10),(2,11),(5,11),(4,12);
/*!40000 ALTER TABLE `student_courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `st_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(16) NOT NULL,
  `last_name` varchar(16) NOT NULL,
  `birthdate` date NOT NULL,
  `student_fees` int NOT NULL,
  PRIMARY KEY (`st_id`),
  UNIQUE KEY `UC_Student` (`first_name`,`last_name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'Doug','Dirk','1999-01-01',2053),(2,'Ulric','Kaety','1991-03-04',2034),(3,'Allyson','Xavior','1994-03-23',1350),(4,'Sloane','Dahlia','1988-03-06',3000),(5,'Jannah Ginnie','Blur','1999-02-03',3500),(6,'Abe','Kashton','1975-04-12',1850),(7,'Buffy','Clarity','1991-03-07',1560),(8,'Aster ','Masterman','1996-03-04',1440),(9,'Emmanuel','Elsa','1993-02-05',1234),(10,'Easter','Christabel','1979-08-07',1244);
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trainer_courses`
--

DROP TABLE IF EXISTS `trainer_courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trainer_courses` (
  `tr_id` int NOT NULL,
  `c_id` int NOT NULL,
  PRIMARY KEY (`tr_id`,`c_id`),
  KEY `c_id` (`c_id`),
  CONSTRAINT `trainer_courses_ibfk_1` FOREIGN KEY (`tr_id`) REFERENCES `trainers` (`tr_id`),
  CONSTRAINT `trainer_courses_ibfk_2` FOREIGN KEY (`c_id`) REFERENCES `courses` (`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trainer_courses`
--

LOCK TABLES `trainer_courses` WRITE;
/*!40000 ALTER TABLE `trainer_courses` DISABLE KEYS */;
INSERT INTO `trainer_courses` VALUES (1,1),(3,1),(6,1),(3,2),(5,2),(2,3),(3,3),(1,4),(2,4),(3,4),(3,5),(3,6),(5,6),(4,8),(4,9),(1,10),(3,10),(5,10),(2,11),(4,11),(1,12),(5,12);
/*!40000 ALTER TABLE `trainer_courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trainers`
--

DROP TABLE IF EXISTS `trainers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trainers` (
  `tr_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(16) NOT NULL,
  `last_name` varchar(16) NOT NULL,
  `trainer_subject` varchar(16) NOT NULL,
  PRIMARY KEY (`tr_id`),
  UNIQUE KEY `UC_Trainer` (`first_name`,`last_name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trainers`
--

LOCK TABLES `trainers` WRITE;
/*!40000 ALTER TABLE `trainers` DISABLE KEYS */;
INSERT INTO `trainers` VALUES (1,'Tammie ','Page','Web Development'),(2,'Jaydon','Salome','DataBases'),(3,'Isbel','Delia','Dev Ops'),(4,'Casey','Ryland','General Courses'),(5,'Tammy ','Dallas','Javascript Pro'),(6,'Gretta','Shania','Python basic');
/*!40000 ALTER TABLE `trainers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-12  1:26:43
