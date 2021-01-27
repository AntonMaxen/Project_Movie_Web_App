from data.MongoDB_MongoEngine.repository import user_repository as ur


def get_user_by_email(email: str):
    return ur.get_user_by_email(email)


def get_user_by_username(username: str):
    return ur.get_user_by_username(username)


def create_user(first_name, last_name, email, password, username):
    ur.create_user(first_name, last_name, email, password, username)


def add_role_to_user(user, role):
    ur.add_role_to_user(user=user, role=role)


def get_all_users():
    return ur.get_all_users()


def add_movie_to_users_watchlist(user, movie):
    ur.add_movie_to_users_watchlist(user, movie)


def add_friendship(user, friend):
    ur.add_friendship(user, friend)


def delete_movie_from_users_watchlist(user, movie):
    ur.delete_movie_from_users_watchlist(user, movie)


def add_profile_picture_to_user(user, profile_picture):
    ur.add_profile_picture_to_user(user, profile_picture)


def delete_profile_picture_if_exists(user):
   ur.delete_profile_picture_if_exists(user)
