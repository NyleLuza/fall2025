"""
Problem 1: Knowledge Q&A
(1) What is data mining?
    - Data mining is the process of discovering unknown and useful patterns in large datasets.
      
(2) When we are discussing ”data mining” in this class, it includes the whole mining
process. What are the processes we are referring to?
    - When talking about mining, the processes that we are referring to are data preparation, which
      include data cleaning, data integration, data transformation, and data selection.
      Then after we have our data prepped we then apply our data mining process, which applies the statistical
      techniques to transform our data into patterns. After we go through the pattern/model evaluation to dictate
      which patterns are important to what we are trying to find. Finally, once we discover these important patterns,
      we present them to the customer.
(3) What is the relationship between databases and data mining?
    - Databases have a big role when it comes to data mining because they are used to structure large datasets that are
      used for mining. Since the data is structured it allows for data preprocessing where we need to make sure our data
      is ready for mining.
(4) Based on whether data have clear structures, how can we categorize data? Name
one example of each.
    - We can categorize data in three ways, they can be structured, semi-structured, or unstructured.
        - Structured: students table where the columns are (student id, name, graduation year, class)
        - Semi-Structured: customers collection where each customer has a key:value pair ex. {name: James Doe, email: jdoe@gmail.com, location: Reseda, CA}
        - Unstrctured: This could be like images since the data is just pixel values that need to be processed.

(5) Describe the difference between an interval-scaled attribute and a ratio-scaled
attribute. List one example of each, excluding examples from the slides (temper-
ature).
    - Interval-scaled attributes are measured on a scale of equal sized units, whose values have order and can be positive, 0, or negative. They also have no true zero point
        - Example: Model year of laptops
    - Ratio-scaled attributes inherent a zero-point and the values can be a magnitude larger than the unit of measurement.
        - Example: Number of steps taken.
(6) What is the name of this plot? What statistical information can we gather from
this plot?
    - This plot is a box plot and the information it is giving us is that the data is slightly positively skewed since the right whisker is longer than the left. Also the median
      is more to the left of the box center. 

(7) Pearson correlation and χ2 correlation are two correlation methods, but they are
suited for different data types. What types are they suited for?
    - x^2 correlation is suited for nominal data, while Pearson correlation is suited for interval and ratio data.
(8) Regarding all the visualizations we have learned, which figure best describes
correlation?
    - scatter plots are the best visualization for correlation because it allows us to see a pattern when comparing two different 
      data points
(9) What is metadata?
    - Metadata is data about the data. It is information that describes the dataset's structure
(10) List three cleaning missing data strategies that first come to mind.
    - First data cleaning strategy that comes to mind is data smoothing. where we break down the data into bins, and the values in each bin are replaced with the mean or median
      of that bin. Second strategy that comes to mind is just by filling in missing values manually. Third strategy that comes to mind is ignoring the entry fully if it is missing
      values, so we just delete it from our dataset.

Problem 2: Identify data types (20%)
Given a sample dataset that describe the vehicle information, for each attribute, answer
following questions:
Last 4 VIN | Vehicle Type | Clean Title | Safety Level | Number of Accidents | Mileage (km)
------------------------------------------------------------------------------------------
13C2       | Sedan        | Yes         | A+           | 0                   | 35,678
24F1       | SUV          | No          | B+           | 2                   | 75,421
3VD3       | Truck        | Yes         | A            | 0                   | 123,560
T54N       | Coupe        | No          | B-           | 3                   | 25,982
1. Which data type (Nominal, Binary, Ordinal, Numeric)?
    - Nominal: Vehicle Type, Last 4 VIN (Categories with no order hierarchy)
    - Binary: Clean Title (Only two options)
    - Ordinal: Safety Level (Categories that have hierarchy)
    - Numeric: Mileage, Number of Accidents (Numeric Value)
2. Is it continuous or discrete?
    - Discrete: Number of Accidents (no fractional values of an accident)
    - Continous: Mileage (You can have a fraction of a mile)
3. If it is numeric data, does it belong to a ratio-based or interval-based attribute?
    - Both numeric data are interval-based attributes because they both have a true 0.

Problem 3: Programming: clean the outliers (20%)
• In this problem, you will use the empirical rule we discussed in class to filter out
the outliers.
• Use the same dataset we used in class, ”adult” from UCIML repository. Instead
of age, we will work on ”education-num” attribute.
• Use 1.5 IQR rule to filter out the outliers.
• Use boxplot to visualize the distribution before and after the outlier removal.
Hint:
• Use pandas.Series.between() function to choose the data in a certain range.
• You can plot multiple boxplots in one figure by putting them into a list:
2
"""

import pandas as pd
import matplotlib.pyplot as plt

# load data into data frame
df = pd.read_csv("assignment1/adult.csv")
plot_before = df['education-num']

# filter out data
filtered_plot = df[df['education-num'].between(5,16)]

plt.boxplot([plot_before, filtered_plot['education-num']], tick_labels=["Before", "After"])
plt.show()

"""
Problem 4: Programming: Filling missing values (30%)
In this problem, you will implement a missing data handling method that we discussed
in class: using the attribute mean, median, or mode for all samples belonging to the
same class as the given tuple.
According to the metadata of the adult dataset, there are missing values in the ”native-
country” attribute. And there are some attributes that doesn’t contain NaN. Our task
will be to use one of the completed attributes, find the most possible value to fill the
missing value.
Let’s start with the single missing value.
1. To start the filling process, we first need to choose an appropriate attribute as a
help attribute. The four candidate attributes that do not contain missing values
are:
• education
• relationship
• race
• sex
Choose the appropriate attributes from candidates by calculating the correlation
between the candidate and ”native-country”. The higher correlation gives us a
higher chance of filling the correct value. You can use any correlation measures
in this step. The example of correlation is provided data exploration.ipynb.
2. Use DataFrame.tail(50) to list the last fifty samples of the dataframe, then
you will notice that the nationality of the No. 48826 data instance is marked as
NaN:
3. Identify the candidate attribute of this sample, in other words, what is the at-
tribute of row 48826 of education/relationship/race/sex, the one attribute you
get the highest correlation from the step 1
Note: to automate the process and further applying this method
to other missing values, we should use the the variable and index-
ing to find the attribute rather than manually inspecting them, i.e.
df.loc[48826, ’sex’] instead of ’female’.
3
4. Find all the samples that belong to the same candidate category.
5. In this subset of the dataframe, find the most common ”native-country” (the
Series.mode() function returns a series, so use index 0 to extract the value).
6. Fill the missing value with this category using DataFrame.at to assign the value.
7. Use DataFrame.tail(50) again to verify the result.
Extra (5%): Now try to apply this method to the whole NaN values shown in ”native-
country” attributes.
Instead of using tail, use value counts before and after to discover the changes.
Hint:
• You can use DataFrame.iterrows() to traverse the entire data frame.
• Use pandas.isna() to check if there are NaN values in the ”native-country”
attribute.
"""