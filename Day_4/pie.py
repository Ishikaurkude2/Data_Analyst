import matplotlib.pyplot as plt

subjects = ["DSA","Web Development","SAD","AI"]
Marks = [90,80,85,95]
plt.pie(Marks, labels=subjects, startangle=90 ,shadow=True)
plt.title("Marks in different subjects",backgroundcolor ='yellow',style='italic')
plt.show()