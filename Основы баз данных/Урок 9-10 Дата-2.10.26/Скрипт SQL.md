CREATE TABLE users_videos(
  id integer PRIMARY key AUTOINCREMENT
);


CREATE TABLE Users (
  id integer PRIMARY key AUTOINCREMENT,
  user_vidios_id integer,
  FOREIGN key (user_vidios_id) REFERENCES user_vidios(id)
);


CREATE TABLE vidios(
  id PRIMARY key AUTOINCREMENT ,
  users_videos_id integer,
  
  FOREIGN key (users_videos_id) REFERENCES users_videos(id)
);


CREATE TABLE watch_histor(
  id integer PRIMARY key AUTOINCREMENT,
  users_videos_id integer,
  FOREIGN key (users_videos_id) REFERENCES users_videos(id)
);


CREATE TABLE analytics_videos(
  id integer PRIMARY key AUTOINCREMENT,
  videos_id integer,
  FOREIGN KEY (videos_id) REFERENCES vidios(id)
);

CREATE TABLE likes_video(
  id integer PRIMARY key AUTOINCREMENT,
  User_id integer not NULL,
  videos_id integer not null,
  FOREIGN key(video_id) REFERENCES videos_id,
  FOREIGN key(Users_id) REFERENCES Users_id
);


CREATE TABLE comments(
  id integer PRIMARY key AUTOINCREMENT,
  videos_id integer, Users_id integer,
  content Text NOT NULL,
  FOREIGN KEY (videos_id) REFERENCES videod(id),
  FOREIGN key (Users_id) REFERENCES Users(id)
);

CREATE TABLE categories(
  id integer PRIMARY key AUTOINCREMENT,
  name varchar(100) NOT NULL UNIQUE,
  FOREIGN key (videos_id) REFERENCES videos(id)
  );

  
  CREATE TABLE playlists(
    id integer PRIMARY key AUTOINCREMENT,
    user_id integer
    FOREIGN key (user_id) REFERENCES user(id)
   );
   
CREATE TABLE department(
  id integer PRIMARY key AUTOINCREMENT
 );
 
 CREATE TABLE moderators(
   id integer PRIMARY key AUTOINCREMENT,
   video_id integer,
   FOREIGN key (video_id) REFERENCES video(id)
);


CREATE TABLE user_notification(
  user_id PRIMARY key AUTOINCREMENT,
  FOREIGN key (user_id) REFERENCES user(id)
  )

CREATE TABLE user_notification(
  user_id PRIMARY key AUTOINCREMENT,
  FOREIGN key (user_id) REFERENCES user(id)
  )
  
CREATE TABLE user_subscribe(
    user_notification integer PRIMARY key AUTOINCREMENT,
    FOREIGN key (user_id) REFERENCES notification(id)
    );
    
CREATE TABLE chanale(
  id integer PRIMARY key AUTOINCREMENT
);

CREATE TABLE user_chanale(
  id integer PRIMARY key AUTOINCREMENT
);


