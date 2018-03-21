# Riddles
Riddles is a simple text-based game to implement Discord's rich presence
using the [discoIPC](https://github.com/k3rn31p4nic/riddles-rich-presence)
Python package.

## Installation
1.  Clone this repository.
    ```bash
    git clone -b master -d 1 https://github.com/k3rn31p4nic/riddles-rich-presence
    ```

2.  Install required dependencies.
    ```bash
    # This will install all required dependencies including discoIPC
    pip install -r requirements.txt
    ```

## Usage
1.  Create a Discord Application at [Discord Developers](https://discordapp.com/developers/applications/me) site.

2.  Enable **Rich Presence**.

3.  Add your required assets in the **Rich Presence Assets** section.  
    You need to add at least 3 image assets, namely `riddles_icon`, `level_1`
    and `level_2`, for this example to work.  
    *Or you can modify the `riddles.py` file to add your own asset keys.*

4.  Edit the `config.ini` file and add your Client ID, that you got from
    [Discord Appliations](https://discordapp.com/developers/applications/me)
    page, to the `client_id` field in the file (obviously replacing the default
    one).  
    **Example**
    ```ini
    [CLIENT]
    client_id=425989775451750401
    ```

5. Run the game:
    ```bash
    python riddles.py
    ```

## More Info...
* [Discord Rich Presence](https://discordapp.com/rich-presence)
* [Discord Developers Documentation](https://discordapp.com/developers)
* [discoIPC Library](https://github.com/k3rn31p4nic/riddles-rich-presence)
