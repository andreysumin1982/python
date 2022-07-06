Скрипт парсит коммутаторы серии (Catalyst, SG300) в открытом контуре (internet) на наличие портов со статусом "admin down" ,"shutdown".
При нахождении, предлагает (ВКЛ, ВЫКЛ) порты. 

----------------------------------
Коммутатор: iSG***-3-1-1
----------------------------------
gi1       FSTEK room_315 Down
gi2       FSTEK room_303 Down
gi5       FSTEK *** k309 083-010-> k305 Down
gi7       FSTEK room_304.1 Down
gi9       FSTEK room_304.2 Down
gi12      FSTEK *** k302 Down
gi13      FSTEK room_307 Down
gi14      FSTEK *** k306 Down
gi18      FSTEK *** k421 Down

Найдено: 9 портов 
Время поиска: 0:00:09 
-----------------------------------------------

Включить или выключить порты: "on"/"off"
Выйти: "Enter"
>: 
aa@test:~/

Включение портов
----------------------------------
Коммутатор: iSG***-3-1-1
----------------------------------
gi1       FSTEK room_315 Down
gi2       FSTEK room_303 Down
gi5       FSTEK *** k309 083-010-> k305 Down
gi7       FSTEK room_304.1 Down
gi9       FSTEK room_304.2 Down
gi12      FSTEK *** k302 Down
gi13      FSTEK room_307 Down
gi14      FSTEK *** k306 Down
gi18      FSTEK *** k421 Down

Найдено: 9 портов 
Время поиска: 0:00:09 
-----------------------------------------------

Включить или выключить порты: "on"/"off"
Выйти: "Enter"
>: on
[1, 2] - no sh
[5] - no sh
[7] - no sh
[9] - no sh
[12, 13, 14] - no sh
[18] - no sh
Время выполнения: 0:00:59
