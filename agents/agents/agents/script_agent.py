
def generate_script(trend):
    topic = trend["topic"]

    script = f"""
Did you know?

{topic} shows us something incredible.

Scientists discovered that small daily habits can completely change the way your brain works.

This simple fact can improve your focus, motivation, and success.

Follow for more daily facts.
"""
    return script.strip()
