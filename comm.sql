
use pnu_scheduletestdb

CREATE TABLE faculty (
    faculty_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(120) NOT NULL
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






CALL generate_schedule_dates('2023-06-05', '2023-06-25')


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
drop table users
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

INSERT INTO timestamps_ (start_date, end_date, date_)
VALUES
    (TIME('08:15:00'), TIME('09:35:00'), '2023-06-05'),
    (TIME('09:50:00'), TIME('11:10:00'), '2023-06-05'),
    (TIME('12:00:00'), TIME('13:20:00'), '2023-06-05'),
    (TIME('13:35:00'), TIME('14:55:00'), '2023-06-05'),
    (TIME('15:10:00'), TIME('16:30:00'), '2023-06-05'),
    (TIME('16:45:00'), TIME('18:05:00'), '2023-06-05'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-06'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-06'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-06'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-06'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-06'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-06'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-07'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-07'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-07'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-07'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-07'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-07'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-08'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-08'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-08'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-08'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-08'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-08'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-09'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-09'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-09'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-09'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-09'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-09'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-10'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-10'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-10'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-10'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-10'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-10'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-11'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-11'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-11'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-11'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-11'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-11'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-12'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-12'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-12'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-12'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-12'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-12'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-13'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-13'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-13'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-13'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-13'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-13'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-14'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-14'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-14'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-14'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-14'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-14'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-15'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-15'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-15'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-15'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-15'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-15'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-16'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-16'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-16'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-16'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-16'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-16'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-17'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-17'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-17'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-17'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-17'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-17'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-18'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-18'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-18'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-18'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-18'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-18'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-19'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-19'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-19'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-19'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-19'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-19'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-20'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-20'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-20'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-20'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-20'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-20'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-21'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-21'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-21'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-21'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-21'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-21'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-22'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-22'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-22'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-22'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-22'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-22'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-23'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-23'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-23'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-23'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-23'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-23'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-24'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-24'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-24'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-24'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-24'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-24'),
(TIME('08:15:00'), TIME('09:35:00'), '2023-06-25'),
(TIME('09:50:00'), TIME('11:10:00'), '2023-06-25'),
(TIME('12:00:00'), TIME('13:20:00'), '2023-06-25'),
(TIME('13:35:00'), TIME('14:55:00'), '2023-06-25'),
(TIME('15:10:00'), TIME('16:30:00'), '2023-06-25'),
(TIME('16:45:00'), TIME('18:05:00'), '2023-06-25');



INSERT INTO faculty (name) VALUES
    ('Інформаційних техногологій, обліку та фінансів'),
    ('Агрономічний'),
    ('Права, публічного управління та національної безпеки'),
    ('Економіки та менеджменту'),
    ('Інженерії та енергетики'),
    ('Технологічний'),
    ('Лісового господарства та екології'),
    ('Аспірантура'),
    ('Ветеринарної медицини');

INSERT INTO groups_ (name, faculty_id) VALUES
    ('КН-21', 1),
    ('ІСТ-21', 1),
    ('A-21-3', 2);

INSERT INTO academics (first_name, second_name, middle_name) VALUES
    ('В.', 'Мельничук', 'В.'),
    ('О.', 'Маєвський', 'B.'),
    ('І.', 'Гіваргізов', 'Г.'),
    ('С.', 'Веретюк', 'М.'),
    ('Д.', 'Оленюк', 'О.'),
    ('М.', 'Ковальчук', 'О.'),
    ('О.', 'Скорий', 'С.'),
    ('С.', 'Роспотнюк', 'В.'),
    ('С.', 'Петрова', 'І.'),
    ('В.', 'Українець', 'Р.');


INSERT INTO audiences (name, description) VALUES
    ('110', ' '),
    ('86(спец)', ' '),
    ('87', ' '),
    ('114', ' '),
    ('85а', ' '),
    ('113', ' '),
    ('111', ' '),
    ('109', ' '),
    ('89', ' '),
    ('82', ' '),
    ('84(спец)', ' '),
    ('Спортзал 1', ' '),
    ('Дистанційно', 'Ідентифікатор: 522 795 3994 Код доступу: 777');

INSERT INTO disciplines (name) VALUES
    ('Методи наукових досліджень'),
    ('Теорія інформації'),
    ('Фізичне виховання'),
    ('Математичні методи дослідження операцій'),
    ('Бази даних'),
    ('Філософія'),
    ('Ділова іноземна мова'),
    ('Web-програмування'),
    ('Розробка мобільних застосунків');



INSERT INTO schedule (academic_id, group_id, audience_id, discipline_id, timestamp_id) VALUES
   
    (6, 1, 9, 9, 5),
    (1, 1, 4, 4, 6),
    (2, 2, 5, 3, 12),
    (1, 1, 4, 4, 13),
    (4, 2, 3, 5, 14),
    (1, 1, 4, 4, 18),
    (1, 1, 4, 4, 19),
    (6, 1, 9, 9, 17),
    (1, 1, 4, 4, 18),
    (2, 2, 5, 3, 19),
    (1, 1, 4, 4, 20),
    (4, 2, 3, 5, 31),
    (1, 1, 4, 4, 32),
    (1, 1, 4, 4, 33),
    (6, 1, 9, 9, 37),
    (1, 1, 4, 4, 38),
    (2, 2, 5, 3, 39),
    (1, 1, 4, 4, 40),
    (4, 2, 3, 5, 48),
    (1, 1, 4, 4, 49),
    (1, 1, 4, 4, 53),
    (6, 1, 9, 9, 54),
    (1, 1, 4, 4, 55),
    (2, 2, 5, 3, 57),
    (1, 1, 4, 4, 58),
    (4, 2, 3, 5, 59),
    (1, 1, 4, 4, 64),
    (1, 1, 4, 4, 65),
    (6, 1, 9, 9, 66),
    (1, 1, 4, 4, 69),
    (2, 2, 5, 3, 70),
    (1, 1, 4, 4, 71),
    (4, 2, 3, 5, 74),
    (1, 1, 4, 4, 75),
    (1, 1, 4, 4, 76),
    (6, 1, 9, 9, 77),
    (1, 1, 4, 4, 82),
    (2, 2, 5, 3, 83),
    (1, 1, 4, 4, 84),
    (4, 2, 3, 5, 88),
    (1, 1, 4, 4, 89),
    (1, 1, 4, 4, 90),
    (6, 1, 9, 9, 94),
    (1, 1, 4, 4, 95),
    (2, 2, 5, 3, 96),
    (1, 1, 4, 4, 100),
    (4, 2, 3, 5, 101),
    (1, 1, 4, 4, 102),
    (1, 1, 4, 4, 103),
    (6, 1, 9, 9, 104),
    (1, 1, 4, 4, 111),
    (2, 2, 5, 3, 112),
    (1, 1, 4, 4, 113),
    (4, 2, 3, 5, 117),
    (1, 1, 4, 4, 118),
    (1, 1, 4, 4, 119),
    (6, 2, 6, 3, 120);