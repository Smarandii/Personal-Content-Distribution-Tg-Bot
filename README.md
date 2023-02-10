# Personal Content Distribution Telegram Bot

## Use cases

#### Main features:
* User will use this bot in order to get unique content from authors


* Client will use this bot in order to not send this unique content manually to the user who satisfied conditions in order to get this content.
For example, send content only if user is subscribed to telegram channel


* Client will use this bot to map trigger word to his content. He will send file with this trigger word in caption to that file.


* Client will use this bot to map trigger word to his conditions. He will send instructions defined by a condition defining protocol and those conditions will be required for user to satisfy in order to obtain content that is mapped to this trigger word,


#### Sub feature (This features does not include in MVP.):
* User will use this bot as some sort of mailing system to notify users of some events.


* Client will use this bot as some sort of database of all users that got unique content from client



## MVP Workflow for v1.0 of this telegram bot

1. User types command
```bash
/start
```
2. Bot checks if user is satisfied conditions of getting content provided by author
3. If those conditions satisfied, then bot sends message to ask which particular content to provide
4. User provide code word for content
5. Bot sends content mapped to that word

## Bot structure and architecture

### This bot uses [aiogram](https://docs.aiogram.dev/en/latest/quick_start.html)

1. There is a long polling loop, for getting updates from telegram server

2. There is a message handlers for /start command. This handler sends greetings to user.
3. There is a message handlers for text. If this user provided trigger word in this text message this handler checks if user is satisfied client conditions mapped to that trigger word.
If clients conditions are satisfied by user, then bot will send content mapped to that trigger word.

### Base classes of this bot are:

### Condition
#### is an abstract class that represents conditions that have to be satisfied by user in order to get Content
##### Condition properties:
- `trigger word: str` (has to be unique, will be used as primary key)
- `user_id: int`
##### Condition methods:
- `is_satisfied(self) -> bool` (returns true if conditions are satisfied by specific user_id and false otherwise)

### IsMember(Condition) - child of Condition class, represents
##### IsMember(Condition) properties:
- `trigger word: str` (has to be unique, will be used as primary key)
- `user_id: int`

##### IsMember methods:
- `of_group(self, group_id) -> bool` (returns true if user is in group with `group_id`)
- `of_channel(self, channel_id) -> bool`
- `is_satisfied(self) -> bool`

#### Content - this is an object that represents content from client to users
###### Content properties:
- `trigger word: str` (has to be unique, will be used as primary key)
- `content_file_id: str` (telegram id of the document)
- `conditions: list[Condition]`