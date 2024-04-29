# Quantium Software Engineering Job Simulation

## Task 1

Soul Foods has provided you with three CSV files which contain transaction data for Soul Foods’s entire morsel line. Each row indicates the quantity of a given type of morsel sold in a given region at a given price on a given day. 

The first field, “product”, contains many different types of morsels. Soul Foods is only interested in Pink Morsels, so we can remove any row which contains another type of product.
Next are “quantity” and “price”. Since we’re interested in the total sales for a given day, these can be combined into a single field, “sales,” by multiplying them together.
The date field is useful as is and can remain untouched.
It would be nice to filter by region in the final visualisation, so we’ll also leave the region field untouched.
 
Your task is to use the above instructions to convert the three CSV files into a single formatted output file. Your output file should contain three fields: Sales, Date, and Region.
 
When you are finished, commit and push your changes.

My code [here](https://github.com/luwoon/Quantium-Software-Engineering/blob/main/process.py).
Output file [here](https://github.com/luwoon/Quantium-Software-Engineering/blob/main/output.csv).

## Task 2

Your task is to create a Dash app to visualise the data you generated in the last task. Your application must incorporate a header which appropriately titles the visualiser, and a line chart which visualises the sales data generated in the last task, sorted by date. 
 
Recall the original purpose of the Dash app you are building — the goal is to answer Soul Foods’s question: “Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?” 
 
When you are finished, commit and push your changes.

My code [here]().
