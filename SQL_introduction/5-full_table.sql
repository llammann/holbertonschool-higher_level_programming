-- Script to get the full description of first_table
-- Author: [Laman]

SELECT CONCAT('first_table', 'CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci') AS description;

