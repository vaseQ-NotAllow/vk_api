import argparse

from vkapi import get_friends


def vk_api_arg_parser():
    parser = argparse.ArgumentParser(description='Parser for vk api')
    subparsers = parser.add_subparsers()

    parser_get_friends = subparsers.add_parser('getFriends', help='get friends of user_id')
    parser_get_friends.add_argument('user_id')
    parser_get_friends.add_argument("--fields", "-f", help="""список дополнительных полей, которые необходимо вернуть.\n
    Доступные значения: nickname, domain, sex, bdate, city, country, timezone, photo_50, photo_100, photo_200_orig,\n
     has_mobile, contacts, education, online, relation, last_seen, status, can_write_private_message,\n
      can_see_all_posts, can_post, universities\n
      список слов, разделенных через запятую""")
    parser_get_friends.add_argument("--count", "-c", help="Необходимое кол-во друзей")
    parser_get_friends.set_defaults(func=get_friends)

    return parser


if __name__ == '__main__':
    props = {"v": 5.103,
             'access_token': "313affaf313affaf313affaf67314bd2413313a313affaf6fa037faab0984af3f4d5dab"}
    args = vk_api_arg_parser().parse_args().__dict__
    for key in args:
        if key != "func":
            props[key] = args[key]
    args["func"](props)
