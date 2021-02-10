import argparse
import os

import requests
import telegram
import vk_api
from dotenv import load_dotenv


def post_vkontakte(message_text, image_path, vk_token, vk_album_id, vk_group_id):
    vk_session = vk_api.VkApi(token=vk_token)
    vk = vk_session.get_api()
    upload = vk_api.VkUpload(vk_session)

    photo = upload.photo(
        image_path,
        album_id=vk_album_id,
        group_id=vk_group_id
    )

    vk.wall.post(
        owner_id=-(vk_group_id),
        from_group=1,
        message=message_text,
        attachments=f'photo{photo[0]["owner_id"]}_{photo[0]["id"]}'
    )


def post_telegram(message_text, image_path, tg_token, tg_channel_id):
    bot = telegram.Bot(tg_token)
    with open(image_path, 'rb') as image:
        bot.send_photo(chat_id=tg_channel_id, photo=image)
    bot.send_message(chat_id=tg_channel_id, text=message_text)


def post_facebook(message_text, image_path, fb_token, fb_group_id):
    data = {
        'access_token': fb_token,
        'caption': message_text
    }

    with open(image_path, 'rb') as image:
        files = {'source': image}
        response = requests.post(
            'https://graph.facebook.com/{}/photos'.format(fb_group_id),
            files=files,
            data=data
        )
        response.raise_for_status()


def parse_args():
    parser = argparse.ArgumentParser(
        description='Скрипт позволяет опубликовать пост в Telegram-канале и в группах Вконтакте и Facebook'
    )
    parser.add_argument('message_text', type=str, help='Текст поста')
    parser.add_argument('image_path', type=str, help='Путь к картинке')

    return parser.parse_args()


if __name__ == '__main__':
    load_dotenv()
    vk_token = os.getenv('VK_TOKEN')
    vk_group_id = int(os.getenv('VK_GROUP_ID'))
    vk_album_id = os.getenv('VK_ALBUM_ID')
    tg_token = os.getenv('TG_TOKEN')
    tg_channel_id = os.getenv('TG_CHANNEL_ID')
    fb_token = os.getenv('FB_TOKEN')
    fb_group_id = os.getenv('FB_GROUP_ID')

    args = parse_args()

    post_vkontakte(args.message_text, args.image_path, vk_token, vk_album_id, vk_group_id)
    post_telegram(args.message_text, args.image_path, tg_token, tg_channel_id)
    post_facebook(args.message_text, args.image_path, fb_token, fb_group_id)
