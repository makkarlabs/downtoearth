--SQLs

-- Stores

insert into store(store_name, store_url, store_address, store_location, store_photo_url, store_online) values ('McDonalds', 'http://www.mcdonalds.com/', 'InOrbit Mall', 'Hyderabad, India', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/McDonald%27s_Golden_Arches.svg/200px-McDonald%27s_Golden_Arches.svg.png',0);

insert into store(store_name, store_url, store_address, store_location, store_photo_url, store_online) values ('Dominos Pizza', 'http://www.dominos.co.in/', 'Gachibowli', 'Hyderabad, India', 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Domino_pizza_logo.svg/200px-Domino_pizza_logo.svg.png',1);


-- Items

insert into item(store_id, item_name, item_photo_url, item_price) values("1", "Veg Nuggets", "", "60 INR");
insert into item(store_id, item_name, item_photo_url, item_price) values("1", "French Fries", "", "50 INR");
insert into item(store_id, item_name, item_photo_url, item_price) values("1", "McVeggie", "", "25 INR");
insert into item(store_id, item_name, item_photo_url, item_price) values("1", "McFlurry Oreo", "", "60 INR");

insert into item(store_id, item_name, item_photo_url, item_price) values("2", "Veg Doubles", "", "180 INR");
insert into item(store_id, item_name, item_photo_url, item_price) values("2", "Cheese Burst Pizza", "", "120 INR");
insert into item(store_id, item_name, item_photo_url, item_price) values("2", "Peppy Paneer", "", "130 INR");