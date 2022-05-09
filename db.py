import sqlite3

conn = sqlite3.connect('Makeup.db', check_same_thread=False)
cur = conn.cursor()


def create_common_tables():
    cur.execute("CREATE TABLE IF NOT EXISTS colors(color TEXT PRIMARY KEY);")
    cur.execute("CREATE TABLE IF NOT EXISTS classifications(classification TEXT PRIMARY KEY);")
    cur.execute("CREATE TABLE IF NOT EXISTS madeIn(country TEXT PRIMARY KEY);")
    cur.execute("CREATE TABLE IF NOT EXISTS brands(brand TEXT PRIMARY KEY);")
    conn.commit()


def insert_common_table():
    cur.executemany('INSERT INTO colors VALUES(?)', [('blue',),
                                                     ('red',),
                                                     ('black',),
                                                     ('pink',),
                                                     ('brown',),
                                                     ('yellow',)])

    cur.executemany('INSERT INTO classifications VALUES(?)', [('elite',),
                                                              ('mass-market',),
                                                              ('middle-up',),
                                                              ('niche',),
                                                              ('professional',),
                                                              ('organic',)])

    cur.executemany('INSERT INTO madeIn VALUES(?)', [('Ukraine',),
                                                     ('Poland',),
                                                     ('USA',),
                                                     ('Turkey',),
                                                     ('Sweden',),
                                                     ('Italy',)])

    cur.executemany('INSERT INTO brands VALUES(?)', [('Bourjois',),
                                                     ('LOreal Paris',),
                                                     ('Maybelline New York',),
                                                     ('Catrice',),
                                                     ('Max Factor',),
                                                     ('Pupa',),
                                                     ('Topface',),
                                                     ('Oriflame',)])

    conn.commit()


def create_eyes_tables():
    cur.execute("CREATE TABLE IF NOT EXISTS mascara(\n"
                "       mascaraId INT PRIMARY KEY,\n"
                "       nameOfProduct TEXT,\n"
                "       brand brands,\n"
                "       classification classification,\n"
                "       country madeIn, \n"
                "       price INT,\n"
                "       volume TEXT);\n"
                "    ")
    cur.execute("CREATE TABLE IF NOT EXISTS eyeshadows(\n"
                "       eyeshadowsId INT PRIMARY KEY,\n"
                "       nameOfProduct TEXT,\n"
                "       brand brands,\n"
                "       classification classification,\n"
                "       country madeIn, \n"
                "       price INT,\n"
                "       color colors);\n"
                "    ")
    cur.execute("CREATE TABLE IF NOT EXISTS eyeliners(\n"
                "       eyelinerId INT PRIMARY KEY,\n"
                "       nameOfProduct TEXT,\n"
                "       brand brands,\n"
                "       classification classification,\n"
                "       country madeIn, \n"
                "       price INT,\n"
                "       eyelinerForm TEXT,\n"
                "       color colors);\n"
                "    ")
    cur.execute("CREATE TABLE IF NOT EXISTS eyeConcealers(\n"
                "       eyeConcealerId INT PRIMARY KEY,\n"
                "       nameOfProduct TEXT,\n"
                "       brand brands,\n"
                "       classification classification,\n"
                "       country madeIn, \n"
                "       price INT,\n"
                "       eyeConcealerForm TEXT,\n"
                "       color colors);\n"
                "    ")
    cur.execute("CREATE TABLE IF NOT EXISTS lashPrimers(\n"
                "       lashPrimerId INT PRIMARY KEY,\n"
                "       nameOfProduct TEXT,\n"
                "       brand brands,\n"
                "       classification classification,\n"
                "       country madeIn, \n"
                "       price INT,\n"
                "       color colors);\n"
                "    ")
    conn.commit()


def insert_eyes_table():
    cur.executemany('INSERT INTO mascara(mascaraId, nameOfProduct, brand, classification, country, price, '
                    'volume) VALUES (?,?,?,?,?,?,?)',
                    [('1', 'MaxFun', 'Bourjois', 'elite', 'Italy', 2000, 'big'),
                     ('2', 'Million Lashes', 'LOreal Paris', 'mass-market', 'USA', 300, 'medium'),
                     ('3', 'Lash Idole', 'Maybelline New York', 'niche', 'Turkey', 4390, 'big'),
                     ('4', 'False Lash', 'Max Factor', 'professional', 'Ukraine', 1200, 'medium'),
                     ('5', 'Glamour', 'Pupa', 'organic', 'Sweden', 690, 'big'),
                     ('6', 'Paradise', 'Oriflame', 'middle-market', 'Poland', 499, 'medium'),
                     ('7', 'Unlimited', 'Max Factor', 'mass-market', 'Ukraine', 560, 'big'),
                     ('8', 'Vamp', 'Pupa', 'mass-market', 'Sweden', 958, 'low'),
                     ('9', 'Curl', 'Oriflame', 'middle-market', 'Poland', 375, 'low')
                     ])

    cur.executemany(
        'INSERT INTO eyeshadows(eyeshadowsId, nameOfProduct, brand, classification, country, price, color) VALUES (?,'
        '?,?,?,?,?,?)',
        [('1', 'Revolution', 'Bourjois', 'elite', 'Italy', 475, 'red'),
         ('2', 'Profit-Style', 'LOreal Paris', 'mass-market', 'USA', 5834, 'blue'),
         ('3', 'Forever', 'Maybelline New York', 'niche', 'Turkey', 5684, 'black'),
         ('4', 'Rich Glow', 'Max Factor', 'professional', 'Ukraine', 384, 'pink'),
         ('5', 'Nude Palette', 'Pupa', 'organic', 'Sweden', 238, 'brown'),
         ('6', 'MAXI', 'Oriflame', 'middle-market', 'Poland', 4882, 'yellow'),
         ('7', 'Ultimate Edit', 'Max Factor', 'mass-market', 'Ukraine', 2943, 'brown'),
         ('8', 'Dreamy', 'Pupa', 'mass-market', 'Sweden', 2839, 'brown'),
         ('9', 'New York', 'Oriflame', 'middle-market', 'Poland', 345, 'pink')
         ])

    cur.executemany(
        'INSERT INTO eyeConcealers(eyeConcealerId, nameOfProduct, brand, classification, country, price, eyeConcealerForm, color) VALUES (?, '
        '?,?,?,?,?,?,?)',
        [('1', 'Revolution', 'Bourjois', 'elite', 'Italy', 552, 'cream', 'pink'),
         ('2', 'Profit-Style', 'LOreal Paris', 'mass-market', 'USA', 132, 'liquid', 'pink'),
         ('3', 'Forever', 'Maybelline New York', 'niche', 'Turkey', 421, 'pencil', 'black'),
         ('4', 'Rich Glow', 'Max Factor', 'professional', 'Ukraine', 134, 'powder', 'pink'),
         ('5', 'Nude Palette', 'Pupa', 'organic', 'Sweden', 312, 'stick', 'brown'),
         ('6', 'MAXI', 'Oriflame', 'middle-market', 'Poland', 234, 'liquid', 'yellow'),
         ('7', 'Ultimate Edit', 'Max Factor', 'mass-market', 'Ukraine', 240, 'cream', 'brown'),
         ('8', 'Dreamy', 'Pupa', 'mass-market', 'Sweden', 402, 'cream', 'brown'),
         ('9', 'New York', 'Oriflame', 'middle-market', 'Poland', 500, 'pencil', 'pink')
         ])

    cur.executemany(
        'INSERT INTO eyeliners(eyelinerId, nameOfProduct, brand, classification, country, price, eyelinerForm, color) VALUES (?, '
        '?,?,?,?,?,?,?)',
        [('1', 'Drama', 'Bourjois', 'elite', 'Italy', 485, 'cream', 'black'),
         ('2', 'Epic-Style', 'LOreal Paris', 'mass-market', 'USA', 394, 'liquid', 'black'),
         ('3', 'Celebrities', 'Maybelline New York', 'niche', 'Turkey', 294, 'pencil', 'black'),
         ('4', 'Precise Glow', 'Max Factor', 'professional', 'Ukraine', 495, 'powder', 'black'),
         ('5', 'Perfect Clim', 'Pupa', 'organic', 'Sweden', 291, 'stick', 'brown'),
         ('6', 'Instyle Gel', 'Oriflame', 'middle-market', 'Poland', 124, 'liquid', 'black'),
         ('7', 'Liquid Eye', 'Max Factor', 'mass-market', 'Ukraine', 145, 'cream', 'brown'),
         ('8', 'Sparkle Eyeliner', 'Pupa', 'mass-market', 'Sweden', 186, 'cream', 'brown'),
         ('9', 'Golden Rose', 'Oriflame', 'middle-market', 'Poland', 179, 'pencil', 'black')
         ])

    cur.executemany(
        'INSERT INTO lashPrimers(lashPrimerId, nameOfProduct, brand, classification, country, price, color) VALUES (?, '
        '?,?,?,?,?,?)',
        [('1', 'Variate', 'Bourjois', 'elite', 'Italy', 1231, 'pink'),
         ('2', 'Black Legend', 'LOreal Paris', 'mass-market', 'USA', 312, 'pink'),
         ('3', 'Gram-Face', 'Maybelline New York', 'niche', 'Turkey', 1452, 'black'),
         ('4', 'Rich Glow', 'Max Factor', 'professional', 'Ukraine', 394, 'pink'),
         ('5', 'Revival Volume', 'Pupa', 'organic', 'Sweden', 596, 'brown'),
         ('6', 'Booster', 'Oriflame', 'middle-market', 'Poland', 679, 'yellow'),
         ('7', 'Collistar', 'Max Factor', 'mass-market', 'Ukraine', 794, 'brown'),
         ('8', 'Dreamy', 'Pupa', 'mass-market', 'Sweden', 359, 'brown'),
         ('9', 'New Delia', 'Oriflame', 'middle-market', 'Poland', 607, 'pink')
         ])

    conn.commit()


def create_lips_tables():
    cur.execute("CREATE TABLE IF NOT EXISTS lipsticks(\n"
                "       lipsticksId INT PRIMARY KEY,\n"
                "       nameOfProduct TEXT,\n"
                "       brand brands,\n"
                "       classification classification,\n"
                "       country madeIn, \n"
                "       price INT,\n"
                "       lipsticksForm TEXT,\n"
                "       volume TEXT);\n"
                "    ")
    cur.execute("CREATE TABLE IF NOT EXISTS lipglosses(\n"
                "       lipglossesId INT PRIMARY KEY,\n"
                "       nameOfProduct TEXT,\n"
                "       brand brands,\n"
                "       classification classification,\n"
                "       country madeIn, \n"
                "       price INT,\n"
                "       lipglossesForm TEXT,\n"
                "       color colors);\n"
                "    ")
    cur.execute("CREATE TABLE IF NOT EXISTS lipliners(\n"
                "       liplinersId INT PRIMARY KEY,\n"
                "       nameOfProduct TEXT,\n"
                "       brand brands,\n"
                "       classification classification,\n"
                "       country madeIn, \n"
                "       price INT,\n"
                "       color colors);\n"
                "    ")
    cur.execute("CREATE TABLE IF NOT EXISTS liptints(\n"
                "       liptintsId INT PRIMARY KEY,\n"
                "       nameOfProduct TEXT,\n"
                "       brand brands,\n"
                "       classification classification,\n"
                "       country madeIn, \n"
                "       price INT,\n"
                "       color colors);\n"
                "    ")
    conn.commit()


def insert_lips_table():
    cur.executemany('INSERT INTO lipsticks(lipsticksId, nameOfProduct, brand, classification, country, price, '
                    'volume, lipsticksForm) VALUES (?,?,?,?,?,?,?,?)',
                    [('1', 'LipFinity', 'Bourjois', 'elite', 'Italy', 2000, 'big', 'cream'),
                     ('2', 'Glam Look', 'LOreal Paris', 'mass-market', 'USA', 300, 'medium', 'cream'),
                     ('3', 'Brilliant Idole', 'Maybelline New York', 'niche', 'Turkey', 4390, 'big', 'gel'),
                     ('4', 'Sensational', 'Max Factor', 'professional', 'Ukraine', 1200, 'medium', 'gel'),
                     ('5', 'Glamour', 'Pupa', 'organic', 'Sweden', 690, 'big', 'lasting'),
                     ('6', 'Velvet', 'Oriflame', 'middle-market', 'Poland', 499, 'medium', 'gel'),
                     ('7', 'Unlimited', 'Max Factor', 'mass-market', 'Ukraine', 560, 'big', 'lasting'),
                     ('8', 'Finish Lipstick', 'Pupa', 'mass-market', 'Sweden', 958, 'low', 'cream'),
                     ('9', 'Soft Matte', 'Oriflame', 'middle-market', 'Poland', 375, 'low', 'cream')
                     ])

    cur.executemany(
        'INSERT INTO lipglosses(lipglossesId, nameOfProduct, brand, classification, country, price, lipglossesForm, color) VALUES (?,'
        '?,?,?,?,?,?,?)',
        [('1', 'KIKO', 'Bourjois', 'elite', 'Italy', 1134, 'cream', 'red'),
         ('2', 'Butter Gloss', 'LOreal Paris', 'mass-market', 'USA', 495, 'cream', 'blue'),
         ('3', 'Maximizer', 'Maybelline New York', 'niche', 'Turkey', 219, 'cream', 'black'),
         ('4', 'Shine Glow', 'Max Factor', 'professional', 'Ukraine', 708, 'gel', 'pink'),
         ('5', 'Loud Max', 'Pupa', 'organic', 'Sweden', 806, '', 'gel'),
         ('6', 'Viper Lip', 'Oriflame', 'middle-market', 'Poland', 670, 'lasting', 'yellow'),
         ('7', 'Color Booster', 'Max Factor', 'mass-market', 'Ukraine', 543, 'gel', 'brown'),
         ('8', 'Dreamy', 'Pupa', 'mass-market', 'Sweden', 670, 'cream', 'brown'),
         ('9', 'New Look', 'Oriflame', 'middle-market', 'Poland', 346, 'cream', 'pink')
         ])

    cur.executemany(
        'INSERT INTO lipliners(liplinersId, nameOfProduct, brand, classification, country, price, color) VALUES (?, '
        '?,?,?,?,?,?)',
        [('1', 'Viper Revolution', 'Bourjois', 'elite', 'Italy', 552, 'pink'),
         ('2', 'Style', 'LOreal Paris', 'mass-market', 'USA', 132, 'pink'),
         ('3', 'Maximizer', 'Maybelline New York', 'niche', 'Turkey', 421, 'black'),
         ('4', 'Balm Glow', 'Max Factor', 'professional', 'Ukraine', 134, 'pink'),
         ('5', 'Nude Cozy', 'Pupa', 'organic', 'Sweden', 312, 'brown'),
         ('6', 'Lip Color', 'Oriflame', 'middle-market', 'Poland', 234, 'yellow'),
         ('7', 'Look Star', 'Max Factor', 'mass-market', 'Ukraine', 240, 'brown'),
         ('8', 'Suede Jo', 'Pupa', 'mass-market', 'Sweden', 402, 'brown'),
         ('9', 'Lip Liner', 'Oriflame', 'middle-market', 'Poland', 500, 'pink')
         ])

    cur.executemany(
        'INSERT INTO liptints(liptintsId, nameOfProduct, brand, classification, country, price, color) VALUES (?, '
        '?,?,?,?,?,?)',
        [('1', 'Yadan Be', 'Bourjois', 'elite', 'Italy', 593, 'black'),
         ('2', 'Revlon-Kiss', 'LOreal Paris', 'mass-market', 'USA', 39, 'black'),
         ('3', 'Dermacol', 'Maybelline New York', 'niche', 'Turkey', 596, 'black'),
         ('4', 'It`s skin', 'Max Factor', 'professional', 'Ukraine', 294, 'black'),
         ('5', 'Holika Clim', 'Pupa', 'organic', 'Sweden', 291, 'brown'),
         ('6', 'Gabriella Gel', 'Oriflame', 'middle-market', 'Poland', 134, 'black'),
         ('7', 'TikTok Tint', 'Max Factor', 'mass-market', 'Ukraine', 1345, 'brown'),
         ('8', 'Golden Tint', 'Pupa', 'mass-market', 'Sweden', 421, 'brown'),
         ('9', 'Brilliant Rose', 'Oriflame', 'middle-market', 'Poland', 6764, 'black')
         ])

    conn.commit()


def create_face_tables():
    cur.execute("CREATE TABLE IF NOT EXISTS facePrimers(\n"
                "       facePrimerId INT PRIMARY KEY,\n"
                "       nameOfProduct TEXT,\n"
                "       brand brands,\n"
                "       classification classification,\n"
                "       country madeIn, \n"
                "       price INT,\n"
                "       volume TEXT,\n"
                "       facePrimerForm TEXT);\n"
                "    ")
    cur.execute("CREATE TABLE IF NOT EXISTS BBcreams(\n"
                "       BBcreamId INT PRIMARY KEY,\n"
                "       nameOfProduct TEXT,\n"
                "       brand brands,\n"
                "       classification classification,\n"
                "       country madeIn, \n"
                "       price INT,\n"
                "       BBcreamForm TEXT,\n"
                "       color colors);\n"
                "    ")
    cur.execute("CREATE TABLE IF NOT EXISTS blushes(\n"
                "       blushId INT PRIMARY KEY,\n"
                "       nameOfProduct TEXT,\n"
                "       brand brands,\n"
                "       classification classification,\n"
                "       country madeIn, \n"
                "       price INT,\n"
                "       color colors);\n"
                "    ")
    cur.execute("CREATE TABLE IF NOT EXISTS bronzers(\n"
                "       bronzerId INT PRIMARY KEY,\n"
                "       nameOfProduct TEXT,\n"
                "       brand brands,\n"
                "       classification classification,\n"
                "       country madeIn, \n"
                "       price INT,\n"
                "       color colors);\n"
                "    ")

    cur.execute("CREATE TABLE IF NOT EXISTS concealers(\n"
                "       concealerId INT PRIMARY KEY,\n"
                "       nameOfProduct TEXT,\n"
                "       brand brands,\n"
                "       classification classification,\n"
                "       country madeIn, \n"
                "       price INT,\n"
                "       color colors);\n"
                "    ")
    conn.commit()


def insert_face_table():
    cur.executemany('INSERT INTO facePrimers(facePrimerId, nameOfProduct, brand, classification, country, price, '
                    'volume, facePrimerForm) VALUES (?,?,?,?,?,?,?,?)',
                    [('1', 'Pore Filler', 'Bourjois', 'elite', 'Italy', 3942, 'big', 'cream'),
                     ('2', 'Primer', 'LOreal Paris', 'mass-market', 'USA', 300, 'medium', 'cream'),
                     ('3', 'Brilliant Primer', 'Maybelline New York', 'niche', 'Turkey', 4453, 'big', 'gel'),
                     ('4', 'Sensational', 'Max Factor', 'professional', 'Ukraine', 1200, 'medium', 'gel'),
                     ('5', 'Glow Face', 'Pupa', 'organic', 'Sweden', 690, 'big', 'lasting'),
                     ('6', 'MakeUp Base', 'Oriflame', 'middle-market', 'Poland', 536, 'medium', 'gel'),
                     ('7', 'Baby skin', 'Max Factor', 'mass-market', 'Ukraine', 560, 'big', 'lasting'),
                     ('8', 'Rimmer Fix', 'Pupa', 'mass-market', 'Sweden', 958, 'low', 'cream'),
                     ('9', 'Poreless', 'Oriflame', 'middle-market', 'Poland', 375, 'low', 'cream')
                     ])

    cur.executemany(
        'INSERT INTO BBcreams(BBcreamId, nameOfProduct, brand, classification, country, price, BBcreamForm, '
        'color) VALUES (?, '
        '?,?,?,?,?,?,?)',
        [('1', 'KIKO skin', 'Bourjois', 'elite', 'Italy', 1134, 'cream', 'red'),
         ('2', 'Butter Gloss', 'LOreal Paris', 'mass-market', 'USA', 495, 'cream', 'blue'),
         ('3', 'Maximizer Primer', 'Maybelline New York', 'niche', 'Turkey', 219, 'cream', 'black'),
         ('4', 'Shine BB', 'Max Factor', 'professional', 'Ukraine', 708, 'gel', 'pink'),
         ('5', 'Loud BB', 'Pupa', 'organic', 'Sweden', 806, '', 'gel'),
         ('6', 'Viper BB', 'Oriflame', 'middle-market', 'Poland', 670, 'lasting', 'yellow'),
         ('7', 'Color BB', 'Max Factor', 'mass-market', 'Ukraine', 543, 'gel', 'brown'),
         ('8', 'Dreamy BB', 'Pupa', 'mass-market', 'Sweden', 670, 'cream', 'brown'),
         ('9', 'New BB Look', 'Oriflame', 'middle-market', 'Poland', 346, 'cream', 'pink')
         ])

    cur.executemany(
        'INSERT INTO blushes(blushId, nameOfProduct, brand, classification, country, price, color) VALUES (?, '
        '?,?,?,?,?,?)',
        [('1', 'Viper Cheek Color', 'Bourjois', 'elite', 'Italy', 552, 'pink'),
         ('2', 'Style Cheek', 'LOreal Paris', 'mass-market', 'USA', 132, 'pink'),
         ('3', 'Maximizer Cheek', 'Maybelline New York', 'niche', 'Turkey', 421, 'black'),
         ('4', 'Cheek Glow', 'Max Factor', 'professional', 'Ukraine', 134, 'pink'),
         ('5', 'Silk Dream', 'Pupa', 'organic', 'Sweden', 312, 'brown'),
         ('6', 'Blush Palette', 'Oriflame', 'middle-market', 'Poland', 234, 'yellow'),
         ('7', 'Blush Stick', 'Max Factor', 'mass-market', 'Ukraine', 240, 'brown'),
         ('8', 'Blush Powder', 'Pupa', 'mass-market', 'Sweden', 402, 'brown'),
         ('9', 'Blush Liner', 'Oriflame', 'middle-market', 'Poland', 500, 'pink')
         ])

    cur.executemany(
        'INSERT INTO bronzers(bronzerId, nameOfProduct, brand, classification, country, price, color) VALUES (?, '
        '?,?,?,?,?,?)',
        [('1', 'Butter Be', 'Bourjois', 'elite', 'Italy', 593, 'black'),
         ('2', 'Torre-Bronzer', 'LOreal Paris', 'mass-market', 'USA', 39, 'black'),
         ('3', 'Contour Palette', 'Maybelline New York', 'niche', 'Turkey', 596, 'black'),
         ('4', 'It`s skin bronzer', 'Max Factor', 'professional', 'Ukraine', 294, 'black'),
         ('5', 'Holika bronzer', 'Pupa', 'organic', 'Sweden', 291, 'brown'),
         ('6', 'Gabriella bronzer', 'Oriflame', 'middle-market', 'Poland', 134, 'black'),
         ('8', 'Bronzer toy', 'Pupa', 'mass-market', 'Sweden', 421, 'brown'),
         ('9', 'Brilliant bronzer', 'Oriflame', 'middle-market', 'Poland', 6764, 'black')
         ])

    cur.executemany(
        'INSERT INTO concealers(concealerId, nameOfProduct, brand, classification, country, price, color) VALUES (?, '
        '?,?,?,?,?,?)',
        [('1', 'Style concealer', 'Bourjois', 'elite', 'Italy', 593, 'pink'),
         ('2', 'Revlon-concealer', 'LOreal Paris', 'mass-market', 'USA', 39, 'black'),
         ('3', 'White and shy', 'Maybelline New York', 'niche', 'Turkey', 596, 'pink'),
         ('4', 'It`s concealer', 'Max Factor', 'professional', 'Ukraine', 294, 'pink'),
         ('5', 'Holika concealer', 'Pupa', 'organic', 'Sweden', 291, 'brown'),
         ('6', 'Gabriella concealer', 'Oriflame', 'middle-market', 'Poland', 134, 'black'),
         ('7', 'TikTok concealer', 'Max Factor', 'mass-market', 'Ukraine', 1345, 'pink'),
         ('8', 'Golden concealer', 'Pupa', 'mass-market', 'Sweden', 421, 'pink'),
         ('9', 'Brilliant concealer', 'Oriflame', 'middle-market', 'Poland', 6764, 'black')
         ])

    conn.commit()


def create_brows_tables():
    cur.execute("CREATE TABLE IF NOT EXISTS browPowders(\n"
                "       browPowderId INT PRIMARY KEY,\n"
                "       nameOfProduct TEXT,\n"
                "       brand brands,\n"
                "       classification classification,\n"
                "       country madeIn, \n"
                "       price INT,\n"
                "       volume TEXT,\n"
                "       facePrimerForm TEXT);\n"
                "    ")
    cur.execute("CREATE TABLE IF NOT EXISTS browMascaras(\n"
                "       browMascaraId INT PRIMARY KEY,\n"
                "       nameOfProduct TEXT,\n"
                "       brand brands,\n"
                "       classification classification,\n"
                "       country madeIn, \n"
                "       price INT,\n"
                "       BBcreamForm TEXT,\n"
                "       color colors);\n"
                "    ")
    cur.execute("CREATE TABLE IF NOT EXISTS browPencil(\n"
                "       browPencilId INT PRIMARY KEY,\n"
                "       nameOfProduct TEXT,\n"
                "       brand brands,\n"
                "       classification classification,\n"
                "       country madeIn, \n"
                "       price INT,\n"
                "       color colors);\n"
                "    ")

    conn.commit()


def insert_brows_table():
    cur.executemany('INSERT INTO browPowders(browPowderId, nameOfProduct, brand, classification, country, price, '
                    'volume, facePrimerForm) VALUES (?,?,?,?,?,?,?,?)',
                    [('1', 'Pore powder', 'Bourjois', 'elite', 'Italy', 2834, 'big', 'cream'),
                     ('2', 'Maxi brows', 'LOreal Paris', 'mass-market', 'USA', 324, 'medium', 'cream'),
                     ('3', 'Brilliant brows', 'Maybelline New York', 'niche', 'Turkey', 4453, 'big', 'gel'),
                     ('4', 'Sensational', 'Max Factor', 'professional', 'Ukraine', 2542, 'medium', 'gel'),
                     ('5', 'Glow powder', 'Pupa', 'organic', 'Sweden', 690, 'big', 'lasting'),
                     ('6', 'MakeUp powder', 'Oriflame', 'middle-market', 'Poland', 542, 'medium', 'gel'),
                     ('7', 'Baby powder', 'Max Factor', 'mass-market', 'Ukraine', 560, 'big', 'lasting'),
                     ('8', 'Powder brows', 'Pupa', 'mass-market', 'Sweden', 958, 'low', 'cream'),
                     ('9', 'Brows star', 'Oriflame', 'middle-market', 'Poland', 375, 'low', 'cream')
                     ])

    cur.executemany(
        'INSERT INTO browMascaras(browMascaraId, nameOfProduct, brand, classification, country, price, BBcreamForm, '
        'color) VALUES (?, '
        '?,?,?,?,?,?,?)',
        [('1', 'KIKO brows mascara', 'Bourjois', 'elite', 'Italy', 1134, 'cream', 'red'),
         ('2', 'Butter brows mascara', 'LOreal Paris', 'mass-market', 'USA', 495, 'cream', 'blue'),
         ('3', 'Maximizer Primer', 'Maybelline New York', 'niche', 'Turkey', 219, 'cream', 'black'),
         ('4', 'Shine brows mascara', 'Max Factor', 'professional', 'Ukraine', 708, 'gel', 'pink'),
         ('5', 'Loud brows mascara', 'Pupa', 'organic', 'Sweden', 806, '', 'gel'),
         ('6', 'Viper oh oui!', 'Oriflame', 'middle-market', 'Poland', 670, 'lasting', 'yellow'),
         ('7', 'Color brows', 'Max Factor', 'mass-market', 'Ukraine', 543, 'gel', 'brown'),
         ('8', 'Dreamy brows', 'Pupa', 'mass-market', 'Sweden', 670, 'cream', 'brown'),
         ('9', 'Coutore Brows', 'Oriflame', 'middle-market', 'Poland', 346, 'cream', 'pink')
         ])

    cur.executemany(
        'INSERT INTO browPencil(browPencilId, nameOfProduct, brand, classification, country, price, color) VALUES (?, '
        '?,?,?,?,?,?)',
        [('1', 'Rimmer Cheek Color', 'Bourjois', 'elite', 'Italy', 552, 'pink'),
         ('2', 'Style Cheek', 'LOreal Paris', 'mass-market', 'USA', 132, 'pink'),
         ('3', 'Maximizer Cheek', 'Maybelline New York', 'niche', 'Turkey', 421, 'black'),
         ('4', 'Color tindet', 'Max Factor', 'professional', 'Ukraine', 134, 'pink'),
         ('5', 'Brows Dream', 'Pupa', 'organic', 'Sweden', 312, 'brown'),
         ('6', 'Blush Palette', 'Oriflame', 'middle-market', 'Poland', 234, 'yellow'),
         ('7', 'Brow fix', 'Max Factor', 'mass-market', 'Ukraine', 240, 'brown'),
         ('8', 'Pencil Creation', 'Pupa', 'mass-market', 'Sweden', 402, 'brown'),
         ('9', 'The browcara', 'Oriflame', 'middle-market', 'Poland', 500, 'pink')
         ])

    conn.commit()


def create_common():
    cur.execute("CREATE TABLE IF NOT EXISTS commonFace(item TEXT PRIMARY KEY);")
    cur.execute("CREATE TABLE IF NOT EXISTS commonEyes(item TEXT PRIMARY KEY);")
    cur.execute("CREATE TABLE IF NOT EXISTS commonLips(item TEXT PRIMARY KEY);")
    cur.execute("CREATE TABLE IF NOT EXISTS commonLash(item TEXT PRIMARY KEY);")
    conn.commit()


def insertCommon():
    cur.executemany('INSERT INTO commonFace(item) VALUES (?)',
                    [('BBcreams',),
                     ('blushes',),
                     ('bronzers',),
                     ('facePrimers',),
                     ('concealers',)
                     ])
    cur.executemany('INSERT INTO commonEyes(item) VALUES (?)',
                    [('eyeConcealers',),
                     ('eyeliners',),
                     ('eyeshadows',),
                     ('mascara',)
                     ])
    cur.executemany('INSERT INTO commonLips(item) VALUES (?)',
                    [('lipglosses',),
                     ('lipliners',),
                     ('lipsticks',),
                     ('liptints',)
                     ])
    cur.executemany('INSERT INTO commonLash(item) VALUES (?)',
                    [('browMascaras',),
                     ('browPencil',),
                     ('browPowders',),
                     ('lashPrimers',)
                     ])
    conn.commit()


def show_face_products_types():
    return select('SELECT item FROM commonFace')


def show_eyes_products_types():
    return select('SELECT item FROM commonEyes')


def show_lips_products_types():
    return select('SELECT item FROM commonLips')


def show_lash_products_types():
    return select('SELECT item FROM commonLash')


def show_lipglosses():
    return select('SELECT brand, nameOfProduct, brand, classification, country, price FROM lipglosses')


def show_lipsticks():
    return select('SELECT brand, nameOfProduct, brand, classification, country, price FROM lipsticks')


def show_liptints():
    return select('SELECT brand, nameOfProduct, brand, classification, country, price FROM liptints')


def show_lipliners():
    return select('SELECT brand, nameOfProduct, brand, classification, country, price FROM lipliners')


def show_all_lips_products():
    return show_lipglosses() + show_lipliners() + show_lipsticks() + show_liptints()


def show_eyeConcealers():
    return select('SELECT brand, nameOfProduct, brand, classification, country, price FROM eyeConcealers')


def show_eyeliners():
    return select('SELECT brand, nameOfProduct, brand, classification, country, price FROM eyeliners')


def show_eyeshadows():
    return select('SELECT brand, nameOfProduct, brand, classification, country, price FROM eyeshadows')


def show_mascara():
    return select('SELECT brand, nameOfProduct, brand, classification, country, price FROM mascara')


def show_all_eyes_products():
    return show_eyeConcealers() + show_eyeliners() + show_eyeshadows() + show_mascara()


def show_BBcreams():
    return select('SELECT brand, nameOfProduct, brand, classification, country, price  FROM BBcreams')


def show_blushes():
    return select('SELECT brand, nameOfProduct, brand, classification, country, price  FROM blushes')


def show_bronzers():
    return select('SELECT brand, nameOfProduct, brand, classification, country, price  FROM bronzers')


def show_face_primers():
    return select('SELECT brand, nameOfProduct, brand, classification, country, price  FROM faceprimers')


def show_concealers():
    return select('SELECT brand, nameOfProduct, brand, classification, country, price  FROM concealers')


def show_all_face_products():
    return show_BBcreams() + show_blushes() + show_bronzers() + show_face_primers() + show_concealers()


def show_brow_mascaras():
    return select('SELECT brand, nameOfProduct, brand, classification, country, price FROM BrowMascaras')


def show_brow_pencil():
    return select('SELECT brand, nameOfProduct, brand, classification, country, price FROM BrowPencil')


def show_brow_powders():
    return select('SELECT brand, nameOfProduct, brand, classification, country, price FROM BrowPowders')


def show_lash_primers():
    return select('SELECT brand, nameOfProduct, brand, classification, country, price FROM lashPrimers')


def show_all_lash_products():
    return show_brow_mascaras() + show_brow_pencil() + show_brow_powders() + show_lash_primers()


def show_all_products():
    return show_all_lips_products() + show_all_lash_products() + show_all_face_products() + show_all_eyes_products()


def show_all_products_types():
    face = show_face_products_types()
    eyes = show_eyes_products_types()
    lips = show_lips_products_types()
    lash = show_lash_products_types()
    return face + eyes + lips + lash


def db_find_lips_by_range_price(a, b):
    return select('SELECT nameOfProduct, brand, price FROM lipglosses WHERE price BETWEEN ? AND ? '
                  'UNION ALL '
                  'SELECT nameOfProduct, brand, price FROM lipsticks WHERE price BETWEEN ? AND ? '
                  'UNION ALL '
                  'SELECT nameOfProduct, brand, price FROM liptints WHERE price BETWEEN ? AND ? '
                  'UNION ALL '
                  'SELECT nameOfProduct, brand, price FROM lipliners WHERE price BETWEEN ? AND ?',
                  (a, b, a, b, a, b, a, b))


def db_find_eyes_by_range_price(a, b):
    return select('SELECT nameOfProduct, brand, price FROM eyeConcealers WHERE price BETWEEN ? AND ? '
                  'UNION ALL '
                  'SELECT nameOfProduct, brand, price FROM eyeliners WHERE price BETWEEN ? AND ? '
                  'UNION ALL '
                  'SELECT nameOfProduct, brand, price FROM eyeshadows WHERE price BETWEEN ? AND ? '
                  'UNION ALL '
                  'SELECT nameOfProduct, brand, price FROM mascara WHERE price BETWEEN ? AND ?',
                  (a, b, a, b, a, b, a, b))


def db_find_face_by_range_price(a, b):
    return select('SELECT nameOfProduct, brand, price FROM BBcreams WHERE price BETWEEN ? AND ? '
                  'UNION ALL '
                  'SELECT nameOfProduct, brand, price FROM blushes WHERE price BETWEEN ? AND ? '
                  'UNION ALL '
                  'SELECT nameOfProduct, brand, price FROM bronzers WHERE price BETWEEN ? AND ? '
                  'UNION ALL '
                  'SELECT nameOfProduct, brand, price FROM faceprimers WHERE price BETWEEN ? AND ?'
                  'UNION ALL '
                  'SELECT nameOfProduct, brand, price FROM concealers WHERE price BETWEEN ? AND ?',
                  (a, b, a, b, a, b, a, b, a, b))


def db_find_lash_by_range_price(a, b):
    return select('SELECT nameOfProduct, brand, price FROM BrowMascaras WHERE price BETWEEN ? AND ? '
                  'UNION ALL '
                  'SELECT nameOfProduct, brand, price FROM BrowPencil WHERE price BETWEEN ? AND ? '
                  'UNION ALL '
                  'SELECT nameOfProduct, brand, price FROM BrowPowders WHERE price BETWEEN ? AND ? '
                  'UNION ALL '
                  'SELECT nameOfProduct, brand, price FROM lashPrimers WHERE price BETWEEN ? AND ?',
                  (a, b, a, b, a, b, a, b))


def select(query, parameters=None):
    if parameters:
        cur.execute(query, parameters)
    else:
        cur.execute(query)
    rows = cur.fetchall()
    products = []
    if rows:
        for row in rows:
            products.append(row)
        return rows
    else:
        return "Sorry, we found nothing for your request."


def create_db():
    create_common_tables()
    create_eyes_tables()
    insert_common_table()
    insert_eyes_table()
    create_lips_tables()
    insert_lips_table()
    create_face_tables()
    insert_face_table()
    create_brows_tables()
    insert_brows_table()
    create_common()
    insertCommon()
