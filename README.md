# Bloom:odoro — A Motivational Pomodoro Timer

Bloomodoro is an interactive productivity timer built in **Python** with **Tkinter**, designed to make studying and working feel rewarding through visual feedback; in turn increasing productivity.  
Each completed Pomodoro session helps your digital flower bloom — turning focus into growth.

## Table of Contents
- [General Information](#general-information)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Screenshots](#screenshots)
- [Setup](#setup)
- [Usage](#usage)
- [Development Journey](#development-journey)
- [Future Improvements](#future-improvements)
- [Learning Resources](#learning-resources)
- [Author](#author)

---

## General Information

**Bloom:odoro** reimagines the Pomodoro technique by integrating a **flower growth mechanic** that visually represents focus, consistency, and overall productivity.  
Each completed study session rewards users with a new stage of a growing flower, which eventually grows into a beautiful bouquet as a digital treat to congratulate  users for being productive.

The project was developed as a creative solution to a real problem that students in particular are facing, that being lack of motivation to complete studies and other everyday tasks. This prototype explores **interaction design**, **motivation visualisation**, and **UI logic**.
  
It uses soft, nature-inspired visuals to cultivate calm focus and a sense of achievement.

---

## Technologies Used

- **Python 3.12+**
- **Tkinter** — GUI interface
- **Threading** — Keeps timer and interface responsive
- **PIL (Pillow)** — Image handling for the flower growth stages
- **time** — Countdown logic
- **ttk** — For styled progress bar integration

---

## Features

**Pomodoro Timer Logic** — 25-minute work sessions, with 5- and 15-minute breaks.  
**Goal Input System** — Set a goal per session to stay intentional.  
**Flower Growth Mechanic** — Watch your flower evolve from a seed, to a sprout, the flower, and finally a bouquet as you complete work sessions.   
**Progress Tracking** — Displays “Cycle Progress: X/4 completed sessions”.  
**Progress Bar** — Smoothly fills as the timer counts down.  
**Cycle Reset** — Resets timer, flower, and goal after every four sessions.  
**Threading Integration** — Keeps the timer responsive while running.

---

## Screenshots

![Final Bouquet](screenshot/Final-Bouquet.png)

---

## Setup

To get Bloomodoro to run locally, follow these steps to ensure success:

1. Clone the repository and navigate to the prototype folder:
git clone https://github.com/alexysc207/Bloomodoro-A2-Code-Prototype.git
cd Bloomodoro-A2-Code-Prototype/Bloomodoro Prototype

2. Install Python 3.10+ if not already installed. Verify by running python --version.

3. Install required packages (Tkinter is included with Python):
pip install pillow

4. Ensure flower images (seed.png, sprout.png, flower.png, bouquet.png) are in the same folder as bloom_odoro.py.

5. Run the application by executing:
python bloom_odoro.py

Troubleshooting tips:

GUI doesn’t appear → check your Tkinter installation.

Images don’t show → verify file names and paths.

Timer freezes → make sure Pillow is installed and the script is run from the main thread.


---

## Usage

1. Launch the application.

2. Enter your focus goal for the session (it will print when the 'Start' Button is clicked).

3. Start the Pomodoro timer (default: 25 minutes).

4. Watch the progress bar fill as time passes.

5. When the timer finishes, your work session will be counted and your flower will grow to the next stage.

6. Select 'Short Break' or 'Long Break' buttons to enjoy some rest time before moving onto the next work session

7. After completing four work sessions, your flower fully blooms — and the cycle resets.

---

## Development Journey

After 6 weeks of coding, Project is: _complete_ for A2 prototype

| **Week** | **Focus** | **Key Achievements** |
|----------|-----------|----------------------|
| **Week 7** | Interface & Timer | Built the GUI in Tkinter, implemented core timer logic, and added start/pause button functionality |
| **Week 8** | Goals & Session Control | Added goal input fields, tweaked button layout, implemented session tracking, and refined pause/resume functionality |
| **Week 9** | Flower Mechanic | Developed flower growth stages, refined session count logic, and connected visual feedback to completed sessions |
| **Week 10** | Animation & Timing | Implemented morphing between flower stages, fixed timing for flower growth to match completed work sessions, and improved scaling/positioning |
| **Week 11** | Cycle Logic | Streamlined cycle completion logic, reset functionality, and refined interface behavior at the end of a full cycle |
| **Week 12** | Finalisation & Polish | Added progress bar, raised button effects, final bug fixes, layout adjustments, and completed testing for smooth user experience |

---

## Future Improvements

Bloomodoro is an application that has endless possibilities. Upon my completion of this project, there are still areas that have room for improvement, these being:

- Data saving using JSON files - being able to save session progress between launches of the application
- Add sound notifications for session transitions or when the flower grows
- Rain animation that triggers the flower growth
- Add ability to customise the theme of the application
- Add an analytics dashboard (track total focus hours per week)

---

## Learning Resources

My main inspiration for the Pomodoro timer was:
* Neural Nine. (2023, October 15). *Python Timer Tutorial* [Video]. YouTube. [https://www.youtube.com/watch?v=FJeXp5yZd-g](https://www.youtube.com/watch?v=FJeXp5yZd-g) — main inspiration for the timer and break button setup

### Tutorials & Video Guides

* Biswal, A. (2022, July 1). *Add pictures and images to Tkinter application* [Video]. YouTube. [https://youtu.be/pk8714VXBC0](https://youtu.be/pk8714VXBC0) — used for my flower growth mechanic
* Madecraft Speaker. (n.d.). *Python for students*. LinkedIn Learning. [https://www.linkedin.com/learning/python-for-students/](https://www.linkedin.com/learning/python-for-students/) — basics of coding using Python

### Tkinter References & GUI Guides

* Python Software Foundation. (n.d.). *Tkinter concepts*. Python Documentation. [https://docs.python.org/3/library/tkinter.html#important-tk-concepts](https://docs.python.org/3/library/tkinter.html#important-tk-concepts) — referenced core Tkinter concepts
* Python Tutorial. (n.d.). *Tkinter Labels*. [https://www.pythontutorial.net/tkinter/tkinter-label/](https://www.pythontutorial.net/tkinter/tkinter-label/) — used for setting up labels in the interface
* Real Python. (n.d.). *Displaying clickable buttons with Button widgets*. [https://realpython.com/python-gui-tkinter/#displaying-clickable-buttons-with-button-widgets](https://realpython.com/python-gui-tkinter/#displaying-clickable-buttons-with-button-widgets) — helped with button layout and GUI design

### Image Handling & Animations

* GeeksforGeeks. (2024, January 10). *Python Pillow tutorial*. [https://www.geeksforgeeks.org/python/python-pillow-tutorial/](https://www.geeksforgeeks.org/python/python-pillow-tutorial/) — learning Pillow for image handling
* GeeksforGeeks. (2023, December 5). *Adding images in Tkinter*. [https://www.geeksforgeeks.org/python/how-to-add-an-image-in-tkinter/](https://www.geeksforgeeks.org/python/how-to-add-an-image-in-tkinter/) — implementing flower growth images
* PlainEnglish. (2023, February 20). *Widget animations in Tkinter*. [https://plainenglish.io/blog/guide-to-widget-animations-with-tkinter](https://plainenglish.io/blog/guide-to-widget-animations-with-tkinter) — guided simple animations for visual feedback
* Python for Beginners. (2025, June 6). *Create animations in Tkinter Python GUI*. [https://www.pythonforbiginners.com/2025/06/create-animations-in-tkinter-python-gui.html](https://www.pythonforbiginners.com/2025/06/create-animations-in-tkinter-python-gui.html) — additional animation techniques
* Stack Overflow. (2015, August 15). *How to fade in/out on a Tkinter frame?* [https://stackoverflow.com/questions/27806669/how-to-fade-in-out-on-a-tkinter-frame](https://stackoverflow.com/questions/27806669/how-to-fade-in-out-on-a-tkinter-frame) — used for fade animation ideas
* Tkinter.com. (n.d.). *Animate widgets tutorial*. [https://tkinter.com/how-to-animate-widgets-python-tkinter-gui-tutorial-164/](https://tkinter.com/how-to-animate-widgets-python-tkinter-gui-tutorial-164/) — extra reference for animating widgets
* TutorialsPoint. (n.d.). *Loading images using PIL*. [https://www.tutorialspoint.com/loading-images-in-tkinter-using-pil](https://www.tutorialspoint.com/loading-images-in-tkinter-using-pil) — helped troubleshoot image loading

### Progress Bar References
* DataCamp. (2020, May 12). *Progress bars in Python*. [https://www.datacamp.com/tutorial/progress-bars-in-python](https://www.datacamp.com/tutorial/progress-bars-in-python) — general reference for progress tracking
* PythonAssets. (n.d.). *Progress bar in Tkinter*. [https://pythonassets.com/posts/progress-bar-in-tk-tkinter/](https://pythonassets.com/posts/progress-bar-in-tk-tkinter/) — implemented countdown progress visualization
* PythonGuides. (n.d.). *Tkinter progress bar tutorial*. [https://pythonguides.com/python-tkinter-progress-bar/](https://pythonguides.com/python-tkinter-progress-bar/) — learning bar increments and formatting
* Python Software Foundation. (n.d.). *ttk Progressbar*. Python Documentation. [https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Progressbar](https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Progressbar) — reference for progress bar setup
* PythonTutorial.net. (n.d.). *Tkinter Progressbar*. [https://www.python-tutorial.net/tkinter/tkinter-progressbar/](https://www.python-tutorial.net/tkinter/tkinter-progressbar/) — additional reference for progress logic
* Stack Overflow. (2016, January 10). *Tkinter GUI with progress bar example*. [https://stackoverflow.com/questions/33768577/tkinter-gui-with-progress-bar](https://stackoverflow.com/questions/33768577/tkinter-gui-with-progress-bar) — example of updating progress bar



### Imported Libraries

* Clark, A., et al. (2023). *Pillow (Python Imaging Library) (Version 10.0.0)* [Computer software]. Python Package Index. https://pypi.org/project/Pillow/ - Used for handling images for the flower growth mechanic.
* Python Software Foundation. (2023). *Python (Version 3.12)* [Computer software]. https://www.python.org/ - Used as the programming language for the project and provides Tkinter and threading modules.
* Python Software Foundation. (2023). *Tkinter (Version included with Python 3.12)* [Computer software]. https://docs.python.org/3/library/tkinter.html - Used for building the GUI interface.
* Python Software Foundation. (2023). *threading (Version included with Python 3.12)* [Computer software]. https://docs.python.org/3/library/threading.html - Used to keep the timer and interface responsive.
* Python Software Foundation. (2023). *time (Version included with Python 3.12)* [Computer software]. https://docs.python.org/3/library/time.html - Used for countdown logic.
* Python Software Foundation. (2023). *ttk (Version included with Python 3.12)* [Computer software]. https://docs.python.org/3/library/tkinter.ttk.html - Used for styled progress bar integration.

### Additional Python Guides

* Python for Engineers. (2025, January 20). *Pomodoro timer example*. [https://www.pythonforengineers.in/2025/01/pomodoro-timer.html](https://www.pythonforengineers.in/2025/01/pomodoro-timer.html) — inspired overall Pomodoro timer logic
* Matthes, E. H. (n.d.). *Beginner's Python cheat sheet* [PDF]. [https://github.com/ehmatthes/pcc_3e/releases/download/v1.0.0/beginners_python_cheat_sheet_pcc_all.pdf](https://github.com/ehmatthes/pcc_3e/releases/download/v1.0.0/beginners_python_cheat_sheet_pcc_all.pdf) — reference for general Python syntax and best practices

---

## Author
Created by [Alexys Cambey] 
