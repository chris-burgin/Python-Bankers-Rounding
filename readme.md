## About
### The Problem
Normally rounding is bias to round up. This is due to the fact that we
round up for 5,6,7,8,9,10 and round down for 1,2,3,4 this means that 60% of
the time we round up and 40% of the time we round down.

### The Fix
By using banker rounding we have a 50% chance of rounding up or down.
- If our number is **6 or above we round up**
- If our number is **4 or below we round down**
- If our number is **5** we have to look at the **digit to the left**
    - If it is **odd** we round up to the **nearest even**
    - If it is **even** we **leave it alone**

### Examples
- ``` >= 6 # 2.966 would become 2.97```
- ``` = 5 # 2.965 would become 2.96```
- ``` = 5 # 2.975 would become 2.98 ```
- ``` <= 6 # 2.973 would become 2.97 ```




## Usage
#### Dependencies
    - Python 3
#### Main Functionality
```
BankersRounding(number, breakpoint) \\ returns a bankers rounded number
    - number \\ required float
    - breakpoint \\ optional integer, rounding location, default=2

```

#### Additional Functionality
```
FloatToList(number) \\  converts 'number' and returns a list of integers
    - number \\ required float

ListToFloat(list) \\ returns a converted float
    - list \\ required list derived from 'FloatToList'

LocateDecimal(list) \\ returns a decimal location
    - list \\ required list derived from 'FloatToList'

Trim(list, endpoint) \\ returns a trimmed list
    - list \\ required list derived from 'FloatToList'
    - endpoint \\ required int, represents trim location





```
