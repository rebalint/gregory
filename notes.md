-=-=-=-=-=-=ADMIN=-=-=-=-=-=-
# eco config 
.addeco <str>name <str>prefix
- creates eco

.removeeco <str>currency
- deletes eco

.editeco <str>currency <str>prefix
- deletes eco

# value editing
.setvalue <str>currency <class>member <int>value
- sets the value of that members currency

.addvalue <str>currency <class>member <int>value
- adds value to someones currency

.removevalue <str>currency <class>member <int>value
- removes value from person

# shop config
.setshop <str>currency
- sets channel as shop log

.removeshop <str>currency
- deletes shop channel

.additem <str>currency <int>value <str>title * <str>description
- addes item to shop

.edititem <str>currency <int>itemid <int>value <str>title * <str>description
- edits item from shop

.removeitem <str>currency <int>itemid
- deletes item id

# transaction setup
.setlog <str>currency
- sets current channel as transaction log

.removelog <str>currency
- removes transaction log from server

=-=-=-=-=-=DEFAULT=-=-=-=-=-=

.bal|balence <str>currency
- checks your balance

.transfer <int>value <class>member
- transfers cash from person to person
- *

.shop <str>currency
- displays shop
- this will need to output somewhere. botlog?** needs shop log set

.buy <str>currency <int>itemID
- buy's an item from currencies' shop

.leaderboard|lb <str>currency
- displayes top 10 people in currency


-=-=-=-=-=-=SQL=-=-=-=-=-=-

guilds table changes
- needs new column. 
- shoplog - varchar(255) - nullable - containes channel id for shop output

shop table
- containes items from shops

eco table
- containes info about eco

player currency
- containes players currency and eco
