from collections import deque

daily_food_portions = [int(x) for x in input().split(", ")]
daily_stamina = deque(int(x) for x in input().split(", "))
peaks = {
    80: "Vihren",
    90: "Kutelo",
    100: 'Banski Suhodol',
    60: "Polezhan",
    70: "Kamenitza"
}
peaks_queue = deque(x for x in peaks)
conquered_peaks = []
while peaks_queue and (daily_food_portions and daily_stamina):
    current_peak = peaks_queue.popleft()
    current_day = daily_food_portions.pop() + daily_stamina.popleft()
    if current_day >= current_peak:
        conquered_peaks.append(peaks[current_peak])
    else:
        peaks_queue.appendleft(current_peak)
    if not peaks_queue:
        print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
        break
    elif not daily_food_portions or not daily_stamina:
        print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
        break
       
if conquered_peaks:
    print(f"Conquered peaks:", *conquered_peaks, sep="\n")
    
# test inputs:

# 40, 40, 40, 40, 40, 40, 40
# 40, 50, 60, 20, 30, 5, 2

# 10, 20, 34, 26, 12, 10, 45
# 30, 28, 17, 17, 13, 10, 10
