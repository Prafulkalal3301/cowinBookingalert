
# cowinBookingalert

This is python program to get push notifications when cowin booking is available near you.

# Requirements:

(cowin 0.0.5)
```python
pip install cowin 
```
(pushbullet)
```python
pip install pushbullet
```
# How to use:</br>
Copy the script and edit at:
</br>

1}.district_id:"your districtid in DistrictidList"

</br>
2}. get your api key from pushbullet and assign it to API_KEy variable
</br>
3}.make list of your nearest block. Assign it to nearestblock variable
Example
```python
mynearestblock=["Ulhasnagar Municipal Corporation","Ambernath"]
```
# Make bat file
</br>
Open notepad, make .bat file having python.exe location and your .py script location.
[notepad bat file](https://user-images.githubusercontent.com/56152599/119224297-66509400-bb1b-11eb-98bb-d367dd727772.PNG)

Now the remaining part is to make a task in your machine where script can run couple of times in a day. 
# Notification screen in Pushbullet
![pushbulletoutput](https://user-images.githubusercontent.com/56152599/119226423-a9fccb00-bb26-11eb-934e-19deb4082147.PNG)
!
