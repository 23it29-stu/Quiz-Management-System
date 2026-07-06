-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: quiz_management
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questions` (
  `question_id` int NOT NULL AUTO_INCREMENT,
  `quiz_id` int DEFAULT NULL,
  `question` text,
  `option1` varchar(255) DEFAULT NULL,
  `option2` varchar(255) DEFAULT NULL,
  `option3` varchar(255) DEFAULT NULL,
  `option4` varchar(255) DEFAULT NULL,
  `correct_answer` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`question_id`),
  KEY `quiz_id` (`quiz_id`),
  CONSTRAINT `questions_ibfk_1` FOREIGN KEY (`quiz_id`) REFERENCES `quiz` (`quiz_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (1,1,'what is python?','programming language','web browser','operating system','Database','Option A'),(2,1,'Which symbol is used for comments in Python?','//','#','<!-- -->','**','Option B'),(3,1,'Which keyword is used to define a function in Python?','function','define','def','func','Option C'),(4,1,'Which data type stores True or False values?','String','Integer','Boolean','Float','Option C'),(5,1,'Which loop is used to iterate a fixed number of times?','while','for','repeat','loop','Option B'),(6,2,'What is the capital city of India?','Mumbai','New Delhi','Chennai','kolkata','Option B'),(7,2,'Which planet is known as the Red Planet?','Venus','Earth','Mars','Jupiter','Option C'),(8,2,'Who is known as the Father of the Nation in India?','Jawaharlal Nehru','Mahatma Gandhi','Subhash Chandra Bose','Bhagat Singh','Option B'),(9,2,'Which is the smallest prime number?','0','1','2','3','Option C'),(10,2,'Which element has the highest melting point?','copper','mercury','tungsten','osmium','Option C'),(11,2,'Which country is known as the \"Land of the Rising Sun\"?','Japan','Thailand','South korea','China','Option A');
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quiz`
--

DROP TABLE IF EXISTS `quiz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `quiz` (
  `quiz_id` int NOT NULL AUTO_INCREMENT,
  `quiz_name` varchar(100) NOT NULL,
  `category` varchar(50) DEFAULT NULL,
  `created_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `description` text,
  `difficulty` varchar(20) DEFAULT NULL,
  `time_limit` int DEFAULT NULL,
  `passing_percentage` int DEFAULT NULL,
  `total_questions` int DEFAULT NULL,
  PRIMARY KEY (`quiz_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quiz`
--

LOCK TABLES `quiz` WRITE;
/*!40000 ALTER TABLE `quiz` DISABLE KEYS */;
INSERT INTO `quiz` VALUES (1,'python basics','programming','2026-07-01 10:19:20',NULL,NULL,NULL,40,NULL),(2,'General Knowledge Challenge','General Knowledge','2026-07-06 14:17:04','Test your general knowledge with 10 interesting questions.','Medium',5,60,6);
/*!40000 ALTER TABLE `quiz` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `results`
--

DROP TABLE IF EXISTS `results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `results` (
  `result_id` int NOT NULL AUTO_INCREMENT,
  `student_name` varchar(100) DEFAULT NULL,
  `quiz_id` int DEFAULT NULL,
  `score` int DEFAULT NULL,
  `percentage` float DEFAULT NULL,
  `attempt_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `status` varchar(10) DEFAULT NULL,
  `time_taken` varchar(20) DEFAULT NULL,
  `attempt_datetime` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`result_id`),
  KEY `quiz_id` (`quiz_id`),
  CONSTRAINT `results_ibfk_1` FOREIGN KEY (`quiz_id`) REFERENCES `quiz` (`quiz_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `results`
--

LOCK TABLES `results` WRITE;
/*!40000 ALTER TABLE `results` DISABLE KEYS */;
INSERT INTO `results` VALUES (1,'Jiya Kishnani',1,5,100,'2026-07-01 10:27:49',NULL,NULL,'2026-07-01 18:53:50'),(2,'rahul',1,3,60,'2026-07-01 10:37:13',NULL,NULL,'2026-07-01 18:53:50'),(3,'MANYA',1,4,80,'2026-07-01 13:55:23','PASS','0 min','2026-07-01 19:25:23'),(4,'naman',1,3,60,'2026-07-03 11:27:33','PASS','0 min 26 sec','2026-07-03 16:57:33'),(5,'sunil K',1,5,100,'2026-07-05 13:53:28','PASS','0 min 32 sec','2026-07-05 19:23:28'),(6,'vishakha',1,0,0,'2026-07-05 14:20:04','FAIL','0 min 19 sec','2026-07-05 19:50:04'),(7,'dax',1,0,0,'2026-07-05 14:37:51','FAIL','0 min 19 sec','2026-07-05 20:07:51'),(8,'jagdish',1,0,0,'2026-07-06 08:53:28','FAIL','0 min 31 sec','2026-07-06 14:23:28'),(9,'jagdish',1,0,0,'2026-07-06 08:57:14','FAIL','4 min 17 sec','2026-07-06 14:27:14'),(10,'devanshi',1,3,60,'2026-07-06 08:58:30','PASS','0 min 22 sec','2026-07-06 14:28:30'),(11,'chahana',1,3,60,'2026-07-06 11:58:12','PASS','0 min 39 sec','2026-07-06 17:28:12'),(12,'asha',2,3,50,'2026-07-06 14:18:45','FAIL','0 min 42 sec','2026-07-06 19:48:45'),(13,'asha',2,0,0,'2026-07-06 14:18:55','FAIL','0 min 52 sec','2026-07-06 19:48:55');
/*!40000 ALTER TABLE `results` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-07-06 20:28:05
