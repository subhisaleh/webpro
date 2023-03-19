#!C:\Users\subhi saleh\AppData\Local\Microsoft\WindowsApps\python.exe
import cgi
import random

def roll_dice(num_dice, max_value, num_tries):
    if not num_dice.isdigit() or not max_value.isdigit() or not num_tries.isdigit():
        return "Error: All inputs must be positive integers"
    num_dice = int(num_dice)
    max_value = int(max_value)
    num_tries = int(num_tries)
    if num_dice <= 0 or num_dice > 10 or max_value <= 0 or max_value > 100 or num_tries <= 0 or num_tries > 100:
        return "Error: Input values are out of range"
    rolls = []
    for _ in range(num_tries):
        rolls.append(sum([random.randint(1, max_value) for _ in range(num_dice)]))
    best_roll = max(rolls)
    return f"The best roll out of {num_tries} tries with {num_dice} dice and a maximum value of {max_value} is: {best_roll}"

form = cgi.FieldStorage()
num_dice = form.getvalue("num_dice")
max_value = form.getvalue("max_value")
num_tries = form.getvalue("num_tries")

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Dice Rolling Game</title>")
print("</head>")
print("<body>")
print("<h2>Enter the parameters for a dice rolling game:</h2>")
print("<form method='get'>")
print("<label for='num_dice'>Number of dice:</label>")
print("<input type='text' name='num_dice' value=''>")
print("<br>")
print("<label for='max_value'>Maximum value:</label>")
print("<input type='text' name='max_value' value=''>")
print("<br>")
print("<label for='num_tries'>Number of tries:</label>")
print("<input type='text' name='num_tries' value=''>")
print("<br>")
print("<input type='submit' value='Roll dice'>")
print("</form>")

if num_dice is not None and max_value is not None and num_tries is not None:
    print(f"<p>{roll_dice(num_dice, max_value, num_tries)}</p>")

print("</body>")
print("</html>")
