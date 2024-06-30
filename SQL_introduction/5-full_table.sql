-- Script to get the full description of first_table
-- Author: [Laman]

SELECT table_name, create_table
FROM information_schema.tables
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';
