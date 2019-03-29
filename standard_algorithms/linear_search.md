# Linear search

## Pseudo-code

Assuming list of strings

```
Line 1 SET item_found TO FALSE
Line 2 SET counter TO 0
Line 3 RECEIVE desired_item FROM (STRING) KEYBOARD
Line 4 REPEAT
Line 5   IF desired_item = nation[counter] THEN
Line 6     SET item_found TO TRUE 
Line 7     SEND "The program found  " & desired_item & " at position " & counter & “ of the nation array.” TO DISPLAY
Line 8   ELSE
Line 9     SET counter TO counter + 1
Line 10  END IF
Line 11 UNTIL counter = 10 OR item_found = TRUE
Line 12 IF item_found = FALSE THEN
Line 13     SEND “The program did not find a match for “ & desired_item & “ within the nation array.” TO DISPLAY
Line 14 END IF
```