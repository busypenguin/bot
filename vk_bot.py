import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
import os
from dotenv import load_dotenv
import random
from google.cloud import dialogflow


def detect_intent_texts(project_id, session_id, text, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)

    text_input = dialogflow.TextInput(text=text, language_code=language_code)

    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response


def get_answer(event, vk_api):
    """Answer the user message."""
    response = detect_intent_texts(project_id, event.user_id, event.text, 'ru-RU')
    if not response.query_result.intent.is_fallback:
        answer = response.query_result.fulfillment_text
        vk_api.messages.send(
            user_id=event.user_id,
            message=answer,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    load_dotenv()
    vk_token = os.getenv('VK_TOKEN')
    project_id = os.getenv('PROJECT_ID')
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            get_answer(event, vk_api)
