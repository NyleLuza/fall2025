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
(8) Regarding all the visualizations we have learned, which figure best describes
correlation?
(9) What is metadata?
    - Metadata is data about the data. It is information that describes the dataset's structure
(10) List three cleaning missing data strategies that first come to mind.

"""