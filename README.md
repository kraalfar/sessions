## Classifying developers’ work using Machine Learning	
### Тестовое задание


Combining activities into work sessions:

1. Split all actions by user_id
2. Within each user_id sort all actions by timestamp
3. Go action by action - if current action happened within some time threshold after previous action then both actions considered in same session

Time threshold is unique for each action_id and can be estimated from some labeled data. Here threshold is set at 30 minutes for RUN and 10 minutes for other actions.