

# IMPORT NEEDED LIBRARIES
import tkinter as tk # needed for GUI
from tkinter import ttk # used for the progress bar
import time # needed for the countdown and timing functionality
import threading # used so that the timer can run and the window stays responsive
from PIL import Image, ImageTk # used to load, process, and display images for the flower growth mechanic

# CONSTANTS:
work_min = 25 # defaul Pomodoro work duration in minutes
short_break_min = 5 # default short break duration in minutes
long_break_min = 15 # default long break duration in minutes
sessions = 4 
cycle = 1 


#################################################################################################################################


class PomodoroTimer:
    def __init__(self): # creates the main application window
        self.root = tk.Tk()
        self.root.title("Bloom:odoro") # sets the name that appears at the top of the window
        self.root.geometry("900x500")   # sets the width and height of the window
        self.root.configure(bg="#cbd5c0") # sets the background colour of the window

        # Setting up the Timer & Session variables
        self.time_left = work_min * 60 # concerts minutes into seconds for the countdown
        self.timer_running = False # keeps track of whether or not the timer is currently active
        self.mode = "work"  # stes timer mode, can be 'work', 'short_break', or 'long_break'

        self.session_count = 0 # tracks number of Pomodoro sessions completed in this cycle
        self.cycle_count = 0 # tracks number of full cycles (4 sessions) completed 
        self.current_stage = 0 # current growth stage of the flower image (starts at 0)

        self.elapsed_time = 0  # keeps track of total time elapsed across pauses
        self.start_time = None  # stores the timestamp when timer starts/resumes    



#################################################################################################################################
        


        # UI ELEMENTS - COUNTDOWN / TRACKING / GOALS

        # Goal Input Field
        self.goal_label = tk.Label(self.root, text="Goal For This Session:", # prompts users to type their study focus
                                   font=("Helvetica", 16), bg="#cbd5c0", fg="#4b6043") # font, size, text colour
        self.goal_label.pack(pady=(20, 5)) # adds some space above and below
        self.goal_entry = tk.Entry(self.root, width=50, font=("Helvetica", 14)) # size of entry text box field
        self.goal_entry.pack(pady=(0, 20)) # adds soem space above and below
        
            # Display the entered goal during the timer (text is inputted by users, then when start button is pressed the text is printed below the input field)
        self.current_goal_label = tk.Label(self.root, text="", font=("Helvetica", 20), # font and size
                                           bg="#cbd5c0", fg="#4b6043") # text colour
        self.current_goal_label.pack(pady=(0, 20)) # adds space above and below


        # Timer Display
        self.timer_label = tk.Label(self.root, text="25:00", # text/time of the timer countdown
                                    font=("Clock", 115, "bold"), bg="#cbd5c0", fg="#4b6043") # font, size, text effects, colour
        self.timer_label.place(x=300, y=210) # positiones text approximately centred

       
        # Progress Label
        self.progress_label = tk.Label(self.root, text="Cycle Progress: 0/4 completed sessions", # text content of text label
                                       font=("Helvetica", 14), bg="#cbd5c0", fg="#4b6043") # font, size, text colour
        self.progress_label.place(x=330, y=150) # position of the label on screen, top and centered


        # Start/Pause Button - button begins the timer when clicked and also pauses when clicked
        self.start_button = tk.Button(self.root, text="START", command=self.toggle_timer, # inital button label "START" & links the button to the toggle_timer method
                                      font=("Helvetica", 20, "bold"), bg="#6F825E", fg="#6F825E",   # sets text font and text size & effect, and text colour
                                      width=15, height=3, relief=tk.RAISED, bd=5) # sets dimension of the size of the button
        self.start_button.place(x=350, y=360) # positiones text near the bottom in the middle

        self._setup_mode_buttons()
        self._setup_flower()
        self._setup_progress_bar()



#################################################################################################################################



        # MODE BUTTONS - right side panel buttons that let the user choose Pomodoro, Short Break, or Long Break
    def _setup_mode_buttons(self):
        self.button_frame = tk.Frame(self.root, bg="#cbd5c0") # use frame to hold other objects there such as the buttons
        self.button_frame.place(x=700, y=200) # sets the frame on the right side

            # Pomodoro Button - sets time for 25 minutes (work mode)
        self.pomo_button = tk.Button(self.button_frame, text="POMODORO", command=self.set_pomodoro, # command calls for the pomodoro timer function to run
                                     font=("Helvetica", 16, "bold"), bg="#6F825E", fg="#6F825E", # sets text font, effect, colour, size
                                     width=15, height=2) # sets dimension of the size of the button
        self.pomo_button.pack(pady=20) # adds space above and below

            # Short Break Button - sets time for 5 minutes
        self.short_button = tk.Button(self.button_frame, text="SHORT BREAK", command=self.set_short,# command calls for the short break function to run
                                      font=("Helvetica", 16, "bold"), bg="#6F825E", fg="#6F825E", # sets text font, effect, colour, size
                                      width=15, height=2) # sets dimension of the size of the button
        self.short_button.pack(pady=15) # adds space above and below

            # Long Break Button - sets time for 15 minutes
        self.long_button = tk.Button(self.button_frame, text="LONG BREAK", command=self.set_long, # command calls for the long break function to run
                                     font=("Helvetica", 16, "bold"), bg="#6F825E", fg="#6F825E", # sets text font, effect, colour, size
                                     width=15, height=2) # sets dimension of the size of the button
        self.long_button.pack(pady=15) # adds space above and below



#################################################################################################################################



        # FLOWER GROWTH MEHANIC
    def _setup_flower(self):
        self.flower_size = (220, 220)  # sdefines display size of the flower image
        blank_img = Image.new("RGBA", self.flower_size, (0, 0, 0, 0)) # creates a transparent placeholder image
        self.blank_photo = ImageTk.PhotoImage(blank_img) # converts the blank image to a format tkinter can use
        self.flower_label = tk.Label(self.root, image=self.blank_photo, bg="#cbd5c0") # image label placeholder
        self.flower_label.image = self.blank_photo ## keeps a reference to prevent image from disappearing
        self.flower_label.place(x=10, y=230) #positions the flower image on the left of the application window



#################################################################################################################################



        # PROGRESS BAR
    def _setup_progress_bar(self): #set up the progress bar
        style = ttk.Style() # create ttk style configuration for bar deisgn 
        style.theme_use("clam") # sets the visual style theme
        style.configure(
            "Green.Horizontal.TProgressbar", # determines direction bar will travel
            troughcolor="#cbd5c0", # colour matches window background
            background="#4b6043", # same dark green as countdown text
            thickness=30, # sets thickness/height of the progress bar
            troughrelief="flat", # removes raised edges
            relief="flat", # removes raised edges
            borderwidth=0) # no border

        # creates the progress bar widget
        self.progress_bar = ttk.Progressbar(
            self.root,
            orient="horizontal", # horizontal progress bar (moves from left to right)
            length=900, # width across the window
            mode="determinate", # fills based on actual value rather than pulsing
            maximum=self.time_left, # maximal value equals total seconds in the timer
            style="Green.Horizontal.TProgressbar") # applies the custom style created above
        self.progress_bar.place(x=0, y=470, height=30) # positions the bar at the bottom of the window
        self.progress_bar["value"] = 0 # sets initial value (empty)



#################################################################################################################################



    # TIMER LOGIC 
    def toggle_timer(self): # handles the start/pause functionality (If the timer is stopped, it starts the countdown and changes the button text to PAUSE. If the timer is running, it stops the countdown and changes the button text back to START)
        if self.start_button.cget("text") == "START": # Retrieve goal text when START is pressed
            # Retrieve goal text when START is pressed
            goal_text = self.goal_entry.get() # reads user's entered goal
            if goal_text.strip() and self.mode == "work": 
                self.current_goal_label.config(text=f"Goal: {goal_text}") # displays goal under input
            self.timer_running = True # activates timer state
            self.start_button.config(text="PAUSE") # change button text to "PAUSE" as the timer is currently running
            threading.Thread(target=self.countdown, daemon=True).start() # starts countdown in separate thread, so it can run in the background so the GUI doesn’t freeze

        elif self.start_button.cget("text") == "PAUSE": # if the button says PAUSE timer is currently running
            # Pause timer
            self.timer_running = False # stops countdown loop, pauses wuthout resetting time left
            self.start_button.config(text="START") # changes button back to say START to indicate time will resume when pressing again

        elif self.start_button.cget("text") == "NEXT": # if button says NEXT, a session has just been completed
            # Prepare timer for next session
            self.reset_timer_for_next_session()

        elif self.start_button.cget("text") == "RESET CYCLE": # if all 4 sessions are completed and a full cycle has ended
            self.reset_cycle() # resets everything - progress, clears goals, and returns app to initial state



    def countdown(self):
        total_time = self.time_left # stores original time for progress calculation
        self.progress_bar["maximum"] = total_time # updates bar maximum for accuracy
        self.progress_bar["value"] = 0 # resets bar to empty

        start_time = time.time() # record when countdown started

        # run countdown loop until time runs out or timer is stopped
        while self.time_left > 0 and self.timer_running:
            elapsed = time.time() - start_time # calculate elapsed time since start
            self.time_left = max(0, total_time - int(elapsed)) # remaining seconds
            mins, secs = divmod(self.time_left, 60) # convert total seconds into minutes and seconds
            self.timer_label.config(text=f"{mins:02d}:{secs:02d}") # formats time as minutes:seconds

            # progress bar animation
            self.progress_bar["value"] = elapsed #increases progress bar smoothly
            self.progress_bar.update_idletasks() # forces UI refresh

            time.sleep(0.1) # small delay for smoother visual update

        if self.time_left <= 0 and self.timer_running: # no more time remaining on the clock
            self.session_finished() #session is completed and recorded



#################################################################################################################################



    # SESSION TRACKING
    def session_finished(self): 
        self.timer_running = False # stops the timer so that countdown() no longer decreases time_left
        self.start_button.config(text="NEXT") # changes the text of the button to direct to next session since the previous session ended
        self.timer_label.config(text="Time's up!", font=("Clock", 80, "bold")) # changing the time text to "Time's Up!"
        self.timer_label.place(x=280, y=210) # adjusts the position of the text on the screen

        # Only grow flower + track progress if in WORK mode
        if self.mode == "work":
            self.session_count += 1 # adds 1 to the number of Pomodoro sessions completed in this cycle
            self.progress_label.config(text=f"Cycle Progress: {self.session_count}/4 sessions") # updates the on-screen progress label to show how many sessions have been completed out of 4

            if self.session_count >= 4:
                # Show bouquet animation for full cycle
                self.update_flower(final_stage=True)
                self.cycle_count += 1
                self.progress_label.config(
                    text=f"Full Study Cycle Complete! ({self.cycle_count} cycle)")
                # Change Start button to RESET CYCLE
                self.start_button.config(text="RESET CYCLE", command=self.reset_cycle)
            else:
                self.update_flower()

        # Clear goal (regardless of mode)
            self.goal_entry.delete(0, tk.END) # clears the text in the goal entry box, ready for the next session’s goal
            self.current_goal_label.config(text="") # clears the on-screen goal display text so the next session starts blank

    def reset_timer_for_next_session(self):
        # Reset timer depending on current mode (work (Pomodoro) or break mode)
        if self.mode == "work":
            self.time_left = work_min * 60
            self.timer_label.config(text=f"{work_min:02d}:00", font=("Clock", 115, "bold"))
        elif self.mode == "short_break":
            self.time_left = short_break_min * 60
            self.timer_label.config(text=f"{short_break_min:02d}:00", font=("Clock", 115, "bold"))
        elif self.mode == "long_break":
            self.time_left = long_break_min * 60
            self.timer_label.config(text=f"{long_break_min:02d}:00", font=("Clock", 115, "bold"))

        # resets label position
        self.timer_label.place(x=300, y=210)
        self.start_button.config(text="START", command=self.toggle_timer) # resets button text/action



#################################################################################################################################



    # RESET CYCLE FUNCTION
    def reset_cycle(self):
        # Reset everything to default values to start a new cycle.
        self.session_count = 0
        self.time_left = work_min * 60
        self.mode = "work"
        self.progress_label.config(text="Cycle Progress: 0/4 completed sessions")
        self.flower_label.config(image=self.blank_photo) # clears flower growth mechanic back to blank
        self.flower_label.image = self.blank_photo
        self.timer_label.config(text=f"{work_min:02d}:00", font=("Clock", 115, "bold"))
        self.start_button.config(text="START", command=self.toggle_timer)
        self.goal_entry.delete(0, tk.END) # clears text entry
        self.current_goal_label.config(text="") # clears displayed goal



#################################################################################################################################



    # FLOWER ANIMATION 
    def morph_flower(self, prev_img_path, next_img_path, step=0, steps=25): # Crossfade + scale between two flower image for growth animation
        prev_img = Image.open(prev_img_path).convert("RGBA") # loads previous image
        next_img = Image.open(next_img_path).convert("RGBA") # loads next stage

        alpha = step / steps # determines blending ration between images (0-1)
        scale = 0.9 + 0.1 * alpha # slightly scales image for growth effect
        new_w = int(self.flower_size[0] * scale) # new width based on growth scale
        new_h = int(self.flower_size[1] * scale) # new height based on growth scale

        prev_resized = prev_img.resize((new_w, new_h), Image.LANCZOS) # high-quality risize for smooth edges
        next_resized = next_img.resize((new_w, new_h), Image.LANCZOS) # smoothly resizes image to match dimensions for blending

        blended = Image.blend(prev_resized, next_resized, alpha) # alpha determins how visbible the new image becomes over the old one
        photo = ImageTk.PhotoImage(blended) # converts blended image to a Tkinter-compatible PhotoImage

        self.flower_label.config(image=photo) # updates label widget's displayed image to blended version
        self.flower_label.image = photo # keeps reference to avoid image disappearing

        # adjust label position to keep image visually centred
        dx = (new_w - self.flower_size[0]) // 2 # horizontal offset caused by scaling
        dy = (new_h - self.flower_size[1]) // 2 # vertical offset caused by scaling
        self.flower_label.place(x=20 - dx, y=210 - dy) # repositions image as it grows

        # continue morphong until all steps complete
        if step < steps: # checks if there are still steps left in the transition
            self.root.after(70, lambda: self.morph_flower(prev_img_path, next_img_path, step + 1, steps)) # schedules next animation frame to occue after 70 milliseconds & lambda keeps the current parameters (steps + 1, etc) for the next call
        else: # finalise transition with sharp next image
            final = next_img.resize(self.flower_size, Image.LANCZOS) # ensures final image matches standard flower size
            photo_final = ImageTk.PhotoImage(final) # converts the final image for Tkinter display
            self.flower_label.config(image=photo_final) # updates the label widget to show fully tranisitoned image
            self.flower_label.image = photo_final # keeps reference so image remains visible

    def update_flower(self, final_stage=False): # determines which flower stages morph based on how many work sessions have been completed
        image_paths = ["seed.png", "sprout.png", "flower.png", "bouquet.png"] # defined sequence of flower growth images in order
        if final_stage: # check if user has completed a full 4 session cycle
            stage_index = len(image_paths) - 1 # final stage index (bouquet) at the end of the full cycle
            prev_index = max(stage_index - 1, 0) # one stage before the final (flower), used as the previous image
        else: # determine current growth stage based on session count
            if self.session_count > 0: #only update flower is at least one Pomodoro session has been completed
                stage_index = min(self.session_count - 1, len(image_paths) - 1) # determines correct stage for current session
                prev_index = max(stage_index - 1, 0) # previous image used for blending transition
            else: # if no sessions are completed yet, no animation should occur
                return # exit function without updating any images
       
        # start the visual transition between the previous and current stage
        self.morph_flower(image_paths[prev_index], image_paths[stage_index]) # passed both images into morph_flower() for animation



#################################################################################################################################



    # MODE FUNCTIONS
    def set_pomodoro(self): # sets time to full Pomodoro session of 25 minutes
        self.mode = "work" # set mode to work session
        self.time_left = work_min * 60 # sets time to 25 mins (1500 seconds)
        self.timer_label.config(text=f"{work_min:02d}:00") # update label text to show 25 mins

    def set_short(self):
        self.mode = "short_break" # sets mode to short break
        self.time_left = short_break_min * 60 # sets time to 5 mins (300 seconds)
        self.timer_label.config(text=f"{short_break_min:02d}:00") # update label text to show 5 mins

    def set_long(self):
        self.mode = "long_break" # sets mode to long break
        self.time_left = long_break_min * 60 # sets time to 15 mins (600 seconds)
        self.timer_label.config(text=f"{long_break_min:02d}:00") # update label text to show 15 mins



#################################################################################################################################



    # RUN APPLICATION
    def run(self):
        self.root.mainloop() # keeps the windoe open and running until user closes it

# MAIN ENTRY POINT - ensures program runs when executed directly
if __name__ == "__main__":
    PomodoroTimer().run()
