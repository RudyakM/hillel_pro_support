1. Social Network
https://www.hackerdraw.com/docs/3ec3d8c4-9563-4b44-8f7e-325a88b643e1
###
```
Table user {
  id integer
  role integer
  first_name varchar
  last_name varchar
  username varchar
  mobile varchar
  email varchar
  password varchar
  profile_bio text
  registered_at timestamp
  last_login timestamp
}

Table roles {
    id integer
    name varchar
    created_at timestamp
    updated_at timestamp

}

Table profiles {
    id integer
    created_at timestamp
    updated_at timestamp
}

Table likes {
    id integer
    user_id integer
    number integer
    created_at timestamp
    updated_at timestamp
}

Table comments {
    id integer
    user_id integer
    text text
    history integer
    created_at timestamp
    updated_at timestamp
}

Ref: user.role > roles.id
Ref: roles.name > user.id
Ref: profiles.id > user.id
Ref: comments.user_id > user.id
Ref: likes.user_id > user.id
Ref: likes.number > likes.id
Ref: comments.history > comments.id
```

Car services
https://www.hackerdraw.com/docs/1c705552-c9a7-480f-8915-a9bfe065d706

```
Table client {
  id integer
  role integer
  last_name varchar
  first_name varchar
  adress_id varchar
  created_at timestamp
  updated_at timestamp
}

Table visit {
  id integer
  client_id integer
  service_id integer
  quantity integer
  input_date timestamp
  output_date timestamp
}

Table role {
  id integer
  name varchar
  created_at timestamp
  updated_at timestamp
}

Table services {
  id integer
  name varchar
  description text
  price integer
  created_at timestamp
  updated_at timestamp
}

Ref: visit.client_id > client.id
Ref: role.id > client.role
Ref: visit.service_id > client.id
Ref: services.id > visit.service_id
```
