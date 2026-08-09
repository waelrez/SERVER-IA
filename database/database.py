import sqlite3
import os

DATABASE_FILE = "ai_server.db"


def get_connection():

    return sqlite3.connect(DATABASE_FILE)


def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            ai_response TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_conversation(user_message, ai_response):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO conversations
        (user_message, ai_response)
        VALUES (?, ?)
        """,
        (user_message, ai_response)
    )

    connection.commit()
    connection.close()
