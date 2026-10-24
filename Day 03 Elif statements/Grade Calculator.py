#8.Student Grade Calculator:
#If average marks > 90 → “Excellent”
#Between 70-90 → “Good”
#Below 70 → “Needs Improvement”

avgmarks = float(input("Enter average marks: "))
if avgmarks > 90:
    print("Excellent")
elif avgmarks >= 70:
    print("Good")
else:
    print("Needs Improvement")
