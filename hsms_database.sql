CREATE DATABASE  IF NOT EXISTS `hsms` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `hsms`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: hsms
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `attribute`
--

DROP TABLE IF EXISTS `attribute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attribute` (
  `attribute_id` bigint NOT NULL AUTO_INCREMENT,
  `attribute_name` varchar(60) NOT NULL,
  PRIMARY KEY (`attribute_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attribute`
--

LOCK TABLES `attribute` WRITE;
/*!40000 ALTER TABLE `attribute` DISABLE KEYS */;
INSERT INTO `attribute` VALUES (1,'Color'),(2,'Quantity'),(3,'Thickness'),(4,'Size'),(5,'Length'),(6,'Type'),(7,'Weight');
/*!40000 ALTER TABLE `attribute` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'Owner'),(2,'Salesman');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=132 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,1,9),(10,1,10),(11,1,11),(12,1,12),(13,1,13),(14,1,14),(15,1,15),(16,1,16),(17,1,17),(18,1,18),(19,1,19),(20,1,20),(21,1,21),(22,1,22),(23,1,23),(24,1,24),(25,1,25),(26,1,26),(27,1,27),(28,1,28),(29,1,29),(30,1,30),(31,1,31),(32,1,32),(33,1,33),(34,1,34),(35,1,35),(36,1,36),(37,1,37),(38,1,38),(39,1,39),(40,1,40),(41,1,41),(42,1,42),(43,1,43),(44,1,44),(45,1,45),(46,1,46),(47,1,47),(48,1,48),(49,1,49),(50,1,50),(51,1,51),(52,1,52),(53,1,53),(54,1,54),(55,1,55),(56,1,56),(57,1,57),(58,1,58),(59,1,59),(60,1,60),(61,1,61),(62,1,62),(63,1,63),(64,1,64),(65,1,65),(66,1,66),(67,1,67),(68,1,68),(69,1,69),(70,1,70),(71,1,71),(72,1,72),(73,1,73),(74,1,74),(75,1,75),(76,1,76),(77,1,77),(78,1,78),(79,1,79),(80,1,80),(81,1,81),(82,1,82),(83,1,83),(84,1,84),(85,1,85),(86,1,86),(87,1,87),(88,1,88),(89,1,89),(90,1,90),(91,1,91),(92,1,92),(93,1,93),(94,1,94),(95,1,95),(96,1,96),(97,1,97),(98,1,98),(99,1,99),(100,1,100),(101,2,21),(102,2,22),(103,2,23),(104,2,24),(105,2,28),(106,2,32),(107,2,36),(108,2,40),(109,2,44),(110,2,48),(111,2,52),(112,2,56),(113,2,60),(114,2,64),(115,2,68),(116,2,85),(117,2,86),(118,2,87),(119,2,88),(120,2,89),(121,2,90),(122,2,91),(123,2,92),(124,2,93),(125,2,94),(126,2,95),(127,2,96),(128,2,97),(129,2,98),(130,2,99),(131,2,100);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add category',7,'add_category'),(26,'Can change category',7,'change_category'),(27,'Can delete category',7,'delete_category'),(28,'Can view category',7,'view_category'),(29,'Can add brand',8,'add_brand'),(30,'Can change brand',8,'change_brand'),(31,'Can delete brand',8,'delete_brand'),(32,'Can view brand',8,'view_brand'),(33,'Can add attribute',9,'add_attribute'),(34,'Can change attribute',9,'change_attribute'),(35,'Can delete attribute',9,'delete_attribute'),(36,'Can view attribute',9,'view_attribute'),(37,'Can add product',10,'add_product'),(38,'Can change product',10,'change_product'),(39,'Can delete product',10,'delete_product'),(40,'Can view product',10,'view_product'),(41,'Can add product attribute',11,'add_productattribute'),(42,'Can change product attribute',11,'change_productattribute'),(43,'Can delete product attribute',11,'delete_productattribute'),(44,'Can view product attribute',11,'view_productattribute'),(45,'Can add product variant',12,'add_productvariant'),(46,'Can change product variant',12,'change_productvariant'),(47,'Can delete product variant',12,'delete_productvariant'),(48,'Can view product variant',12,'view_productvariant'),(49,'Can add variant attribute value',13,'add_variantattributevalue'),(50,'Can change variant attribute value',13,'change_variantattributevalue'),(51,'Can delete variant attribute value',13,'delete_variantattributevalue'),(52,'Can view variant attribute value',13,'view_variantattributevalue'),(53,'Can add product detail',14,'add_productdetail'),(54,'Can change product detail',14,'change_productdetail'),(55,'Can delete product detail',14,'delete_productdetail'),(56,'Can view product detail',14,'view_productdetail'),(57,'Can add product price',15,'add_productprice'),(58,'Can change product price',15,'change_productprice'),(59,'Can delete product price',15,'delete_productprice'),(60,'Can view product price',15,'view_productprice'),(61,'Can add warehouse',16,'add_warehouse'),(62,'Can change warehouse',16,'change_warehouse'),(63,'Can delete warehouse',16,'delete_warehouse'),(64,'Can view warehouse',16,'view_warehouse'),(65,'Can add stock detail',17,'add_stockdetail'),(66,'Can change stock detail',17,'change_stockdetail'),(67,'Can delete stock detail',17,'delete_stockdetail'),(68,'Can view stock detail',17,'view_stockdetail'),(69,'Can add supplier',18,'add_supplier'),(70,'Can change supplier',18,'change_supplier'),(71,'Can delete supplier',18,'delete_supplier'),(72,'Can view supplier',18,'view_supplier'),(73,'Can add purchase header detail',19,'add_purchaseheaderdetail'),(74,'Can change purchase header detail',19,'change_purchaseheaderdetail'),(75,'Can delete purchase header detail',19,'delete_purchaseheaderdetail'),(76,'Can view purchase header detail',19,'view_purchaseheaderdetail'),(77,'Can add purchase item',20,'add_purchaseitem'),(78,'Can change purchase item',20,'change_purchaseitem'),(79,'Can delete purchase item',20,'delete_purchaseitem'),(80,'Can view purchase item',20,'view_purchaseitem'),(81,'Can add purchase payment',21,'add_purchasepayment'),(82,'Can change purchase payment',21,'change_purchasepayment'),(83,'Can delete purchase payment',21,'delete_purchasepayment'),(84,'Can view purchase payment',21,'view_purchasepayment'),(85,'Can add customer',22,'add_customer'),(86,'Can change customer',22,'change_customer'),(87,'Can delete customer',22,'delete_customer'),(88,'Can view customer',22,'view_customer'),(89,'Can add sale header detail',23,'add_saleheaderdetail'),(90,'Can change sale header detail',23,'change_saleheaderdetail'),(91,'Can delete sale header detail',23,'delete_saleheaderdetail'),(92,'Can view sale header detail',23,'view_saleheaderdetail'),(93,'Can add sale item',24,'add_saleitem'),(94,'Can change sale item',24,'change_saleitem'),(95,'Can delete sale item',24,'delete_saleitem'),(96,'Can view sale item',24,'view_saleitem'),(97,'Can add sale payment',25,'add_salepayment'),(98,'Can change sale payment',25,'change_salepayment'),(99,'Can delete sale payment',25,'delete_salepayment'),(100,'Can view sale payment',25,'view_salepayment');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$720000$ANFPjgQ3cBJ0ko4SueQXFz$jz7AjPNldqvF0OtWdh1xjbOOVrqSZrXeRMJuDJ5QaU8=','2024-07-18 06:50:09.402973',1,'shopowner','','','',1,1,'2024-06-26 13:57:18.000000'),(2,'pbkdf2_sha256$720000$qaczH07ajFaZzvuaxKjrTb$orAadTGSyR0Adueff8JieiMDm3Uy/4W3L8I9GXgsxsE=','2024-07-18 06:45:20.560724',0,'salesman','','','',0,1,'2024-07-04 06:29:29.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,1,1),(2,2,2);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brand`
--

DROP TABLE IF EXISTS `brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brand` (
  `brand_id` bigint NOT NULL AUTO_INCREMENT,
  `brand_name` varchar(100) NOT NULL,
  PRIMARY KEY (`brand_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brand`
--

LOCK TABLES `brand` WRITE;
/*!40000 ALTER TABLE `brand` DISABLE KEYS */;
INSERT INTO `brand` VALUES (1,'AsianPaints'),(2,'Nerolac'),(3,'Indigo'),(4,'Nippon'),(5,'Freemans'),(6,'Implemental'),(7,'PIdelite'),(8,'Godrej'),(9,'Bosch');
/*!40000 ALTER TABLE `brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `category_id` bigint NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Pipe'),(2,'Paint'),(3,'Farming Equipment'),(4,'General Tool'),(5,'General Hardwares');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `customer_id` bigint NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(60) NOT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `dob` varchar(20) DEFAULT NULL,
  `phoneno` varchar(13) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `address` longtext,
  `added_date` datetime(6) NOT NULL,
  `profession` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Saravanan','male','01/01/2001','9876543210',NULL,'','2024-06-29 05:35:25.768019','Farmer'),(2,'Shankar','male','01/01/2001',NULL,NULL,'','2024-07-02 10:12:41.042659','Plumber'),(3,'John','male',NULL,NULL,NULL,'','2024-07-02 10:14:04.225867','Painter'),(4,'Malar','female',NULL,NULL,NULL,'','2024-07-02 10:17:18.233314','Teacher'),(5,'Ponni','female',NULL,NULL,NULL,'','2024-07-02 10:18:43.322004',NULL),(6,'Anandhi','transgender',NULL,NULL,NULL,'','2024-07-02 10:19:47.538368','Police'),(7,'Karthik','male',NULL,NULL,NULL,'','2024-07-02 10:22:28.848539','Carpenter'),(8,'Manimaran','male',NULL,NULL,NULL,'','2024-07-02 10:25:18.434753','Business man'),(9,'Nandha','male',NULL,NULL,NULL,'','2024-07-02 10:30:02.288110','Farmer'),(10,'Radha','female',NULL,NULL,NULL,'','2024-07-02 10:36:14.142623','House wife'),(11,'Vetriselvan','male',NULL,NULL,NULL,'','2024-07-02 10:37:08.303682','Business man'),(12,'Kalaiselvan','male',NULL,NULL,NULL,'','2024-07-02 10:38:11.593791','Driver');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-07-04 06:23:43.759879','1','Owner',1,'[{\"added\": {}}]',3,1),(2,'2024-07-04 06:24:16.648174','2','Saleman',1,'[{\"added\": {}}]',3,1),(3,'2024-07-04 06:24:38.895102','1','Owner',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(4,'2024-07-04 06:27:43.677110','2','Saleman',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(5,'2024-07-04 06:28:31.199825','1','shopowner',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(6,'2024-07-04 06:29:30.565461','2','salesman',1,'[{\"added\": {}}]',4,1),(7,'2024-07-04 06:29:43.381799','2','salesman',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(8,'2024-07-04 10:55:07.807763','2','Salesman',2,'[{\"changed\": {\"fields\": [\"Name\"]}}]',3,1),(9,'2024-07-04 14:33:45.471874','2','Salesman',2,'[]',3,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(9,'database','attribute'),(8,'database','brand'),(7,'database','category'),(22,'database','customer'),(10,'database','product'),(11,'database','productattribute'),(14,'database','productdetail'),(15,'database','productprice'),(12,'database','productvariant'),(19,'database','purchaseheaderdetail'),(20,'database','purchaseitem'),(21,'database','purchasepayment'),(23,'database','saleheaderdetail'),(24,'database','saleitem'),(25,'database','salepayment'),(17,'database','stockdetail'),(18,'database','supplier'),(13,'database','variantattributevalue'),(16,'database','warehouse'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-06-26 13:52:12.246681'),(2,'auth','0001_initial','2024-06-26 13:52:28.646837'),(3,'admin','0001_initial','2024-06-26 13:52:32.145862'),(4,'admin','0002_logentry_remove_auto_add','2024-06-26 13:52:32.309763'),(5,'admin','0003_logentry_add_action_flag_choices','2024-06-26 13:52:32.436932'),(6,'contenttypes','0002_remove_content_type_name','2024-06-26 13:52:35.044219'),(7,'auth','0002_alter_permission_name_max_length','2024-06-26 13:52:36.226861'),(8,'auth','0003_alter_user_email_max_length','2024-06-26 13:52:36.523365'),(9,'auth','0004_alter_user_username_opts','2024-06-26 13:52:36.635911'),(10,'auth','0005_alter_user_last_login_null','2024-06-26 13:52:37.878675'),(11,'auth','0006_require_contenttypes_0002','2024-06-26 13:52:37.947202'),(12,'auth','0007_alter_validators_add_error_messages','2024-06-26 13:52:38.017812'),(13,'auth','0008_alter_user_username_max_length','2024-06-26 13:52:39.447721'),(14,'auth','0009_alter_user_last_name_max_length','2024-06-26 13:52:41.266624'),(15,'auth','0010_alter_group_name_max_length','2024-06-26 13:52:41.503505'),(16,'auth','0011_update_proxy_permissions','2024-06-26 13:52:41.595203'),(17,'auth','0012_alter_user_first_name_max_length','2024-06-26 13:52:43.103389'),(18,'sessions','0001_initial','2024-06-26 13:52:44.206625'),(19,'database','0001_initial','2024-06-26 13:55:53.533288'),(20,'database','0002_alter_purchaseitem_product_detail_ref_and_more','2024-06-28 15:48:23.554604'),(21,'database','0003_stockdetail_status','2024-06-29 15:17:18.480801'),(22,'database','0004_alter_productdetail_options_and_more','2024-07-02 10:07:56.236493');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4mo24b2ldtrdo5xotpnm5ks0gwgk72id','.eJxVjEEOwiAQRe_C2hAYoKBL9z0DGYZBqqYkpV0Z765NutDtf-_9l4i4rTVunZc4ZXERWpx-t4T04HkH-Y7zrUlq87pMSe6KPGiXY8v8vB7u30HFXr-1SZhDYQ3F50wmqAGgEEFyaENylrXD4tiiC0pZHqAEIvZncIYV-EG8PwPkOC0:1sUHu6:eyX9VcXKryjfq6xtItOGXzYVEYgsxN0Mus90Ej3PX94','2024-08-01 03:34:02.335651'),('76k5thdak20w9htu87uif5xxdw30fhzq','.eJxVjEEOwiAQRe_C2hAYoKBL9z0DGYZBqqYkpV0Z765NutDtf-_9l4i4rTVunZc4ZXERWpx-t4T04HkH-Y7zrUlq87pMSe6KPGiXY8v8vB7u30HFXr-1SZhDYQ3F50wmqAGgEEFyaENylrXD4tiiC0pZHqAEIvZncIYV-EG8PwPkOC0:1sPMfo:iq6ycTg6lSVKnuWOSpupDlj2lceek8mQZgpQ9n73a4U','2024-07-18 13:38:56.434106'),('d69xu0yk1c7uy0qhhxktbddp8mxyz8mx','.eJxVjEEOwiAQRe_C2hAYoKBL9z0DGYZBqqYkpV0Z765NutDtf-_9l4i4rTVunZc4ZXERWpx-t4T04HkH-Y7zrUlq87pMSe6KPGiXY8v8vB7u30HFXr-1SZhDYQ3F50wmqAGgEEFyaENylrXD4tiiC0pZHqAEIvZncIYV-EG8PwPkOC0:1sU7y2:4EI23mpq3zM0wrotEIs1yC5QcCizRIT-hXBgegqeC_o','2024-07-31 16:57:26.277360'),('pix5spsihuryszhw5nn68vv9lylyfyal','.eJxVjEEOwiAQRe_C2hAYoKBL9z0DGYZBqqYkpV0Z765NutDtf-_9l4i4rTVunZc4ZXERWpx-t4T04HkH-Y7zrUlq87pMSe6KPGiXY8v8vB7u30HFXr-1SZhDYQ3F50wmqAGgEEFyaENylrXD4tiiC0pZHqAEIvZncIYV-EG8PwPkOC0:1sUKxt:NTAqUN-_0grdo2Xm1GnJF-HAyB7bV59mMow6uPivtaQ','2024-08-01 06:50:09.510334'),('pox0wxm5ul0pgnsv9w1tqj7gr73ci31w','.eJxVjEEOwiAQRe_C2hAYoKBL9z0DGYZBqqYkpV0Z765NutDtf-_9l4i4rTVunZc4ZXERWpx-t4T04HkH-Y7zrUlq87pMSe6KPGiXY8v8vB7u30HFXr-1SZhDYQ3F50wmqAGgEEFyaENylrXD4tiiC0pZHqAEIvZncIYV-EG8PwPkOC0:1sUJWs:Iz7gFhvAPLpOxujDiIa9cvcEUpYhpdWjWsCOgX82C18','2024-08-01 05:18:10.359358'),('vlbkvh29djw9n5gqydx0im1kca4qp0ag','.eJxVjEEOwiAQRe_C2hAYoKBL9z0DGYZBqqYkpV0Z765NutDtf-_9l4i4rTVunZc4ZXERWpx-t4T04HkH-Y7zrUlq87pMSe6KPGiXY8v8vB7u30HFXr-1SZhDYQ3F50wmqAGgEEFyaENylrXD4tiiC0pZHqAEIvZncIYV-EG8PwPkOC0:1sUHu7:T2oOU1sU6jCTVL_mA20ls1vSlQtkMNG7vS5a0gG_Rh0','2024-08-01 03:34:03.174171');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `product_id` bigint NOT NULL AUTO_INCREMENT,
  `product_name` varchar(100) NOT NULL,
  `description` longtext,
  `has_variants` tinyint(1) NOT NULL,
  `brand_ref_id` bigint DEFAULT NULL,
  `category_ref_id` bigint DEFAULT NULL,
  PRIMARY KEY (`product_id`),
  KEY `product_brand_ref_id_52a3aea9_fk_brand_brand_id` (`brand_ref_id`),
  KEY `product_category_ref_id_aa47e052_fk_category_category_id` (`category_ref_id`),
  CONSTRAINT `product_brand_ref_id_52a3aea9_fk_brand_brand_id` FOREIGN KEY (`brand_ref_id`) REFERENCES `brand` (`brand_id`),
  CONSTRAINT `product_category_ref_id_aa47e052_fk_category_category_id` FOREIGN KEY (`category_ref_id`) REFERENCES `category` (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Sickle','used for harvesting crops',0,NULL,3),(2,'Apcolite Premium Emulsion','',1,1,2),(3,'Freemans Measuring Tape','',1,5,4),(4,'Castor Wheel with Brake','',0,6,5),(5,'M seal','',0,7,4),(6,'Door Lock','',0,8,5),(7,'Padlock','',1,8,4),(8,'Drilling Machine','',0,9,4);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_attribute`
--

DROP TABLE IF EXISTS `product_attribute`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_attribute` (
  `product_attr_id` bigint NOT NULL AUTO_INCREMENT,
  `attribute_ref_id` bigint NOT NULL,
  `product_ref_id` bigint NOT NULL,
  PRIMARY KEY (`product_attr_id`),
  KEY `product_attribute_attribute_ref_id_b8ef6c49_fk_attribute` (`attribute_ref_id`),
  KEY `product_attribute_product_ref_id_b581ecd9_fk_product_product_id` (`product_ref_id`),
  CONSTRAINT `product_attribute_attribute_ref_id_b8ef6c49_fk_attribute` FOREIGN KEY (`attribute_ref_id`) REFERENCES `attribute` (`attribute_id`),
  CONSTRAINT `product_attribute_product_ref_id_b581ecd9_fk_product_product_id` FOREIGN KEY (`product_ref_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_attribute`
--

LOCK TABLES `product_attribute` WRITE;
/*!40000 ALTER TABLE `product_attribute` DISABLE KEYS */;
INSERT INTO `product_attribute` VALUES (1,1,2),(2,2,2),(3,4,3),(4,6,7);
/*!40000 ALTER TABLE `product_attribute` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_detail`
--

DROP TABLE IF EXISTS `product_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_detail` (
  `product_detail_id` bigint NOT NULL AUTO_INCREMENT,
  `product_code` varchar(30) DEFAULT NULL,
  `product_image` varchar(100) DEFAULT NULL,
  `low_stock_threshold` int NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `product_ref_id` bigint NOT NULL,
  `variant_ref_id` bigint DEFAULT NULL,
  PRIMARY KEY (`product_detail_id`),
  UNIQUE KEY `product_code` (`product_code`),
  KEY `product_detail_variant_ref_id_a1cf439d_fk_product_v` (`variant_ref_id`),
  KEY `product_detail_product_ref_id_b9f964a8_fk_product_product_id` (`product_ref_id`),
  CONSTRAINT `product_detail_product_ref_id_b9f964a8_fk_product_product_id` FOREIGN KEY (`product_ref_id`) REFERENCES `product` (`product_id`),
  CONSTRAINT `product_detail_variant_ref_id_a1cf439d_fk_product_v` FOREIGN KEY (`variant_ref_id`) REFERENCES `product_variant` (`variant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_detail`
--

LOCK TABLES `product_detail` WRITE;
/*!40000 ALTER TABLE `product_detail` DISABLE KEYS */;
INSERT INTO `product_detail` VALUES (1,'p101','product_images/sickle.jfif',5,1,1,NULL),(2,'P201','product_images/apcolite-premium-emulsion_V3MsgZf.png',5,1,2,1),(3,'P202','product_images/apcolite-premium-emulsion_1ophQYm.png',10,1,2,2),(4,'P301','product_images/freemans_measuring_tape.jpg',5,1,3,3),(5,'P302','product_images/freemans_topline_measuring_tape.jpg',5,1,3,4),(6,'P303','product_images/30m-x-9-5mm-freemans.webp',5,1,3,5),(7,'P401','product_images/castor_wheel.jpg',5,1,4,NULL),(8,'P501','product_images/m_seal_1.jpg',5,1,5,NULL),(9,'P601','product_images/godrej_door_lock.webp',5,1,6,NULL),(10,'P701','product_images/godrej_padlock_7_levers.webp',5,1,7,6),(11,'P801','product_images/bosch_drilling_machine.webp',2,1,8,NULL),(12,'P203','product_images/apcolite-premium-emulsion_xElN334.png',5,1,2,7),(13,'P204','product_images/apcolite-premium-emulsion_kGxDSQM.png',5,1,2,8);
/*!40000 ALTER TABLE `product_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_price`
--

DROP TABLE IF EXISTS `product_price`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_price` (
  `product_price_id` bigint NOT NULL AUTO_INCREMENT,
  `cost_price` decimal(10,2) NOT NULL,
  `selling_price` decimal(10,2) NOT NULL,
  `updated_date` datetime(6) NOT NULL,
  `product_detail_ref_id` bigint NOT NULL,
  PRIMARY KEY (`product_price_id`),
  KEY `product_price_product_detail_ref_i_1fcc6495_fk_product_d` (`product_detail_ref_id`),
  CONSTRAINT `product_price_product_detail_ref_i_1fcc6495_fk_product_d` FOREIGN KEY (`product_detail_ref_id`) REFERENCES `product_detail` (`product_detail_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_price`
--

LOCK TABLES `product_price` WRITE;
/*!40000 ALTER TABLE `product_price` DISABLE KEYS */;
INSERT INTO `product_price` VALUES (1,30.00,60.00,'2024-06-26 12:00:04.000000',1),(2,150.00,300.00,'2024-07-02 06:35:45.277916',2),(3,500.00,1040.00,'2024-06-28 15:56:28.634627',3),(4,40.00,80.00,'2024-07-02 08:07:05.344241',4),(5,180.00,390.00,'2024-07-02 08:07:06.310484',5),(6,300.00,525.00,'2024-07-02 08:07:07.611813',6),(7,40.00,80.00,'2024-07-02 08:07:08.445025',7),(8,15.00,30.00,'2024-07-02 08:07:10.579565',8),(9,400.00,900.00,'2024-07-02 08:07:12.372017',9),(10,300.00,650.00,'2024-07-02 08:07:13.941417',10),(11,1000.00,2200.00,'2024-07-02 08:07:15.348773',11),(12,150.00,300.00,'2024-07-02 08:07:03.916884',12),(13,150.00,300.00,'2024-07-02 08:07:04.988156',13),(14,32.00,65.00,'2024-07-07 14:15:14.516281',1),(15,160.00,300.00,'2024-07-02 08:10:49.908312',12),(16,50.00,80.00,'2024-07-02 08:10:50.722505',7),(17,16.00,30.00,'2024-07-02 08:10:51.423681',8),(18,420.00,900.00,'2024-07-02 08:10:51.709753',9),(19,160.00,300.00,'2024-07-02 08:10:52.826031',13),(20,550.00,1040.00,'2024-07-02 08:10:53.114105',3),(21,140.00,280.00,'2024-07-07 14:46:19.594514',2),(22,160.00,320.00,'2024-07-07 14:46:20.494743',2),(23,140.00,300.00,'2024-07-02 08:16:43.203116',13),(24,170.00,390.00,'2024-07-02 08:16:44.582463',5),(25,500.00,2200.00,'2024-07-02 10:28:45.043429',11);
/*!40000 ALTER TABLE `product_price` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_variant`
--

DROP TABLE IF EXISTS `product_variant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_variant` (
  `variant_id` bigint NOT NULL AUTO_INCREMENT,
  `variant_name` varchar(100) DEFAULT NULL,
  `product_ref_id` bigint NOT NULL,
  PRIMARY KEY (`variant_id`),
  KEY `product_variant_product_ref_id_b259386e_fk_product_product_id` (`product_ref_id`),
  CONSTRAINT `product_variant_product_ref_id_b259386e_fk_product_product_id` FOREIGN KEY (`product_ref_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_variant`
--

LOCK TABLES `product_variant` WRITE;
/*!40000 ALTER TABLE `product_variant` DISABLE KEYS */;
INSERT INTO `product_variant` VALUES (1,'Apcolite Premium Emulsion variant1',2),(2,'Apcolite Premium Emulsion variant2',2),(3,'Freeman measuring tape 5m',3),(4,'Freemans Topline Professional Steel Measuring Tape 15m',3),(5,'Freemans Topline Professional Steel Measuring Tape 30m',3),(6,'Godrej Nav-tal Padlock 7 levers',7),(7,'Apcolite Premium Emulsion variant3',2),(8,'Apcolite Premium Emulsion variant4',2);
/*!40000 ALTER TABLE `product_variant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchase_header_detail`
--

DROP TABLE IF EXISTS `purchase_header_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchase_header_detail` (
  `purchase_id` bigint NOT NULL AUTO_INCREMENT,
  `purchased_date` datetime(6) NOT NULL,
  `bill_amount` decimal(10,2) NOT NULL,
  `supplier_ref_id` bigint DEFAULT NULL,
  PRIMARY KEY (`purchase_id`),
  KEY `purchase_header_deta_supplier_ref_id_8939bd29_fk_supplier_` (`supplier_ref_id`),
  CONSTRAINT `purchase_header_deta_supplier_ref_id_8939bd29_fk_supplier_` FOREIGN KEY (`supplier_ref_id`) REFERENCES `supplier` (`supplier_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase_header_detail`
--

LOCK TABLES `purchase_header_detail` WRITE;
/*!40000 ALTER TABLE `purchase_header_detail` DISABLE KEYS */;
INSERT INTO `purchase_header_detail` VALUES (1,'2024-04-03 13:48:57.000000',19950.00,1),(2,'2024-05-03 13:49:46.000000',12650.00,2),(3,'2024-05-23 15:28:54.000000',6075.00,1),(4,'2024-06-12 15:28:42.000000',4865.00,2),(5,'2024-07-02 09:58:03.925421',12300.00,1),(6,'2024-07-02 10:28:44.610315',1000.00,1);
/*!40000 ALTER TABLE `purchase_header_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchase_item`
--

DROP TABLE IF EXISTS `purchase_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchase_item` (
  `purchase_item_id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `unit_cost_price` decimal(10,2) NOT NULL,
  `product_detail_ref_id` bigint DEFAULT NULL,
  `purchase_ref_id` bigint NOT NULL,
  PRIMARY KEY (`purchase_item_id`),
  KEY `purchase_item_purchase_ref_id_943980d4_fk_purchase_` (`purchase_ref_id`),
  KEY `purchase_item_product_detail_ref_i_d4b70e50_fk_product_d` (`product_detail_ref_id`),
  CONSTRAINT `purchase_item_product_detail_ref_i_d4b70e50_fk_product_d` FOREIGN KEY (`product_detail_ref_id`) REFERENCES `product_detail` (`product_detail_id`),
  CONSTRAINT `purchase_item_purchase_ref_id_943980d4_fk_purchase_` FOREIGN KEY (`purchase_ref_id`) REFERENCES `purchase_header_detail` (`purchase_id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase_item`
--

LOCK TABLES `purchase_item` WRITE;
/*!40000 ALTER TABLE `purchase_item` DISABLE KEYS */;
INSERT INTO `purchase_item` VALUES (1,5,30.00,1,1),(2,5,150.00,2,1),(3,5,500.00,3,1),(4,5,150.00,12,1),(5,5,150.00,13,1),(6,5,40.00,4,1),(7,5,180.00,5,1),(8,5,300.00,6,1),(9,20,40.00,7,1),(10,10,15.00,8,1),(11,10,400.00,9,1),(12,15,300.00,10,1),(13,3,1000.00,11,1),(14,5,32.00,1,2),(15,10,160.00,12,2),(16,5,40.00,4,2),(17,20,50.00,7,2),(18,15,16.00,8,2),(19,5,420.00,9,2),(20,10,300.00,10,2),(21,10,160.00,13,2),(22,5,550.00,3,2),(23,5,140.00,2,3),(24,5,150.00,12,3),(25,10,40.00,7,3),(26,15,15.00,8,3),(27,10,300.00,10,3),(28,1,1000.00,11,3),(29,2,300.00,6,4),(30,5,160.00,2,4),(31,5,140.00,13,4),(32,5,40.00,4,4),(33,15,15.00,8,4),(34,5,400.00,9,4),(35,2,170.00,5,4),(36,10,500.00,3,5),(37,10,150.00,13,5),(38,10,40.00,4,5),(39,5,50.00,7,5),(40,10,15.00,8,5),(41,5,400.00,9,5),(42,10,300.00,10,5),(43,2,500.00,11,6);
/*!40000 ALTER TABLE `purchase_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchase_payment`
--

DROP TABLE IF EXISTS `purchase_payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchase_payment` (
  `purchase_payment_id` bigint NOT NULL AUTO_INCREMENT,
  `payment_date` datetime(6) NOT NULL,
  `paid_amount` decimal(10,2) NOT NULL,
  `balance_amount` decimal(10,2) NOT NULL,
  `purchase_ref_id` bigint NOT NULL,
  PRIMARY KEY (`purchase_payment_id`),
  KEY `purchase_payment_purchase_ref_id_0f98d7dd_fk_purchase_` (`purchase_ref_id`),
  CONSTRAINT `purchase_payment_purchase_ref_id_0f98d7dd_fk_purchase_` FOREIGN KEY (`purchase_ref_id`) REFERENCES `purchase_header_detail` (`purchase_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase_payment`
--

LOCK TABLES `purchase_payment` WRITE;
/*!40000 ALTER TABLE `purchase_payment` DISABLE KEYS */;
INSERT INTO `purchase_payment` VALUES (1,'2024-07-02 08:07:40.452128',15000.00,4950.00,1),(2,'2024-07-02 08:11:02.892568',10000.00,2650.00,2),(3,'2024-07-02 08:13:08.242468',5000.00,1075.00,3),(4,'2024-07-02 08:16:57.896848',4865.00,0.00,4),(5,'2024-07-02 09:58:16.804708',12300.00,0.00,5),(6,'2024-07-02 09:59:27.955830',3950.00,1000.00,1),(7,'2024-07-02 09:59:40.913131',1000.00,1650.00,2),(8,'2024-07-02 09:59:54.157503',1075.00,0.00,3),(9,'2024-07-15 05:09:31.326751',650.00,1000.00,2);
/*!40000 ALTER TABLE `purchase_payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sale_header_detail`
--

DROP TABLE IF EXISTS `sale_header_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sale_header_detail` (
  `sale_id` bigint NOT NULL AUTO_INCREMENT,
  `sold_date` datetime(6) NOT NULL,
  `bill_amount` decimal(10,2) NOT NULL,
  `discount_percent` decimal(10,2) NOT NULL,
  `discount_amount` decimal(10,2) NOT NULL,
  `customer_ref_id` bigint DEFAULT NULL,
  PRIMARY KEY (`sale_id`),
  KEY `sale_header_detail_customer_ref_id_d314151d_fk_customer_` (`customer_ref_id`),
  CONSTRAINT `sale_header_detail_customer_ref_id_d314151d_fk_customer_` FOREIGN KEY (`customer_ref_id`) REFERENCES `customer` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sale_header_detail`
--

LOCK TABLES `sale_header_detail` WRITE;
/*!40000 ALTER TABLE `sale_header_detail` DISABLE KEYS */;
INSERT INTO `sale_header_detail` VALUES (1,'2024-04-06 11:27:42.000000',260.00,0.00,0.00,1),(2,'2024-04-19 20:12:34.000000',220.00,0.00,0.00,2),(3,'2024-04-24 20:12:53.000000',1040.00,0.00,0.00,3),(4,'2024-04-25 20:13:01.000000',1360.00,0.00,0.00,2),(5,'2024-05-05 20:13:50.000000',600.00,8.33,50.00,3),(6,'2024-05-14 20:17:08.000000',1305.00,0.00,0.00,4),(7,'2024-05-18 20:17:17.000000',810.00,0.00,0.00,5),(8,'2024-05-24 20:17:23.000000',2600.00,0.00,0.00,6),(9,'2024-05-28 20:20:38.000000',2200.00,0.00,0.00,2),(10,'2024-06-01 20:17:39.000000',9580.00,2.92,280.00,7),(11,'2024-06-08 20:17:49.000000',13660.00,0.00,0.00,8),(12,'2024-06-13 20:17:58.000000',180.00,0.00,0.00,9),(13,'2024-06-17 20:18:04.000000',300.00,0.00,0.00,2),(14,'2024-06-22 20:18:11.000000',2000.00,10.00,200.00,7),(15,'2024-06-25 20:19:35.000000',1300.00,0.00,0.00,10),(16,'2024-06-29 20:19:43.000000',1950.00,0.00,0.00,11),(17,'2024-07-02 20:19:49.000000',1300.00,0.00,0.00,12);
/*!40000 ALTER TABLE `sale_header_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sale_item`
--

DROP TABLE IF EXISTS `sale_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sale_item` (
  `sale_item_id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `unit_sell_price` decimal(10,2) NOT NULL,
  `product_with_price_ref_id` bigint DEFAULT NULL,
  `sale_ref_id` bigint NOT NULL,
  PRIMARY KEY (`sale_item_id`),
  KEY `sale_item_sale_ref_id_51f4ad6d_fk_sale_header_detail_sale_id` (`sale_ref_id`),
  KEY `sale_item_product_with_price_r_1c42feb4_fk_product_p` (`product_with_price_ref_id`),
  CONSTRAINT `sale_item_product_with_price_r_1c42feb4_fk_product_p` FOREIGN KEY (`product_with_price_ref_id`) REFERENCES `product_price` (`product_price_id`),
  CONSTRAINT `sale_item_sale_ref_id_51f4ad6d_fk_sale_header_detail_sale_id` FOREIGN KEY (`sale_ref_id`) REFERENCES `sale_header_detail` (`sale_id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sale_item`
--

LOCK TABLES `sale_item` WRITE;
/*!40000 ALTER TABLE `sale_item` DISABLE KEYS */;
INSERT INTO `sale_item` VALUES (1,3,60.00,1,1),(2,1,80.00,4,1),(3,2,80.00,4,2),(4,2,30.00,8,2),(5,1,1040.00,3,3),(6,2,30.00,8,4),(7,2,650.00,10,4),(8,2,300.00,13,5),(9,2,390.00,5,6),(10,1,525.00,6,6),(11,2,80.00,7,7),(12,1,650.00,10,7),(13,4,650.00,10,8),(14,1,2200.00,11,9),(15,2,80.00,4,10),(16,4,30.00,8,10),(17,4,900.00,9,10),(18,2,2200.00,11,10),(19,2,650.00,10,10),(20,1,1040.00,3,11),(21,4,300.00,12,11),(22,4,300.00,19,11),(23,1,80.00,4,11),(24,1,390.00,5,11),(25,10,80.00,7,11),(26,10,30.00,8,11),(27,5,900.00,9,11),(28,3,650.00,10,11),(29,1,2200.00,11,11),(30,2,60.00,1,12),(31,1,60.00,14,12),(32,10,30.00,8,13),(33,18,80.00,7,14),(34,7,80.00,16,14),(35,2,650.00,10,15),(36,3,650.00,10,16),(37,2,650.00,10,17);
/*!40000 ALTER TABLE `sale_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sale_payment`
--

DROP TABLE IF EXISTS `sale_payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sale_payment` (
  `sale_payment_id` bigint NOT NULL AUTO_INCREMENT,
  `payment_date` datetime(6) NOT NULL,
  `paid_amount` decimal(10,2) NOT NULL,
  `balance_amount` decimal(10,2) NOT NULL,
  `sale_ref_id` bigint NOT NULL,
  PRIMARY KEY (`sale_payment_id`),
  KEY `sale_payment_sale_ref_id_b57b1578_fk_sale_header_detail_sale_id` (`sale_ref_id`),
  CONSTRAINT `sale_payment_sale_ref_id_b57b1578_fk_sale_header_detail_sale_id` FOREIGN KEY (`sale_ref_id`) REFERENCES `sale_header_detail` (`sale_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sale_payment`
--

LOCK TABLES `sale_payment` WRITE;
/*!40000 ALTER TABLE `sale_payment` DISABLE KEYS */;
INSERT INTO `sale_payment` VALUES (1,'2024-07-02 10:12:07.846204',260.00,0.00,1),(2,'2024-07-02 10:13:28.243695',220.00,0.00,2),(3,'2024-07-02 10:15:08.695287',1040.00,0.00,3),(4,'2024-07-02 10:16:11.491292',1360.00,0.00,4),(5,'2024-07-02 10:16:47.491477',550.00,0.00,5),(6,'2024-07-02 10:18:02.677642',1305.00,0.00,6),(7,'2024-07-02 10:20:10.049105',2600.00,0.00,8),(8,'2024-07-02 10:21:25.598357',2200.00,0.00,9),(9,'2024-07-02 10:21:41.198331',810.00,0.00,7),(10,'2024-07-02 10:24:12.701999',9300.00,0.00,10),(11,'2024-07-02 10:27:25.470143',13660.00,0.00,11),(12,'2024-07-02 10:30:36.313782',180.00,0.00,12),(13,'2024-07-02 10:33:34.378130',300.00,0.00,13),(14,'2024-07-02 10:35:01.013225',1800.00,0.00,14),(15,'2024-07-02 10:36:31.737618',1300.00,0.00,15),(16,'2024-07-02 10:37:38.376737',1950.00,0.00,16),(17,'2024-07-02 10:39:04.103225',1300.00,0.00,17);
/*!40000 ALTER TABLE `sale_payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock_detail`
--

DROP TABLE IF EXISTS `stock_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stock_detail` (
  `stock_id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `updated_date` datetime(6) NOT NULL,
  `product_with_price_ref_id` bigint NOT NULL,
  `warehouse_ref_id` bigint NOT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`stock_id`),
  KEY `stock_detail_product_with_price_r_bde41a8a_fk_product_p` (`product_with_price_ref_id`),
  KEY `stock_detail_warehouse_ref_id_9207d3ca_fk_warehouse_warehouse_id` (`warehouse_ref_id`),
  CONSTRAINT `stock_detail_product_with_price_r_bde41a8a_fk_product_p` FOREIGN KEY (`product_with_price_ref_id`) REFERENCES `product_price` (`product_price_id`),
  CONSTRAINT `stock_detail_warehouse_ref_id_9207d3ca_fk_warehouse_warehouse_id` FOREIGN KEY (`warehouse_ref_id`) REFERENCES `warehouse` (`warehouse_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock_detail`
--

LOCK TABLES `stock_detail` WRITE;
/*!40000 ALTER TABLE `stock_detail` DISABLE KEYS */;
INSERT INTO `stock_detail` VALUES (2,5,'2024-07-02 08:07:02.808607',2,1,'good'),(3,13,'2024-07-02 10:27:13.850201',3,1,'good'),(4,6,'2024-07-02 10:27:14.486339',12,1,'good'),(5,13,'2024-07-02 10:16:38.223112',13,1,'good'),(6,19,'2024-07-02 10:27:15.266539',4,1,'good'),(7,2,'2024-07-02 10:27:15.478599',5,1,'good'),(8,6,'2024-07-02 10:17:51.593814',6,1,'good'),(10,22,'2024-07-02 10:33:24.337568',8,1,'good'),(11,11,'2024-07-02 10:27:16.397828',9,1,'good'),(12,26,'2024-07-02 10:38:54.749924',10,1,'good'),(14,4,'2024-07-02 10:30:20.245682',14,1,'good'),(15,10,'2024-07-02 08:10:50.312401',15,1,'good'),(16,18,'2024-07-02 10:34:49.083184',16,1,'good'),(17,15,'2024-07-02 08:10:51.544710',17,1,'good'),(18,5,'2024-07-02 08:10:51.895801',18,1,'good'),(19,6,'2024-07-02 10:27:14.926449',19,1,'good'),(20,5,'2024-07-02 08:10:53.217125',20,1,'good'),(21,5,'2024-07-02 08:12:48.677500',21,1,'good'),(22,5,'2024-07-02 08:16:42.916041',22,1,'good'),(23,5,'2024-07-02 08:16:43.363155',23,1,'good'),(24,2,'2024-07-02 08:16:44.809523',24,1,'good'),(25,2,'2024-07-02 10:28:45.541555',25,1,'good');
/*!40000 ALTER TABLE `stock_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier` (
  `supplier_id` bigint NOT NULL AUTO_INCREMENT,
  `shop_name` varchar(100) NOT NULL,
  `owner_name` varchar(60) NOT NULL,
  `phoneno` varchar(13) DEFAULT NULL,
  `address` longtext,
  `date_added` datetime(6) NOT NULL,
  PRIMARY KEY (`supplier_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES (1,'Chennai Traders','abc',NULL,'','2024-06-26 13:57:58.175321'),(2,'Trichy Hardwares','xyz',NULL,'','2024-06-26 13:58:03.991331');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `variant_attribute_value`
--

DROP TABLE IF EXISTS `variant_attribute_value`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `variant_attribute_value` (
  `variant_attr_value_id` bigint NOT NULL AUTO_INCREMENT,
  `value` varchar(60) NOT NULL,
  `product_attr_ref_id` bigint NOT NULL,
  `variant_ref_id` bigint NOT NULL,
  PRIMARY KEY (`variant_attr_value_id`),
  KEY `variant_attribute_va_product_attr_ref_id_4480f284_fk_product_a` (`product_attr_ref_id`),
  KEY `variant_attribute_va_variant_ref_id_ff4e9cc3_fk_product_v` (`variant_ref_id`),
  CONSTRAINT `variant_attribute_va_product_attr_ref_id_4480f284_fk_product_a` FOREIGN KEY (`product_attr_ref_id`) REFERENCES `product_attribute` (`product_attr_id`),
  CONSTRAINT `variant_attribute_va_variant_ref_id_ff4e9cc3_fk_product_v` FOREIGN KEY (`variant_ref_id`) REFERENCES `product_variant` (`variant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `variant_attribute_value`
--

LOCK TABLES `variant_attribute_value` WRITE;
/*!40000 ALTER TABLE `variant_attribute_value` DISABLE KEYS */;
INSERT INTO `variant_attribute_value` VALUES (1,'Intense Purple',1,1),(2,'1 ltr',2,1),(3,'Intense Purple',1,2),(4,'4 ltr',2,2),(7,'5m',3,3),(8,'15Mtr x 9.5mm',3,4),(9,'30Mtr x 9.5mm',3,5),(10,'7 levers',4,6),(11,'Orange Spark',1,7),(12,'1 ltr',2,7),(13,'Rosy Coral',1,8),(14,'1 ltr',2,8);
/*!40000 ALTER TABLE `variant_attribute_value` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `warehouse`
--

DROP TABLE IF EXISTS `warehouse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `warehouse` (
  `warehouse_id` bigint NOT NULL AUTO_INCREMENT,
  `warehouse_name` varchar(60) NOT NULL,
  `location` longtext,
  `incharge_person_id` int NOT NULL,
  PRIMARY KEY (`warehouse_id`),
  KEY `warehouse_incharge_person_id_b16f8dc7_fk_auth_user_id` (`incharge_person_id`),
  CONSTRAINT `warehouse_incharge_person_id_b16f8dc7_fk_auth_user_id` FOREIGN KEY (`incharge_person_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warehouse`
--

LOCK TABLES `warehouse` WRITE;
/*!40000 ALTER TABLE `warehouse` DISABLE KEYS */;
INSERT INTO `warehouse` VALUES (1,'shop','',1),(2,'warehouse 1','',1);
/*!40000 ALTER TABLE `warehouse` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-22 10:55:22
