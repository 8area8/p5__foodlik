CREATE TABLE category (
    title VARCHAR (80) PRIMARY KEY
);


CREATE TABLE product (
    title           VARCHAR (150) PRIMARY KEY,
    description     VARCHAR (1000),
    stores          VARCHAR (300),
    site_url        VARCHAR (200),
    score           SMALLINT
);


CREATE TABLE category_per_product (
    category_title  VARCHAR (80),
    product_title   VARCHAR (150),
    PRIMARY KEY (category_title, product_title),
    FOREIGN KEY (category_title) REFERENCES category(title) ON DELETE CASCADE,
    FOREIGN KEY (product_title) REFERENCES product(title) ON DELETE CASCADE
);
