Version 1.0

Features:
-	parse le fichier memstruct_entry.txt et construit la structure de la memstruct
-	Genere le fichier memstruct.c
-	Genere le fichier memstruct.h
-	Verification partiel des entry

TODO:
-Ajouter les global define au debut du .h
-Generer le XML pour la telemetrie
-Generer les XML pour le vector
-Verification de l'intégrite des messages
-Tester la detection d'erreur dans le parser
-ajouter plus de datatype pour supporter les uint32_t par exemple et pas juste U32


HOW TO USE:

La memstruct est séparer en 3, on y retouve les boards, les messages et les signaux. Chaque board à des messages can qui eux possède des signaux.

Pour chaque Board on entre sa string de définition:
b:Board_name,Board_offset,Is_extended, is_little_endian

Ensuite on définie chacun des messages avec ces signaux 
m:Message_name,message_id
s:signal_name,signaldatatype,init_value,factor,offset,unit

une fois les entry de completer, runner le script eclipseMemstructGen.py

Exemple:

b:BMS, 0x100, 0, 1
m:M_BMS_HEARTBEAT, 0x00
s:S_BMS_DEVICEID, 		U32,	0,	0,	0,	ID
s:S_BMD_SERIAL, 		U32,	0,	0,	0,	Serial

m:M_BMS_CMU1_ID_TEMP, 0x01
s:S_BMS_CMU1_SERIAL,	U32,	0,	0,	0,	Serial
s:S_BMS_CMU1_PCB_TEMP,	U16,	0,	0,	0,	Degré
s:S_BMS_CMU1_CELL_TEMP,	U16,	0,	0,	0,	Degré

b:bla bla bla