from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import find_dotenv, load_dotenv
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

load_dotenv(find_dotenv())

def draft_email(user_input, name="Dave"):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

    template = """
    You are a helpful assistant that drafts an email reply based on an a new email.
    Your goal is to help the user quickly create a perfect email reply.
    Keep your reply short and to the point and mimic the style of the email so you reply in a similar manner to match the tone.
    Start your reply by saying: "Hi {name}, here's a draft for your reply:". And then proceed with the reply on a new line.
    Make sure to sign of with {signature}.
    """
    
    signature = f"Kind regards, \n\{name}"
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = "Here's the email to reply to and consider any other comments from the user for reply as well: {user_input}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input, signature=signature, name=name)
    
    """
    API_URL = "https://ai.btsmomenta.com/api/v1/prediction/80f44dc0-fc05-40dc-9ae3-974f38054eaa"

    def query(payload):
        response = ""
        response = requests.post(API_URL, json=payload)
        return response.json()
        
    response = query({"question": user_input})
    """
    
    return response


def call_flowise(message):
    """
    API_URL = "https://ai.btsmomenta.com/api/v1/prediction/80f44dc0-fc05-40dc-9ae3-974f38054eaa"

    def query(payload):
        response = requests.post(API_URL, json=payload)
        return response.json()
        
    return response = query({
        "question": message,
    })
    """