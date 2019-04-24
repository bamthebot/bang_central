import sqlite3


def get_user_list(db_location):
    connection = sqlite3.connect(db_location)
    cursor = connection.cursor()
    users_qs = cursor.execute("SELECT user_id FROM burritobot_twitchuser").fetchall()
    users = [q[0] for q in users_qs]
    return users


def get_response(db_location, command, id):
    """
    :param db_location: location of database.
    :param command: command for which we want a response
    :return: False if command doesn't exist, response if it does exists
    """
    connection = sqlite3.connect(db_location)
    cursor = connection.cursor()
    exists = cursor.execute("SELECT EXISTS(SELECT 1 FROM burritobot_command WHERE command==? AND user_id=?)", (command, id))
    exists = exists.fetchone()[0]
    if exists:
        response = cursor.execute("SELECT response FROM burritobot_command WHERE command==? AND user_id=?", (command, id))
        return response.fetchall()[0][0]
    else:
        return False


def get_commands(db_location, id):
    """
    :param db_location: location of database.
    :return: returns list containing commands.
    """
    connection = sqlite3.connect(db_location)
    cursor = connection.cursor()
    commands = cursor.execute("SELECT command,response FROM burritobot_command WHERE user_id=?", (id, ))
    return [pair for pair in commands.fetchall()]


def get_access_token(db_location, id):
    connection = sqlite3.connect(db_location)
    cursor = connection.cursor()
    token = cursor.execute("SELECT (access_token) FROM burritobot_twitchuser WHERE user_id=? LIMIT 1", (id, )).fetchone()[0]
    return token


def get_id_from_channel(db_location, channel):
    connection = sqlite3.connect(db_location)
    cursor = connection.cursor()
    id = cursor.execute("SELECT user_id FROM burritobot_twitchuser WHERE twitch_name=?",(channel,)).fetchone()[0]
    return id


def get_channel_from_id(db_location, id):
    connection = sqlite3.connect(db_location)
    cursor = connection.cursor()
    channel = cursor.execute("SELECT twitch_name FROM burritobot_twitchuser WHERE user_id=?",(id,)).fetchone()[0]
    return channel
