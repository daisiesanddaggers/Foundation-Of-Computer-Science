CREATE DATABASE assignment;
USE assignment;

DROP TABLE IF EXISTS Membership;
DROP TABLE IF EXISTS Club;
DROP TABLE IF EXISTS Student;

CREATE TABLE Student (
    StudentID   INT             PRIMARY KEY,
    StudentName VARCHAR(100)    NOT NULL,
    Email       VARCHAR(150)    UNIQUE NOT NULL
);

CREATE TABLE Club (
    ClubID      VARCHAR(10)     PRIMARY KEY,
    ClubName    VARCHAR(100)    NOT NULL,
    ClubRoom    VARCHAR(50),
    ClubMentor  VARCHAR(100)
);

CREATE TABLE Membership (
    MembershipID    VARCHAR(10)     PRIMARY KEY,
    StudentID       INT,
    ClubID          VARCHAR(10),
    JoinDate        DATE,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (ClubID)    REFERENCES Club(ClubID)
);
