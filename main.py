import time
import daemon
import pygame
import logging
import tkinter as tk
from tkinter import filedialog
import os
import signal
from asterisk.ami import AMIClient, SimpleAction, EventListener

timings = []

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)  # Wait for the audio to finish playing

def schedule_audio():
    while True:
        current_time = time.localtime()
        for hour, minute, file_path in timings:
            if current_time.tm_hour == hour and current_time.tm_min == minute:
                logging.info(f'Playing {file_path} at {current_time.tm_hour}:{current_time.tm_min}')
                play_audio(file_path)
                # Sleep for 60 seconds to avoid multiple plays within the same minute
                time.sleep(60)
        # Check every minute
        time.sleep(60)

def add_timing():
    try:
        hour = int(hour_entry.get())
        minute = int(minute_entry.get())
        file_path = filedialog.askopenfilename(title="Select Audio File", filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            timings.append((hour, minute, file_path))
            timing_listbox.insert(tk.END, f"{hour:02}:{minute:02} - {file_path}")
    except ValueError:
        logging.error("Invalid hour or minute entered")

def start_daemon():
    pid = os.fork()
    if pid == 0:
        with daemon.DaemonContext(
            stdout=open('/tmp/schedule_audio.log', 'w+'),
            stderr=open('/tmp/schedule_audio_error.log', 'w+'),
            pidfile=open('/tmp/schedule_audio.pid', 'w+')
        ):
            logging.basicConfig(filename='/tmp/schedule_audio.log', level=logging.INFO)
            with open('/tmp/schedule_audio.pid', 'w') as pidfile:
                pidfile.write(str(os.getpid()))
            schedule_audio()
    else:
        with open('/tmp/schedule_audio.pid', 'w') as pidfile:
            pidfile.write(str(pid))

def stop_daemon():
    try:
        with open('/tmp/schedule_audio.pid', 'r') as pidfile:
            pid = int(pidfile.read().strip())
            os.kill(pid, signal.SIGTERM)
            logging.info(f'Killed process with PID {pid}')
            pidfile.close()
        os.remove('/tmp/schedule_audio.pid')
    except FileNotFoundError:
        logging.error("PID file not found")
    except ProcessLookupError:
        logging.error("No such process")
    except Exception as e:
        logging.error(f"Error killing process: {e}")

# AMI configuration
ami_host = 'your_issabel_host'
ami_port = 5038
ami_user = 'your_ami_user'
ami_secret = 'your_ami_secret'
ami_context = 'default'
ami_extension = '100'  # The extension to dial
ami_callerid = '100'  # Caller ID for the call

def make_call():
    try:
        client = AMIClient(address=ami_host, port=ami_port)
        client.login(username=ami_user, secret=ami_secret)

        action = SimpleAction(
            'Originate',
            Channel=f'SIP/{ami_extension}',
            Context=ami_context,
            Exten=ami_extension,
            Priority=1,
            CallerID=ami_callerid,
            Timeout=30000
        )

        client.send_action(action)
        logging.info(f'Calling {ami_extension} via AMI')
        client.logoff()
    except Exception as e:
        logging.error(f"Error making call: {e}")

# Create the GUI
root = tk.Tk()
root.title("Audio Scheduler")

tk.Label(root, text="Hour:").grid(row=0, column=0)
hour_entry = tk.Entry(root)
hour_entry.grid(row=0, column=1)

tk.Label(root, text="Minute:").grid(row=1, column=0)
minute_entry = tk.Entry(root)
minute_entry.grid(row=1, column=1)

tk.Button(root, text="Add Timing", command=add_timing).grid(row=2, column=0, columnspan=2)

timing_listbox = tk.Listbox(root, width=50)
timing_listbox.grid(row=3, column=0, columnspan=2)

tk.Button(root, text="Start Scheduler", command=start_daemon).grid(row=4, column=0, columnspan=2)
tk.Button(root, text="Stop Scheduler", command=stop_daemon).grid(row=5, column=0, columnspan=2)
tk.Button(root, text="Call Issabel", command=make_call).grid(row=6, column=0, columnspan=2)

root.mainloop()
