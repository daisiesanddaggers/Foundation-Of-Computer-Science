INSERT INTO Student (StudentID, StudentName, Email) VALUES
    (1, 'Asha',   'asha@email.com'),
    (2, 'Bikash', 'bikash@email.com'),
    (3, 'Nisha',  'nisha@email.com'),
    (4, 'Rohan',  'rohan@email.com'),
    (5, 'Suman',  'suman@email.com'),
    (6, 'Pooja',  'pooja@email.com'),
    (7, 'Aman',   'aman@email.com');

INSERT INTO Club (ClubID, ClubName, ClubRoom, ClubMentor) VALUES
    ('C1', 'Music Club',  'R101', 'Mr. Raman'),
    ('C2', 'Sports Club', 'R202', 'Ms. Sita'),
    ('C3', 'Drama Club',  'R303', 'Mr. Kiran'),
    ('C4', 'Coding Club', 'Lab1', 'Mr. Anil');

INSERT INTO Membership (MembershipID, StudentID, ClubID, JoinDate) VALUES
    ('M1',  1, 'C1', '2024-01-10'),
    ('M2',  2, 'C2', '2024-01-12'),
    ('M3',  1, 'C2', '2024-01-15'),
    ('M4',  3, 'C1', '2024-01-20'),
    ('M5',  4, 'C3', '2024-01-18'),
    ('M6',  5, 'C1', '2024-01-22'),
    ('M7',  2, 'C3', '2024-01-25'),
    ('M8',  6, 'C2', '2024-01-27'),
    ('M9',  3, 'C4', '2024-01-28'),
    ('M10', 7, 'C4', '2024-01-30');
