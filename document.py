import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models


def multiturn_generate_content():
  vertexai.init(project="lk-chatbot-cx", location="us-central1")
  model = GenerativeModel(
    "gemini-1.5-pro-preview-0409",
    system_instruction=["""give me answer only from the document"""]
  )
  chat = model.start_chat()
  print(chat.send_message(
      ["""i want to order biryani"""],
      generation_config=generation_config,
      safety_settings=safety_settings
  ))
  print(chat.send_message(
      ["""can you show me menu pls"""],
      generation_config=generation_config,
      safety_settings=safety_settings
  ))
  print(chat.send_message(
      [document3_1, """who is pm"""],
      generation_config=generation_config,
      safety_settings=safety_settings
  ))
  print(chat.send_message(
      ["""who is prime minister of india"""],
      generation_config=generation_config,
      safety_settings=safety_settings
  ))
  print(chat.send_message(
      ["""givi me details about NASA"""],
      generation_config=generation_config,
      safety_settings=safety_settings
  ))
  print(chat.send_message(
      [document6_1, """give me info about google"""],
      generation_config=generation_config,
      safety_settings=safety_settings
  ))
  print(chat.send_message(
      ["""what this doc containts"""],
      generation_config=generation_config,
      safety_settings=safety_settings
  ))
  print(chat.send_message(
      ["""what is the name in document"""],
      generation_config=generation_config,
      safety_settings=safety_settings
  ))
  print(chat.send_message(
      ["""what about his education"""],
      generation_config=generation_config,
      safety_settings=safety_settings
  ))
  print(chat.send_message(
      ["""skills"""],
      generation_config=generation_config,
      safety_settings=safety_settings
  ))

document3_1 = Part.from_uri(
    mime_type="application/pdf",
    uri="gs://priyankblue/docaitest.pdf")
document6_1 = Part.from_uri(
    mime_type="application/pdf",
    uri="gs://priyankblue/print english.pdf")

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

multiturn_generate_content()

