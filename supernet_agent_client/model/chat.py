from pydantic import BaseModel, Field, model_validator, ValidationError
from typing import Dict, List, Optional

class MoreLikeThisConfig(BaseModel):
    enabled: bool = False

class SuggestedQuestionsAfterAnswerConfig(BaseModel):
    enabled: bool = False

class TextToSpeechConfig(BaseModel):
    enabled: bool = False

class SpeechToTextConfig(BaseModel):
    enabled: bool = False

class RetrieverResourceConfig(BaseModel):
    enabled: bool = False

class SensitiveWordAvoidanceConfig(BaseModel):
    enabled: bool = False
    type: str = ""
    configs: List[str] = []

class AgentModeConfig(BaseModel):
    max_iteration: int = 5
    enabled: bool = False
    strategy: str = ""
    tools: List[str] = []
    prompt: Optional[str] = None

class DatasetConfigs(BaseModel):
    retrieval_model: str = ""
    top_k: int = 5
    reranking_enable: bool = False
    datasets: Dict[str, List] = {}

class FileUploadImageConfig(BaseModel):
    detail: str = ""
    enabled: bool = False
    number_limits: int = 0
    transfer_methods: List[str] = []

class FileUploadConfig(BaseModel):
    image: FileUploadImageConfig = FileUploadImageConfig()
    enabled: bool = False
    allowed_file_types: List[str] = []
    allowed_file_extensions: List[str] = []
    allowed_file_upload_methods: List[str] = []
    number_limits: int = 0
    fileUploadConfig: Dict[str, int] = {}

class AnnotationReplyConfig(BaseModel):
    enabled: bool = False

class ModelConfig(BaseModel):
    pre_prompt: str = ""
    prompt_type: str = ""
    chat_prompt_config: Dict[str, str] = {}
    completion_prompt_config: Dict[str, str] = {}
    user_input_form: List[str] = []
    dataset_query_variable: str = ""
    opening_statement: str = ""
    more_like_this: MoreLikeThisConfig = MoreLikeThisConfig()
    suggested_questions: List[str] = []
    suggested_questions_after_answer: SuggestedQuestionsAfterAnswerConfig = SuggestedQuestionsAfterAnswerConfig()
    text_to_speech: TextToSpeechConfig = TextToSpeechConfig()
    speech_to_text: SpeechToTextConfig = SpeechToTextConfig()
    retriever_resource: RetrieverResourceConfig = RetrieverResourceConfig()
    sensitive_word_avoidance: SensitiveWordAvoidanceConfig = SensitiveWordAvoidanceConfig()
    agent_mode: AgentModeConfig = AgentModeConfig()
    dataset_configs: DatasetConfigs = DatasetConfigs()
    file_upload: FileUploadConfig = FileUploadConfig()
    annotation_reply: AnnotationReplyConfig = AnnotationReplyConfig()
    supportAnnotation: bool = False
    appId: str = ""
    supportCitationHitInfo: bool = False
    model: Dict[str, str] = {}

class Chat(BaseModel):
    response_mode: str = ""
    conversation_id: str = ""
    files: List[str] = []
    query: str = ""
    inputs: Dict = {}
    config: Dict = Field(default_factory={}, alias="model_config")
    parent_message_id: Optional[str] = None

    @model_validator(mode='before')
    @classmethod
    def check_model_config(cls, data: Dict) -> Dict:
        print("Received data:", data)
        if isinstance(data, dict) and ('model_config' not in data or not data['model_config']):
            raise ValueError('model_config cannot be empty')
        print("AFTER Received data:", data)
        
        return data