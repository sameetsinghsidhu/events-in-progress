# events-in-progress
 Events in progress calculator for my ITV interview

## The Problem
ITV would like to know how successful a new ITV Hub Programme launch was. They will measure the success of the launch by the number of users who were playing the programme concurrently.

The data we have to report on this is a collection of records in the form:

```python
VideoPlay {
    start: an instant in time,
    end:   an instant in time
}
```

We are allowed to make a few assumptions about the data:

- All end times are after their corresponding start time
- Each play lasts at most a few hours
- All of the plays happen within one calendar month

## My Solution

### Data generation
Firstly, I decided to write some code which would generate a synthetic dataset. This would allow me to test my code on fresh data while I was developing. You can find this code in [synthetic.py](synthetic_data.py)

It is pretty easy to use:

```python
from synthetic_data.py import generate_dataset

dataset = generate_dataset(n = 10)
```

This code would return a list containing 10 dictionaries of the form described above.

The dataset is generated based on the assumptions mentioned above. However, the algorithm does work on data that includes plays lasting an arbitrary number of hours and even on plays which occur in different months/years. I decided to make the data generator code follow these assumptions because they increase the probability of plays being concurrent. (If I let the generator produce data from any random year/month combination the likelihood of concurrent plays on small datasets would be low). This is an easy change to make if you did want it to do that though.

Another thing to note about the data generated from this script is:
- The end datetime will always be greater than the start datetime by:
  - Atleast 1 hour
  - A maximum of 12 hours
  
### Algorithm
The first step of my algorithm preprocesses the data.

The data generator produces a dataset which matches the form specified in the problem statement. So the raw data looks like this:

```python
[{'start': 1991-11-29 00:55:14,
  'end': 1991-11-29 02:24:40},
 {'start': 1991-11-22 18:02:06,
  'end': 1991-11-22 20:17:26},
 {'start': 1991-11-23 23:05:39,
  'end': 1991-11-24 04:40:21}]
```

I then create tuples from these dictionaries replacing "start" with the integer 1 and "end" with the integer -1 (This step will make more sense later). The dataset then looks like this:

```python
[(('29/11/1991, 00:55:14', 1), ('29/11/1991, 02:24:40', -1)),
 (('22/11/1991, 18:02:06', 1), ('22/11/1991, 20:17:26', -1)),
 (('23/11/1991, 23:05:39', 1), ('24/11/1991, 04:40:21', -1))]
```

Next I unpack and chain the iterables together to produce a dataset like this:

```python
[('29/11/1991, 00:55:14', 1),
 ('29/11/1991, 02:24:40', -1),
 ('22/11/1991, 18:02:06', 1),
 ('22/11/1991, 20:17:26', -1),
 ('23/11/1991, 23:05:39', 1),
 ('24/11/1991, 04:40:21', -1)]
```
 
The next step is to sort this list of tuples by datetime, here is an example from a larger dataset (more concurrency):
 
```python
(01/09/1988, 04:20:49, 1)
(01/09/1988, 04:56:05, 1)
(01/09/1988, 11:52:51, -1)
(01/09/1988, 12:51:17, -1)
(01/09/1988, 20:06:43, 1)
(01/09/1988, 22:00:59, 1)
(02/09/1988, 00:28:07, 1)
(02/09/1988, 01:30:22, -1)
```

Starting from the top all we have to do now is calculate a running total, summing the integers in the tuple. From this snippet we can see the maximum concurrent plays would be 3. In the code this is achieved by a simple reduce function.

The output of the reduce job for this snippet would look like this:

```python
[1, 2, 1, 0, 1, 2, 3, 2]
```

Then we take the maximum of this list which is 3 and thus the maximum concurrent jobs is 3.

### Unit testing

I have developed unit tests for the algorithm ([algorithm_unittest.py](algorithm_unittest.py)) and the data generator ([data_generator_unittest.py](data_generator_unittest.py)) script.

You can run the unit tests in the notebook using these commands:

```python
%run -i 'algorithm_unittest.py'
%run -i 'data_generator_unittest.py'
```
