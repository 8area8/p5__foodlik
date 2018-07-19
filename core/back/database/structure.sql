CREATE TABLE category (
    title VARCHAR (80) PRIMARY KEY,
    product_number INT DEFAULT 0
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


CREATE TABLE substitute
(
    product_title VARCHAR (80),
    PRIMARY KEY (product_title),
    FOREIGN KEY (product_title) REFERENCES product(title) ON DELETE CASCADE
);


CREATE TABLE product_per_substitute
(
    substitute_title VARCHAR(80),
    product_title VARCHAR (80),
    PRIMARY KEY (substitute_title, product_title),
    FOREIGN KEY (substitute_title) REFERENCES substitute(product_title) ON DELETE CASCADE,
    FOREIGN KEY (product_title) REFERENCES product(title) ON DELETE CASCADE
);