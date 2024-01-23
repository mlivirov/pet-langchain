create or replace table vehicle_owner_data(
    pii int,
    name varchar(255),
    address varchar(255),
    city varchar(64),
    state varchar(2),
    zip varchar(8),
    vin varchar(255),
    model varchar(255),
    make varchar(255),
    year smallint
) engine MergeTree order by (name, address, city, state, zip, model, make)