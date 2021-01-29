from data.MongoDB_MongoEngine.repository import chat_repository as cr


def initiate_chat(user_1, user_2):
    return cr.initiate_chat(user_1, user_2)


def get_all_chats():
    return cr.get_all_chats()


def get_chat_by_id(id):
    return cr.get_chat_by_id(id)


def get_chat_between_users(user1, user2):
    return cr.get_chat_between_users(user1, user2)


def add_message_to_chat(chat, message):
    cr.add_message_to_chat(chat, message)
