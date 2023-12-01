# YesUCan't

YesUCan't is a versatile Discord bot designed to interact with the Canvas learning management system's API, providing users with valuable information and functionality right within their Discord server. This integration allows for a seamless experience for students who use Canvas.

## Getting Started

Follow these steps to set up and run the YesUCan't Discord bot on your server.

### Prerequisites

- [Python](https://www.python.org/) installed on your machine
- [Discord Developer Account](https://discord.com/developers/applications) to create a bot and obtain a token
- [Canvas API Key](https://canvas.instructure.com/doc/api/file.oauth.html) for Canvas integration
- [dotenv](https://pypi.org/project/python-dotenv/) Python library installed (`pip install python-dotenv`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Stingray07/YesUCant

2. Create a .env file in the project root and add your Discord bot token and Canvas API key:

   ```bash 
   DISCORD_TOKEN='your_discord_bot_token'
   CANVAS_API_KEY='your_canvas_api_key'

## Usage
Run the bot with the following command :

```bash
python main.py
```

## Bot Commands
- **!courses**: Gives all current courses for the current trimester.
- **!all_asm**: Gives all unsubmitted assignments.
- **!asm <assignment ID>**: Gives information for the assignment with the given ID

Feel free to explore more commands by interacting with the bot on your Discord server!

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)