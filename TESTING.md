# Testing

Return back to the [README.md](README.md) file.


## Code Validation


### Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.


| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| run.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LewisMDillon/escape-from-fell-manor/main/run.py) | ![screenshot](documentation/py-validation-run.png) | Pass: No Errors |
| dictionary.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LewisMDillon/escape-from-fell-manor/main/dictionary.py) | ![screenshot](documentation/py-validation-dictionary.png) | Pass: No Errors |
| gametext.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LewisMDillon/escape-from-fell-manor/main/gametext.py) | ![screenshot](documentation/py-validation-gametext.png) | Pass: No Errors |
| art.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/LewisMDillon/escape-from-fell-manor/main/art.py) | ![screenshot](documentation/py-validation-art.png) | Pass: No Errors |

## Lighthouse Audit


I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Mobile | ![screenshot](documentation/lighthouse-home-mobile.png) | Some minor warnings |
| Home | Desktop | ![screenshot](documentation/lighthouse-home-desktop.png) | Some minor warnings |


## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/browser-chrome.png) | Works as expected |
| Firefox | ![screenshot](documentation/browser-firefox.png) | Works as expected |
| Edge | ![screenshot](documentation/browser-edge.png) | Works as expected |
| Safari | ![screenshot](documentation/browser-safari.png) | Minor ASCII art differences |
| Brave | ![screenshot](documentation/browser-brave.png) | Works as expected |
| Opera | ![screenshot](documentation/browser-opera.png) | Works as expected |
| Internet Explorer | ![screenshot](documentation/browser-iex.png) | Works as expected(!) |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues. Issues on smaller screen sizes are unfixable due to terminal provided by Code Institute.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsive-mobile.png) | Screen clipping issues |
| Tablet (DevTools) | ![screenshot](documentation/responsive-tablet.png) | Screen clipping issues |
| Desktop | ![screenshot](documentation/responsive-desktop.png) | Works as expected |
| XL Monitor | ![screenshot](documentation/responsive-xl.png) | Scaling starts to have minor issues |
| 4K Monitor | ![screenshot](documentation/responsive-4k.png) | Noticeable scaling issues |
| Oneplus Nord 2 | ![screenshot](documentation/responsive-oneplus.png) | Screen clipping issues |
| iPhone 13 | ![screenshot](documentation/responsive-iphone.png) | Screen clipping issues |


## Defensive Programming


Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Main Menu | | | | |
| | Input only from options given | Execute based on input | Pass | Input of any other text throws error an repeats prompt to user | ![screenshot](documentation/defensive-programming01.png) |
| User Name Request | | | | |
| | Input 2-15 alpha characters | Store name as player name | Pass | Input of any other kind e.g. numbers, special characters or whitespace throws error an repeats prompt to user | ![screenshot](documentation/defensive-programming02.png) |
| Main Game Prompt | | | | |
| | Input only from options given | Execute based on input | Pass | Input of any other text throws error an repeats prompt to user | ![screenshot](documentation/defensive-programming03.png) |
| Yes/No Prompts | | | | |
| | Input only 'yes' or 'no' | Execute based on input | Pass | Input of any other text throws error an repeats prompt to user. User is able to input any word beginning with 'y' for yes and 'n' for no | ![screenshot](documentation/defensive-programming04.png) |


## Bugs


- Enemy attacks not affecting player health

    ![screenshot](documentation/bug01.png)

    - To fix this, I fixed a syntax error in the `update_player_health()` call.

- Player location not updating properly

    ![screenshot](documentation/bug02.png)

    - To fix this, I fixed direction errors in the `room_map` dictionary.

- Player name not displaying properly

    ![screenshot](documentation/bug03.png)

    - To fix this, I used an f string in the name prompt.

- Player equipment not updating

    ![screenshot](documentation/bug04.png)

    - To fix this, I added a missing update to the Player class object inside the weapon find event.

- Game events not resetting to default state on soft reset of game.

    ![screenshot](documentation/bug04.png)

    - To fix this, I created a new file, dictionary.py and moved the main room_map dictionary to that file. Then used a deep copy of that dictionary within run.py. This allowed the game to work with the temporary copy of the game rooms rather than altering the dictionary itself.

### GitHub **Issues**

**Fixed Bugs**

All previously closed/fixed bugs can be tracked [here](https://github.com/LewisMDillon/escape-from-fell-manor/issues?q=is%3Aissue+is%3Aclosed).

![screenshot](documentation/github-issues.png)


## Unfixed Bugs

- The user can type text into the terminal window when prompted to press ENTER

    ![screenshot](documentation/unfixed-bug01.png)

    - This is a limitation of the Code Institute terminal and unfixable by me.

- If the user presses CTRL + C, the program will quit and display a non user-friendly keyboard interrupt message.

    ![screenshot](documentation/unfixed-bug02.png)

    - This is a limitation of th Code Institute terminal and unfixable by me.

There are no other remaining bugs that I am aware of.

## Code Refactoring

I refactored a 14 line if/else conditional check to a single, reusable print statement.

Original:

```python
    if color == 'red':
        print(f"{Fore.RED}{Style.NORMAL} ", end="", flush=True)
    elif color == 'green':
        print(f"{Fore.GREEN} ", end="", flush=True)
    elif color == 'yellow':
        print(f"{Fore.YELLOW} ", end="", flush=True)
    elif color == 'blue':
        print(f"{Fore.BLUE} ", end="", flush=True)
    elif color == 'magenta':
        print(f"{Fore.MAGENTA} ", end="", flush=True)
    elif color == 'cyan':
        print(f"{Fore.CYAN} ", end="", flush=True)
    elif color == 'white':
        print(f"{Fore.WHITE} ", end="", flush=True)
```

Reformatted to:

```python
print(f"{color}{Style.NORMAL} ", end="", flush=True)
```