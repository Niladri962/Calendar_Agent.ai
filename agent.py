from tools import schedule_event
from calcom import create_booking_link
from openrouter import run_openrouter


def run_agent(user_input, chat_history=None):

    text = user_input.lower()

    # ---------------------
    # Quick link shortcut
    # ---------------------
    if "link" in text or "booking" in text:
        return f"Here’s your booking link:\n{create_booking_link()}"

    # ---------------------
    # Build memory context
    # ---------------------
    history_text = ""

    if chat_history:
        for msg in chat_history[-10:]:
            history_text += f"{msg['role']}: {msg['content']}\n"

    prompt = f"""
You are an intelligent AI calendar assistant.

Conversation history:
{history_text}

User: {user_input}

Rules:
- Understand context
- Ask if info missing
- Schedule events if possible

STRICT OUTPUT FORMAT:
schedule | title | date | time | suggestion(optional)
ask | question
advice | message
"""

    try:
        output = run_openrouter(prompt)
        parts = [p.strip() for p in output.split("|")]
        intent = parts[0].lower()

        # ---------------------
        # SCHEDULE EVENT
        # ---------------------
        if intent == "schedule":
            if len(parts) < 4:
                return "❌ Missing details (title, date, time)"

            title = parts[1]
            date = parts[2]
            time = parts[3]

            result = schedule_event(title, date, time)

            suggestion = parts[4] if len(parts) > 4 else ""

            return result + ("\n💡 " + suggestion if suggestion else "")

        # ---------------------
        # ASK
        # ---------------------
        if intent == "ask":
            return parts[1] if len(parts) > 1 else "Can you clarify?"

        # ---------------------
        # ADVICE
        # ---------------------
        if intent == "advice":
            return parts[1] if len(parts) > 1 else ""

        return output

    except Exception as e:
        return f"❌ Error: {str(e)}"