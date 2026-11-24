--Task1&2

CREATE TABLE epa_ghg_1990s (
    ROWNUMBER int,
    ECON_SECTOR varchar,
    ECON_SOURCE varchar,
    SECTOR varchar,
    SUBSECTOR varchar,
    CATEGORY varchar,
    FUEL varchar,
    SUBCATEGORY1 varchar,
    SUBCATEGORY2 varchar,
    SUBCATEGORY3 varchar,
    SUBCATEGORY4 varchar,
    STATE varchar,
    GHG varchar,
    Y1990 double precision,
    Y1991 double precision,
    Y1992 double precision,
    Y1993 double precision,
    Y1994 double precision,
    Y1995 double precision,
    Y1996 double precision,
    Y1997 double precision,
    Y1998 double precision,
    Y1999 double precision
);

CREATE TABLE epa_ghg_2000s (
    ROWNUMBER int,
    ECON_SECTOR varchar,
    ECON_SOURCE varchar,
    SECTOR varchar,
    SUBSECTOR varchar,
    CATEGORY varchar,
    FUEL varchar,
    SUBCATEGORY1 varchar,
    SUBCATEGORY2 varchar,
    SUBCATEGORY3 varchar,
    SUBCATEGORY4 varchar,
    STATE varchar,
    GHG varchar,
    Y2000 double precision,
    Y2001 double precision,
    Y2002 double precision,
    Y2003 double precision,
    Y2004 double precision,
    Y2005 double precision,
    Y2006 double precision,
    Y2007 double precision,
    Y2008 double precision,
    Y2009 double precision,
    Y2010 double precision,
    Y2011 double precision,
    Y2012 double precision,
    Y2013 double precision,
    Y2014 double precision,
    Y2015 double precision,
    Y2016 double precision,
    Y2017 double precision,
    Y2018 double precision,
    Y2019 double precision,
    Y2020 double precision
);


-- Download the csvs, put this into the PSQL tool, and change the paths to your own

\copy epa_ghg_1990s FROM '/Users/lexiluong/Documents/ENVS 5726 Fundamentals of Data for Env Studies/Week 11/EPA_GHG_By_Industry_1990s.csv' DELIMITER ',' CSV HEADER
\copy epa_ghg_2000s FROM '/Users/lexiluong/Documents/ENVS 5726 Fundamentals of Data for Env Studies/Week 11/EPA_GHG_By_Industry_2000s.csv' DELIMITER ',' CSV HEADER

--Task3
-- Join the 1990s and 2000s EPA GHG tables using their shared ROWNUMBER.
-- "a" = epa_ghg_1990s, and "b" = epa_ghg_2000s.

CREATE TABLE epa_ghg AS
SELECT
    a.*,
    b.Y2000,
    b.Y2001,
    b.Y2002,
    b.Y2003,
    b.Y2004,
    b.Y2005,
    b.Y2006,
    b.Y2007,
    b.Y2008,
    b.Y2009,
    b.Y2010,
    b.Y2011,
    b.Y2012,
    b.Y2013,
    b.Y2014,
    b.Y2015,
    b.Y2016,
    b.Y2017,
    b.Y2018,
    b.Y2019,
    b.Y2020
FROM epa_ghg_1990s AS a
INNER JOIN epa_ghg_2000s AS b
    ON a.ROWNUMBER = b.ROWNUMBER;

-- check if the join was successful
SELECT *
FROM epa_ghg
LIMIT 10;

--Task4
-- Add a new double precision column to store the mean GHG value and calculate the mean
ALTER TABLE epa_ghg
ADD COLUMN mean_ghg_1990_to_2020 double precision;

UPDATE epa_ghg
SET mean_ghg_1990_to_2020 = (
    Y1990 + Y1991 + Y1992 + Y1993 + Y1994
    + Y1995 + Y1996 + Y1997 + Y1998 + Y1999
    + Y2000 + Y2001 + Y2002 + Y2003 + Y2004
    + Y2005 + Y2006 + Y2007 + Y2008 + Y2009
    + Y2010 + Y2011 + Y2012 + Y2013 + Y2014
    + Y2015 + Y2016 + Y2017 + Y2018 + Y2019
    + Y2020
) / 31.0;

-- check if the added column and mean calculation was successful
SELECT
    ROWNUMBER,
    Y1990,
    Y2020,
    mean_ghg_1990_to_2020
FROM epa_ghg
LIMIT 10;