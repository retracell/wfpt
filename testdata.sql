INSERT INTO prices (date, location_name, good_name, high, low, mean)
VALUES (CURDATE(), 'canada', 'carrot', 3, 1, 2);

INSERT INTO prices (date, location_name, good_name, high, low, mean)
VALUES (CURDATE() - INTERVAL 1 DAY, 'canada', 'carrot', 4, 2, 3);

INSERT INTO prices (date, location_name, good_name, high, low, mean)
VALUES (CURDATE(), 'syria', 'bread', 30, 10, 20);

INSERT INTO prices (date, location_name, good_name, high, low, mean)
VALUES (CURDATE(), 'syria', 'sugar', 20, 1, 19);
