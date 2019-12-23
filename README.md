# Ultimate proxy master
ver 1.5.1 
Пофикшены баги, сделана возможность делать фильтрацию подсетей в двух режимах. Добавлен выход на ctrl + c
## Что это такое?
Это программа для парсинга, обработки, и фильтрации проксей. Она парсит прокси и прогоняет их через различные фильтры, о которых ниже. Так же эта возможно написание самостоятельной проверки путем собственного запроса на сайт.  

## Как запускать?
1. Заходим на `https://www.python.org/` и ставим питон  
2. Запускаем `python main.py` или если 2 питона `python3 main.py`. поддерживает запуск `./main.py`  
3. Ждем, прогресс можно наблюдать в выводах консоли  
4. Берем готовый продукт из `proxies.txt`, забаненные прокси в `banned.txt`, мертвые прокси в `died.txt`  

## Как настроить под себя?  
**АТЕНШН!** По дефолту все работает изкоробки! Настраивать не обязательно!  
В папке **texts** находятся файлы для фильтров  
`subnets.txt` - файл содержит в себе записи о подсетях в CIDR формате (пример: `0.0.0.0/8`), скрипт удаляет все прокси из этих подсетей  
`blacklist.txt` - файл содержит в себе айпи, которые скрипт будет убирать   
`countries.txt` - сюда вписывать страны, айпи из которых будет убирать скрипт, уже стоит свежая база данных. Но при желании можно погуглить базы для `pygeoip`, которых много. Страны вписывать на английском с большой буквы.  
`ASN.txt` - сюда вписывать ASN номер провайдера, айпи которого будут удаляться. Это гораздол легче тонны подсетей. Пример формата для вписывания: `AS16276` . По дефолту уже лежат ASN провайдеры, чьи айпи заблокированы на сосаче. [Что это такое?](https://ru.wikipedia.org/wiki/%D0%90%D0%B2%D1%82%D0%BE%D0%BD%D0%BE%D0%BC%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0_(%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82))  
`headers.json` - здесь хранятся заголовки для двух типов запросов. `HEADERS_2CH` это заголовки для проверки проксей. `HEADERS_CUSTOM` заголовки для отправки реквеста к `WEBFORPING`. Юзерагенты к обоим заголовкам берутся из `usrAgents.txt` рандомно для каждого запроса.  
`usrAgents` - как уже было сказано выше, файл с юзерагентами для запросов. Изкоробки все отлично.  
`countriesCodes` - сюда вписывать коды стран для фильтрования с помощью сервися 2ip.ru  
`userParams.json` - параметры для отправки юзерзапросов с помощью `USER-CHECK`  


## Настройки работы  
Файл - `settings.ini`.  
**Общие значения, повторящиеся в нескольких модулях**  
`MAXTRIES` - количество попыток отправки запроса  
`TIMEOUT` - время ожидания соединения с сервером  
`TASKS` - количество асинхронных задач. "Потоков" по-народному  

**[main]**  
`FILENAME_EXPORT` - имя выходного файла с проксями.  
`NORMALINPUT` - вводить ли через аргументы командной строки протокол. (`python main.py <протокол>`)  
`PROTOCOLOUT` - записывать на выходе прокси в формат для вайпалки, пример: socks4://1.2.34.56:7890  
`NAME` - да это же имя, которое пишется перед каждый выводом чекера! Можно написать что угодно  
`FILTERINGBAD` - чистить ли нестандартные прокси. Выключать если проверяете прокси с паролями и/или юрловые.  
`PROXY` - прокси для получения данных из апи сосача. Пример: `socks5://1.2.3.4:5678`  

**[modules]**  
`PARSE` - парсить ли прокси  
`SUBNETS` - удалять ли прокси, входящие в подсети в *texts/subnets.txt*  
`BLACKLIST` - удалять ли прокси, чей айпи входит в *texts/blacklist.txt*  
`COUNTRIES` - удалять ли прокси из стран в *texts/countries.txt*  
`CHECK_ADVANCED`- проверять ли прокси которые принадлежать провайдерам с ASN номерами в *texts/ASN.txt*  
`SAME_FILTERING` - удалять ли прокси с одинаковыми айпи.  
`CHECK2IP` - удалять ли прокси из стран в *texts/countries.txt*. Использует сайт 2ip.ru, требует токента из личного кабинета там.  
`CHECK2IP_CODES` - удалять ли прокси из стран с кодом *texts/countriesCodes.txt*. Использует сайт 2ip.ru  
`CHECKON2CH` - проверять ли на баны на 2ch.hk, не удаляет "Доступ запрещен"  
`CHECK_HEADERS` - проверять ли прокси на дырявость и/или на анонимность.  
`USER_CHECK` - проверка прокси с помозью юзерзапроса.  

**[COUNTRIES_ADVANCED]**  
`UNKNOWN` - считать прокси с неизвестным ASN-номером хорошими  

**[2IP]**  
`TOKEN` - ваш токен для использования API сайта 2ip.ru, необходима регистрация там.  
`UNKNOWOUT` - считать прокси из неизвестной страны хорошими  

**[BANS_CHECKER]**  
`BOARD` - доска для отправки запросов.  

**[USER_CHECKER]**  
`PARAMS` - использова параметры из `userParams.json` `"params"`.  
`DATA` - использовать данные из `userParams.json` `"data"`.  
`URL` - юрл для запроса.  
`REQUEST` - тип запроса. На данный момент поддерживаются GET, POST, HEAD.  
Запрос будет отправляться с вашими данными и параметрами (если включено) на юрл, а ответ обрабатываться функцией
`userFilter(self, response)` которая принимает соответсвенно текст ответа и в случае если ответ нужный, возвращает `True`  

**[HEADERS_CHECKER]**  
`ANON` - оставлять только прокси, которые не выдают использование прокси в заголовках.  

**[SUBNETS]**  
`MODE` - как фильтровать подсети. `EXCEPT` - исключать из подсетей в *texts/subnets.txt*, `INCLUDE` - только из этих подсетей.  



По всем вопросам/багам/предложениям писать BUND-development@protonmail.com  
Не стесняйтесь критиковать, ведь без критики нет прогресса. Отдельное спасибо анону, который подсказал про прокси в aiohttp  

