# Stash-Tracker

## API Endpoints

### GET Endpoints:
- `/stashes`  
  Retrieves a list of all stashes.  
  - **Query parameters** (optional):
    - `name`: Filter by stash name (partial match).
    - `location`: Filter by stash location (partial match).
    - `created_after`: Filter by creation date after a specific date (format: `YYYY-MM-DD`).
    - `created_before`: Filter by creation date before a specific date (format: `YYYY-MM-DD`).
  
- `/kits`  
  Retrieves a list of all kits.  
  - **Query parameters** (optional):
    - `name`: Filter by kit name (partial match).
    - `stash_id`: Filter by associated stash ID.
    - `created_after`: Filter by creation date after a specific date (format: `YYYY-MM-DD`).
    - `created_before`: Filter by creation date before a specific date (format: `YYYY-MM-DD`).

- `/items`  
  Retrieves a list of all items.  
  - **Query parameters** (optional):
    - `name`: Filter by item name (partial match).
    - `minecraft_item`: Filter by the Minecraft item type (partial match).
    - `kit_id`: Filter by associated kit ID.
    - `count`: Filter by item count.
    - `created_after`: Filter by creation date after a specific date (format: `YYYY-MM-DD`).
    - `created_before`: Filter by creation date before a specific date (format: `YYYY-MM-DD`).

### POST Endpoints:
- `/stashes`  
  Creates a new stash.

- `/kits`  
  Creates a new kit.

- `/items`  
  Creates a new item.

### DELETE Endpoints:
- `/stashes/{stash_id}`  
  Deletes the stash with the given ID.

- `/kits/{kit_id}`  
  Deletes the kit with the given ID.

- `/items/{item_id}`  
  Deletes the item with the given ID.

### PUT Endpoints:
- `/stashes/{stash_id}`  
  Updates the stash with the given ID.

- `/kits/{kit_id}`  
  Updates the kit with the given ID.

- `/items/{item_id}`  
  Updates the item with the given ID.
