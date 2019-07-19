DROP TABLE parcels;
CREATE TABLE parcels (
parcel_id           varchar,
parcel_address      varchar,
city                varchar,
owner_name          varchar,
owner_address       varchar,
property_class      varchar,
school_district     varchar,
parcel_size         decimal,
grid_coord_east     integer,
grid_coord_north    integer,
deed_book           varchar,
market_value        integer,
county_tax          integer,
city_tax            integer,
school_tax          integer,
year_built          integer
);
.separator "\t"
.import parsed.tsv parcels
