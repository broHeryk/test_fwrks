All tasks should be done for unittest and nosetest

1. Write unit tests which do testing of dict methods like: 
- update
- get 
- pop 
- keys 
- values
- items 

2. Write unit tests for the following function. Try to cover all cases.

It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from  to . Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.
Determine the minimum number of bribes that took place to get to the given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.
```python
def minimumBribes(queue):
    bribes = 0

    for idx,el in enumerate(queue, start=1):
        if el - idx > 2:
            return 'Too chaotic'
            
        
        for potential_briber in queue[max(0,el-3):idx]:
            if potential_briber > el:
                bribes += 1
    return bribes
```

3. Write function/class which read .csv file with the following format:

```
timestamp,temperature
1612734231,20
...
```
Where timestamp is seconds since Jan 01 1970 and temperature is temperature value by Celsius.
Function/class should covert data and write to an output file. 
```
{"temperature_statistic" : 
    [
        {"datetime":"02/07/2021T9:43pm", "celsius_temp": 111,  "fahrenheit_temp": 111, "kelvin_temp": 111,},
...
    ]
}
```
Format of output file should be:
	 .txt for windows 
	 .json for linux
Input args:
	path to csv file - migth be passed as environment variable 
	path to folder for output file - migth be passed as environment variable
	output datetime format  

Function should be covered by unit tests and next cases should be covered. 
- path to the input file does not exist
- path to the output folder does not exist
- path to CSV or output path is passed as an env variable
- converting DateTime and temperature value/ incorrect values also should be checked. 
- creation an output file for different platforms 
- whatever else you'll consider as a possible case 