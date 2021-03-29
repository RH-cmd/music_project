DROP TABLE IF EXISTS data_cleaned;
DROP TABLE IF EXISTS corr_heatmap_vals;
DROP TABLE IF EXISTS year_table;

Create table data_cleaned (
"title" VARCHAR NOT NULL,
"artist" VARCHAR NOT NULL,
"genre" VARCHAR NOT NULL,
"genre_num" INT NOT NULL,
"subgenre" VARCHAR NOT NULL,
"year" INT NOT NULL,
"bpm" NUMERIC NOT NULL,
"nrgy" NUMERIC NOT NULL,
"dnce" NUMERIC NOT NULL,
"dB" NUMERIC NOT NULL,
"live" NUMERIC NOT NULL,
"val" NUMERIC NOT NULL,
"dur" NUMERIC NOT NULL,
"acous" NUMERIC NOT NULL,
"spch" NUMERIC NOT NULL,
"pop" NUMERIC NOT NULL);

create table corr_heatmap_vals (
"feat1" VARCHAR NOT NULL,
"feat2" VARCHAR NOT NULL,
"val" NUMERIC NOT NULL);

create table year_table (
"year" INT NOT NULL,
"nrgy" INT NOT NULL,
"dnce" INT NOT NULL,
"val" INT NOT NULL,
"pop" INT NOT NULL);