-- MySQL dump 10.16  Distrib 10.1.10-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: mycuteoffice
-- ------------------------------------------------------
-- Server version	10.1.10-MariaDB-1~trusty-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `space_bazzinga`
--

DROP TABLE IF EXISTS `space_bazzinga`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `space_bazzinga` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Primary key of bazzinga entity',
  `type` varchar(255) NOT NULL COMMENT 'type name',
  `category` varchar(255) NOT NULL COMMENT 'category name',
  `author` varchar(255) DEFAULT NULL COMMENT 'author',
  `subject` varchar(255) DEFAULT NULL COMMENT 'subject',
  `template` varchar(255) DEFAULT NULL,
  `created` int(11) NOT NULL DEFAULT '0' COMMENT 'The Unix timestamp.',
  `changed` int(11) NOT NULL DEFAULT '0' COMMENT 'The Unix timestamp.',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=141 DEFAULT CHARSET=utf8 COMMENT='The base table for the bazzinga entity';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `space_bazzinga`
--

LOCK TABLES `space_bazzinga` WRITE;
/*!40000 ALTER TABLE `space_bazzinga` DISABLE KEYS */;
INSERT INTO `space_bazzinga` VALUES (2,'email','space','provider','space status complete ','complete',1447063796,1449137712),(3,'email','space','provider','Congratulations! Your space is now live on MyCuteOffice.com','publish',1447063908,1449137156),(4,'email','book','provider',' Booking Notification:  @name has booked your space.','new',1447063971,1449493285),(5,'email','space','provider','status of your space has been changed ','change',1447065543,1449137430),(6,'email','enq','provider','@name is interested in your space','space',1447066145,1449123312),(7,'email','enq','admin','New Enquiry created for Enquiry ID : @enq_id','created',1447066488,1449142867),(8,'email','book','admin','Booking ID: @booking_id has been Accepted','accept',1447066844,1449663674),(11,'email','enq','admin','Enquiry status for Enquiry ID: @enq_id  - Accepted ','accept',1447670051,1449062411),(12,'email','enq','admin','Enquiry status for Enquiry ID: @enq_id - Rejected','reject',1447672580,1449062384),(13,'email','enq','seeker','Your enquiry on My Cute Office','created',1447677599,1449142846),(14,'email','req','seeker','Your requirement on My Cute Office','new',1447742137,1449138806),(15,'email','req','admin','new requirement generated','new',1447746196,1449054138),(16,'email','book','provider','Confirmation of the cancellation of Booking ID: @booking_id for your space ID: @space_id','cancel_approve',1447756464,1449125724),(17,'email','book','admin','Booking confirmation for booking ID: @booking_id overdue','noreply',1447760798,1449127307),(20,'email','req','admin','requirement_reply by admin','reply',1447829910,1449140962),(21,'email','enq','admin','Reply to enquiry for Enquiry ID : @enq_id','reply',1447830735,1449140902),(22,'email','enq','provider','enquiry_reply to provider','reply',1447833396,1449219726),(23,'email','enq','seeker',' A new reply has been posted for your Enquiry ID: @enq_id','reply',1447833427,1449219746),(24,'email','book','seeker','Having issues with booking? Let us help you','incomp_rem',1447842219,1449127482),(25,'email','enq','admin',' Enquiry ID: @enq_id has exceeded 48 hours without a reply','noreply',1447842489,1449123022),(26,'email','book','seeker','Your request to cancel booking ID: @booking_id','cancel',1447843237,1449129351),(27,'email','space','admin','Space ID: @space_id awaiting Approval','await_approval',1448006226,1449136579),(29,'email','book','provider',' [name] Booking ID: @booking_id has requested to cancel the booking ','cancel_disapp',1449126062,1449126062),(30,'email','book','seeker','Booking reminder Booking ID: @booking_id','reminder',1449127590,1449127590),(31,'email','book','admin','Request to cancel the booking ID: @booking_id','cancel',1449129289,1449129289),(32,'email','book','seeker','Cancellation for the Booking ID: @booking_id is Approved','cancel_approve',1449130338,1449130338),(33,'email','book','seeker','Cancellation for the Booking ID: @booking_id is Disapproved','cancel_disapp',1449130394,1449130394),(34,'email','space','admin','added new city','cityadd',1449136690,1449136690),(35,'email','space','admin','Space ID: @space_id has been revoked','revoke',1449138240,1449138240),(36,'email','space','provider','space  completion reminder','completion_reminder',1449138360,1449138384),(37,'email','book','admin',' Booking ID: @booking_id has been created','new',1449232972,1449232972),(38,'email','general','common','change password','change_pwd',1449233841,1449233841),(39,'sms','enq','provider','added a space','space',1449301750,1449301750),(40,'sms','enq','seeker','enquiry created','created',1449302242,1449302242),(43,'sms','book','seeker','reject booking','reject',1449472926,1449473123),(44,'sms','book','seeker','accept booking seeker','accept',1449472976,1449472976),(45,'email','book','seeker','Status of Booking ID: @booking_id is Accepted ','accept',1449473225,1449473225),(46,'email','book','seeker','Status of Booking ID: @booking_id is Rejected','reject',1449473272,1449660704),(47,'sms','enq','provider','provider replly','reply',1449474559,1449474559),(48,'sms','enq','seeker','reply by seeker','reply',1449475617,1449475628),(51,'sms','book','seeker','cancel approved','cancel_approve',1449475973,1449475973),(53,'sms','book','seeker','cancel seeker','cancel_disapp',1449481976,1449481976),(62,'sms','book','provider','new booking by provider','new',1449495069,1449495069),(64,'email','book','seeker','Booking Receipt for Booking ID: @booking_id','receipt',1449495951,1449559287),(65,'sms','book','seeker','seeker receipt','receipt',1449495990,1449559304),(67,'email','book','provider','You have Confirmed the booking request ID: @booking_id ','accept',1449566082,1449566082),(68,'sms','book','provider','provider accept','accept',1449566129,1449566129),(69,'email','book','provider','You have Cancelled the booking request ID: @booking_id ','reject',1449566168,1449660969),(70,'sms','book','provider','reject booking','reject',1449566194,1449566194),(73,'sms','book','provider','cancel booking','cancel_approve',1449567839,1449567839),(74,'sms','book','provider','cancel booking','cancel_disapp',1449567877,1449567877),(76,'email','book','admin','Booking ID: @booking_id has been Rejected','reject',0,1449660939),(78,'email','enq','provider','Enquiry status for Enquiry ID: @enq_id - Accepted','accept',0,0),(88,'email','enq','provider','Enquiry status for Enquiry ID: @enq_id - Rejected','reject',0,0),(90,'sms','book','seeker','incomp_reminder','incomp_rem',0,0),(91,'sms','book','seeker','reminder','reminder',0,0),(93,'email','enq','seeker','Your Enquiry is accepted','accept',0,0),(94,'email','enq','seeker','your enquiry is rejected',NULL,0,0),(97,'email','enq','seeker','Your Enquiry is rejected','reject',0,0),(98,'sms','enq','seeker','Your Enquiry is acceptes','accept',0,0),(99,'sms','enq','seeker','Your Enquiry is Rejected','reject',0,0),(103,'sms','req','seeker','new req','new',0,0),(104,'email','general','common','New account on MCO','signup',1449822059,1449822059),(107,'email','general','common','forget password','forgot_pwd',0,0),(120,'push','book','seeker','accept booking seeker','accept',0,0),(121,'push','book','seeker','reject booking seeker','reject',0,0),(122,'push','book','seeker','cancel approved','cancel_approve',0,0),(123,'push','book','seeker','cancel disapproved','cancel_disapp',0,0),(124,'push','book','seeker','seeker receipt','receipt',0,0),(125,'push','book','seeker','incomplete_reminder','incomp_rem',0,0),(126,'push','book','seeker','reminder','reminder',0,0),(127,'push','book','provider','new bookinng by providder','new',0,0),(128,'push','book','provider','accept provider','accept',0,0),(129,'push','book','provider','reject booking','reject',0,0),(130,'push','book','provider','cancel booking','cancel_approve',0,0),(131,'push','book','provider','cancel disapp','cancel_disapp',0,0),(133,'push','enq','seeker','enquiry created','created',0,0),(134,'push','enq','seeker','reply to seeker','reply',0,0),(135,'push','enq','seeker','enquiry is accepted','accept',0,0),(136,'push','enq','seeker','enquiry is rejected','reject',0,0),(137,'push','enq','provider','added a space','space',0,0),(138,'push','enq','provider','provider reply','reply',0,0),(140,'push','req','seeker','new req','new',0,0);
/*!40000 ALTER TABLE `space_bazzinga` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-01-06 13:52:52
