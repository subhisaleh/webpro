#!C:\Users\subhi saleh\AppData\Local\Microsoft\WindowsApps\python.exe
import cgi

def sum_of_digits(number):
    if not str(number).isdigit():
        return "Error: Input must be a positive integer"
    if number < 0:
        return "Error: Input must be a positive integer"
    digits_sum = 0
    for digit in str(number):
        digits_sum += int(digit)
    return f"The sum of digits in {number} is {digits_sum}"

form = cgi.FieldStorage()
number = form.getvalue("number")

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Sum of Digits</title>")
print("</head>")
print("<body>")
print("<h2>Enter a positive integer to find the sum of its digits:</h2>")
print("<form method='get'>")
print("<input type='text' name='number' value=''>")
print("<input type='submit' value='Submit'>")
print("</form>")

if number is not None:
    print(f"<p>{sum_of_digits(number)}</p>")

print("</body>")
print("</html>")
