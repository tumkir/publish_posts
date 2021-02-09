import argparse
import os

import requests
import telegram
import vk_api
from dotenv import load_dotenv


def post_vkontakte(message_text, image_path):
    vk_session = vk_api.VkApi(token=os.getenv('VK_TOKEN'))
    vk = vk_session.get_api()
    upload = vk_api.VkUpload(vk_session)

    photo = upload.photo(
        image_path,
        album_id=os.getenv('VK_ALBUM_ID'),
        group_id=os.getenv('VK_GROUP_ID')
    )

    vk.wall.post(
        owner_id=-(int(os.getenv('VK_GROUP_ID'))),
        from_group=1,
        message=message_text,
        attachments=f'photo{photo[0]["owner_id"]}_{photo[0]["id"]}'
    )


def post_telegram(message_text, image_path):
    bot = telegram.Bot(token=os.getenv('TG_TOKEN'))
    bot.send_photo(chat_id=os.getenv('TG_CHANNEL_ID'), photo=open(image_path, 'rb'))
    bot.send_message(chat_id=os.getenv('TG_CHANNEL_ID'), text=message_text)


def post_facebook(message_text, image_path):
    data = {
        'access_token': os.getenv('FB_TOKEN'),
        'caption': message_text
    }

    with open(image_path, 'rb') as image:
        files = {'source': image}
        response = requests.post('https://graph.facebook.com/{}/photos'.format(os.getenv('FB_GROUP_ID')), files=files, data=data)
        response.raise_for_status()


def post_everywhere(message_text, image_path):
    post_vkontakte(message_text, image_path)
    post_telegram(message_text, image_path)
    post_facebook(message_text, image_path)


def parse_args():
    parser = argparse.ArgumentParser(description='Скрипт позволяет опубликовать пост в Telegram-канале и в группах Вконтакте и Facebook')
    parser.add_argument('message_text', type=str, help='Текст поста')
    parser.add_argument('image_path', type=str, help='Путь к картинке')

    return parser.parse_args()


if __name__ == '__main__':
    load_dotenv()
    args = parse_args()
    post_everywhere(args.message_text, args.image_path)
