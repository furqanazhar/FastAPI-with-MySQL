CREATE TABLE IF NOT EXISTS `customers` (
  `clientID` int NOT NULL,
  `fullName` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `mobileNo` varchar(45) NOT NULL,
  `officeName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`clientID`)
)