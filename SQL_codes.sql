-- Convert csv file into sql database
-- 1. Create database and select it
CREATE DATABASE dataset;
USE dataset;

-- 2. Create table
CREATE TABLE traindata(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	class VARCHAR(1),
	cap_shape VARCHAR(1),
	cap_surface VARCHAR(1),
	cap_color VARCHAR(1),
	bruises VARCHAR(1),
	odor VARCHAR(1),
	gill_attachment VARCHAR(1),
	gill_spacing VARCHAR(1),
	gill_size VARCHAR(1),
	gill_color VARCHAR(1),
	stalk_shape VARCHAR(1),
	stalk_root VARCHAR(1),
	stalk_surface_above_ring VARCHAR(1),
	stalk_surface_below_ring VARCHAR(1),
	stalk_color_above_ring VARCHAR(1),
	stalk_color_below_ring VARCHAR(1),
	veil_type VARCHAR(1),
	veil_color VARCHAR(1),
	ring_number VARCHAR(1),
	ring_type VARCHAR(1),
	spore_print_color VARCHAR(1),
	population VARCHAR(1),
	habitat VARCHAR(1)
);

SELECT * FROM traindata;

-- 3. Load data from csv file to the created table 
LOAD DATA LOCAL INFILE  "C:/Users/cmehb/Desktop/Mushroom Classification/mushrooms.csv"
INTO TABLE traindata
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 

-- Select all records from table where class is x and capshape is not y
SELECT * FROM traindata where class = 'x' and cap_shape != 'y';

-- Select all classes where it starts with letter x and capshape is not y
SELECT * FROM traindata where class like 'x%' and cap_shape != 'y';

-- Select all classes where it letter x is there and capshape is not y
SELECT * FROM traindata where class like '%x%' and cap_shape != 'y';

