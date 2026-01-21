# Card Games

Focus:
- Lists

<br>

Comments:
- In line 64, instead of "return bool(first_last == average or hand[median_position] == average)", I can do "return bool(average in (first_last, hand[median_position]))" instead.
- It is faster and easier to understand at a glance.
