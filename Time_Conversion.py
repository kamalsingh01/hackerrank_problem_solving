'''
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
    s = '12:01:00PM'

Return '12:01:00'.

    s = '12:01:00AM'

Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in 12 hour format
Returns

string: the time in 24 hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM ).

Constraints

All input times are valid
Sample Input

07:05:45PM
Sample Output

19:05:45

===========================================================================================================
NOTE: 
    Test Case to take care, s = '12:45:05PM'
'''

# The function is expected to return a STRING.
# The function accepts STRING s as parameter.

def timeConversion(s):
    lst = [ ]
    if s[-2] == 'A':
        s = s.rstrip("AM")
        lst = s.split(':')
        lst[0] = (int(lst[0])%12)
        if lst[0]<10:
            lst[0] = '0'+str(lst[0])
        s = ':'.join(lst)
        
    if s[-2] == 'P':
        s = s.rstrip("PM")
        lst = s.split(':')
        lst[0] = str((int(lst[0])%12)+12)
        s = ':'.join(lst)
    
    return s

if __name__ == '__main__':

    s = input()
    result = timeConversion(s)
    print(result)


