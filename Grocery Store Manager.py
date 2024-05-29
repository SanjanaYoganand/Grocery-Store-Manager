
'''Modules and tables used
Databases used:
1. Customer
2. Shops
3. Illness
4. INDCUST
5. Restocking
6. Payment_and_delivery
Tables used:
1. Customer:
1.1 Customers
2. Shops:
2.1 Grandmarket
2.2 Freshorigin
2.3 Crystalmart
2.4 Budgetfoods
2.5 Smartmart
2.6 Freshmakers
3. Illness:
3.1 Diabetes
3.2 Obesity
3.3 Eczema
3.4 Glucose_intolerance
3.5 Peanut_allergy
4. INDCUST:
Tables of all the customers individually to store pre-orders
5. Restocking:
5.1 Restocking
6. Payment_and_delivery:
6.1 Delivery 
Modules used:
1. Mysql.connector:
3
 To use the facilities of mysql databases and tables.
2. Threading:
 To access timers to enable timely restocking of products.
3. Datetime:
 To keep track of time.
4. Prettytable:
 To print grocery lists, shop lists and product lists in a 
picturesque manner.
4
User-built in functions used
1. createindcust(): 
 New customer for registration
2. restock():
 To restock after selling out
3. GETLIST():
4. getprevord():
5. getallcustdtails():
6. outofstk():
7. Healthissuemsg():
8. checkhealth():
9. Dayintervals():
 10. ordplace():
 11. restockdays():
 12. notavail():
 13. ALT():
 14. checkavail():
 15. payment():'''
 


import mysql.connector
con1=mysql.connector.connect(host='localhost',user='root',passwd='Sanj',databa
se='Customer')
cur1=con1.cursor()
con2=mysql.connector.connect(host='localhost',user='root',passwd='Sanj',databa
se='Shops')
cur2=con2.cursor()
con3=mysql.connector.connect(host='localhost',user='root',passwd='Sanj',databa
se='Illness')
cur3=con3.cursor()
con4=mysql.connector.connect(host='localhost',user='root',passwd='Sanj',databa
se='INDCUST')
cur4=con4.cursor()
con5=mysql.connector.connect(host='localhost',user='root',passwd='Sanj',databa
se='Restocking')
cur5=con5.cursor()
con6=mysql.connector.connect(host='localhost',user='root',passwd='Sanj',databa
se='Payment_and_delivery')
cur6=con6.cursor()
#Aparna,Customer database, con1
cur1.execute("create table Customers(custid int, custname char(30), Illness 
char(20), shoppref char(15), noofbuys int default(0))")
cur1.execute("insert into Customers 
values(1,'Harry','Glucose_intolerance','crystalmart',0))
cur1.execute("insert into Customers 
values(2,'Hermione','Glucose_intolerance','crystalmart',0)")
cur1.execute("insert into Customers 
values(3,'Ron','Peanut_allergy','freshorigin',0)")
cur1.execute("insert into Customers values(4,'Vernon','Obesity','freshorigin',0)")
cur1.execute("insert into Customers 
values(5,'Luna','Peanut_allergy','grandmarket',0)")
6
cur1.execute("insert into Customers 
values(6,'Rubeus','Diabetes','freshorigin',0)")
cur1.execute("insert into Customers 
values(7,'Albus','Diabetes','grandmarket',0)")
cur1.execute("insert into Customers 
values(8,'Dudely','Obesity','grandmarket',0)")
cur1.execute("insert into Customers 
values(9,'Fred','Peanut_allergy','crystalmart',0)")
cur1.execute("insert into Customers 
values(10,'Lucius','Diabetes','freshorigin',0)")
cur1.execute("insert into Customers 
values(11,'Lily','Glucose_intolerance','crystalmart',0)")
cur1.execute("insert into Customers 
values(12,'Nymphadora','Diabetes','freshorigin',0)")
cur1.execute("insert into Customers 
values(13,'James','Peanut_allergy','grandmarket',0)")
#SAAHITHI, Shops database, con2
#Table1, Grandmarket
cur2.execute('create table grandmarket(Sno int, ITEM_NAME 
varchar(25),QUANTITY int, PRICE int)')
cur2.execute("insert into Grandmarket values(1,'sweetbread',70,30)")
cur2.execute("insert into Grandmarket values(2,'cheese',30,200)")
cur2.execute("insert into Grandmarket values(3,'wheat flour',35,70)")
cur2.execute("insert into Grandmarket values(4,'sunfeast biscuits',45,10)")
cur2.execute("insert into Grandmarket values(5,'cakes',55,100)")
cur2.execute("insert into Grandmarket values(6,'corn flour',40',110)")
cur2.execute("insert into Grandmarket values(7,'rice flour',50,75)")
cur2.execute("insert into Grandmarket values(8,'maida',50,80)")
cur2.execute("insert into Grandmarket values(9,'milk',60,20)")
cur2.execute("insert into Grandmarket values(10,'milk Bikkis',50,20)")
7
cur2.execute("insert into Grandmarket values(11,'vegan milk',25,70)")
cur2.execute("insert into Grandmarket values(12,'noodles',70,60)")
cur2.execute("insert into Grandmarket values(13,'maggi',50,40)")
cur2.execute("insert into Grandmarket values(14,'eggs',100,7)")
cur2.execute("insert into Grandmarket values(15,'butter',150,260)")
cur2.execute("insert into Grandmarket values(16,'yogurt box',100,60)")
cur2.execute("insert into Grandmarket values(17'soda',80,30)")
cur2.execute("insert into Grandmarket values(18,'cheddar cheese',170,300)")
cur2.execute("insert into Grandmarket values(19,'sandwich bread',80,60)")
cur2.execute("insert into Grandmarket values(20,'oatmeal',60,85)")
cur2.execute("insert into Grandmarket values(21,'breakfast bars',300,40)")
cur2.execute("insert into Grandmarket values(22,'packed snack',200,40)")
cur2.execute("insert into Grandmarket values(23,'peanut butter',60,180)")
cur2.execute("insert into Grandmarket values(24,'coffee powder',80,50)")
cur2.execute("insert into Grandmarket values(25,'tea powder',75,55)")
cur2.execute("insert into Grandmarket values(26,'sugar',800,45)")
cur2.execute("insert into Grandmarket values(27,'fruit juice',700,120)")
cur2.execute("insert into Grandmarket values(28,'salt',70,20)")
cur2.execute("insert into Grandmarket values(29,'cookies',250,50)")
cur2.execute("insert into Grandmarket values(30,'multigrain bread',200,80)")
cur2.execute("insert into Grandmarket values(31,'candy bars',200,10)")
cur2.execute("insert into Grandmarket values(32,'oil',50,300)")
cur2.execute("insert into Grandmarket values(33,'toor Dhal',65,140)")
cur2.execute("insert into Grandmarket values(34,'popsicles',750,30)")
cur2.execute("insert into Grandmarket values(35,'ice cream',100,45)")
cur2.execute("insert into Grandmarket values(36,'frozen pizza',90,75)")
cur2.execute("insert into Grandmarket values(37,'sausages',90,75)")
cur2.execute("insert into Grandmarket values(38,'batter',120,50)")
cur2.execute("insert into Grandmarket values(39,'cheescake mix',70,30)")
8
cur2.execute("insert into Grandmarket values(40,'cupcakes',50,40)")
cur2.execute("insert into Grandmarket values(41,'pasta',85,45)")
cur2.execute("insert into Grandmarket values(42,'bacon',850,30)")
cur2.execute("insert into Grandmarket values(43,'dog food',30,150)")
cur2.execute("insert into Grandmarket values(44,'cat food',30,150)")
cur2.execute("insert into Grandmarket values(45,'canned foods',30,65)")
cur2.execute("insert into Grandmarket values(46,'toothpaste',60,35)")
cur2.execute("insert into Grandmarket values(47,'dispossable cups',1000,15)")
cur2.execute("insert into Grandmarket values(48,'honey',90,45)")
cur2.execute("insert into Grandmarket values(49,'soap',600,45)")
cur2.execute("insert into Grandmarket values(50,'toothbrush',80,35)")
cur2.execute("insert into Grandmarket values(51,'tissues',1000,75)")
cur2.execute("insert into Grandmarket values(52,'chocolates',90,50)")
cur2.execute("insert into Grandmarket values(53,'brittania buiscuits',70,10)")
cur2.execute("insert into Grandmarket values(54,'chewing gum',80,15)")
cur2.execute("insert into Grandmarket values(55,'jam',100,65)")
cur2.execute("insert into Grandmarket values(56,'sauces',400,56)")
cur2.execute("insert into Grandmarket values(57,'shampoo',80,90)")
cur2.execute("insert into Grandmarket values(58,'sanitizer',300,40)")
cur2.execute("insert into Grandmarket values(59,'lipstick',100,45)")
cur2.execute("insert into Grandmarket values(60,'sunscreen',20,35)")
cur2.execute("insert into Grandmarket values(61,'vinegar',100,25)")
cur2.execute("insert into Grandmarket values(62,'processed meat',30,480)")
cur2.execute("insert into Grandmarket values(63,'battery(9V)',450,45)")
cur2.execute("insert into Grandmarket values(64,'vanilla essence',75,80)")
cur2.execute("insert into Grandmarket values(65,'fried chips',750,20)")
cur2.execute("insert into Grandmarket values(66,'fish',45,55)"
cur2.execute("insert into Grandmarket values(67,'pringles',75,45)")
cur2.execute("insert into Grandmarket values(68,'condensed milk',120,120)")
9
cur2.execute("insert into Grandmarket values(69,'soft drinks',80,35)")
cur2.execute("insert into Grandmarket values(70,'soya chunks',80,45)")
cur2.execute("insert into Grandmarket values(71,'nutella',30,320)")
cur2.execute("insert into Grandmarket values(72,'mayonnaise',30,50)")
cur2.execute("insert into Grandmarket values(73,'ghee',72,175)")
cur2.execute("insert into Grandmarket values(74,'neem Face wash',630,85)")
cur2.execute("insert into Grandmarket values(75,'boost',560,90)")
cur2.execute("insert into Grandmarket values(76,'wrapers',50,50)")
cur2.execute("insert into Grandmarket values(77,'wafers',36,50)")
cur2.execute("insert into Grandmarket values(78,'pickle',80,110)")
cur2.execute("insert into Grandmarket values(79,'sanitary napkins',70,200)")
cur2.execute("insert into Grandmarket values(80,'complan',70,150)"
cur2.execute("insert into Grandmarket values(81,'horlicks',36,150)")
cur2.execute("insert into Grandmarket values(82,'vermicelli',36,75)")
cur2.execute("insert into Grandmarket values(83,'bay leaf',40,45)")
cur2.execute("insert into Grandmarket values(84,'red peppers',400,75)")
cur2.execute("insert into Grandmarket values(85,'veggie mix',400,100)")
cur2.execute("insert into Grandmarket values(86,'apples',30,250)")
cur2.execute("insert into Grandmarket values(87,'pulses',150,45)")
cur2.execute("insert into Grandmarket values(88,'aluminium foil',20,35)")
cur2.execute("insert into Grandmarket values(89,'paper plates',78,45)")
cur2.execute("insert into Grandmarket values(90,'garlic',20,45)")
cur2.execute("insert into Grandmarket values(91,'ziplock bag',180,25)")
cur2.execute("insert into Grandmarket values(92,'toothpicks',130,40)")
cur2.execute("insert into Grandmarket values(93,'body lotion',102,65)")
cur2.execute("insert into Grandmarket values(94,'conditioner',60,140)")
cur2.execute("insert into Grandmarket values(95,'dish wash soap',450,90)")
cur2.execute("insert into Grandmarket values(96,'mouth wash',65,90)")
cur2.execute("insert into Grandmarket values(97,'pencil',80,10)")
10
cur2.execute("insert into Grandmarket values(98,'moisturizer',100,55)")
cur2.execute("insert into Grandmarket values(99,'chilli sauce',73,65)")
cur2.execute("insert into Grandmarket values(100,'scrubs',45,45)")
#Table2, Freshorigin
cur2.execute('create table freshorigin(Sno int, ITEM_NAME 
varchar(25),QUANTITY int, PRICE int)')
cur2.execute("insert into Freshorigin values(1,'sweetbread',70,45)")
cur2.execute("insert into Freshorigin values(2,'cheese',30,150)")
cur2.execute("insert into Freshorigin values(3,'flour',35,55)")
cur2.execute("insert into Freshorigin values(4,'sunfeast biscuits',45,10)")
cur2.execute("insert into Freshorigin values(5,'cake mix',55,75)")
cur2.execute("insert into Freshorigin values(6,'corn flour',40,60)")
cur2.execute("insert into Freshorigin values(7,'rice flour',50,70)")
cur2.execute("insert into Freshorigin values(8,'maida',50,75)")
cur2.execute("insert into Freshorigin values(9,'milk',60,20)")
cur2.execute("insert into Freshorigin values(10,'A4 sheets',50,300)")
cur2.execute("insert into Freshorigin values(11,'vegan milk',25,75)")
cur2.execute("insert into Freshorigin values(12,'noodles',70,75)")
cur2.execute("insert into Freshorigin values(13,'maggi',50,78)")
cur2.execute("insert into Freshorigin values(14,'eggs',100,5)")
cur2.execute("insert into Freshorigin values(15,'butter',150,65)")
cur2.execute("insert into Freshorigin values(16,'yogurt box',100,75)")
cur2.execute("insert into Freshorigin values(17'soda',80,35)")
cur2.execute("insert into Freshorigin values(18,'cheddar cheese',170,200)")
cur2.execute("insert into Freshorigin values(19,'sandwich bread',80,55)")
cur2.execute("insert into Freshorigin values(20,'oatmeal',60,66)")
cur2.execute("insert into Freshorigin values(21,'breakfast bars',300,35)")
11
cur2.execute("insert into Freshorigin values(22,'snack cakes',200,40)")
cur2.execute("insert into Freshorigin values(23,'peanut butter',60,55)")
cur2.execute("insert into Freshorigin values(24,'coffee powder',80,55)")
cur2.execute("insert into Freshorigin values(25,'tea powder',75,55)")
cur2.execute("insert into Freshorigin values(26,'sugar',800,75)")
cur2.execute("insert into Freshorigin values(27,'fruit juices',700,65)")
cur2.execute("insert into Freshorigin values(28,'salt',70,45)")
cur2.execute("insert into Freshorigin values(29,'cookies',250,35)")
cur2.execute("insert into Freshorigin values(30,'multigrain bread',200,65)")
cur2.execute("insert into Freshorigin values(31,'candy bars',200,25)")
cur2.execute("insert into Freshorigin values(32,'oil',50,65)")
cur2.execute("insert into Freshorigin values(33,'hot dogs',65,35)")
cur2.execute("insert into Freshorigin values(34,'popsicles',750,15)")
cur2.execute("insert into Freshorigin values(35,'icecream',100,40)")
cur2.execute("insert into Freshorigin values(36,'frozen pizza',90,45)")
cur2.execute("insert into Freshorigin values(37,'sausages',90,45)")
cur2.execute("insert into Freshorigin values(38,'brocoli',120,45)")
cur2.execute("insert into Freshorigin values(39,'cheescake mix',70,70)")
cur2.execute("insert into Freshorigin values(40,'cupcakes',50,45)")
cur2.execute("insert into Freshorigin values(41,'macaroni pasta',85,65)")
cur2.execute("insert into Freshorigin values(42,'bacon',850,36)")
cur2.execute("insert into Freshorigin values(43,'dog food',30,150)")
cur2.execute("insert into Freshorigin values(44,'cat food',30,150)")
cur2.execute("insert into Freshorigin values(45,'canned chicken',30,110)")
cur2.execute("insert into Freshorigin values(46,'toothpastes',60,45)")
cur2.execute("insert into Freshorigin values(47,'dispossable cups',1000,45)")
cur2.execute("insert into Freshorigin values(48,'honey',90,110)")
cur2.execute("insert into Freshorigin values(49,'soaps',600,55)")
cur2.execute("insert into Freshorigin values(50,'toothbrush',80,25)")
12
cur2.execute("insert into Freshorigin values(51,'tissues',1000,45)")
cur2.execute("insert into Freshorigin values(52,'chocolates',90,15)")
cur2.execute("insert into Freshorigin values(53,'brittania buiscuits',70,5):")
cur2.execute("insert into Freshorigin values(54,'chewing gum',80,10)")
cur2.execute("insert into Freshorigin values(55,'jam',100,150)")
cur2.execute("insert into Freshorigin values(56,'sauces',400,79)")
cur2.execute("insert into Freshorigin values(57,'shampoo',80,115)")
cur2.execute("insert into Freshorigin values(58,'sanitizer',300,95)")
cur2.execute("insert into Freshorigin values(59,'chapstick',100,90)")
cur2.execute("insert into Freshorigin values(60,'sunscreen',20,45)")
cur2.execute("insert into Freshorigin values(61,'vinegar',100,45)")
cur2.execute("insert into Freshorigin values(62,'batter',30,55)")
cur2.execute("insert into Freshorigin values(63,'batteries(2V)',450,30)")
cur2.execute("insert into Freshorigin values(64,'seasonings',75,55)")
cur2.execute("insert into Freshorigin values(65,'chips',750,10)")
cur2.execute("insert into Freshorigin values(66,'spices',45,65)")
cur2.execute("insert into Freshorigin values(67,'pringles',75,35)")
cur2.execute("insert into Freshorigin values(68,'condensed milk',120,45)")
cur2.execute("insert into Freshorigin values(69,'soft drinks',80,35)")
cur2.execute("insert into Freshorigin values(70,'soya chunks',80,35)")
cur2.execute("insert into Freshorigin values(71,'nutella',30,180)")
cur2.execute("insert into Freshorigin values(72,'mayonnaise',30,)")
cur2.execute("insert into Freshorigin values(73,'ghee',72,150)")
cur2.execute("insert into Freshorigin values(74,'face wash',630,55)")
cur2.execute("insert into Freshorigin values(75,'boost',560,90)")
cur2.execute("insert into Freshorigin values(76,'wrapers',50,45)")
cur2.execute("insert into Freshorigin values(77,'wafers',36,45)")
cur2.execute("insert into Freshorigin values(78,'pickle',80,75)")
cur2.execute("insert into Freshorigin values(79,'sanitary napkins',70,135)")
13
cur2.execute("insert into Freshorigin values(80,'complan',70,90)")
cur2.execute("insert into Freshorigin values(81,'horlicks',36,90)")
cur2.execute("insert into Freshorigin values(82,'vermicelli',36,55)")
cur2.execute("insert into Freshorigin values(83,'bay leaf',40,55)")
cur2.execute("insert into Freshorigin values(84,'red pepper',400,250)")
cur2.execute("insert into Freshorigin values(85,'veggie mix',400,75)")
cur2.execute("insert into Freshorigin values(86,'Kiwi',30,150)")
cur2.execute("insert into Freshorigin values(87,'pulse mix',150,75)")
cur2.execute("insert into Freshorigin values(88,'aluminium foil',20,35)")
cur2.execute("insert into Freshorigin values(89,'paper plates',78,45)")
cur2.execute("insert into Freshorigin values(90,'garlic',20,45)")
cur2.execute("insert into Freshorigin values(91,'ziplock bag',180,45)")
cur2.execute("insert into Freshorigin values(92,'toothpicks',130,30)")
cur2.execute("insert into Freshorigin values(93,'body lotion',102,55)")
cur2.execute("insert into Freshorigin values(94,'conditioner',60,88)")
cur2.execute("insert into Freshorigin values(95,'dish wash soap',450,66)")
cur2.execute("insert into Freshorigin values(96,'mouth wash',65,45)")
cur2.execute("insert into Freshorigin values(97,'eraser',80,15)")
cur2.execute("insert into Freshorigin values(98,'moisturizer',100,55)")
cur2.execute("insert into Freshorigin values(99,'chilli sauce',73,60)")
cur2.execute("insert into Freshorigin values(100,'scrubs',45,55)")
#Table 3, crystalmart
cur2.execute("create table crystalmart(Sno int, ITEM_NAME 
varchar(25),QUANTITY int, PRICE int)")
cur2.execute("insert into crystalmart values(1,'sweetbread',30,45)")
cur2.execute("insert into crystalmart values(2,'corn flour',40,45)")
cur2.execute("insert into crystalmart values(3,'rice flour',50,45)")
14
cur2.execute("insert into crystalmart values(4,'cake mix',45,65)")
cur2.execute("insert into crystalmart values(5,'sunfeast biscuits',45,10)")
cur2.execute("insert into crystalmart values(6,'maida',50,45)")
cur2.execute("insert into crystalmart values(7,'milk',60,25)")
cur2.execute("insert into crystalmart values(8,'vegan milk',20,47)")
cur2.execute("insert into crystalmart values(9,'noodles',70,67)")
cur2.execute("insert into crystalmart values(10,'maggi',50,55)")
cur2.execute("insert into crystalmart values(11,'eggs',100,5)")
cur2.execute("insert into crystalmart values(12,'cheese',150,110)")
cur2.execute("insert into crystalmart values(13,'yogurt box',170,77)")
cur2.execute("insert into crystalmart values(14,'soda',80,30)")
cur2.execute("insert into crystalmart values(15,'sandwich bread',80,55)")
cur2.execute("insert into crystalmart values(16,'oatmeal',60,56)")
cur2.execute("insert into crystalmart values(17,'cedar cheese',170,170)")
cur2.execute("insert into crystalmart values(18,'multigrain bread',200,55)")
cur2.execute("insert into crystalmart values(19,'candy bars',200,15)")
cur2.execute("insert into crystalmart values(20,'snack cakes',200,55)")
cur2.execute("insert into crystalmart values(21,'cookies',250,30)")
cur2.execute("insert into crystalmart values(22,'breakfast bars',300,25)")
cur2.execute("insert into crystalmart values(23,'oil',500,78)")
cur2.execute("insert into crystalmart values(24,'sugar',800,77)")
cur2.execute("insert into crystalmart values(25,'salt',700,65)")
cur2.execute("insert into crystalmart values(26,'coffee powder',800,45)")
cur2.execute("insert into crystalmart values(27,'tea powder',700,45)")
cur2.execute("insert into crystalmart values(28,'fruit juices',700,55)")
cur2.execute("insert into crystalmart values(29,'peanut butter',600,75)")
cur2.execute("insert into crystalmart values(30,'hot dogs',650,67)")
cur2.execute("insert into crystalmart values(31,'cheescake mix',750,80)")
cur2.execute("insert into crystalmart values(32,'popsicles',750,15)")
15
cur2.execute("insert into crystalmart values(33,'icecream',1000,60)")
cur2.execute("insert into crystalmart values(34,'frozen pizza',900,75)")
cur2.execute("insert into crystalmart values(35,'sausages',900,75)")
cur2.execute("insert into crystalmart values(36,'butter',1200,75)")
cur2.execute("insert into crystalmart values(37,'macaroni pasta',850,90)")
cur2.execute("insert into crystalmart values(38,'bacon',850,35)")
cur2.execute("insert into crystalmart values(39,'cupcakes',500,40)")
cur2.execute("insert into crystalmart values(40,'dog food',300,155)")
cur2.execute("insert into crystalmart values(41,'cat food',300,145)")
cur2.execute("insert into crystalmart values(42,'canned chicken',300,180)")
cur2.execute("insert into crystalmart values(43,'toothpastes',600,45)")
cur2.execute("insert into crystalmart values(44,'soaps',600,55)")
cur2.execute("insert into crystalmart values(45,'toothbrush',800,25)")
cur2.execute("insert into crystalmart values(46,'tissues',1000,55)")
cur2.execute("insert into crystalmart values(47,'dispossable cups',1000,12)")
cur2.execute("insert into crystalmart values(48,'flour',1300,55)")
cur2.execute("insert into crystalmart values(49,'honey',900,75)")
cur2.execute("insert into crystalmart values(50,'chocolates',900,15)")
cur2.execute("insert into crystalmart values(51,'brittania buiscuits',700,10)")
cur2.execute("insert into crystalmart values(52,'chewing gum',800,15)")
cur2.execute("insert into crystalmart values(53,'shampoo',800,65)")
cur2.execute("insert into crystalmart values(54,'sauces',400,45)")
cur2.execute("insert into crystalmart values(55,'jam',1000,55)")
cur2.execute("insert into crystalmart values(56,'sunscreen',200,40)")
cur2.execute("insert into crystalmart values(57,'mascara',100,44)")
cur2.execute("insert into crystalmart values(58,'vinegar',100,44)")
cur2.execute("insert into crystalmart values(59,'sanitizer',300,75)")
cur2.execute("insert into crystalmart values(60,'batter',300,55)")
cur2.execute("insert into crystalmart values(61,'batteries(2V)',450,29)")
16
cur2.execute("insert into crystalmart values(62,'spices',450,45)")
cur2.execute("insert into crystalmart values(63,'seasonings',75,55)")
cur2.execute("insert into crystalmart values(64,'chips',750,15)")
cur2.execute("insert into crystalmart values(65,'pringles',750,25)")
cur2.execute("insert into crystalmart values(66,'soft drinks',800,35)")
cur2.execute("insert into crystalmart values(67,'soya chunks',800,35)")
cur2.execute("insert into crystalmart values(68,'condensed milk',1200,45)")
cur2.execute("insert into crystalmart values(69,'nutella',300.325)")
cur2.execute("insert into crystalmart values(70,'mayonnaise',300,45)")
cur2.execute("insert into crystalmart values(71,'chilli sauce',730,55)")
cur2.execute("insert into crystalmart values(72,'ghee',720,180)")
cur2.execute("insert into crystalmart values(73,'dish wash soap',450,55)")
cur2.execute("insert into crystalmart values(74,'scrubs',450,45)")
cur2.execute("insert into crystalmart values(75,'conditioner',600,76)")
cur2.execute("insert into crystalmart values(76,'face wash',630,47)")
cur2.execute("insert into crystalmart values(77,'mouth wash',650,46)")
cur2.execute("insert into crystalmart values(78,'razor',650,25)")
cur2.execute("insert into crystalmart values(79,'scissor',800,30)")
cur2.execute("insert into crystalmart values(80,'ear buds',200,45)")
cur2.execute("insert into crystalmart values(81,'moisturizer',1000,45)")
cur2.execute("insert into crystalmart values(82,'body lotion',1200,47)")
cur2.execute("insert into crystalmart values(83,'toothpicks',1300,30)")
cur2.execute("insert into crystalmart values(84,'ziplock bag',180,30)")
cur2.execute("insert into crystalmart values(85,'paper plates',25)")
cur2.execute("insert into crystalmart values(86,'aluminium foil',200,25)")
cur2.execute("insert into crystalmart values(87,'garlic',200,45)")
cur2.execute("insert into crystalmart values(88,'pulses',150,67)")
cur2.execute("insert into crystalmart values(89,'strawberries',300,180)")
cur2.execute("insert into crystalmart values(90,'veggie mix',400,89)")
17
cur2.execute("insert into crystalmart values(91,'pepper',400,78")
cur2.execute("insert into crystalmart values(92,'bay leaf',400,77)")
cur2.execute("insert into crystalmart values(93,'vermicelli',360,67)")
cur2.execute("insert into crystalmart values(94,'horlicks',360,90)")
cur2.execute("insert into crystalmart values(95,'boost',560,95)")
cur2.execute("insert into crystalmart values(96,'complan',700,93)")
cur2.execute("insert into crystalmart values(97,'sanitary napkins',700,140)")
cur2.execute("insert into crystalmart values(98,'pickle',800,65)")
cur2.execute("insert into crystalmart values(99,'wafers',360,43)")
cur2.execute("insert into crystalmart values(100,'wrapers',500,45)")
#divya-table-1
#-------------
cur2.execute("create table budgetfoods(Sno int, ITEM_NAME 
varchar(25),QUANTITY int, PRICE int);")
cur2.execute("insert into budgetfoods values(1,'white bread',30, 30);")
cur2.execute("insert into budgetfoods values(2,'brown bread', 40, 35);")
cur2.execute("insert into budgetfoods values(3,'curd', 65, 20);")
cur2.execute("insert into budgetfoods values(4,'flavored yogurt box', 40, 40);")
cur2.execute("insert into budgetfoods values(5,'rice packed 1 kg', 70, 65);")
cur2.execute("insert into budgetfoods values(6,'cheese 500gm', 400, 15);")
cur2.execute("insert into budgetfoods values(7,'cheddar cheese', 100, 90);")
cur2.execute("insert into budgetfoods values(8,'ramen hot', 70, 35);")
cur2.execute("insert into budgetfoods values(9,'ramen instant', 100, 25);")
cur2.execute("insert into budgetfoods values(10,'soy sauce', 40, 75);")
cur2.execute("insert into budgetfoods values(11,'chilli sauce', 50, 75);")
cur2.execute("insert into budgetfoods values(12,'soy sauce', 40, 75);")
cur2.execute("insert into budgetfoods values(13,'ketchup', 60, 55);")
cur2.execute("insert into budgetfoods values(14,'onions 1kg', 50, 40);")
18
cur2.execute("insert into budgetfoods values(15,'carrots 1kg', 60, 30);")
cur2.execute("insert into budgetfoods values(16,'chilli 1kg', 50, 30);")
cur2.execute("insert into budgetfoods values(17,'tomato 1kg', 40, 20);")
cur2.execute("insert into budgetfoods values(18,'radish 1kg', 35, 20);")
cur2.execute("insert into budgetfoods values(19,'milk', 35, 20);")
cur2.execute("insert into budgetfoods values(20,'hot sauce', 50, 30);")
cur2.execute("insert into budgetfoods values(21,'readymade chappati', 400, 
15);")
cur2.execute("insert into budgetfoods values(22,'dosa batter', 65, 20);")
cur2.execute("insert into budgetfoods values(23,'vinegar', 100, 90);")
cur2.execute("insert into budgetfoods values(24,'eggs', 40, 35);")
cur2.execute("insert into budgetfoods values(25,'soda', 100, 25);")
cur2.execute("insert into budgetfoods values(26,'vegetable oil', 60, 30);")
cur2.execute("insert into budgetfoods values(27,'sunflower oil', 60, 55);")
cur2.execute("insert into budgetfoods values(28,'chilli powder', 50, 75);")
cur2.execute("insert into budgetfoods values(29,'milk powder', 400, 15);")
cur2.execute("insert into budgetfoods values(30,'pepper whole', 35, 20);")
cur2.execute("insert into budgetfoods values(31,'pepper powder', 35, 20);")
cur2.execute("insert into budgetfoods values(32,'chocolate', 50, 75);")
cur2.execute("insert into budgetfoods values(33,'lemon', 35, 20);")
cur2.execute("insert into budgetfoods values(34,'milk maid', 65, 20);")
cur2.execute("insert into budgetfoods values(35,'white sugar', 50, 75);")
cur2.execute("insert into budgetfoods values(36,'biscuits', 50, 30);")
cur2.execute("insert into budgetfoods values(37,'cookies', 50, 75);")
cur2.execute("insert into budgetfoods values(38,'jam', 60, 55);")
cur2.execute("insert into budgetfoods values(39,'honey', 60, 55);")
cur2.execute("insert into budgetfoods values(40,'maple syrup', 50, 40);")
cur2.execute("insert into budgetfoods values(41,'salt', 50, 75);")
cur2.execute("insert into budgetfoods values(42,'turmeric powder', 35, 20);")
19
cur2.execute("insert into budgetfoods values(43,'rice', 35, 20);")
cur2.execute("insert into budgetfoods values(44,'sugar free', 50, 30);")
cur2.execute("insert into budgetfoods values(45,'spaghetti', 50, 30);")
cur2.execute("insert into budgetfoods values(46,'ricebran oil', 60, 55);")
cur2.execute("insert into budgetfoods values(47,'ladysfinger 1kg', 35, 20);")
cur2.execute("insert into budgetfoods values(48,'sambar powder', 40, 50);")
cur2.execute("insert into budgetfoods values(49,'garam masala powder', 400, 
15);")
cur2.execute("insert into budgetfoods values(50,'ink pen', 75, 50);")
cur2.execute("insert into budgetfoods values(51,'canned drinks', 400, 50);")
cur2.execute("insert into budgetfoods values(52,'mango drink', 150, 40);")
cur2.execute("insert into budgetfoods values(53,'apple juice', 100, 35);")
cur2.execute("insert into budgetfoods values(54,'pencil', 85, 25);")
cur2.execute("insert into budgetfoods values(55,'potato chips', 80, 30);")
cur2.execute("insert into budgetfoods values(56,'potato 1 kg', 40, 50);")
cur2.execute("insert into budgetfoods values(57,'cabbage 1 kg', 400, 75);")
cur2.execute("insert into budgetfoods values(58,'tapioca chips', 40, 90);")
cur2.execute("insert into budgetfoods values(59,'cleaning fluid', 400, 50);")
cur2.execute("insert into budgetfoods values(60,'milkshakes', 40, 75);")
cur2.execute("insert into budgetfoods values(61,'corn 1kg', 50, 40);")
cur2.execute("insert into budgetfoods values(62,'mixed nuts', 50, 75);")
cur2.execute("insert into budgetfoods values(63,'popcorn', 35, 20);")
cur2.execute("insert into budgetfoods values(64,'washing powder', 35, 20);")
cur2.execute("insert into budgetfoods values(65,'detergent', 50, 30);")
cur2.execute("insert into budgetfoods values(66,'washing soap', 50, 30);")
cur2.execute("insert into budgetfoods values(67,'body soap', 60, 55);")
cur2.execute("insert into budgetfoods values(68,'shampoo', 35, 20);")
cur2.execute("insert into budgetfoods values(69,'body wash', 40, 50);")
cur2.execute("insert into budgetfoods values(70,'candy', 400, 15);")
20
cur2.execute("insert into budgetfoods values(71,'lollipop', 75, 50);")
cur2.execute("insert into budgetfoods values(72,'mangoes 1kg', 400, 50);")
cur2.execute("insert into budgetfoods values(73,'apples 1kg', 150, 40);")
cur2.execute("insert into budgetfoods values(74,'pineapples 1kg', 100, 35);")
cur2.execute("insert into budgetfoods values(75,'custard apples 1kg', 85, 25);")
cur2.execute("insert into budgetfoods values(76,'bananas 1kg', 80, 30);")
cur2.execute("insert into budgetfoods values(77,'cauliflower 1kg', 40, 50);")
cur2.execute("insert into budgetfoods values(78,'crystal salt', 400, 75);")
cur2.execute("insert into budgetfoods values(79,'himalayan salt', 20, 69);")
cur2.execute("insert into budgetfoods values(80,'crystal sugar', 400, 50);")
cur2.execute("insert into budgetfoods values(81,'powdered sugar', 40, 75);")
cur2.execute("insert into budgetfoods values(82,'custard mix', 40, 75);")
cur2.execute("insert into budgetfoods values(83,'heat flour', 50, 40);")
cur2.execute("insert into budgetfoods values(84,'aida', 50, 75);")
cur2.execute("insert into budgetfoods values(85,'rice flour', 35, 20);")
cur2.execute("insert into budgetfoods values(86,'corn flour', 35, 20);")
cur2.execute("insert into budgetfoods values(87,'jeera powder', 50, 30);")
cur2.execute("insert into budgetfoods values(88,'washing soap', 50, 30);")
cur2.execute("insert into budgetfoods values(89,'body soap', 60, 55);")
cur2.execute("insert into budgetfoods values(90,'shampoo', 35, 20);")
cur2.execute("insert into budgetfoods values(91,'body wash', 40, 50);")
cur2.execute("insert into budgetfoods values(92,'candy', 400, 15);")
cur2.execute("insert into budgetfoods values(93,'lollipop', 75, 50);")
cur2.execute("insert into budgetfoods values(94,'mangoes 1kg', 400, 50);")
cur2.execute("insert into budgetfoods values(95,'apples 1kg', 150, 40);")
cur2.execute("insert into budgetfoods values(96,'pineapples 1kg', 100, 35);")
cur2.execute("insert into budgetfoods values(97,'custard apples 1kg', 85, 25);")
cur2.execute("insert into budgetfoods values(98,'bananas 1kg', 80, 30);")
cur2.execute("insert into budgetfoods values(99,'cauliflower 1kg', 40, 50);")
21
cur2.execute("insert into budgetfoods values(100'crystal salt', 400, 75);")
#divya-table-2
#--------------
cur2.execute("create table smartmart(Sno int, ITEM_NAME 
varchar(25),QUANTITY int, PRICE int);")
cur2.execute("insert into smartmart values(1,'white bread',30, 25);")
cur2.execute("insert into smartmart values(2,'brown bread', 40, 30);")
cur2.execute("insert into smartmart values(3,'curd', 65, 25);")
cur2.execute("insert into smartmart values(4,'flavored yogurt box', 40, 43);")
cur2.execute("insert into smartmart values(5,'rice packed 1 kg', 70, 65);")
cur2.execute("insert into smartmart values(6,'cheese 500gm', 400, 13);")
cur2.execute("insert into smartmart values(7,'cheddar cheese', 100, 96);")
cur2.execute("insert into smartmart values(8,'ramen hot', 70, 32);")
cur2.execute("insert into smartmart values(9,'ramen instant', 100, 25);")
cur2.execute("insert into smartmart values(10,'soy sauce', 40, 73);")
cur2.execute("insert into smartmart values(11,'chilli sauce', 50, 71);")
cur2.execute("insert into smartmart values(12,'soy sauce', 40, 76);")
cur2.execute("insert into smartmart values(13,'ketchup', 60, 25);")
cur2.execute("insert into smartmart values(14,'onions 1kg', 50, 42);")
cur2.execute("insert into smartmart values(15,'carrots 1kg', 60, 36);")
cur2.execute("insert into smartmart values(16,'chilli 1kg', 50, 32);")
cur2.execute("insert into smartmart values(17,'tomato 1kg', 40, 28);")
cur2.execute("insert into smartmart values(18,'radish 1kg', 35, 23);")
cur2.execute("insert into smartmart values(19,'red chilli', 35, 25);")
cur2.execute("insert into smartmart values(20,'peanut butter', 50, 60);")
cur2.execute("insert into smartmart values(21,'readymade chappati', 40, 25);")
cur2.execute("insert into smartmart values(22,'dosa batter', 65, 25);")
cur2.execute("insert into smartmart values(23,'vinegar', 100, 92);")
cur2.execute("insert into smartmart values(24,'eggs', 40, 37);")
22
cur2.execute("insert into smartmart values(25,'soda', 10, 23);")
cur2.execute("insert into smartmart values(26,'vegetable oil', 60, 35);")
cur2.execute("insert into smartmart values(27,'sunflower oil', 60, 53);")
cur2.execute("insert into smartmart values(28,'chilli powder', 50, 35);")
cur2.execute("insert into smartmart values(29,'coriander', 400, 35);")
cur2.execute("insert into smartmart values(30,'pepper whole', 35, 21);")
cur2.execute("insert into smartmart values(31,'pepper powder', 35, 60);")
cur2.execute("insert into smartmart values(32,'chocolate', 50, 35);")
cur2.execute("insert into smartmart values(33,'lemon', 35, 60);")
cur2.execute("insert into smartmart values(34,'rice crisps', 65, 23);")
cur2.execute("insert into smartmart values(35,'white sugar', 50, 73);")
cur2.execute("insert into smartmart values(36,'biscuits', 50, 36);")
cur2.execute("insert into smartmart values(37,'cookies', 50, 72);")
cur2.execute("insert into smartmart values(38,'jam', 60, 65);")
cur2.execute("insert into smartmart values(39,'honey', 60, 35);")
cur2.execute("insert into smartmart values(40,'maple syrup', 50, 45);")
cur2.execute("insert into smartmart values(41,'salt', 50, 35);")
cur2.execute("insert into smartmart values(42,'turmeric powder', 35, 60);")
cur2.execute("insert into smartmart values(43,'rice', 35, 40);")
cur2.execute("insert into smartmart values(44,'sugar free', 50, 70);")
cur2.execute("insert into smartmart values(45,'spaghetti', 50, 80);")
cur2.execute("insert into smartmart values(46,'ricebran oil', 60, 58);")
cur2.execute("insert into smartmart values(47,'red cabbage 1kg', 35, 28);")
cur2.execute("insert into smartmart values(48,'sambar powder', 40, 55);")
cur2.execute("insert into smartmart values(49,'garam masala powder', 400, 67);")
cur2.execute("insert into smartmart values(50,'ink pen', 75, 56);")
cur2.execute("insert into smartmart values(51,'canned drinks', 400, 53);")
cur2.execute("insert into smartmart values(52,'mango drink', 150, 42);")
cur2.execute("insert into smartmart values(53,'apple juice', 100, 55);")
23
cur2.execute("insert into smartmart values(54,'pencil', 85, 75);")
cur2.execute("insert into smartmart values(55,'potato chips', 80, 30);")
cur2.execute("insert into smartmart values(56,'potato 1 kg', 40, 60);")
cur2.execute("insert into smartmart values(57,'cabbage 1 kg', 400, 75);")
cur2.execute("insert into smartmart values(58,'milk chocolate', 40, 30);")
cur2.execute("insert into smartmart values(59,'cleaning fluid', 400, 70);")
cur2.execute("insert into smartmart values(60,'milkshakes', 40, 74);")
cur2.execute("insert into smartmart values(61,'corn 1kg', 50, 70);")
cur2.execute("insert into smartmart values(62,'mixed nuts', 50, 25);")
cur2.execute("insert into smartmart values(63,'popcorn', 35, 27);")
cur2.execute("insert into smartmart values(64,'washing powder', 35, 40);")
cur2.execute("insert into smartmart values(65,'detergent', 50, 60);")
cur2.execute("insert into smartmart values(66,'washing soap', 50, 20);")
cur2.execute("insert into smartmart values(67,'body soap', 60, 56);")
cur2.execute("insert into smartmart values(68,'shampoo', 35, 22);")
cur2.execute("insert into smartmart values(69,'body wash', 69, 69);")
cur2.execute("insert into smartmart values(70,'milk maid', 40, 13);")
cur2.execute("insert into smartmart values(71,'chat masala', 75, 50);")
cur2.execute("insert into smartmart values(72,'mangoes 1kg', 45, 30);")
cur2.execute("insert into smartmart values(73,'apples 1kg', 150, 47);")
cur2.execute("insert into smartmart values(74,'pineapples 1kg', 104, 65);")
cur2.execute("insert into smartmart values(75,'masala peanuts', 85, 28);")
cur2.execute("insert into smartmart values(76,'bananas 1kg', 80, 34);")
cur2.execute("insert into smartmart values(77,'cauliflower 1kg', 40, 53);")
cur2.execute("insert into smartmart values(78,'soup mix', 400, 77);")
cur2.execute("insert into smartmart values(79,'himalayan salt', 20, 63);")
cur2.execute("insert into smartmart values(80,'crystal sugar', 400, 57);")
cur2.execute("insert into smartmart values(81,'powdered sugar', 40, 73);")
cur2.execute("insert into smartmart values(82,'custard mix', 40, 78);")
24
cur2.execute("insert into smartmart values(83,'milk powder', 50, 42);")
cur2.execute("insert into smartmart values(84,'maida', 50, 78);")
cur2.execute("insert into smartmart values(85,'rice flour', 35, 22);")
cur2.execute("insert into smartmart values(86,'corn flour', 35, 26);")
cur2.execute("insert into smartmart values(87,'jeera powder', 50, 32);")
cur2.execute("insert into smartmart values(88,'washing soap', 50, 37);")
cur2.execute("insert into smartmart values(89,'body soap', 60, 52);")
cur2.execute("insert into smartmart values(90,'shampoo', 35, 27);")
cur2.execute("insert into smartmart values(91,'body wash', 40, 52);")
cur2.execute("insert into smartmart values(92,'candy', 400, 16);")
cur2.execute("insert into smartmart values(93,'lollipop', 75, 52);")
cur2.execute("insert into smartmart values(94,'mangoes 1kg', 400, 54);")
cur2.execute("insert into smartmart values(95,'apples 1kg', 150, 42);")
cur2.execute("insert into smartmart values(96,'pineapples 1kg', 100, 36);")
cur2.execute("insert into smartmart values(97,'peanut candy', 85, 22);")
cur2.execute("insert into smartmart values(98,'bananas 1kg', 80, 37);")
cur2.execute("insert into smartmart values(99,'milk', 40, 52);")
cur2.execute("insert into smartmart values(100,'crystal salt', 400, 78);")
cur2.execute("create table freshmakers(Sno int, ITEM_NAME 
varchar(25),QUANTITY int, PRICE int);")
cur2.execute("insert into freshmakers values(1,'white bread',30, 25);")
cur2.execute("insert into freshmakers values(2,'brown bread', 40, 30);")
cur2.execute("insert into freshmakers values(3,'curd', 65, 25);")
cur2.execute("insert into freshmakers values(4,'flavored yogurt box', 40, 43);")
cur2.execute("insert into freshmakers values(5,'rice packed 1 kg', 70, 65);")
cur2.execute("insert into freshmakers values(6,'cheese 500gm', 400, 13);")
cur2.execute("insert into freshmakers values(7,'coca cola', 100, 96);")
25
cur2.execute("insert into freshmakers values(8,'ramen hot', 70, 32);")
cur2.execute("insert into freshmakers values(9,'lemon tea', 100, 25);")
cur2.execute("insert into freshmakers values(10,'soy sauce', 40, 73);")
cur2.execute("insert into freshmakers values(11,'chilli sauce', 50, 71);")
cur2.execute("insert into freshmakers values(12,'soy sauce', 40, 76);")
cur2.execute("insert into freshmakers values(13,'ketchup', 60, 25);")
cur2.execute("insert into freshmakers values(14,'ice cream', 50, 42);")
cur2.execute("insert into freshmakers values(15,'carrots 1kg', 60, 36);")
cur2.execute("insert into freshmakers values(16,'chilli 1kg', 50, 32);")
cur2.execute("insert into freshmakers values(17,'tomato 1kg', 40, 28);")
cur2.execute("insert into freshmakers values(18,'radish 1kg', 35, 23);")
cur2.execute("insert into freshmakers values(19,'red chilli', 35, 25);")
cur2.execute("insert into freshmakers values(20,'frozen desserts', 50, 60);")
cur2.execute("insert into freshmakers values(21,'readymade chappati', 40, 25);")
cur2.execute("insert into freshmakers values(22,'dosa batter', 65, 25);")
cur2.execute("insert into freshmakers values(23,'vinegar', 100, 92);")
cur2.execute("insert into freshmakers values(24,'eggs', 40, 37);")
cur2.execute("insert into freshmakers values(25,'soda', 10, 23);")
cur2.execute("insert into freshmakers values(26,'butter', 60, 35);")
cur2.execute("insert into freshmakers values(27,'sunflower oil', 60, 53);")
cur2.execute("insert into freshmakers values(28,'chilli powder', 50, 35);")
cur2.execute("insert into freshmakers values(29,'coriander', 400, 35);")
cur2.execute("insert into freshmakers values(30,'pepper whole', 35, 21);")
cur2.execute("insert into freshmakers values(31,'pepper powder', 35, 60);")
cur2.execute("insert into freshmakers values(32,'chocolate', 50, 35);")
cur2.execute("insert into freshmakers values(33,'lemon', 35, 60);")
cur2.execute("insert into freshmakers values(34,'rice crisps', 65, 23);")
cur2.execute("insert into freshmakers values(35,'tea sachets', 50, 73);")
cur2.execute("insert into freshmakers values(36,'biscuits', 50, 36);")
26
cur2.execute("insert into freshmakers values(37,'cookies', 50, 72);")
cur2.execute("insert into freshmakers values(38,'bun', 60, 65);")
cur2.execute("insert into freshmakers values(39,'honey', 60, 35);")
cur2.execute("insert into freshmakers values(40,'maple syrup', 50, 45);")
cur2.execute("insert into freshmakers values(41,'salt', 50, 35);")
cur2.execute("insert into freshmakers values(42,'burger buns', 35, 60);")
cur2.execute("insert into freshmakers values(43,'rice', 35, 40);")
cur2.execute("insert into freshmakers values(44,'sugar free', 50, 70);")
cur2.execute("insert into freshmakers values(45,'coffee powder flavored', 50, 
80);")
cur2.execute("insert into freshmakers values(46,'ricebran oil', 60, 58);")
cur2.execute("insert into freshmakers values(47,'red cabbage 1kg', 35, 28);")
cur2.execute("insert into freshmakers values(48,'condensed milk', 40, 55);")
cur2.execute("insert into freshmakers values(49,'garam masala powder', 400, 
67);")
cur2.execute("insert into freshmakers values(50,'pav buns', 75, 56);")
cur2.execute("insert into freshmakers values(51,'canned drinks', 400, 53);")
cur2.execute("insert into freshmakers values(52,'mango drink', 150, 42);")
cur2.execute("insert into freshmakers values(53,'apple juice', 100, 55);")
cur2.execute("insert into freshmakers values(54,'pencil', 85, 75);")
cur2.execute("insert into freshmakers values(55,'potato chips', 80, 30);")
cur2.execute("insert into freshmakers values(56,'milk tea bags', 40, 60);")
cur2.execute("insert into freshmakers values(57,'cabbage 1 kg', 400, 75);")
cur2.execute("insert into freshmakers values(58,'milk chocolate', 40, 30);")
cur2.execute("insert into freshmakers values(59,'cleaning fluid', 400, 70);")
cur2.execute("insert into freshmakers values(60,'milkshakes', 40, 74);")
cur2.execute("insert into freshmakers values(61,'burger patty veg', 50, 70);")
cur2.execute("insert into freshmakers values(62,'mixed nuts', 50, 25);")
cur2.execute("insert into freshmakers values(63,'popcorn', 35, 27);")
27
cur2.execute("insert into freshmakers values(64,'chocolate milk mix', 35, 40);")
cur2.execute("insert into freshmakers values(65,'detergent', 50, 60);")
cur2.execute("insert into freshmakers values(66,'washing soap', 50, 20);")
cur2.execute("insert into freshmakers values(67,'body soap', 60, 56);")
cur2.execute("insert into freshmakers values(68,'shampoo', 35, 22);")
cur2.execute("insert into freshmakers values(69,'body wash', 69, 69);")
cur2.execute("insert into freshmakers values(70,'milk maid', 40, 13);")
cur2.execute("insert into freshmakers values(71,'chat masala', 75, 50);")
cur2.execute("insert into freshmakers values(72,'mangoes 1kg', 45, 30);")
cur2.execute("insert into freshmakers values(73,'apples 1kg', 150, 47);")
cur2.execute("insert into freshmakers values(74,'pineapples 1kg', 104, 65);")
cur2.execute("insert into freshmakers values(75,'burger patty nonveg', 85, 28);")
cur2.execute("insert into freshmakers values(76,'bananas 1kg', 80, 34);")
cur2.execute("insert into freshmakers values(77,'coffee powder', 40, 53);")
cur2.execute("insert into freshmakers values(78,'soup mix', 400, 77);")
cur2.execute("insert into freshmakers values(79,'himalayan salt', 20, 63);")
cur2.execute("insert into freshmakers values(80,'crystal sugar', 400, 57);")
cur2.execute("insert into freshmakers values(81,'powdered sugar', 40, 73);")
cur2.execute("insert into freshmakers values(82,'custard mix', 40, 78);")
cur2.execute("insert into freshmakers values(83,'milk powder', 50, 42);")
cur2.execute("insert into freshmakers values(84,'maida', 50, 78);")
cur2.execute("insert into freshmakers values(85,'rice flour', 35, 22);")
cur2.execute("insert into freshmakers values(86,'corn flour', 35, 26);")
cur2.execute("insert into freshmakers values(87,'jeera powder', 50, 32);")
cur2.execute("insert into freshmakers values(88,'sausages', 50, 37);")
cur2.execute("insert into freshmakers values(89,'body soap', 60, 52);")
cur2.execute("insert into freshmakers values(90,'milk 2', 35, 27);")
cur2.execute("insert into freshmakers values(91,'body wash', 40, 52);")
cur2.execute("insert into freshmakers values(92,'candy', 400, 16);")
28
cur2.execute("insert into freshmakers values(93,'lollipop', 75, 52);")
cur2.execute("insert into freshmakers values(94,'vegan butter', 400, 54);")
cur2.execute("insert into freshmakers values(95,'tea leaves', 150, 42);")
cur2.execute("insert into freshmakers values(96,'pineapples 1kg', 100, 36);")
cur2.execute("insert into freshmakers values(97,'peanut candy', 85, 22);")
cur2.execute("insert into freshmakers values(98,'bananas 1kg', 80, 37);")
cur2.execute("insert into freshmakers values(99,'milk', 40, 52);")
cur2.execute("insert into freshmakers values(100,'crystal salt', 400, 78);")
#meghana, con3
#--------
#cs project
#illness : Diabetes, Obesity, Eczema
#1 DIABETES
cur3.execute("Create table diabetes(Sno int, Food_not_to_be_taken char(30), 
Alternative_food char(30));")
cur3.execute("Insert into Diabetes values(1,'sugar','sugar free powder');")
cur3.execute("Insert into Diabetes values(2,'oil', 'ghee");')
cur3.execute("insert into Diabetes values(3,'trans fats', 'olive oil');")
cur3.execute("insert into Diabetes values(4,'white bread', 'Whole grain 
tortilla');")
cur3.execute("insert into Diabetes values(5,'rice', 'Quinoa');')
cur3.execute("insert into Diabetes values(6,'pasta', 'Onion noodles');")
cur3.execute("insert into Diabetes values(7,'fruit yogurt', 'Plain yogurt');")
cur3.execute("insert into Diabetes values(8,'cereal', 'Chia pudding');")
cur3.execute("insert into Diabetes values(9,'Coffee', 'Lemon water');")
29
cur3.execute("insert into Diabetes values(10,'Honey', 'Brown sugar');")
cur3.execute("insert into Diabetes values(11,'Maple syrup', 'Coconut nectar');")
cur3.execute("insert into Diabetes values(12,'Dried fruit', 'Fresh fruit');")
cur3.execute("insert into Diabetes values(13,'Packed snack', 'oats');")
cur3.execute("insert into Diabetes values(14,'Chocolate', 'protein bar');")
cur3.execute("insert into Diabetes values(15,'Fruit juice', 'Coconut water');")
cur3.execute("insert into Diabetes values(16,'French fries', 'Baked potato');")
cur3.execute("insert into Diabetes values(17,'Milk', 'Soy milk');")
cur3.execute("insert into Diabetes values(18,'Pickles', 'Olives');")
cur3.execute("insert into Diabetes values(19,'Fried meat', 'Chickpea fry');")
cur3.execute("insert into Diabetes values(20,'Soda', 'Sparkling water');")
#2 OBESITY
cur3.execute("Create table obesity(Sno integer, Food_not_to_be_taken char(30), 
Alternative_food char(30));")
cur3.execute('Insert into Obesity values(1,"Red meat", "Fish");')
cur3.execute('Insert into Obesity values(2,"Sugar","sugar free powder");')
cur3.execute('Insert into Obesity values(3,"Chocolates", "fruits");')
cur3.execute('Insert into Obesity values(4,"Carbonated drinks", " Fruit juice");')
cur3.execute('Insert into Obesity values(5,"Ice cream", "Yogurt");')
cur3.execute('Insert into Obesity values(6,"Pizza", "Quinoa");')
cur3.execute('Insert into Obesity values(7,"cheese", "Ricota");')
cur3.execute('Insert into Obesity values(8,"Fried chips", "Baked potatoes");')
cur3.execute('Insert into Obesity values(9,"Milk sweets ", "Karuppati sweets");')
cur3.execute('Insert into Obesity values(10,"Paneer", "Tofu");')
cur3.execute('Insert into Obesity values(11,"Milk", "Oat milk");')
cur3.execute('Insert into Obesity values(12,"White Bread", "Wheat bread");')
30
cur3.execute('Insert into Obesity values(13,"Oil", "Olive oil");')
cur3.execute('Insert into Obesity values(14,"Ghee", "Coconut oil");')
cur3.execute('Insert into Obesity values(15,"Alcohol", "Fresh lime juice");')
cur3.execute('Insert into Obesity values(16,”coke", "Diet coke");')
cur3.execute('Insert into Obesity values(17,"Trans fat", "Soy oil");')
cur3.execute('Insert into Obesity values(18,"Pasta", "Salad");')
cur3.execute('Insert into Obesity values(19,"Refined grains", "Oats");')
cur3.execute('Insert into Obesity values(20,"White rice", "Quinoa");')
#3 ECZEMA
cur3.execute("Create table eczema(Sno integer, Food_not_to_be_taken char(30), 
Alternative_food char(30));")
cur3.execute('Insert into Eczema values(1,"Milk", "Oat milk");')
cur3.execute('Insert into Eczema values(2,"Eggs", "Tofu cheese");') 
cur3.execute('Insert into Eczema values(3,"Peanuts", "Sorry, No alternative");')
cur3.execute('Insert into Eczema values(4,"Soy", "Sorry, No alternative");')
cur3.execute('Insert into Eczema values(5,"Fish ", "Tofu");')
cur3.execute('Insert into Eczema values(6,”Citrus Fruits", "Broccoli");')
cur3.execute('Insert into Eczema values(7,"Tomatoes", "Squash");')
cur3.execute('Insert into Eczema values(8,"Canned foods ", "Dried fruits");')
cur3.execute('Insert into Eczema values(9,"Gluten", "Corn");')
cur3.execute('Insert into Eczema values(10,"Butter", "Coconut oil");')
cur3.execute('Insert into Eczema values(11,"Grapes", "Canteloupe");')
cur3.execute('Insert into Eczema values(12,"Tea", "Coconut water");')
cur3.execute('Insert into Eczema values(13,"MSG", "Shiittake mushrooms");')
cur3.execute('Insert into Eczema values(14,"Salt", "Mint");')
cur3.execute('Insert into Eczema values(15,"Seafood", "Jackfruit");')
31
cur3.execute('Insert into Eczema values(16,"Red peppers ", "Jalapeno");')
cur3.execute('Insert into Eczema values(17,"Berries", "Acai");')
cur3.execute('Insert into Eczema values(18,"Paneer", "Tofu");')
cur3.execute('Insert into Eczema values(19,"Cakes", "Cinnamon roll");')
cur3.execute('Insert into Eczema values(20,"Chocolates", "Fruits");')
#priya
#------
#GLUCOSE INTOLERANCE
 
cur3.execute("create table glucose_intolerance(Sno int,Food_not_to_be_taken 
char(30),Altrenative_food char(30));")
cur3.execute("insert into glucose_intolerance values(1,'Fruit Juices','Water');")
cur3.execute("insert into glucose_intolerance values(2,'Soda','Coconut water');")
cur3.execute("insert into glucose_intolerance values(3,'Corn flour','Arrowroot 
flour');")
cur3.execute("insert into glucose_intolerance values(4,'Ice cream','Vegan ice 
cream');")
cur3.execute("insert into glucose_intolerance values(5,'Chocolate','Dark 
chocolate');")
cur3.execute("insert into glucose_intolerance values(6,'White bread','Rye 
bread');")
cur3.execute("insert into glucose_intolerance values(7,'Rice','Quinoa');")
cur3.execute("insert into glucose_intolerance values(8,'Pasta','Multigrain 
pasta');")
cur3.execute("insert into glucose_intolerance values(9,'Maida','Maize flour');")
cur3.execute("insert into glucose_intolerance values(10,'Chips','Carrot slices');")
cur3.execute("insert into glucose_intolerance values(11,'Butter','Vegetable 
oil');")
cur3.execute("insert into glucose_intolerance values(12,'Cereal','Oats');")
32
cur3.execute("insert into glucose_intolerance values(13,'Biscuits','Digestable 
biscuits');")
cur3.execute("insert into glucose_intolerance values(14,'Flavoured 
yogurt','Unflavouredyogurt');")
cur3.execute("insert into glucose_intolerance values(15,'Coffee','Tea');")
cur3.execute("insert into glucose_intolerance values(16,'Honey','Brown rice 
syrup');")
cur3.execute("insert into glucose_intolerance values(17,'Mapel syrup','Sorry, No 
alternative');")
cur3.execute("insert into glucose_intolerance values(18,'Dried fruit','Fresh 
fruit');")
cur3.execute("insert into glucose_intolerance values(19,'Frozen french 
fries','Carrot slices');")
cur3.execute("insert into glucose_intolerance values(20,'Microwave 
popcorn','Sorry, No alternative');")
#PEANUT_ALLERGY
cur3.execute("create table peanut_allergy(Sno int,Food_not_to_be_taken 
char(30),Alternative char(30));")
cur3.execute("insert into peanut_allergy values(1,'Nut ice cream','Nut free 
icecream');")
cur3.execute("insert into peanut_allergy values(2,'Barbeque sauce','Sorry, No 
alternative');")
cur3.execute("insert into peanut_allergy values(3,'Peanut butter','Almond');")
cur3.execute("insert into peanut_allergy values(4,'Peanut oil','Avocado oil');")
cur3.execute("insert into peanut_allergy values(5,'Szechwan sauce','Sorry, No 
alternative');")
cur3.execute("insert into peanut_allergy values(6,'Chocolate','Nut free 
chocolate');")
cur3.execute("insert into peanut_allergy values(7,'Mixed nuts','Sorry, No 
alternative');")
33
cur3.execute("insert into peanut_allergy values(8,'Salted peanuts','Sesame 
seeds');")
cur3.execute("insert into peanut_allergy values(9,'Masala peanuts','Roasted 
soybeans');")
cur3.execute("insert into peanut_allergy values(10,'Raw peanuts','Sunflower 
seeds');")
cur3.execute("insert into peanut_allergy values(11,'Candied peanuts','Sunflower 
seeds');")
cur3.execute("insert into peanut_allergy values(12,'Peanut chutney','Sorry, No 
alternative');")
cur3.execute("insert into peanut_allergy values(13,'Grain breads','Grain free 
flour');")
cur3.execute("insert into peanut_allergy values(14,'Puddings','Avacado');")
cur3.execute("insert into peanut_allergy values(15,'Peanut cookies','Nut free 
cookies');")
cur3.execute("insert into peanut_allergy values(16,'Peanut flour','White flour');")
cur3.execute("insert into peanut_allergy values(17,'Peanut oil','Olive oil');")
cur3.execute("insert into peanut_allergy values(18,'Peanut donuts','Nut free');")
cur3.execute("insert into peanut_allergy values(19,'Peanut candy','Nut free');")
cur3.execute("insert into peanut_allergy values(20,'Peanut lollipop','Nut free');")
#OBESITY
 
cur3.execute("insert into obesity values(1,'French fries','Baked potato');")
cur3.execute("insert into obesity values(2,'Coca cola','Tea');")
cur3.execute("insert into obesity values(3,'Jam','Honey');")
cur3.execute("insert into obesity values(4,'White Bread','Whole wheat');")
cur3.execute("insert into obesity values(5,'Ice cream','Coconut milk icecream');")
cur3.execute("insert into obesity values(6,'Processed meat','Sorry, No
alternative');")
cur3.execute("insert into obesity values(7,'Smoothies','Banana rice smoothie');")
34
cur3.execute("insert into obesity values(8,'Chips','Carrot slices');")
cur3.execute("insert into obesity values(9,'White rice','Millet');")
cur3.execute("insert into obesity values(10,'Sweetened yogurt','Unsweetened');")
cur3.execute("insert into obesity values(11,'Candied dried fruits','Almonds');")
cur3.execute("insert into obesity values(12,'White pasta','Whole grain');")
cur3.execute("insert into obesity values(13,'Sugary,refined cereals','Millet');")
cur3.execute("insert into obesity values(14,'Soda','Tea');")
cur3.execute("insert into obesity values(15,'Juice','Green tea');")
cur3.execute("insert into obesity values(16,'Muffins','Fruits');")
cur3.execute("insert into obesity values(17,'Energy drinks','Coconut water');")
cur3.execute("insert into obesity values(18,'Cakes','Carrot');")
cur3.execute("insert into obesity values(19,'Candy bars','Fresh fruits');")
cur3.execute("insert into obesity values(20,'Burger','Salad');")
#neha-table-1, restocking, con5
#-------------
cur5.execute("create table restocking(Sno int, SHOP_NAME char(50), 
RESTOCKING_DAYS int);")
cur5.execute("insert into RESTOCKING values(1, 'grandmarket', 3);")
cur5.execute("insert into RESTOCKING values(2, 'crystalmart', 2);")
cur5.execute("insert into RESTOCKING values(3, 'freshorigin', 7);")
cur5.execute("insert into RESTOCKING values(4, 'freshmakers', 4);")
cur5.execute("insert into RESTOCKING values(5, 'smartmart', 3);")
cur5.execute("insert into RESTOCKING values(6, 'budgetfoods', 3);")
#neha, delivery, con6
#-----
cur6.execute("create table delivery (Sno int , SHOP_NAME 
CHAR(50),DELIVERY_TIME varchar(10), DELIVERY_CHARGES int);")
35
cur6.execute("insert into DELIVERY values(1, 'crystalmart', '3hrs', 90)")
cur6.execute("insert into DELIVERY values(2, 'freshorigin', '1hr', 75)")
cur6.execute("insert into DELIVERY values(3, 'grandmarket', '2hrs', 60)")
cur6.execute("insert into DELIVERY values(4, 'budgetfoods', '4hrs', 150)")
cur6.execute("insert into DELIVERY values(5, 'smartmart', '2hrs', 65)")
cur6.execute("insert into DELIVERY values(6, 'freshmakers', '1hr', 80)")
36
import mysql.connector
import threading
import datetime
import prettytable
con1=mysql.connector.connect(host='localhost',user='root',passwd='Sanj',databa
se='Customer')
cur1=con1.cursor()
con2=mysql.connector.connect(host='localhost',user='root',passwd='Sanj',databa
se='Shops')
cur2=con2.cursor()
con3=mysql.connector.connect(host='localhost',user='root',passwd='Sanj',databa
se='Illness')
cur3=con3.cursor()
con4=mysql.connector.connect(host='localhost',user='root',passwd='Sanj',databa
se='INDCUST')
cur4=con4.cursor()
con5=mysql.connector.connect(host='localhost',user='root',passwd='Sanj',databa
se='Restocking')
cur5=con5.cursor()
con6=mysql.connector.connect(host='localhost',user='root',passwd='Sanj',databa
se='Payment and delivery')
cur6=con6.cursor()
print('\t\t\tConsumer or Shop Owner:')
option=input('Choose User:')
#timetaknforrestk-(today-dayappliedforrestk)=remaining time
List_of_restocking_info=[]
#Functions
#New Customer for registration
def createindcust(newname,illness,shoppref):
 cur1.execute("select * from Customers;")
 V=cur1.fetchall()
37
 if V.rowcount!=0:
 cur1.execute("insert into Customers values((select max(cust_id) from 
Customers)+1,'{}','{}','{}',0);".format(newname,illness,shoppref))
 cur1.execute("select max(cust_id) from customers;")
 cid=cur1.fetchall()
 cur4.execute("create table '{}'(CustName char(30) default('{}'),Itemordered 
char(20), Dateoforder date default(curdate()),Ordernumber int, shop_name 
char(20));".format(str(cid[0][0]+'T',newname) )
 else:
 cur1.execute("insert into Customers 
values(1,'{}','{}','{}',0);".format(newname,illness,shoppref))
 cur1.execute("select max(cust_id) from customers;")
 cid=cur1.fetchall()
 cur4.execute("create table '{}'(CustName char(30) default('{}'),Itemordered 
char(20), Dateoford
#Restocking after selling out
def restock(prod,shop):
 cur2.execute("update '{}' set '{}'='{}'+40;".format(shop,prod,prod))
 for removal in List_of_restocking_info:
 if removal[0:2]==[shop,prod]:
 List_of_restocking_info.remove(removal)
 
#Getting grocery list
def GETGLIST():
 n=int(input('No of items to order:'))
 for i in range(n):
 List=[]
 ITEM=input('Item:')
 Amount=input('Quantity:')
38
 List.append([ITEM,Amount])
 return(List)
#Getting previous order
def getprevord(custid):
 cur4.execute("select * from '{}' where dateoforder=(select max(dateoforder) 
from '{}';);".format(str(custid)+'T',custid))
 buy_details=cur4.fetchall()
 table = [['Item_no','Item_Name','Date_of_Order']]
 for pbuy in buy_details:
 table.append([pbuy[3],pbuy[1],pbuy[2]])
 tab = PrettyTable(table[0])
 tab.add_rows(table[1:])
 print(tab)
#Getting all prev buy information
def getallcustdetails(custid):
 cur4.execute("select * from '{}';".format(str(custid)+'T'))
 alldet=cur4.fetchall()
 table = [['Item_no','Item_Name','Date_of_Order']]
 for pall in alldet:
 table.append([pall[3], pall[1], pall[2]])
 tab = PrettyTable(table[0])
 tab.add_rows(table[1:])
 print(tab)
#Out of stock message
def outofstk(x):
 print("Your requested item is out of stock, it'll be restocked in", x, "days.")
39
#Healthissuemsg
def healthissue(Y,issue):
 print('This item is not preferrable for your healh:',Y, 'due to',issue)
#Checking for health issue and suggesting alternate item
def checkhealth(itemn,issues):
 result=True
 for i in issues:
 cur3.execute("select * from '{}';".format(i,))
 nopro=cur3.fetchall()
 for j in nopro:
 if itemn.lower()==j[1].lower():
 healthissue(itemn,i)
 print('Alternate item for',itemn,':',j[2])
 result=False
 else:
 return(result)
 
#Used to obtain date after which restocking is done and STARTS restock timer
def Dayintervals(prodn,shopn):
 Day_app=cur1.execute("select curdate();")
 x=Day_app
 List_of_restocking_info.append[[shopn,prodn,x]]
 timer1 = threading.Timer(x*24*60*60,restock(prodn,shopn))
 timer1.start()
#BUYING, ORDER PLACEMENT
def ordplace(cust_id,prodn,shopn,qua):
40
 cur2.execute("update '{}' set quantity=quantity-{} where 
item_name='{}';".format(shopn,qua,prodn))
 cur4.excute("insert into '{}'(Itemordered,orderno) 
values('{}',{});".format(str(cust_id)+'T',prodn,i+1))
 cur2.execute("select quantity from '{}' where 
item_name='{}';".format(shopn,prodn))
 cur1.execute("update customers set noofbuys=noofbuys+1 where 
custid={};".format(cust_id,))
 Quant_chck=cur2.fetchall()
 if Quant_chck[0][0]==0:
 Dayintervals(prodn,shopn)
 
#To find days after which restocking is done for preferred shop
def restockdays(shopn):
 cur5.execute("select days from Restocking where 
shop_name='{}';".format(shohpn,))
 DAYS=cur5.fetchall()
 return(DAYS[0][0])
#Not available in pref shop ever
def notavail():
 print('Requested item is not available in shop')
#Suggesting Alternate shop for out of stock or unavailable product
def ALT(prodn,QUA):
 cur2.execute("show tables;")
 SHOPS=cur2.fetchall()
 Avail_shops=[]
 Avail_shopslq=[]
 for j in SHOPS:
41
 cur2.execute("select * from '{}';".format(j[0],))
 shopp_info=cur2.fetchall()
 for k in shopp_info:
 if k[1].lower()==prodn.lower() and k[2]>=QUA:
 Avail_shops.append([j,prodn,k[2]])
 elif k[1].lower()==prodn.lower() and k[2]<QUA:
 Avail_shopslq.append([j,prodn,k[2])
 print('Other shops with',prodn,'available at the moment')
 if: Avail_shops==[]and Avail_shopslq==[]:
 print('No shop has the required product at the moment.')
 else:
 print('Quantity also available:')
 if Avail_shops==[]:
 print('No shop has required product and the required amount')
 table = [['Shop_name','Item_name','Quantity']]+Avail_shops
 tab = PrettyTable(table[0])
 tab.add_rows(table[1:])
 print(tab)
 print('Quantity not available:')
 if Avail_shopslq==[]:
 print('No shop has required product and quantity less than required 
amount')
 table1 = [['Shop_name','Item_name','Quantity']]+Avail_shopslq
 tab1 = PrettyTable(table1[0])
 tab1.add_rows(table1[1:])
 print(tab1)
 print('With the above information, please place further purchase after 
current purchase')
42
#Check availability of product
def checkavail(prodn,shopn):
 cur2.execute("select item_name,quantity from '{}';".format(shopn,))
 list_prod=cur2.fetchall()
 for prod in list_prod:
 if prod[0].lower()==prodn.lower():
 print('The product',prodn,'is available in',shopn,'. Quantity 
available:',prod[2],'at price',prod[3])
 break
 else:
 print('Product unavailable.')
#Printing items in a shop
def printshop(shopn):
 cur2.execute("select * from '{}';".format(shopn,))
 table2=[['Sno','Prod_name','Quantity','Price'],]+cur2.fetchall()
 tab2 = PrettyTable(table2[0])
 tab2.add_rows(table2[1:])
 print(tab2)
 
#Payment portal 
def payment(cost,shop):
 cur6.execute("select delivery_days, delivery_charge from Delivery where 
shopname='{}';".format(shop,))
 X=cur6.fetchall()
 print('Delivery will occur in ',X[0],' hours. Payment method: Cash on delivery 
to be done.')
 print('Total amount to be paid(Delivery Charge included):', cost+X[1]) 
#Shop owner interface functions
43
def addprod(sname):
 n=int(input("No. of records to be added : "))
 print("Enter the following details : ")
 for i in range(n):
 sno=int(input("Item code : "))
 iname=input("Item name : ")
 quantity=int(input("Quantity : "))
 price=float(input("Price : "))
 cm="insert into {} 
values({},'{}',{},{})".format(sname,snp,iname,quantity,price)
 cur2.execute(cm)
 con2.commit()
def updateprod(sname):
 print("1. Item code\n2. Item name\n3. Quantity\n4. Price")
 d={1:'Item code',2:'Item name',3:'Quantity',4:'Price'}
 x=int(input("Field to be updated : "))
 if x==4:
 print("Update price of")
 print("A. One or many Products\nB. All products\n")
 p=input("Enter option(A/B) : ")
 if p=='A':
 while True:
 ic=int(input("Enter item code to be updated : "))
 v=float(input("New value : "))
 cm="update {} set price = {} where sno = {}".format(sname,v,ic)
 cur2.execute(cm)
 con2.commit()
 ans=input("Want to update more records(y/n)? : ")
 if ans=='n':
44
 break
 elif p=='B':
 print("I. To a specific price")
 print("II. To increase/decrease by a specific percentage")
 print("III. To increase/decrease by a specific amount")
 ch=input("Enter choice(I/II/III) : ")
 if ch=='I':
 v=float(input("New value : "))
 cm="update {} set price = {}".format(sname,v)
 elif ch=='II':
 cg=input("Increase/decrease(i/d) : ")
 percnt=float(input("Percentage : "))
 if cg=='i':
 v=(100+percnt)/100
 else:
 v=(100-percnt)/100
 cm="update {} set price = price*{}".format(sname,v)
 elif ch=='III':
 cg=input("Increase/decrease(i/d) : ")
 amy=float(input("Amount : "))
 if cg=='i':
 v=amt
 else:
 v=-amt
 cm="update {} set price = price+{}".format(sname,v)
 cur2.execute(cm)
 con2.commit()
 
 else:
45
 while True:
 ic=int(input("Enter item code to be updated : "))
 v=eval(input("New value : "))
 cm="update {} set {} = {} where sno = {}".format(sname,d[x],v,ic)
 cur2.execute(cm)
 con2.commit()
 ans=input("Want to update more records(y/n)? : ")
 if ans=='n':
 break
 
def deleteprod(sname):
 ic=int(input("Enter item code to be deleted : "))
 cm="delete from {} where sno = {} ".format(sname,ic)
 cur2.execute(cm)
 con2.commit()
 
if option=='Customer':
 m=input('Are you an already registered member of the Grocmarket:')
 if m=='yes':
 custid=int(input('Enter registered CustomerID:'))
 custnm=input('Enter registered CustomerName:')
 cur1.execute('select * from Customers;')
 X=cur1.fetchall()
 Status='Unavailable'
 for cust in X:
 if cust[0]==custid and cust[1]==custnm:
 Cust_details=cust
 Status='Available'
 print('Successfully Customer Information retrieved!')
46
 break
 else:
 print('Customer not found.')
 while True:
 if Status=='Available':
 print('What do you want to do?')
 print('''1. Check Previous buy
 2. Place an Order
 3. Check Availability of product
 4. Check all previous purchases
 5. Check out items in a shop''')
 Action=int(input('Choose from above(1/2/3/4/5):'))
 if Action==1:
 getprevord(custid)
 elif Action==5:
 print('Shops available:')
 cur2.execute("show tables;")
 SHOPS=cur2.fetchall()
 table3 = [['Shops']]
 for i in SHOPS:
 table3.append(i[0])
 tab3 = PrettyTable3(table[0])
 tab3.add_rows(table3[1:])
 print(tab3)
 ss=input('Enter Shop name to display item details:')
 printshop(ss)
 
 elif Action==4:
 getallcustdetails(custid)
47
 
 elif Action==2:
 sum_amount=0
 Groc_list=GETGLIST()
 shopchoice=input('Registered preferred shop or other shops?')
 if shopchoice=='Preferred shop':
 prefshop=Cust_details[3]
 else:
 print('Shops available:')
 cur2.execute("show tables;")
 SHOPS=cur2.fetchall()
 table = [['Shops']]
 for i in SHOPS:
 table.append([i])
 tab = PrettyTable(table[0])
 tab.add_rows(table[1:])
 print(tab)
 prefshop=input('Shop to purchase from:')
 cur2.execute("select item_name,quantity,price from 
'{}';".format(prefshop,))
 Products=cur2.fetchall()
 #it is what customer wants, i is what is available
 for it in Groc_list:
 if checkhealth(it[0],X[2].split(','))==True:
 for i in Products:
 if i[0]==it[0]:
 if i[1]>=it[1]:
 sum_amount+=(i[2]*it[1])
 ordplac(Cust_details[0],i[0],prefshop,i[1])
48
 break
 if i[1]==0:
 #Out of stock product, to check the no of days after 
which product will be available
 for restkinfo in List_of_restocking_info: 
 #Restocking has been ordered
 if restkinfo[0]==prefshop and restkinfo[1]==it[0]:
 Y=cur3.execute("select 
datediff(curdate(),'{}');".format(restkinfo[2]))
 no_of_days=restockdays(prefshop)-Y
 outofstk(no_of_days)
 ALT(it[0],it[1])
 break
 break
 else: #Out of stock product, but restocking hasnt been 
placed yet
 Dayintervals(it[0],prefshop)
 ALT(it[0],it[1])
 if i[1]<it[1]:
 sum_amount+=(i[2]*(it[1]-i[1]))
 ordplac(Cust_details[0],i[0],prefshop,i[1])
 print('Needed quantity of ',i[0],' is ',i[1]-it[1],' more than 
what is available currently at the moment.')
 print('Order has been placed over available quantity.')
 ALT(it[0],it[1]-i[1])#Finding alternate shops for 
remaining quantity
 break
 else:
 notavail()
 ALT(it[0],it[1])
49
 else:#All items on user list has been run through and necessary 
action(ordplacement/alternate shops)has been taken
 print('Your order:')
 getprevord(custid)
 print('Total price:',sum_amount)
 payment(sum_amount,prefshop)
 elif Action==3:
 prn=input('Product name to check availability for:')
 shn=input('Shopname to check availability in:')
 checkavail(prn,shn)
 contpur=input('Do you want to continue purchase?(yes/no) ')
 if contpur.lower()=='no':
 break
 elif m=='no':
 nAme=input('Enter name to register:')
 ill=input('Enter the illnesses you want to avoid in a single line separated 
by commas')
 print('Shops available:')
 cur2.execute("show tables;")
 SHOPS=cur2.fetchall()
 table = [['Shops']]
 for i in SHOPS:
 table.append(i[0])
 tab = PrettyTable(table[0])
 tab.add_rows(table[1:])
 print(tab)
 #retrieve all table names using show tables from shops database and 
display available shops
 prefs=input('Enter the preferred shop in the above list:')
 createindcust(nAme,ill,prefs)
50
if option=='Shop owner':
 sname=input("Shop Name : ")
 print("a. Add record")
 print("b. Update record")
 print("c. Delete record")
 choice=input("Enter command(a/b/c) :")
 if choice=='a':
 addprod(sname)
 elif choice=='b':
 updateprod(sname)
 elif choice=='c':
 deleteprod(sname)
 
con1.commit()
con2.commit()
con3.commit()
con4.commit()
con5.commit()
con6.commit() 
 
