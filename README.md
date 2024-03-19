## Flask Application Design

**HTML Files:**

- **index.html:**
  - The main page of the chat app, providing options to create room or join room through a provided link.
- **room.html:**
  - The actual chat room, displaying messages and allowing users to send new messages.

**Routes:**

- **/:** The homepage where users create or join rooms.
 - **Method:** GET
 - **Purpose:** Displays the index.html file.
- **create_room:** Creates a new chat room.
 - **Method:** POST
 - **Purpose:** Generates a unique room ID and redirects the user to the appropriate room URL.
- **join_room:** Allows a user to join an existing chat room.
 - **Method:** POST
 - **Purpose:** Checks if the provided room ID is valid and redirects the user to the room URL if found.
- **room/<room_id>:** The chat room itself.
 - **Method:** GET
 - **Purpose:** Displays the room.html file with the specified room ID.
- **send_message:** Allows a user to send a message in the current room.
 - **Method:** POST
 - **Purpose**: Processes the message and broadcasts it to all connected users in the room.