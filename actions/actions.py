# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

#from typing import Any, Text, Dict, List, Union

#from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher
#from rasa_sdk.forms import FormAction

'''class HealthForm(FormAction):

    def name(self):
        return "health_form"

    @staticmethod
    def required_slots(tracker):

        if tracker.get_slot("confirm_exercise") == True:
            return ["confirm_exercise","exercise","sleep","diet","stress","goal"]
        else:
            return ["confirm_exercise","sleep","diet","stress","goal"]

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "confirm_exercise":[
                self.from_intent(intent='affirm', value=True),
                self.form_intent(intent= 'deny', value=False),
                self.from_intent(intent='inform', value= True),
            ],
            "sleep": [
                self.from_entity(entity="sleep"),
                self.from_intent(intent='deny', value = "None")
            ],
            "diet" : [
                self.from_text(intent='inform'),
                self.from_text(intent="affirm"),
                self.from_text(intent = "deny"),
            ],
            "goal" : [
                self.from_text(intent="inform"),
                
            ]
        }'''
from typing import Text, List

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

class ValidateHealthForm(FormValidationAction):

  def name(self) -> Text:
      return "validate_health_form"

  async def required_slots(
    self,
    slots_mapped_in_domain: List[Text],
    dispatcher: "CollectingDispatcher",
    tracker: "Tracker",
    domain: "DomainDict"
  ) -> List[Text]:
    if tracker.get_slot("confirm_exercise") == True:
      return ["confirm_exercise", "exercise", "sleep", "diet", "stress", "goal"]
    else:
      return ["confirm_exercise", "sleep", "diet", "stress", "goal"]
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
