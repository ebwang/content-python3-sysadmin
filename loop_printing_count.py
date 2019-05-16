#In that example, we also show off how to “string interpolation” in Python 3 by prefixing a string literal with an f and then using curly braces to substitute in variables or expressions (in this case the count value).

#!/usr/bin/env python3.6
count = 1
while count < 10:
        print(f"Feio {count}")
        count += 1
