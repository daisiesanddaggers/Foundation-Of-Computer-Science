SELECT * FROM Student;

SELECT ClubID, ClubName, ClubRoom, ClubMentor FROM Club;

SELECT s.StudentName, c.ClubName, m.JoinDate
FROM Membership m
    INNER JOIN Student s ON m.StudentID = s.StudentID
    INNER JOIN Club    c ON m.ClubID    = c.ClubID
ORDER BY s.StudentName, m.JoinDate;
