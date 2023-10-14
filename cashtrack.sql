USE cashtrack;
CREATE TABLE spent (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    userID INT,
    amount DECIMAL(10, 2),
    category VARCHAR(255),
    onWhat VARCHAR(255),
    note TEXT,
    datetime DATETIME
);

-- Inserting a sample record
INSERT INTO spent (userID, amount, category, onWhat, note, datetime)
VALUES (1, 50.00, 'Food', 'Dinner at a restaurant', 'Enjoyed a nice meal', '2023-10-15 19:30:00');

-- Inserting another sample record
INSERT INTO spent (userID, amount, category, onWhat, note, datetime)
VALUES (2, 25.00, 'Entertainment', 'Movie tickets', 'Watched a new release', '2023-10-15 20:15:00');
