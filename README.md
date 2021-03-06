# Usage guide

Bet at a fishing spot, 
*using a terminal* run `python src` inside the downloaded folder (*"Lost-Ark-Fishing-Bot"*)  
and switch over to the game.

```yml
advanced usage: src [-h] [-r] [-tts] [-ak]

options:
  -h, --help            show this help message and exit
  -r , --repair         Defines after how many fishing rod casts repairs happen. 
                        Set as 0 to disable
  -tts , --timeTillStart
                        How long to wait (in seconds) till the bot starts
  -ak , --actionKey     The action key for fishing
```

#### Fishing Spots

This bot works best with fishing spots which are contrast to the caught fishing icon ![fishingIcon](Resources/fishing_icon.png). So in places which are as dissimilar to this image as possible (comparison is done in greyscale).
Arthetine has so far been the only fishing spot where this bot doesn't work.

List of places where I've gotten it to work:

- East Luterra (**Wavestrand Port**)
- Feiton (**Wailing Swamp**) -- if the exclamation mark isn't hidden behind foliage
- North Vern (**Port Krona**)

#### Repairs

Supported aspect ratio is 16:9, repairs _currently_ will not work with any other aspect ratio.

# Configuration

The only supported way to configure stuff _(change keybindings, when repairs happen)_ is by editing the [`src/__main__.py`](src/__main__.py) file.

# Installation

- Install [Python](https://www.python.org/downloads/)
- Clone repo `git clone https://github.com/GetUsernameFromDatabase/Lost-Ark-Fishing-Bot.git`
- Go into repo `cd Lost-Ark-Fishing-Bot`
- Install required python modules `pip install -r requirements.txt`
