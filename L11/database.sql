DROP TABLE IF EXISTS 'student';
DROP INDEX IF EXISTS 'sqlite_autoindex_student_1';
DROP TABLE IF EXISTS 'student_marks';
DROP TABLE IF EXISTS 'groups';
CREATE TABLE student (
id INTEGER PRIMARY KEY,
name VARCHAR(255) UNIQUE,
group_id INTEGER REFERENCES groups (id) NOT NULL);
INSERT INTO 'student' VALUES(1,'Артём',1);
INSERT INTO 'student' VALUES(2,'Денис',3);
INSERT INTO 'student' VALUES(3,'Данил',2);
null;
CREATE TABLE student_marks (
student_id INTEGER REFERENCES student (id) PRIMARY KEY,
math_mark_average FLOAT,
physics_mark_average FLOAT,
python_mark_average FLOAT);
INSERT INTO 'student_marks' VALUES(1,5,4.5,5);
INSERT INTO 'student_marks' VALUES(2,3,4,4.5);
INSERT INTO 'student_marks' VALUES(3,5,4.3,4.5);
CREATE TABLE groups (
id INTEGER PRIMARY KEY,
name VARCHAR(255) NOT NULL,
description VARCHAR(255));
INSERT INTO 'groups' VALUES(1,'БПИ-2401','умные ребята');
INSERT INTO 'groups' VALUES(2,'БПИ-2402','крутые ребята');
INSERT INTO 'groups' VALUES(3,'БПИ-2403','не умные ребята');
