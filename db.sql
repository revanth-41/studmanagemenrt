-- insert into management_app_admin(email,password)
-- values('rev@gmail.com','revi@1234');


-- use db.sqlite;

-- DELETE FROM management_app_blogpost;
-- DELETE FROM management_app_userprofile;

DELETE FROM student_management_app_user;

INSERT INTO student_management_app_access(user_id_id,access)
VALUES(5,1),(6,1);

UPDATE student_management_app_blogpost set status=0 where id=1;