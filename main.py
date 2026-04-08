import customtkinter as ctk
import threading
from db import get_events, clear_events

from agent import run_agent
from db import get_events

# ======================
# APP CONFIG
# ======================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("900x600")
app.title("AI Calendar Agent 💬")

# ======================
# MEMORY
# ======================
chat_history = []

# ======================
# LEFT PANEL (EVENTS)
# ======================
sidebar = ctk.CTkFrame(app, width=250)
sidebar.pack(side="left", fill="y")

ctk.CTkLabel(sidebar, text="📅 Events", font=("Arial", 16)).pack(pady=10)

event_box = ctk.CTkTextbox(sidebar)
event_box.pack(fill="both", expand=True, padx=10, pady=10)


def refresh_events():
    event_box.delete("1.0", "end")
    for e in get_events():
        event_box.insert("end", f"• {e[1]} | {e[2]} {e[3]}\n")


# ======================
# CHAT AREA
# ======================
chat_frame = ctk.CTkFrame(app)
chat_frame.pack(side="right", fill="both", expand=True)

chat_box = ctk.CTkTextbox(chat_frame, wrap="word")
chat_box.pack(fill="both", expand=True, padx=10, pady=10)


def add_message(sender, msg):
    chat_box.insert("end", f"{sender}: {msg}\n\n")
    chat_box.see("end")


# ======================
# TYPING INDICATOR
# ======================
def show_typing():
    chat_box.insert("end", "🤖 Bot: typing...\n\n")
    chat_box.see("end")


def remove_typing():
    content = chat_box.get("1.0", "end")
    content = content.replace("🤖 Bot: typing...\n\n", "")
    chat_box.delete("1.0", "end")
    chat_box.insert("end", content)


# ======================
# CLEAR CHAT (FULL RESET)
# ======================
def clear_chat():
    global chat_history

    # 🧠 Clear memory
    chat_history = []

    # 🧹 Clear chat UI
    chat_box.delete("1.0", "end")
    entry.delete(0, "end")

    # ❗ CLEAR DATABASE EVENTS
    clear_events()

    # 🔄 Refresh sidebar
    refresh_events()

    # 🤖 Fresh start
    add_message("🤖 Bot", "Everything cleared! 🧹 New session started.")

# ======================
# INPUT AREA
# ======================
input_frame = ctk.CTkFrame(chat_frame)
input_frame.pack(fill="x", padx=10, pady=10)

entry = ctk.CTkEntry(input_frame, placeholder_text="Type a message...")
entry.pack(side="left", fill="x", expand=True, padx=5)


# ======================
# SEND MESSAGE
# ======================
def send_message():
    user_text = entry.get().strip()
    if not user_text:
        return

    entry.delete(0, "end")

    add_message("🧑 You", user_text)

    # Save memory
    chat_history.append({"role": "user", "content": user_text})

    # Show typing
    show_typing()

    # Background thread
    def worker():
        try:
            response = run_agent(user_text, chat_history)
        except Exception as e:
            response = f"❌ Error: {str(e)}"

        chat_history.append({"role": "assistant", "content": response})

        def update_ui():
            remove_typing()
            add_message("🤖 Bot", response)
            refresh_events()

        app.after(0, update_ui)

    threading.Thread(target=worker, daemon=True).start()


# ======================
# BUTTONS
# ======================
send_btn = ctk.CTkButton(input_frame, text="Send", command=send_message)
send_btn.pack(side="right", padx=5)

clear_btn = ctk.CTkButton(
    input_frame,
    text="Clear",
    fg_color="red",
    hover_color="#aa0000",
    command=clear_chat
)
clear_btn.pack(side="right", padx=5)


# ======================
# ENTER KEY SUPPORT
# ======================
app.bind("<Return>", lambda e: send_message())


# ======================
# START
# ======================
add_message("🤖 Bot", "Hello! I am your AI Calendar Assistant 📅")
refresh_events()

app.mainloop()