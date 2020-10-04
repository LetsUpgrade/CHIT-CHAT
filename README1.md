# Documentation for Covid19-assist-bot

## Data needed for RASA chatbot
Inside the data directory you can find two files:
- nlu.md
- stories.md

## What is NLU file?
- At a fundamental level, natural language understanding (NLU) does two things: it identifies the goal or meaning of the text and extracts key pieces of information from it. 
- In other words, NLU does intent identification and entity recognition. 
- It allows you to include additional labels to your training data to define certain concepts and make your AI assistant more accurate.
- nlu.md is the file where you should write the nlu model training examples.
- The file consists of some example training data used to train the bot.
- NLU training data consists of intent labels
- It also includes some examples how users would communicate or how users will respond to the bot.
- NLU training data is structured into different parts:
  - training examples
  - synonyms
  - regex features and
  - lookup tables

## Where are the receipts?
- Entity Roles and Groups is a useful feature that allows you to further define concepts within your training data to make your AI assistant perform better. 
- To validate this feature, our research team ran several experiments; one of the most important first steps is to find the right training dataset.
- In choosing the right dataset, the team looks at public datasets and ones created by Rasa, and also looks for:
- Suitability: is the dataset suitable for the task we want to evaluate?
- Adaptability: can we adapt an existing dataset to fit our needs?
- Feasibility: if an existing dataset won’t do, is it feasible to create a new dataset

## Forms
- Define a custom slot mapping to fill a slot with an entity that has a specific role and/or group label.

## What is inside Stories file?
- Stories are a type of training data used to train your assistant's dialogue management model. 
- Stories can be used to train models that are able to generalize to unseen conversation paths.
- A story is a representation of a conversation between a user and an AI assistant, converted into a specific format where user inputs are expressed as intents (and entities when necessary), while the assistant's responses and actions are expressed as action names.

## User Messages
- While writing stories, you do not have to deal with the specific contents of the messages that the users send. 
- Instead, you can take advantage of the output from the NLU pipeline, which lets you use just the combination of an intent and entities to refer to all the possible messages the users can send to mean the same thing.
- It is important to include the entities here as well because the policies learn to predict the next action based on a combination of both the intent and entities (you can, however, change this behavior using the use_entities attribute).

## Actions
- All actions executed by the bot, including responses are listed in stories under the action key.
- You can use a response from your domain as an action by listing it as one in a story. 
- Similarly, you can indicate that a story should call a custom action by including the name of the custom action from the actions list in your domain.

## Events
- During training, Rasa Open Source does not call the action server. 
- This means that your assistant's dialogue management model doesn't know which events a custom action will return.
- Because of this, events such as setting a slot or activating/deactivating a form have to be explicitly written out as part of the stories. 
- For more info, see the documentation on Events.

## Slot Events
- Slot events are written under slot_was_set in a story. 
- If this slot is set inside a custom action, add the slot_was_set event immediately following the custom action call. 

## Form Events
- There are three kinds of events that need to be kept in mind while dealing with forms in stories.
- A form action event (e.g. - action: restaurant_form) is used in the beginning when first starting a form, and also while resuming the form action when the form is already active.
- A form activation event (e.g. - active_loop: restaurant_form) is used right after the first form action event.
- A form deactivation event (e.g. - active_loop: null), which is used to deactivate the form.

## Checkpoints
- You can use checkpoints to modularize and simplify your training data. 
- Checkpoints can be useful, but do not overuse them. Using lots of checkpoints can quickly make your example stories hard to understand, and will slow down training.

## Or Statements
- Another way to write shorter stories, or to handle multiple intents the same way, is to use an or statement. 
- For example, if you ask the user to confirm something, and you want to treat the affirm and thankyou intents in the same way.

## Test Conversation Format
- The test conversation format is a format that combines both NLU data and stories into a single file for evaluation.
