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
