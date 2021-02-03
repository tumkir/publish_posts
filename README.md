# Публикация поста в Telegram-канале и в группах Вконтакте и Facebook

Скрипт позволяет опубликовать пост с картинкой в Telegram-канале и в группах Вконтакте и Facebook

## Как установить
Перед запуском в папке со скриптом создайте `.env` файл и пропишите туда необходимые токены и id групп в таком формате: `ПЕРЕМЕННАЯ=значение`.

Необходимо прописать:
- `VK_TOKEN` — токен приложения VK, полученный с помощью Implicit Flow
- `VK_GROUP_ID` — id группы из адресной строки браузера
- `VK_ALBUM_ID` — id альбома
- `TG_TOKEN` — токен телеграм бота
- `TG_CHANNEL_ID` — id или ссылка на канал в телеграме
- `FB_TOKEN` — токен Facebook
- `FB_GROUP_ID` — id группы из адресной строки браузера

В Вконтакте [создайте группу](https://vk.com/groups?tab=admin). Создайте [приложение](https://vk.com/apps?act=manage) и с помощью [Implicit Flow](https://vk.com/dev/implicit_flow_user) получите ключ с правами `photos`, `groups`, `wall` и `offline`. В группе создайте фотоальбом: перейдите по ссылке https://vk.com/albums-{group_id} (замените {group_id} на group_id вашей группы). Перейдите на страницу созданного фотоальбома и в адресной строке будет ссылка вида: https://vk.com/album-{group_id}_{album_id}.

Для телеграма [создайте бота](https://t.me/BotFather) и получите токен. Создайте канал, добавьте туда созданного бота и сделайте его администратором. Если канал закрытый, то [получите его id](https://stackoverflow.com/a/33862907/640260), а если открытый, то просто впишите ссылку на канал (например, `TG_CHANNEL_ID=@channel_smm_test`)

Для FB [создайте группу](https://www.facebook.com/groups/create/) и из ссылки на группу возьмите id. Создайте приложение и получите для него `маркер доступа пользователя` с правом publish_to_groups ([Руководство по работе с Graph API Explorer](https://developers.facebook.com/docs/graph-api/explorer/)). При необходимости [можете продлить токен](https://developers.facebook.com/tools/debug/accesstoken/) с 2 часов до 2 месяцев.

Python3 должен быть уже установлен.
Затем используйте 'pip' (или 'pip3', есть есть конфликт с Python2) для установки зависимостей:

```bash
pip install -r requirements.txt
```

## Как запустить
Запускайте скрипт из командной строки, передав в аргументах текст поста и путь к файлу-картинке

```bash
python3 publish_posts.py 'Привет, новый пост' './index.png'
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).