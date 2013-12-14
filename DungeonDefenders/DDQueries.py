DDQUERIES = {
    'createdb': {
        'drop_tables':[
            'DROP TABLE IF EXISTS Stats;',
            'DROP TABLE IF EXISTS Hero;',
            'DROP TABLE IF EXISTS Armor;',
            'DROP TABLE IF EXISTS ArmorSet;'
        ],
        'create_tables':[
            '''CREATE TABLE IF NOT EXISTS Stats (
                Stats_ID INTEGER PRIMARY KEY AUTOINCREMENT,

                Stats_Value INTEGER,
                Stats_Level INTEGER,
                Stats_Max_Level INTEGER,

                Stats_Hero_Health INTEGER,
                Stats_Hero_Damage INTEGER,
                Stats_Hero_Speed INTEGER,
                Stats_Hero_Casting_Rate INTEGER,

                Stats_Hero_Special1 INTEGER,
                Stats_Hero_Special2 INTEGER,

                Stats_Defense_Health INTEGER,
                Stats_Defense_Damage INTEGER,
                Stats_Defense_Area_Effect INTEGER,
                Stats_Defense_Attack_Rate INTEGER,

                Stats_Armor_Resist_Base INTEGER,
                Stats_Armor_Resist_Fire INTEGER,
                Stats_Armor_Resist_Electric INTEGER,
                Stats_Armor_Resist_Poison INTEGER
            );''',
            '''CREATE TABLE IF NOT EXISTS Hero(
                Hero_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Stats_ID INTEGER,
                ArmorSet_ID INTEGER,

                Hero_Name TEXT
            );''',
            '''CREATE TABLE IF NOT EXISTS Armor(
                Armor_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Stats_ID INTEGER,
                Armor_Name TEXT,

                Armor_Quality TEXT,
                Armor_Type TEXT,
                Armor_Kind TEXT
            );''',
            '''CREATE TABLE IF NOT EXISTS ArmorSet(
                ArmorSet_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                ArmorSet_Name TEXT,

                ArmorSet_Helm_ID INTEGER,
                ArmorSet_Chest_ID INTEGER,
                ArmorSet_Gloves_ID INTEGER,
                ArmorSet_Boots_ID INTEGER
            );'''
        ]
    },
    'modifydb': {
        'insert': {
            'Stats':'''INSERT INTO Stats(Stats_Value,
                                    Stats_Level,
                                    Stats_Max_Level,
                                    Stats_Hero_Health,
                                    Stats_Hero_Damage,
                                    Stats_Hero_Speed,
                                    Stats_Hero_Casting_Rate,
                                    Stats_Hero_Special1,
                                    Stats_Hero_Special2,
                                    Stats_Defense_Health,
                                    Stats_Defense_Damage,
                                    Stats_Defense_Area_Effect,
                                    Stats_Defense_Attack_Rate,
                                    Stats_Armor_Resist_Base,
                                    Stats_Armor_Resist_Fire,
                                    Stats_Armor_Resist_Electric,
                                    Stats_Armor_Resist_Poison) 
                       VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);''',
            'Hero':'INSERT INTO Hero(Stats_ID, ArmorSet_ID, Hero_Name) VALUES(?,?,?);',
            'Armor':'''INSERT INTO
                       Armor(Stats_ID,
                             Armor_Name,
                             Armor_Quality,
                             Armor_Type,
                             Armor_Kind)
                       VALUES(?,?,?,?,?);''',
            'ArmorSet':'''INSERT INTO ArmorSet(ArmorSet_Name,
                                            ArmorSet_Helm_ID, 
                                            ArmorSet_Chest_ID, 
                                            ArmorSet_Gloves_ID, 
                                            ArmorSet_Boots_ID) 
                          VALUES(?,?,?,?,?);'''
        },
        'update': {
            'Stats':'''UPDATE Stats
                       SET Stats_Value = ?
                           Stats_Level = ?,
                           Stats_Max_Level = ?,
                           Stats_Hero_Health = ?,
                           Stats_Hero_Damage = ?,
                           Stats_Hero_Speed = ?,
                           Stats_Hero_Casting_Rate = ?,
                           Stats_Hero_Special1 = ?,
                           Stats_Hero_Special2 = ?,
                           Stats_Defense_Health = ?,
                           Stats_Defense_Damage = ?,
                           Stats_Defense_Area_Effect = ?,
                           Stats_Defense_Attack_Rate = ?,
                           Stats_Armor_Resist_Base = ?,
                           Stats_Armor_Resist_Fire = ?,
                           Stats_Armor_Resist_Electric = ?,
                           Stats_Armor_Resist_Poison = ?
                       WHERE Stats_ID = ?;''',
            'Hero':'UPDATE Hero SET Stats_ID = ?, ArmorSet_ID = ?, Hero_Name = ? WHERE Hero_ID = ?;',
            'Armor':'UPDATE Armor SET Stats_ID = ?, Armor_Name = ? WHERE Armor_ID = ?;',
            'ArmorSet':'''UPDATE ArmorSet SET ArmorSet_Name = ?,
                                              ArmorSet_Helm_ID = ?, 
                                              ArmorSet_Chest_ID = ?, 
                                              ArmorSet_Gloves_ID = ?, 
                                              ArmorSet_Boots_ID = ?
                          WHERE ArmorSet_ID = ?;'''
        }
    }
}
