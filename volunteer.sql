CREATE TABLE volunteer_info (
user_id CHARACTER(36) NOT NULL,
first_name varchar(255) NOT NULL,
last_name varchar(255) DEFAULT NULL,
cyf_city varchar(255) NOT NULL,
email varchar(255) NOT NULL,
phone_number integer DEFAULT NULL,
experience varchar(255) DEFAULT NULL,
weekend_availability BOOLEAN NOT NULL DEFAULT FALSE,
current_volunteer BOOLEAN NOT NULL DEFAULT FALSE,
PRIMARY KEY (user_id));

CREATE TABLE volunteer_technical_skill (
user_id CHARACTER(36) NOT NULL,
skill_type varchar(255) NOT NULL,
level integer DEFAULT 0,
FOREIGN KEY (user_id) REFERENCES volunteer_info(user_id));