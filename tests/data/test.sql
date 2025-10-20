CREATE TABLE Animes(
    ID INT NOT NULL PRIMARY KEY,
    Name VARCHAR(150),
    Rating FLOAT
);

INSERT INTO Animes([ID], [Name], [Rating])
VALUES
    (1, 'One Piece', 9),
    (2, 'Naruto Shippuden', 10),
    (3, 'Bleach', 10),
    (4, 'Hunter X Hunter', 8.5),
    (5, 'Naruto', 8),
    (6, 'Berserk', 10),
    (7, 'Fullmetal Alchemist: Brotherhood', 9.2),
    (8, 'Code Geass', 8.9),
    (9, 'Trigun', 8.2),
    (10,'Attack On Titan', 8.5);

CREATE TABLE Characters(
    ID INT NOT NULL PRIMARY KEY,
    Name VARCHAR(100),
    Anime INT,
    CONSTRAINT UQ_Character UNIQUE([Name], [Anime]),
    FOREIGN KEY ([Anime]) REFERENCES Animes([ID])
);

INSERT INTO Characters([ID], [Name], [Anime])
VALUES
    (1, 'Ichigo Kurosaki', 3),
    (2, 'Naruto Uzumaki', 2),
    (3, 'Naruto Uzumaki', 8),
    (4, 'Byakuya Kuchiki', 3),
    (5, 'Edward Elric', 7),
    (6, 'Lelouch Lamperouge', 8);
