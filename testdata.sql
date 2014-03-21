INSERT INTO prices (date, location_name, good_name, high, low, mean)
VALUES (CURDATE(), 'canada', 'carrot', 3, 1, 2);

INSERT INTO prices (date, location_name, good_name, high, low, mean)
VALUES (CURDATE() - INTERVAL 1 DAY, 'canada', 'carrot', 4, 2, 3);

INSERT INTO prices (date, location_name, good_name, high, low, mean)
VALUES (CURDATE(), 'syria', 'sugar', 20, 1, 19);

INSERT INTO prices (date, location_name, good_name, high, low, mean)
VALUES (CURDATE(), 'syria', 'bread', 30, 10, 20);

INSERT INTO prices (date, location_name, good_name, high, low, mean)
VALUES (CURDATE()-1, 'syria', 'bread', 25, 9, 17);

INSERT INTO prices (date, location_name, good_name, high, low, mean)
VALUES (CURDATE()-2, 'syria', 'bread', 25, 12, 22);

INSERT INTO prices (date, location_name, good_name, high, low, mean)
VALUES (CURDATE()-3, 'syria', 'bread', 30, 14, 21);

INSERT INTO prices (date, location_name, good_name, high, low, mean)
VALUES (CURDATE()-4, 'syria', 'bread', 31, 15, 21);

INSERT INTO prices (date, location_name, good_name, high, low, mean)
VALUES (CURDATE()-5, 'syria', 'bread', 32, 20, 25);

INSERT INTO prices (date, location_name, good_name, high, low, mean)
VALUES (CURDATE()-6, 'syria', 'bread', 29, 17, 24);

INSERT INTO prices (date, location_name, good_name, high, low, mean)
VALUES (CURDATE()-7, 'syria', 'bread', 28, 16, 20);
