# Bot Factory Tickets

**Bot Factory Tickets** by Calestial Ashley is a simple ticketing system for managing support tickets on your Discord server. This module allows users to create support tickets, which are then managed in dedicated channels. Administrators can close these tickets, removing the channels once resolved.

## Features
- **Create Tickets:** Users can create a support ticket channel where they can describe their issues.
- **Close Tickets:** Administrators can close and delete ticket channels when they are resolved.

## Setup Instructions

1. **Clone or Open the Repository**
   - Access the project at [Bot Factory Tickets on Replit](https://replit.com/@calestialashley/Bot-Factory-Tickets?s=app).

2. **Install Dependencies**
   - Ensure `discord.py` is installed. Run the following command in the Replit Shell:
     ```bash
     pip install discord.py
     ```

3. **Add Your Bot Token**
   - Replace `'YOUR_BOT_TOKEN'` in `main.py` with your actual Discord bot token. Obtain the token from the [Discord Developer Portal](https://discord.com/developers/applications).

4. **Run the Bot**
   - Click the "Run" button in Replit to start the bot.

## Usage

### Commands

1. **Create a Ticket**
   - Command: `!ticket`
   - Example: `!ticket`
   - This command creates a new support ticket channel under the "Tickets" category. The user who issued the command will have access to this channel.

2. **Close a Ticket**
   - Command: `!close`
   - Example: `!close`
   - Use this command in the ticket channel to close and delete it. Only administrators can use this command.

### Permissions
- The bot needs permissions to create, manage, and delete channels. Ensure it has these permissions in your Discord server.

### Notes
- The "Tickets" category will be created if it does not exist. You can customize the category name in the code if needed.
- Make sure to adjust the permissions for the ticket channels according to your server’s needs.

## License
This project is licensed under the MIT License. You can modify and distribute it according to the terms of the license.

## Contributing
Contributions are welcome! If you have ideas or improvements, feel free to fork the repository and submit a pull request.

## Contact
For support or questions, you can reach out to Calestial Ashley on [GitHub](https://github.com/CalestialAshley35) or join the support Discord server.

---

Enjoy using Bot Factory Tickets to streamline support and issue tracking on your Discord server!
