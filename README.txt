Version 1.0

Prerequisites:
-	Python 2 dernière version (ne fontionne pas avec Python 3)

Features:
-	Parse le fichier memstruct_entry.txt qui contient la définition des messages et signaux CAN d'Éclipse
-	Génère le fichier memstruct.c pour le stack CAN des microcontrôleurs
-	Génère le fichier memstruct.h pour le stack CAN des microcontrôleurs
-	Génère le fichier protocoleV9.xml pour la télémétrie Java
-	Génère le fichier CAN_DB_E9.dbc pour le logiciel CANAlyzer de Vector
-	Vérification partielle des entries

TODO:
-	Ajouter les global define au debut du .h
-	Vérification de l'intégrité des messages
-	Tester la détection d'erreurs dans le parser
-	Ajouter plus de datatypes pour supporter les uint32_t par exemple et pas juste U32

HOW TO USE:

La memstruct est séparée en 3, on y retouve les boards, les messages et les signaux. Chaque board a des messages qui eux possèdent des signaux.

Pour chaque Board on entre sa string de définition:
b:board_name, board_offset, is_extended, is_little_endian

Ensuite on définit chacun des messages avec ses signaux:
m:message_name, message_id
s:signal_name, data_type, init_value, factor, offset, unit, min_value, max_value

Une fois les entries de completées, runnez le script eclipseMemstructGen.py

Types supportés: 8, 16, 32, U8, U16, U32, F

**IMPORTANT**
-	N'utilisez que des caractères ASCII pour les unités (pas de '%', de '°' ou de 'é')
-	Le nom des messages ou signaux ne doit pas dépasser 32 caractères (requis pour la DB du CANAlyzer)
-	La liste des signaux dans les messages commence par celui qui occupe le LSB (offset 0)
-	Si le signal n'a pas d'unité, inscrivez n/a

Exemple du memstruct_entry.txt:

b:BMS, 0x100, 0, 1
m:M_BMS_HEARTBEAT, 0x00
s:S_BMS_DEVICEID, 		U32,	0,	0,	0,	ID,     0, 100
s:S_BMD_SERIAL, 		U32,	0,	0,	0,	Serial, 0, 100

m:M_BMS_CMU1_ID_TEMP, 0x01
s:S_BMS_CMU1_SERIAL,	U32, 0,	0,	0,	Serial, 0, 100
s:S_BMS_CMU1_PCB_TEMP,	16,  0,	0,	0,	Deg,    0, 100
s:S_BMS_CMU1_CELL_TEMP,	16,	 0,	0,	0,	Deg,    0, 100

b:DRIVE, 0x200, 0, 1
...