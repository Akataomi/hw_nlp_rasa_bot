# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
'''
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSubmitApplication(Action):

    def name(self) -> str:
        return "action_submit_application"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain) -> list:

        position = tracker.get_slot('position')
        skills = tracker.get_slot('skills')
        experience = tracker.get_slot('experience')
        expected_salary = tracker.get_slot('expected_salary')

        # Логика оценки соответствия вакансии (упрощенная)
        if position == "Data Scientist" and "Python" in skills and experience >= "2 года":
            suitability = "Подходите для позиции Data Scientist."
        else:
            suitability = "К сожалению, вы не подходите ни на одну из позиций."

        dispatcher.utter_message(text=suitability)
        return []
'''