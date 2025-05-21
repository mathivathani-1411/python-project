import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Course': ['Python', 'Data Science', 'Web Dev', 'AI', 'Python', 'Data Science', 'Web Dev', 'AI'],
    'Rating': [4.5, 4.7, 4.2, 4.8, 4.6, 4.5, 4.1, 4.9],
    'Date': ['2025-01', '2025-01', '2025-01', '2025-01', '2025-02', '2025-02', '2025-02', '2025-02'],
    'Feedback': [90, 95, 88, 96, 91, 92, 85, 97]
}
df = pd.DataFrame(data)

# Bar plot: Average rating by course
df.groupby('Course')['Rating'].mean().plot(kind='bar', title='Average Rating by Course')
plt.ylabel('Rating')
plt.show()

# Line plot: Average rating over time
df.groupby('Date')['Rating'].mean().plot(marker='o', title='Average Rating Over Time')
plt.ylabel('Rating')
plt.show()

# Box plot: Feedback score distribution
df.boxplot(column='Feedback', by='Course')
plt.title('Feedback Score Distribution by Course')
plt.suptitle('')
plt.ylabel('Score')
plt.show()
