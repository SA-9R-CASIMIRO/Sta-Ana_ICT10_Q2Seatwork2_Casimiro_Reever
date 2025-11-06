from pyscript import document, when

@when("click", "#calculateBtn")
def calculate_everything(event):
    btn = document.querySelector("#calculateBtn")
    btn.classList.add("flash-effect")
    def remove_flash(evt):
        btn.classList.remove("flash-effect")
    btn.addEventListener("animationend", remove_flash)
    first_name = document.querySelector("#firstName").value.strip()
    last_name = document.querySelector("#lastName").value.strip()
    if not first_name or not last_name:
        document.querySelector("#result").innerHTML = """
            <div style="color: #ff4500;">
                ⚠️ Please enter your name first!
            </div>
        """
        document.querySelector("#result").style.display = "block"
        return
    try:
        labels = ["science", "math", "english", "filipino", "socialStudies", "ve", "music", "pe", "lt", "tle", "ict"]
        grades = [float(document.querySelector(f"#{x}").value or 0) for x in labels]
    except ValueError:
        document.querySelector("#result").innerHTML = """
            <div style="color: #ff4500;">
                ⚠️ Please enter REAL valid numbers!
            </div>
        """
        document.querySelector("#result").style.display = "block"
        return

  
    valid_grades = [g for g in grades if g > 0]
    if not valid_grades:
        document.querySelector("#result").innerHTML = """
            <div style="color: #ff4500;">
                ⚠️ Please PUT at least one grade
            </div>
        """
        document.querySelector("#result").style.display = "block"
        return

    average = sum(valid_grades) / len(valid_grades)
    if average >= 95:
        message, color, img = "Ms. Onofre would be proud!", "#00ff00", "jinu.png"
    elif average >= 90:
        message, color, img = "Woah, Amazing, let's get it chuzz!", "#7fff00", "abby.png"
    elif average >= 85:
        message, color, img = "Not bad, Not bad, But instead of being a Romance, just study well ", "#ffd700", "romance.png"
    elif average >= 80:
        message, color, img = "Ehh It's okay I guess", "#ffb347", "baby.png"
    elif average >= 75:
        message, color, img = "Wonder how you got that score.. Such a 'mystery' ", "#ff8c00", "mystery.png"
    else:
        message, color, img = "You failed.. 67.. 😤", "#ff4500", "oof.png"
    document.querySelector("#result").innerHTML = f"""
        <div style="color: {color}; text-align:center;">
            <img src="{img}" style="width:130px; margin-bottom:10px;"><br>
            <strong>{first_name} {last_name}</strong><br>
            Average Grade: {average:.2f}%<br>
            {message}
        </div>
    """
    document.querySelector("#result").style.display = "block"
