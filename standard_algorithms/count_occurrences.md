1. SET occurrence TO 0
1. RECEIVE desired_value FROM (INTEGER) KEYBOARD
1. FOR counter FROM 0 TO 9 DO
1.  IF age [counter] = desired_value THEN
1.   SET occurrence TO occurrence + 1
1.  END IF
1. END FOR
1. SEND "There were " & occurrence & " occurrences of " & desired_value TO DISPLAY