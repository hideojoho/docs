DROP TABLE IF EXISTS "papers" cascade;
CREATE TABLE "papers" (
    "id" SERIAL PRIMARY KEY,
    "title" varchar,
    "author" varchar,
    "citation_number" int
);