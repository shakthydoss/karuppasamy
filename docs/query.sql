use karuppasamy;

drop table app;
drop table secret;
drop table usr_token;

create table app(
app_id int AUTO_INCREMENT,
name varchar(40) not null,
description varchar(255),
updated_date timestamp default current_timestamp,
UNIQUE(name),
primary key (app_id)
);

create table secret(
uid varchar(40) not null,
username varchar(40) not null,
email varchar(255) null default null,
password_enc varchar(40) not null,
is_active char(1) default 'y',
updated_by varchar(20) not null,
updated_date timestamp default current_timestamp,
UNIQUE(username),
primary key (uid)
);

create table usr_token(
id int AUTO_INCREMENT,
uid varchar(40) not null,
token varchar(128) not null,
updated_date timestamp default current_timestamp,
UNIQUE(uid),
primary key (id)
);


# Adding default app
insert into app(app_id,name,description) values ('1','bhoomi','bhoomi application');

# Adding default secret
insert into secret (uid,username,password_enc,updated_by) values ('1','admin','Reset123', 'system');


