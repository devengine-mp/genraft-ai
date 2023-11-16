from pydantic import BaseModel
from datetime import datetime

class Project(BaseModel):
    id: int
    name: str
    idea_initial: str
    idea_final: str
    folder_path: str
    created_at: datetime

class ChatMessage(BaseModel):
    id: int
    thread_id: str
    content: str
    role: str
    created_at: datetime

class Assistant(BaseModel):
    id: int
    assistant_id: str
    assistant_name: str
    assistant_type: str
    assistant_instructions: str
    assistant_model: str
    created_at: datetime

class ProjectAssistantAssociation(BaseModel):
    project_id: int
    assistant_id: int

class ProjectChatAssociation(BaseModel):
    project_id: int
    chat_message_id: int
    chat_type: str

class ProjectStats(BaseModel):
    total_projects: int
    total_files: int
    total_assets: int

class InitializeProjectRequest(BaseModel):
    name: str
    idea: str

class CreateAssistantRequest(BaseModel):
    assistant_name: str
    assistant_instructions: str
    assistant_model: str