
use pnu_scheduletestdb

CREATE TABLE faculty (
    faculty_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE groups_ (
    group_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    faculty_id INT NOT NULL,
    FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id)
);

CREATE TABLE academics (
    academic_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    second_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50) NOT NULL,
    is_active BOOLEAN DEFAULT true,
    on_vacation BOOLEAN DEFAULT false
);

CREATE TABLE audiences (
    audience_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(50)
);

CREATE TABLE disciplines (
    discipline_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE timestamps_ (
    timestamp_id INT PRIMARY KEY AUTO_INCREMENT,
    start_date TIME NOT NULL,
    end_date TIME NOT NULL,
    date_ DATE NOT NULL
);

CREATE TABLE schedule (
    schedule_id INT PRIMARY KEY AUTO_INCREMENT,
    academic_id INT NOT NULL,
    group_id INT NOT NULL,
    audience_id INT NOT NULL,
    discipline_id INT NOT NULL,
    timestamp_id INT NOT NULL,
    FOREIGN KEY (academic_id) REFERENCES academics(academic_id),
    FOREIGN KEY (group_id) REFERENCES groups_(group_id),
    FOREIGN KEY (audience_id) REFERENCES audiences(audience_id),
    FOREIGN KEY (discipline_id) REFERENCES disciplines(discipline_id),
    FOREIGN KEY (timestamp_id) REFERENCES timestamps_(timestamp_id)
);

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    group_id INT,
    academic_id INT,
    FOREIGN KEY (group_id) REFERENCES groups_(group_id),
    FOREIGN KEY (academic_id) REFERENCES academics(academic_id)
);

SELECT schedule.schedule_id, academics.first_name, academics.second_name, groups_.name, audiences.name, disciplines.name, timestamps_.start_date, timestamps_.end_date, timestamps_.date_
FROM schedule
inner JOIN academics ON schedule.academic_id = academics.academic_id
inner JOIN groups_ ON schedule.group_id = groups_.group_id
inner JOIN audiences ON schedule.audience_id = audiences.audience_id
inner JOIN disciplines ON schedule.discipline_id = disciplines.discipline_id
inner JOIN timestamps_ ON schedule.timestamp_id = timestamps_.timestamp_id
ORDER BY timestamps_.date_;






CALL generate_schedule_dates('2023-06-01', '2023-06-30')


select * from users
select * from schedule
select * from timestamps_
select * from disciplines
select * from audiences
select * from groups_
select * from faculty
select * from academics


drop table schedule
drop table timestamps_
drop table disciplines
drop table audiences
drop table groups_
drop table faculty
drop table academics


delete from timestamps_ where timestamp_id != -1
delete from disciplines where discipline_id != -1
delete from users where user_id != -1
delete from groups_ where group_id != -1
delete from faculty where faculty_id != -1
delete from academics where academic_id != -1
delete from schedule where schedule_id != -1







































CREATE PROCEDURE generate_schedule_dates(IN start_date DATE, IN end_date DATE)
BEGIN
    DECLARE loop_date DATE;
    
    SET loop_date = start_date;
    
    WHILE loop_date <= end_date DO

        INSERT INTO timestamps_ (start_date, end_date, date_)
        VALUES
            (TIME('08:15:00'), TIME('09:35:00'), loop_date),
            (TIME('09:50:00'), TIME('11:10:00'), loop_date),
            (TIME('12:00:00'), TIME('13:20:00'), loop_date),
            (TIME('13:35:00'), TIME('14:55:00'), loop_date),
            (TIME('15:10:00'), TIME('16:30:00'), loop_date),
            (TIME('16:45:00'), TIME('18:05:00'), loop_date);
        
        SET loop_date = DATE_ADD(loop_date, INTERVAL 1 DAY);
    END WHILE;
END

DROP PROCEDURE IF EXISTS generate_schedule_dates;