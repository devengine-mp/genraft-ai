from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy import ForeignKey

metadata = MetaData()

projects = Table(
    "projects",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("idea_initial", String, nullable=False),
    Column("idea_final", String, nullable=False),
    Column("folder_path", String, nullable=False),
    Column("created_at", DateTime, nullable=False)
)

chat_messages = Table(
    "chat_messages",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("thread_id", String, nullable=False),
    Column("content", String, nullable=False),
    Column("role", String, nullable=False),
    Column("created_at", DateTime, nullable=False)
)

assistants = Table(
    "assistants",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("assistant_id", String, nullable=False),  # ID returned by OpenAI API
    Column("type", String, nullable=False),  # Type of assistant, e.g., 'stakeholder', 'consultant'
    Column("created_at", DateTime, nullable=False)
)

project_assistant_association = Table(
    "project_assistant_association",
    metadata,
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True),
    Column("assistant_id", Integer, ForeignKey("assistants.id"), primary_key=True)
)

project_chat_association = Table(
    "project_chat_association",
    metadata,
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True),
    Column("chat_message_id", Integer, ForeignKey("chat_messages.id"), primary_key=True),
    Column("chat_type", String, nullable=False)  # This column can be used to distinguish different types of chats
)

def create_tables(engine):
    metadata.create_all(bind=engine)