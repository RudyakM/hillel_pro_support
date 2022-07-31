1. Social Network
https://www.hackerdraw.com/docs/3ec3d8c4-9563-4b44-8f7e-325a88b643e1
###
```
Table user {
  id integer
  role integer
  first_name varchar
  last_name varchar
  mobile varchar
  email varchar
  username varchar
  password varchar
}

Table roles {
    id integer
    name varchar
    created_at timestamp
    updated_at timestamp

}

Table profiles {
    id integer
    profile_bio text
    registered_at timestamp
    last_login timestamp
    created_at timestamp
    updated_at timestamp
}

Table likes {
    id integer
    user_id integer
    history integer
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

Table post {
    id integer
    text text
    created_at timestamp
    updated_at timestamp
}

Ref: user.role > roles.id
Ref: roles.name > user.id
Ref: profiles.id > user.id
Ref: comments.user_id > user.id
Ref: comments.history > comments.id
Ref: post.id > profiles.id
Ref: likes.history > likes.id
Ref: likes.id > post.id
Ref: likes.user_id > user.id
Ref: comments.id > post.id
```

Car services
https://www.hackerdraw.com/docs/1c705552-c9a7-480f-8915-a9bfe065d706

```
Table client {
  id integer
  car_name integer
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
  input_date timestamp
  output_date timestamp
}

Table car {
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
  quantity integer
  created_at timestamp
  updated_at timestamp
}

Ref: visit.client_id > client.id
Ref: visit.service_id > client.id
Ref: services.id > visit.service_id
Ref: car.name > client.car_name
```
