CREATE TABLE groups(
  id integer PRIMARY key AUTOINCREMENT,
  name integer
);

CREATE TABLE student(
  id integer PRIMARY key AUTOINCREMENT,
  name text not null,
  group_id integer,
  FOREIGN key (group_id) REFERENCES groups(id)
);

CREATE TABLE grades(
  id integer PRIMARY KEY,
  grade integer,
  student_id integer,
  FOREIGN key (student_id) REFERENCES student(id)
  );
  
CREATE TABLE teachers(
  id integer PRIMARY key,
  name text NOT null
  );
  
CREATE TABLE subjects(
  id integer PRIMARY key,
  name text not null,
  teacher_id integer,
  FOREIGN key (teacher_id) REFERENCES teachers(id)
  );
  
CREATE TABLE exam_date(
  id integer PRIMARY key,
  date integer,
  subject_id integer,
  FOREIGN key (subject_id) REFERENCES subjects(id)
  );