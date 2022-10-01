# dota2accepter
Первая версия моего скрипта для принятия игры в Dota2
Он проверяет белый цвет в одной точке на твоем экране. После нахождения игры он нажимает на кнопку принятия игры и отправляет сообщение в Телеграме. Скрипт работает с
тремя разрешениями: 1366x768, 1600x900 and 1920x1080.

При первом запуске скрипт запрашивает три переменные. Токен телеграм бота, айди аккаунта и разрешение. Токен берется из BotFather, айди аккаунта можно взять из IDBot.
Для более легкого доступа к скрипту может быть использована библиотека pyinstaller и выведен ярлык на рабочий стол






First version of my simple Dota2 game accepter. 
Script checks white color in 1 pixel on your screen. After finding a game it clicks on the button and send message in Telegram. Script works with 3 resolutions:
1366x768, 1600x900 and 1920x1080.

At the first lauch script asks for three variables. Your telegram bot token, account chat id and resolution.  Token can be taken from BotFather, chat id from IDBot.
For the ease acces to the script can be used pyinstaller module. 
